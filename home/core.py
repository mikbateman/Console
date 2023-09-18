#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def simple(title, l1, l2):
    labels = ["Paid", "Remaining"] if title == "Loans" else ["Balance", "Expenses"]
    sizes = [l1, l2]

    outer_colors = ["#7fec61", "#fb4444"]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=outer_colors, pctdistance=0.85)

    # Inner pie to make a donut shape
    inner_sizes = [15]
    inner_colors = ["white"]
    ax.pie(inner_sizes, colors=inner_colors, radius=0.6)

    inner_title = title
    ax.text(0, 0, inner_title, ha='center', va='center', fontsize=14, fontweight='bold', color='black')

    # To make sure pie is a circle
    ax.axis('equal')

    return plt


def cat(c1, c2, c3, c4, c5, c6, c7):
    labels = ["utilities", "food", "entertainment", "groceries", "subscription", "emi", "other"]
    sizes = [c1, c2, c3, c4, c5, c6, c7]

    fig, ax = plt.subplots()
    wedges, texts = ax.pie(sizes, wedgeprops=dict(width=0.5), startangle=-40)
    ax.pie(sizes, autopct='%1.1f%%', startangle=140, pctdistance=0.85)

    # Inner pie to make a donut shape
    inner_sizes = [15]
    inner_colors = ["white"]
    ax.pie(inner_sizes, colors=inner_colors, radius=0.6)

    inner_title = "Categories"
    ax.text(0, 0, inner_title, ha='center', va='center', fontsize=14, fontweight='bold', color='black')

    # Different kind of annotations
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)

    return plt
