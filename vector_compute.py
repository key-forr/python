import time
import os
import numpy as np
import pyopencl as cl

os.environ['PYOPENCL_CTX'] = '0'

VECTOR_SIZE = 3_000_000


kernelsource = """
__kernel void compute_gpu(
    __global const int *a_g, 
    __global const int *b_g, 
    __global int *res_g)
{
    int gid = get_global_id(0);
    res_g[gid] = 1 * a_g[gid] + 4 * b_g[gid];
}
"""


a_np = np.random.randint(0, 100, VECTOR_SIZE).astype(np.int32)
b_np = np.random.randint(0, 100, VECTOR_SIZE).astype(np.int32)
c_np = np.empty(VECTOR_SIZE).astype(np.int32)


start_time = time.time()
c_np = 1 * a_np + 4 * b_np
duration = time.time() - start_time
print('CPU Time: ', duration * 1_000, 'ms')


platforms = cl.get_platforms()
print("\nNumber of OpenCL platforms:", len(platforms))
print("\n-------------------------")

for p in platforms:
    print("Platform:", p.name)
    print("Vendor:", p.vendor)
    print("Version:", p.version)
    
    devices = p.get_devices()
    print("Number of devices:", len(devices))
    
    for d in devices:
        print("\t-------------------------")
        print("\t\tName:", d.name)
        print("\t\tVersion:", d.opencl_c_version)
        print("\t\tMax. Compute Units:", d.max_compute_units)
        print("\t\tLocal Memory Size:", d.local_mem_size/1024, "KB")
        print("\t\tGlobal Memory Size:", d.global_mem_size/(1024*1024), "MB")
        print("\t\tMax Alloc Size:", d.max_mem_alloc_size/(1024*1024), "MB")
        print("\t\tMax Work-group Total Size:", d.max_work_group_size)
        
        dim = d.max_work_item_sizes
        print("\t\tMax Work-group Dims:(", dim[0], " ".join(map(str, dim[1:])), ")")
        print("\t-------------------------")
    
    print("\n-------------------------")

ctx = cl.create_some_context(interactive=False)

queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
b_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

res_g = cl.Buffer(ctx, mf.WRITE_ONLY, a_np.nbytes)

prg = cl.Program(ctx, kernelsource).build()

start_time = time.time()

prg.compute_gpu(queue, a_np.shape, None, a_g, b_g, res_g)

duration = time.time() - start_time
print('GPU Time: ', duration * 1_000, 'ms')

res_np = np.empty_like(a_np)
cl.enqueue_copy(queue, res_np, res_g)

verification = res_np - (1 * a_np + 4 * b_np)
print("\nПеревірка коректності (різниця між GPU та CPU):")
print("Максимальна різниця:", np.max(np.abs(verification)))
print("Сума різниць:", np.sum(np.abs(verification)))

print("\nПриклад перших 5 елементів:")
print("A:", a_np[:5])
print("B:", b_np[:5])
print("C = 1*A + 4*B (GPU):", res_np[:5])
print("C = 1*A + 4*B (CPU):", (1 * a_np + 4 * b_np)[:5])