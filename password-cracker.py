import os
from multiprocessing import cpu_count


def n_cpu():
    c = os.cpu_count()
    return c or cpu_count()


def main():
    cores = n_cpu()
    print(f"Detected CPU cores: {cores}")


if __name__ == '__main__':
    main()
