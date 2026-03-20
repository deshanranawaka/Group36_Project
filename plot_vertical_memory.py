import matplotlib.pyplot as plt

#Group 36 plots


# ─────────────────────────────────────────────
#  Vertical Memory Scaling Results
#  3 worker nodes, 6 cores total — only RAM changes
# ─────────────────────────────────────────────

memory = [0.5, 1.0, 2.5]   # GB per worker
runtimes = [403.83, 402.03, 452.31]  # seconds

BLUE_DARK = "#1F4E79"
BLUE_MID  = "#2E75B6"
GREY = "#666666"
ORANGE = "#C55A11"

plt.rcParams.update({
    "font.family":       "DejaVu Sans",
    "font.size":         12,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.grid":         True,
    "grid.color":        "#E0E0E0",
    "grid.linestyle":    "--",
    "grid.linewidth":    0.8,
    "figure.dpi":        150,
})

# ── Plot: Runtime vs Memory ───────────────────
fig, ax = plt.subplots(figsize=(7, 4.5))

ax.plot(memory, runtimes,
        color=BLUE_DARK, marker="o", markersize=8,
        linewidth=2.5, label="Measured runtime")

# Label each point
for x, y in zip(memory, runtimes):
    ax.annotate(f"{y:.1f}s", xy=(x, y), xytext=(0, 12),
                textcoords="offset points", ha="center",
                fontsize=11, color=BLUE_DARK, fontweight="bold")

# Highlight the sweet spot at 1.0 GB
ax.axvline(x=1.0, color=ORANGE, linestyle="--", linewidth=1.5, alpha=0.7)
ax.text(1.03, max(runtimes) * 1.08, "Sweet spot\n(1.0 GB)",
        color=ORANGE, fontsize=10)

ax.set_xlabel("Executor Memory per Worker (GB)", fontsize=12, color=GREY)
ax.set_ylabel("Runtime (seconds)", fontsize=12, color=GREY)
ax.set_title("Runtime vs. Executor Memory\n(Vertical Memory Scaling — 3 Workers, 6 Cores)",
             fontsize=13, fontweight="bold", color=BLUE_DARK, pad=14)
ax.set_xticks(memory)
ax.set_xticklabels(["0.5 GB", "1.0 GB", "2.5 GB"])
ax.set_xlim(0.3, 2.7)
ax.set_ylim(350, max(runtimes) * 1.2)
ax.tick_params(colors=GREY)
ax.legend(fontsize=11)

fig.tight_layout()
fig.savefig("plot_vertical_memory.png", bbox_inches="tight")
print("Saved: plot_vertical_memory.png")

plt.show()
