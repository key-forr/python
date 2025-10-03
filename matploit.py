import matplotlib.pyplot as plt
import numpy as np

# Визначення діапазону x
x = np.linspace(-10, 10, 100)

# Визначення функцій
y1 = 3*x**2 + 12*x + 12
y2 = 1*x**2 + 5*x + 7
y3 = 4*x**2 + 7*x + 16
y4 = 1*x**2 + 12*x + 44

# ===== ГРАФІК 1: Всі функції в одному полі =====
plt.figure(figsize=(12, 8))

plt.plot(x, y1, color='blue', linestyle='-.', marker='+', markevery=10, 
         label='y1 = 3x² + 12x + 12', linewidth=2)
plt.plot(x, y2, color='green', linestyle='--', marker='x', markevery=10, 
         label='y2 = 1x² + 5x + 7', linewidth=2)
plt.plot(x, y3, color='black', linestyle=':', marker='*', markevery=10, 
         label='y3 = 4x² + 7x + 16', linewidth=2)
plt.plot(x, y4, color='red', linestyle='-', marker=',', markevery=10, 
         label='y4 = 1x² + 12x + 44', linewidth=2)

plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Графіки функцій y1-y4', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(loc='upper center', fontsize=10)
plt.tight_layout()

# ===== ГРАФІК 2: Subplot 2x2 =====
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# y1
axes[0, 0].plot(x, y1, color='blue', linestyle='-.', marker='+', markevery=10, linewidth=2)
axes[0, 0].set_xlabel('x', fontsize=11)
axes[0, 0].set_ylabel('y1', fontsize=11)
axes[0, 0].set_title('y1 = 3x² + 12x + 12', fontsize=12, fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

# y2
axes[0, 1].plot(x, y2, color='green', linestyle='--', marker='x', markevery=10, linewidth=2)
axes[0, 1].set_xlabel('x', fontsize=11)
axes[0, 1].set_ylabel('y2', fontsize=11)
axes[0, 1].set_title('y2 = 1x² + 5x + 7', fontsize=12, fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

# y3
axes[1, 0].plot(x, y3, color='black', linestyle=':', marker='*', markevery=10, linewidth=2)
axes[1, 0].set_xlabel('x', fontsize=11)
axes[1, 0].set_ylabel('y3', fontsize=11)
axes[1, 0].set_title('y3 = 4x² + 7x + 16', fontsize=12, fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

# y4
axes[1, 1].plot(x, y4, color='red', linestyle='-', marker=',', markevery=10, linewidth=2)
axes[1, 1].set_xlabel('x', fontsize=11)
axes[1, 1].set_ylabel('y4', fontsize=11)
axes[1, 1].set_title('y4 = 1x² + 12x + 44', fontsize=12, fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()

# ===== ДІАГРАМИ НАСЕЛЕННЯ КРАЇН =====
# Дані про країни та населення
countries = ['Сьєрра-Леоне', 'Колумбія', 'Малайзія', 'Уругвай', 
             'Кот-д\'Івуар', 'Ліван', 'Болгарія']
population = [6624933, 49084841, 32652083, 3387605, 27481086, 5469612, 6966899]

# Створення фігури з двома діаграмами
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Стовпчаста діаграма
colors_bar = plt.cm.viridis(np.linspace(0, 1, len(countries)))
bars = ax1.bar(range(len(countries)), population, color=colors_bar, edgecolor='black', linewidth=1.5)
ax1.set_xlabel('Країни', fontsize=12, fontweight='bold')
ax1.set_ylabel('Населення', fontsize=12, fontweight='bold')
ax1.set_title('Населення країн (стовпчаста діаграма)', fontsize=14, fontweight='bold')
ax1.set_xticks(range(len(countries)))
ax1.set_xticklabels(countries, rotation=45, ha='right')
ax1.grid(axis='y', alpha=0.3)

# Додавання значень на стовпці
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height):,}',
             ha='center', va='bottom', fontsize=9)

# Кругова діаграма
colors_pie = plt.cm.Set3(np.linspace(0, 1, len(countries)))
wedges, texts, autotexts = ax2.pie(population, labels=countries, autopct='%1.1f%%',
                                     colors=colors_pie, startangle=90,
                                     textprops={'fontsize': 10})
ax2.set_title('Населення країн (кругова діаграма)', fontsize=14, fontweight='bold')

# Покращення читабельності відсотків
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(9)

plt.tight_layout()

# Відображення всіх графіків
plt.show()