#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def simple(title, l1, l2):
    if title == "Loans":
        labels = ["Paid", "Remaining"]
        outer_colors = ["#7fec61", "#fb4444"]
    else:
        labels = ["Balance", "Expenses"]
        outer_colors = ["#ffa64d", "#80ffff"]

    sizes = [l1, l2]

    fig, ax = plt.subplots()
    tmp = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=outer_colors, pctdistance=0.85)

    # Inner pie to make a donut shape
    inner_sizes = [15]
    inner_colors = ["white"]
    ax.pie(inner_sizes, colors=inner_colors, radius=0.6)

    inner_title = title
    ax.text(0, 0, inner_title, ha='center', va='center', fontsize=17, fontweight='bold', color='black')

    for text in tmp[1]:
        text.set_fontsize(15)

    # To make sure pie is a circle
    ax.axis('equal')

    return plt


def cat(c1, c2, c3, c4, c5, c6, c7, c8):
    labels = ["utilities", "food", "fuel", "shopping", "groceries", "subscription", "emi", "other"]
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    recipe = ["utilities",
              "food",
              "fuel",
              "shopping",
              "groceries",
              "subscriptinos",
              "emis",
              "other",
              ]

    data = [c1, c2, c3, c4, c5, c6, c7, c8]

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    inner_sizes = [15]
    inner_colors = ["white"]
    ax.pie(inner_sizes, colors=inner_colors, radius=0.6)

    inner_title = "Categories"
    ax.text(0, 0, inner_title, ha='center', va='center', fontsize=20, fontweight='bold', color='black')


    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(recipe[i],fontsize=23, xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)

    return plt


def bar(l1, l2):
    cat = (
        "Stocks",
        "MF",
        "Gold",
        "Assets"
    )
    weight_counts = {
        "previous": np.array(l2),
        "new investments": np.array(l1),
    }
    width = 0.4

    fig, ax = plt.subplots()
    bottom = np.zeros(4)

    for boolean, weight_count in weight_counts.items():
        p = ax.bar(cat, weight_count, width, label=boolean, bottom=bottom)
        bottom += weight_count

    ax.legend(loc="upper right")

    return plt
