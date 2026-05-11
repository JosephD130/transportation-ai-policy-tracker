"""Build the inheritance + contractor-binding chart for Issue 11."""

import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec

HERE = Path(__file__).parent
CSV_PATH = HERE / "transportation-ai-policy-tracker.csv"
OUT_PNG = HERE / "issue-11-chart.png"

# Color scheme
COLORS = {
    "FORBID": "#c0392b",       # red
    "ENCOURAGE": "#27ae60",    # green
    "PARTIAL": "#f39c12",      # orange
    "SILENT": "#7f8c8d",       # gray
}
CONTRACTOR_COLOR = "#2c3e50"   # dark navy for contractor-binding marker

REGIONS = ["West", "Midwest", "South", "Northeast"]
BUCKETS = ["FORBID", "ENCOURAGE", "PARTIAL", "SILENT"]


def load_data():
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_chart():
    rows = load_data()

    # Prepare regional bucket counts
    region_bucket = {r: Counter() for r in REGIONS}
    for row in rows:
        region_bucket[row["region"]][row["bucket"]] += 1

    # Contractor-binding states
    contractor_states = [r["entity"] for r in rows if r["contractor_binding"] == "Yes"]

    # DOT-direct policy states (only the 4 — exclude Caltrans which has CDAO authority but no standalone DOT policy)
    dot_direct_states = [r["entity"] for r in rows if r["has_dot_specific_policy"] == "Yes"]

    # Build the figure
    fig = plt.figure(figsize=(13, 6))
    gs = GridSpec(1, 2, figure=fig, width_ratios=[1.3, 1], wspace=0.35)

    # -----------------------------------------------------
    # PANEL 1 (left): Regional bucket distribution
    # -----------------------------------------------------
    ax1 = fig.add_subplot(gs[0, 0])

    region_data = []
    for region in REGIONS:
        region_data.append([region_bucket[region][b] for b in BUCKETS])

    y_pos = list(range(len(REGIONS)))
    left = [0] * len(REGIONS)

    for i, bucket in enumerate(BUCKETS):
        widths = [region_bucket[r][bucket] for r in REGIONS]
        ax1.barh(y_pos, widths, left=left, label=bucket, color=COLORS[bucket], edgecolor="white", linewidth=1.2)
        # Add count labels inside bars
        for y, (w, l) in enumerate(zip(widths, left)):
            if w > 0:
                ax1.text(l + w / 2, y, str(w), ha="center", va="center",
                         color="white", fontweight="bold", fontsize=11)
        left = [l + w for l, w in zip(left, widths)]

    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(REGIONS, fontsize=11)
    ax1.set_xlabel("Number of state DOT entities", fontsize=10)
    ax1.set_title("Where each state DOT's AI rule actually lives, by region",
                  fontsize=12, fontweight="bold", pad=12, loc="left")
    ax1.invert_yaxis()
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.legend(loc="upper right", framealpha=0.95, fontsize=9, title="Policy posture", title_fontsize=10)
    ax1.set_xlim(0, 15)

    # -----------------------------------------------------
    # PANEL 2 (right): The headline numbers
    # -----------------------------------------------------
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.axis("off")

    # Big numbers display
    headline_y = 0.92
    line_h = 0.16

    ax2.text(0.5, headline_y, "52 entities", ha="center", fontsize=20,
             fontweight="bold", color="#2c3e50", transform=ax2.transAxes)
    ax2.text(0.5, headline_y - 0.05, "50 states + DC + PR", ha="center", fontsize=10,
             color="#7f8c8d", style="italic", transform=ax2.transAxes)

    # 4 DOT-direct
    ax2.text(0.5, headline_y - line_h - 0.04, "4", ha="center", fontsize=28,
             fontweight="bold", color="#27ae60", transform=ax2.transAxes)
    ax2.text(0.5, headline_y - line_h - 0.13, "DOTs publish their own AI policy",
             ha="center", fontsize=10, transform=ax2.transAxes)
    ax2.text(0.5, headline_y - line_h - 0.18, "MnDOT • MoDOT • FDOT • TxDOT",
             ha="center", fontsize=9, color="#7f8c8d", transform=ax2.transAxes)

    # 48 inherit
    ax2.text(0.5, headline_y - 2 * line_h - 0.13, "48", ha="center", fontsize=28,
             fontweight="bold", color="#c0392b", transform=ax2.transAxes)
    ax2.text(0.5, headline_y - 2 * line_h - 0.22, "inherit from somewhere else",
             ha="center", fontsize=10, transform=ax2.transAxes)
    ax2.text(0.5, headline_y - 2 * line_h - 0.27, "state CIO • OIT • OCTO • Governor EO",
             ha="center", fontsize=9, color="#7f8c8d", transform=ax2.transAxes)

    # 8 contractor-binding (was 7 prior to Idaho correction on 2026-05-11)
    contractor_count = sum(1 for r in rows if r["contractor_binding"] == "Yes")
    ax2.text(0.5, headline_y - 3 * line_h - 0.22, str(contractor_count), ha="center", fontsize=28,
             fontweight="bold", color="#2c3e50", transform=ax2.transAxes)
    ax2.text(0.5, headline_y - 3 * line_h - 0.31, "states bind contractors",
             ha="center", fontsize=10, transform=ax2.transAxes)
    ax2.text(0.5, headline_y - 3 * line_h - 0.36, "IA • KS • OH • MN • LA • DC • NJ • ID",
             ha="center", fontsize=9, color="#7f8c8d", transform=ax2.transAxes)

    # Footer
    fig.text(0.5, 0.005,
             "Transportation AI Policy Tracker, installment 1 of 4 (state DOT layer), refreshed 2026-05-11",
             ha="center", fontsize=8, color="#7f8c8d", style="italic")

    plt.suptitle("Building the Transportation AI Policy Tracker: the state DOT layer",
                 fontsize=14, fontweight="bold", y=0.99)

    plt.savefig(OUT_PNG, dpi=160, bbox_inches="tight", facecolor="white")
    print(f"Chart saved to {OUT_PNG}")


if __name__ == "__main__":
    build_chart()
