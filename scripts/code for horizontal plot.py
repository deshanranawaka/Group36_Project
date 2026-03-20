import matplotlib.pyplot as plt
import numpy as np

# Horizontal scaling: 1, 2, 3 workers (2 cores each)
workers  = [1, 2, 3]
runtimes = [964.59, 523.17, 386.71]

t1 = runtimes[0]
speedups = [t1 / t for t in runtimes]
ideal_speedup = [float(w) for w in workers]

BLUE_DARK = "#1F4E79"
GREY = "#666666"
RED_IDEAL = "#C00000"

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

# Plot 1: Runtime vs Workers
fig1, ax1 = plt.subplots(figsize=(7, 4.5))
ax1.plot(workers, runtimes, color=BLUE_DARK, marker="o", markersize=8,
         linewidth=2.5, label="Measured runtime")
for x, y in zip(workers, runtimes):
    ax1.annotate(f"{y:.1f}s", xy=(x, y), xytext=(0, 12),
                 textcoords="offset points", ha="center",
                 fontsize=11, color=BLUE_DARK, fontweight="bold")
ax1.set_xlabel("Number of Workers", fontsize=12, color=GREY)
ax1.set_ylabel("Runtime (seconds)", fontsize=12, color=GREY)
ax1.set_title("Runtime vs. Number of Workers\n(Horizontal Scaling — Fixed Dataset)",
              fontsize=13, fontweight="bold", color=BLUE_DARK, pad=14)
ax1.set_xticks(workers)
ax1.set_xticklabels(["1 worker\n(2 cores)", "2 workers\n(4 cores)", "3 workers\n(6 cores)"])
ax1.set_xlim(0.7, 3.3)
ax1.set_ylim(0, max(runtimes) * 1.25)
ax1.tick_params(colors=GREY)
ax1.legend(fontsize=11)
fig1.tight_layout()
fig1.savefig("plot_runtime.png", bbox_inches="tight")
print("Saved: plot_runtime.png")

# Plot 2: Speedup vs Ideal
fig2, ax2 = plt.subplots(figsize=(7, 4.5))
ax2.plot(workers, ideal_speedup, color=RED_IDEAL, linestyle="--", linewidth=2,
         marker="s", markersize=7, label="Ideal (linear) speedup")
ax2.plot(workers, speedups, color=BLUE_DARK, marker="o", markersize=8,
         linewidth=2.5, label="Measured speedup")
for x, y in zip(workers, speedups):
    ax2.annotate(f"{y:.2f}x", xy=(x, y), xytext=(0, 12),
                 textcoords="offset points", ha="center",
                 fontsize=11, color=BLUE_DARK, fontweight="bold")
ax2.fill_between(workers, speedups, ideal_speedup,
                 alpha=0.12, color=RED_IDEAL, label="Efficiency loss")
ax2.set_xlabel("Number of Workers", fontsize=12, color=GREY)
ax2.set_ylabel("Speedup Factor  (T₁ / Tₙ)", fontsize=12, color=GREY)
ax2.set_title("Speedup Factor vs. Ideal Linear Speedup\n(Horizontal Scaling)",
              fontsize=13, fontweight="bold", color=BLUE_DARK, pad=14)
ax2.set_xticks(workers)
ax2.set_xticklabels(["1 worker\n(2 cores)", "2 workers\n(4 cores)", "3 workers\n(6 cores)"])
ax2.set_xlim(0.7, 3.3)
ax2.set_ylim(0, max(ideal_speedup) * 1.25)
ax2.tick_params(colors=GREY)
ax2.legend(fontsize=11)
fig2.tight_layout()
fig2.savefig("plot_speedup.png", bbox_inches="tight")
print("Saved: plot_speedup.png")
plt.show()