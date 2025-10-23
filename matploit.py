import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)

functions = [
    {"y": 3*x**2 + 12*x + 12, "color": "blue", "linestyle": "-.", "marker": "+", "label": "y1 = 3x² + 12x + 12"},
    {"y": 1*x**2 + 5*x + 7,   "color": "green", "linestyle": "--", "marker": "x", "label": "y2 = 1x² + 5x + 7"},
    {"y": 4*x**2 + 7*x + 16,  "color": "black", "linestyle": ":", "marker": "*", "label": "y3 = 4x² + 7x + 16"},
    {"y": 1*x**2 + 12*x + 44, "color": "red", "linestyle": "-", "marker": ",", "label": "y4 = 1x² + 12x + 44"},
]

# figsize 12 x 8, one big axes for all functions
fig, ax = plt.subplots(figsize=(12, 8))
for f in functions:
    # set x and y and other parameters
    # plot it is the main function to plot(графік)
    ax.plot(x, f["y"], color=f["color"], linestyle=f["linestyle"], marker=f["marker"],
            markevery=10, linewidth=2, label=f["label"])

ax.axhline(0, color="black", linewidth=2)
ax.axvline(0, color="black", linewidth=2)
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.set_title("Графіки функцій y1-y4", fontsize=14, fontweight="bold")
#shows symbols based on drawn graphs in a window on the left
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
for ax, f in zip(axes.ravel(), functions):
    ax.plot(x, f["y"], color=f["color"], linestyle=f["linestyle"], marker=f["marker"], markevery=10, linewidth=2)
    ax.axhline(0, color="black", linewidth=1.5)
    ax.axvline(0, color="black", linewidth=1.5)
    ax.set_title(f["label"], fontsize=12, fontweight="bold")
    ax.set_xlabel("x", fontsize=11)
    ax.set_ylabel("y", fontsize=11)
    ax.grid(True, alpha=0.3)

plt.tight_layout()


countries = ["Сьєрра-Леоне", "Колумбія", "Малайзія", "Уругвай", 
             "Кот-д'Івуар", "Ліван", "Болгарія"]
population = [6624933, 49084841, 32652083, 3387605, 27481086, 5469612, 6966899]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# cm stands for colormap and viridis it's a gradient of colors that goes from purple to yellow
colors_bar = plt.cm.viridis(np.linspace(0, 1, len(countries)))
# create bar chart where countries on x axis and population on y axis
bars = ax1.bar(countries, population, color=colors_bar, edgecolor="black", linewidth=1.5)
ax1.set_title("Населення країн (стовпчаста діаграма)", fontsize=14, fontweight="bold")
ax1.set_ylabel("Населення", fontsize=12)
ax1.grid(axis="y", alpha=0.3)

for bar in bars:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f"{bar.get_height():,}", ha="center", va="bottom", fontsize=9)

colors_pie = plt.cm.Set3(np.linspace(0, 1, len(countries)))
# autopct to show percentage on pie chart for example 35.2%
wedges, texts, autotexts = ax2.pie(
    population, labels=countries, autopct="%1.1f%%",
    colors=colors_pie, startangle=90, textprops={"fontsize": 10}
)
ax2.set_title("Населення країн (кругова діаграма)", fontsize=14, fontweight="bold")

for autotext in autotexts:
    autotext.set_color("black")
    autotext.set_fontweight("bold")

plt.tight_layout()
plt.show()
