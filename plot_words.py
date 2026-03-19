import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

words  = ["people", "know", "really", "time", "dont",
          "one", "get", "would", "im", "like"]
counts = [2315229, 2408555, 2410097, 2974381, 2981402,
          3034093, 3271024, 3369711, 3967393, 4100458]

BLUE_DARK  = "#1F4E79"
BLUE_MID = "#2E75B6"
BLUE_LIGHT = "#9DC3E6"
GREY = "#666666"

colors = [BLUE_LIGHT] * 7 + [BLUE_MID, BLUE_MID, BLUE_DARK]

plt.rcParams.update({
    "font.family":       "DejaVu Sans",
    "font.size":         12,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.spines.left":  False,
    "axes.grid":         True,
    "grid.color":        "#E0E0E0",
    "grid.linestyle":    "--",
    "grid.linewidth":    0.8,
    "figure.dpi":        150,
})

fig, ax = plt.subplots(figsize=(8, 5.5))

bars = ax.barh(words, counts, color=colors, height=0.65, edgecolor="white", linewidth=0.5)
ax.set_axisbelow(True)
ax.xaxis.grid(True)
ax.yaxis.grid(False)

for bar, val in zip(bars, counts):
    ax.text(bar.get_width() + 40000, bar.get_y() + bar.get_height() / 2,
            f"{val:,}", va="center", ha="left", fontsize=10.5, color=GREY)

ax.set_xlabel("Word Frequency (count)", fontsize=12, color=GREY)
ax.set_title("Top 10 Most Frequent Words in Reddit Comments\n(stop words excluded)",
             fontsize=13, fontweight="bold", color=BLUE_DARK, pad=14)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(
    lambda x, _: f"{x/1e6:.1f}M" if x >= 1e6 else f"{int(x/1e3)}K"))
ax.set_xlim(0, max(counts) * 1.18)
ax.tick_params(axis="y", colors=BLUE_DARK, labelsize=12, length=0)
ax.tick_params(axis="x", colors=GREY)

fig.tight_layout()
fig.savefig("plot_words.png", bbox_inches="tight")
print("Saved: plot_words.png")
plt.show()
