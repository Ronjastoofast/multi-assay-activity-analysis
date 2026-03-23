"""
Author: Travis Coyle
Project: Dual-assay data interpretation
WHat is it? Several functions to process data from 2 csv files into: positive controls, negative controls, and experimental data, and plot them.

ONE CSV ANALYSIS:
example use = one_readout_ctrl("EOS300008_confluence.csv")
one_readout_ctrl_hist: input one csv and generate separate histograms for the positive control values and the negative control values
ctrl_combined_hist: input one csv and generate histograms for the positive controls and negative controls, on the same plot, with the mean and standard deviations

TWO CSV ANALYSIS:
example use = "dualAssay_bar(
        "EOS300008_confluence.csv",
        "EOS300008_inhibition.csv",
        10,
        20"

active_compounds_hist: input one csv, and generate histograms for the active compounds (pink) and inactive compounds (grey) on the same plot. then plot the histogram for the active compounds alone
dualAssay_hist: input 2 csv's (one for each readout) and the cutoff values for 'active' in each readout. scatter plot of experimental data with histograms of the negative controls
dualAssay_violin: as for dualAssay_hist but violin plots replace the histograms of the control values
dualAssay_bar: as for dualAssay_hist, but the control values are represented by a shaded bar in the plot (more heavily shaded = higher count for that value)
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
reads a csv, selects positive control (entry in 'control' column is 'high') and negative control ('control' column entry is 'low')
plots a histogram of the positive control values, then a separate histogram of the negative control values
INPUTS: path to .csv file for one readout
"""
def one_readout_ctrl_hist(csv):
    rawdata = pd.read_csv(csv)
    neg_ctrl = rawdata[rawdata['control'] == "low"]
    pos_ctrl = rawdata[rawdata['control'] == 'high']

    #negative control analysis
    plt.hist(neg_ctrl["value"], bins=40, label="Negative Control Values Histogram")
    plt.title("Negative Control Values Histogram")
    plt.xlabel('value')
    plt.ylabel('occurrence of value')
    plt.show()

    #positive control analysis
    plt.hist(pos_ctrl["value"], bins=40, label="Positive Control Values Histogram")
    plt.title("Positive Control Values Histogram")
    plt.xlabel('value')
    plt.ylabel('occurrence of value')
    plt.show()





"""
reads a csv, selects positive control (entry in 'control' column is 'high') and negative control ('control' column entry is 'low')
plots histograms of the positive and negative controls on the same plot with the mean and standard deviation
INPUTS: path to .csv file for one readout
"""
def ctrl_combined_hist(csv):
    rawdata = pd.read_csv(csv)
    neg_ctrl = rawdata[rawdata['control'] == "low"]
    pos_ctrl = rawdata[rawdata['control'] == 'high']

    # calculate mean and stdev
    n_mean = neg_ctrl["value"].mean()
    n_std = neg_ctrl["value"].std()

    p_mean = pos_ctrl["value"].mean()
    p_std = pos_ctrl["value"].std()

    # histogram of controls
    plt.hist(neg_ctrl["value"], bins=40, color="red", label="Negative Control Values Histogram")
    plt.hist(pos_ctrl["value"], bins=40, color="blue", label="Positive Control Values Histogram")

    ax = plt.gca()
    ax.axvline(n_mean, linestyle="--", linewidth=2, color="plum", label=f"Negative Ctrl Mean = {p_mean:.2f}")
    ax.axvline(p_mean, linestyle="--", linewidth=2, color="plum", label=f"Positive Ctrl Mean = {p_mean:.2f}")

    ymax = ax.get_ylim()[1]
    xmax = ax.get_xlim()[1]
    ax.text(
        0.5 * xmax, 0.95 * ymax,
        f"Negative Control\nMean: {n_mean:.2f}\nStd:  {n_std:.2f}",
        ha="right", va="top",
        bbox=dict(boxstyle="round", color="red", alpha=0.15, edgecolor="none")
    )
    ax.text(
        0.5 * xmax, 0.5 * ymax,
        f"Positive Control\nMean: {p_mean:.2f}\nStd:  {p_std:.2f}",
        ha="right", va="top",
        bbox=dict(boxstyle="round", color="blue", alpha=0.15, edgecolor="none")
    )

    # plot it
    plt.title("Control Values Histogram (+blue, -red)")
    plt.xlabel('value')
    plt.ylabel('occurrence of value')
    plt.show()

"""
reads a csv, selects active compounds (entry in 'activity' column is 'active') and inactive compounds ('activity' column entry is 'inactive')

plots histograms of the active ans inactive compounds on the same plot 
then plots a histogram of just the active compounds
INPUTS: Path to CSV file for one readout
"""
def active_compounds_hist(csv):
    # make df for test compounds (exclude controls)
    rawdata = pd.read_csv(csv)
    exptl = rawdata[rawdata['control'].isnull()]

    # make df for compounds labelled active
    active = exptl[exptl['activity'] == 'active']
    active_mean = active["value"].mean()
    active_std = active["value"].std()

    # make df for compounds labelled inactive
    inactive = exptl[exptl['activity'] == 'inactive']
    inactive_mean = inactive["value"].mean()
    inactive_std = inactive["value"].std()

    # make marker lines for means, and put mean and stdev on plot
    plt.hist(active["value"], bins=100, alpha=0.35, edgecolor='k', color="fuchsia",
             label="Active vs inactive (grey) compounds Values Histogram")
    plt.hist(inactive["value"], bins=100, alpha=0.35, edgecolor='k', color="grey")
    ax = plt.gca()
    ax.axvline(active_mean, linestyle="--", linewidth=2, color="plum",
               label=f"Active compound Mean = {active_mean:.2f}")
    ax.axvline(inactive_mean, linestyle="--", linewidth=2, color="plum",
               label=f"Inactive compound Mean = {inactive_mean:.2f}")
    ymax = ax.get_ylim()[1]
    xmax = ax.get_xlim()[1]
    ax.text(
        0.9 * xmax, 0.9 * ymax,
        f"Active Compounds:\nMean: {active_mean:.2f}\nStd:  {active_std:.2f}\nInactive Compounds:\nMean: {inactive_mean:.2f}\nStd:  {inactive_std:.2f}",
        ha="right", va="top",
        bbox=dict(boxstyle="round", color="navajowhite", alpha=0.15, edgecolor="none")
    )



    plt.title("Active vs inactive compounds Values Histogram")
    plt.xlabel('value')
    plt.ylabel('occurence of value')
    plt.show()


    ax = plt.gca()
    ax.axvline(active_mean, linestyle="--", linewidth=2, color="plum",
               label=f"Active compound Mean = {active_mean:.2f}")
    plt.hist(active["value"], bins=100, alpha=0.35, edgecolor='k', color="fuchsia",
             label="Active vs inactive (grey) compounds Values Histogram")
    plt.title("Active compounds Histogram")
    plt.xlabel('value')
    plt.ylabel('occurence of value')
    plt.show()





"""
merges two assay CSVs on eos, then visualizes the joint activity as a quadrant-colored scatter plot with cutoff lines and marginal histograms of negative controls.
INPUTS: paths to csv's of the two readouts, and the cutoff value for 'active' designation for each readout
"""
def dual_assay_hist(csv1, csv2, csv1cutoff, csv2cutoff):
    assay1 = pd.read_csv(csv1)
    exptl1 = assay1[assay1['control'].isnull()]
    negctrl1 = assay1[assay1['control'] == "low"]
    # make a dummy assay2 result for the controls
    negctrl1 = negctrl1.copy()
    negctrl1['assay2'] = -5

    assay1label = str(csv1)
    assay1label = assay1label.split("_")[1]
    assay1label = assay1label.split(".")[0]

    assay2 = pd.read_csv(csv2)
    exptl2 = assay2[assay2['control'].isnull()]
    negctrl2 = assay2[assay2['control'] == "low"]
    negctrl2["assay1"] = -5
    assay2label = str(csv2)
    assay2label = assay2label.split("_")[1]
    assay2label = assay2label.split(".")[0]

    # combine them
    exptl2 = exptl2.drop(['control', 'compound_name', 'smiles', 'inchikey', 'concentration', 'activity'], axis=1)
    exptl2 = exptl2.rename(columns={'eos': "eos", "value": f"{assay2label}"})
    combined = pd.merge(left=exptl1, right=exptl2, on="eos")




    # build a category: lets call exptl1 x and exptl2 y
    combined["segment"] = np.select(
        [
            (combined["value"] > csv1cutoff) & (combined[assay2label] > csv2cutoff),
            (combined["value"] > csv1cutoff),
            (combined[assay2label] > csv2cutoff),

        ], ["x & y above", "x above", "y above"],
        default="below both",
    )
    sns.set_context("talk")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax = sns.scatterplot(
        legend=False,
        data=combined, x="value", y=assay2label,
        hue="segment",
        hue_order=["below both", "x above", "y above", "x & y above"],
        palette={"below both": "black", "x above": "blue",
                 "y above": "red", "x & y above": "purple"},
        s=40, alpha=0.8
    )
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position('right')
    ax.tick_params(axis='y', right=True, labelright=True, left=False, labelleft=False)
    ax.set_title(f"{assay1label} vs {assay2label}")


    # reference lines
    ax.axvline(csv1cutoff, ls="--", lw=1)
    ax.axhline(csv2cutoff, ls="--", lw=1)

    ax.set_xlabel(f"{assay1label}")
    ax.set_ylabel(f"{assay2label}")

    # inset histogram
    # assay 1 is the X axis
    # so negctrl1 needs to go on the X axis
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(ax)
    ax_top = divider.append_axes("top", 1.0, pad=0.1, sharex=ax)  # height in inches
    ax_left = divider.append_axes("left", 1.0, pad=0.1, sharey=ax)

    ax_top.hist(negctrl1["value"], bins=20, color="lightgrey")
    ax_left.hist(negctrl2["value"], bins=20, orientation="horizontal", color="lightgrey")

    # after you've drawn the histogram on ax_hist
    for spine in ["top", "right", "left", "bottom"]:
        ax_top.spines[spine].set_visible(False)  # remove the box
    ax_top.tick_params(left=False, labelleft=False)  # hide y (count) ticks & labels
    ax_top.tick_params(bottom=False, labelbottom=False)
    ax_top.patch.set_alpha(0)
    ax_top.grid(False)  # optional: no grid

    for spine in ["top", "right", "left", "bottom"]:
        ax_left.spines[spine].set_visible(False)  # remove the box
    ax_left.tick_params(bottom=False, labelbottom=False)  # hide y (count) ticks & labels
    ax_left.tick_params(left=False, labelleft=False)
    ax_left.patch.set_alpha(0)  # make background transparent
    ax_left.invert_xaxis()
    ax_left.grid(False)


    plt.tight_layout()
    plt.show()

    best = combined[combined["segment"] == "x & y above"]
    # print(best["compound_name"])


"""
merges two assay CSVs on eos, then visualizes the joint activity as a quadrant-colored scatter plot with cutoff lines and marginal violin plots of negative controls.
INPUTS: paths to csv's of the two readouts, and the cutoff value for 'active' designation for each readout
"""
def dual_assay_violin(csv1, csv2, csv1cutoff, csv2cutoff):
    # reading in and procesing
    assay1 = pd.read_csv(csv1)
    exptl1 = assay1[assay1['control'].isnull()]
    negctrl1 = assay1[assay1['control'] == "low"]
    # make a dummy assay2 result for the controls
    negctrl1 = negctrl1.copy()
    negctrl1['assay2'] = -5
    assay1label = str(csv1)
    assay1label = assay1label.split("_")[1]
    assay1label = assay1label.split(".")[0]

    assay2 = pd.read_csv(csv2)
    exptl2 = assay2[assay2['control'].isnull()]
    negctrl2 = assay2[assay2['control'] == "low"]
    negctrl2["assay1"] = -5
    assay2label = str(csv2)
    assay2label = assay2label.split("_")[1]
    assay2label = assay2label.split(".")[0]

    # merge
    exptl2 = exptl2.drop(['control', 'compound_name', 'smiles', 'inchikey', 'concentration', 'activity'], axis=1)
    exptl2 = exptl2.rename(columns={'eos': "eos", "value": f"{assay2label}"})
    combined = pd.merge(left=exptl1, right=exptl2, on="eos")

    # plots

    # quadrant coloring
    combined["segment"] = np.select(
        [
            (combined["value"] > csv1cutoff) & (combined[assay2label] > csv2cutoff),
            (combined["value"] > csv1cutoff),
            (combined[assay2label] > csv2cutoff),

        ], ["x & y above", "x above", "y above"],
        default="below both",
    )
    # scatter plot
    sns.set_context("talk")
    fig, ax_scatter = plt.subplots(figsize=(7, 5))
    ax_scatter = sns.scatterplot(
        legend=False,
        data=combined, x="value", y=assay2label,
        hue="segment",
        hue_order=["below both", "x above", "y above", "x & y above"],
        palette={"below both": "black", "x above": "blue",
                 "y above": "red", "x & y above": "purple"},
        s=40, alpha=0.8
    )
    ax_scatter.yaxis.tick_right()
    ax_scatter.yaxis.set_label_position('right')
    ax_scatter.tick_params(axis='y', right=True, labelright=True, left=False, labelleft=False)
    ax_scatter.set_title(f"{assay1label} vs {assay2label}")

    # reference lines
    ax_scatter.axvline(csv1cutoff, ls="--", lw=1, color="black")
    ax_scatter.axhline(csv2cutoff, ls="--", lw=1, color="black")

    ax_scatter.set_xlabel(f"{assay1label}")
    ax_scatter.set_ylabel(f"{assay2label}")

    #  inset violinplots
    # assay 1 is the X axis
    # so negctrl1 needs to go on the X axis

    xlim = ax_scatter.get_xlim()
    ylim = ax_scatter.get_ylim()

    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(ax_scatter)
    ax_top = divider.append_axes("top", 1.0, pad=0.1, sharex=ax_scatter)  # height in inches
    ax_left = divider.append_axes("left", 1.0, pad=0.1, sharey=ax_scatter)

    sns.violinplot(
        x=negctrl1["value"],
        orient="v",  # horizontal violin along the shared X axis
        ax=ax_top,
        inner="box",
        cut=0,  # don’t extend beyond data range
        scale="count"
    )

    sns.violinplot(
        y=negctrl2["value"],
        orient="h",  # horizontal violin along the shared X axis
        ax=ax_left,
        inner="box",
        # cut=0,  # don’t extend beyond data range
        density_norm="count"
    )


    ax_scatter.set_xlim(xlim)
    ax_scatter.set_ylim(ylim)
    ax_top.set_xlim(xlim)
    ax_left.set_ylim(ylim)

    for spine in ["top", "right", "left", "bottom"]:
        ax_top.spines[spine].set_visible(False)  # remove the box
    ax_top.tick_params(left=False, labelleft=False)  # hide y (count) ticks & labels
    ax_top.tick_params(bottom=False, labelbottom=False)
    ax_top.patch.set_alpha(0)
    ax_top.grid(False)
    ax_top.set(xlabel=None, ylabel=None)  # remove label

    for spine in ["top", "right", "left", "bottom"]:
        ax_left.spines[spine].set_visible(False)  # remove the box
    ax_left.tick_params(bottom=False, labelbottom=False)  # hide y (count) ticks & labels
    ax_left.tick_params(left=False, labelleft=False)
    ax_left.patch.set_alpha(0)  # make background transparent
    ax_left.invert_xaxis()
    ax_left.grid(False)
    ax_left.set(xlabel=None, ylabel=None)

    plt.tight_layout()
    plt.show()

    best = combined[combined["segment"] == "x & y above"]



def dual_assay_bar(csv1, csv2, csv1cutoff, csv2cutoff):
    # reading in and processing
    assay1 = pd.read_csv(csv1)
    exptl1 = assay1[assay1['control'].isnull()]
    negctrl1 = assay1[assay1['control'] == "low"]
    # make a dummy assay2 result for the controls
    negctrl1 = negctrl1.copy()
    negctrl1['assay2'] = -5
    assay1label = str(csv1)
    assay1label = assay1label.split("_")[1]
    assay1label = assay1label.split(".")[0]

    assay2 = pd.read_csv(csv2)
    exptl2 = assay2[assay2['control'].isnull()]
    negctrl2 = assay2[assay2['control'] == "low"]
    negctrl2["assay1"] = -5
    assay2label = str(csv2)
    assay2label = assay2label.split("_")[1]
    assay2label = assay2label.split(".")[0]

    # merge the dataframes
    exptl2 = exptl2.drop(['control', 'compound_name', 'smiles', 'inchikey', 'concentration', 'activity'], axis=1)
    exptl2 = exptl2.rename(columns={'eos': "eos", "value": f"{assay2label}"})
    combined = pd.merge(left=exptl1, right=exptl2, on="eos")

    #  make plots

    # quadrant coloring
    combined["segment"] = np.select(
        [
            (combined["value"] > csv1cutoff) & (combined[assay2label] > csv2cutoff),
            (combined["value"] > csv1cutoff),
            (combined[assay2label] > csv2cutoff),

        ], ["x & y above", "x above", "y above"],
        default="below both",
    )
    # scatter plot
    sns.set_context("talk")
    fig, ax_scatter = plt.subplots(figsize=(7, 5))
    ax_scatter = sns.scatterplot(
        legend=False,
        data=combined, x="value", y=assay2label,
        hue="segment",
        hue_order=["below both", "x above", "y above", "x & y above"],
        palette={"below both": "black", "x above": "blue",
                 "y above": "red", "x & y above": "purple"},
        s=40, alpha=0.8
    )
    ax_scatter.yaxis.tick_right()
    ax_scatter.yaxis.set_label_position('right')
    ax_scatter.tick_params(axis='y', right=True, labelright=True, left=False, labelleft=False)
    ax_scatter.set_title(f"{assay1label} vs {assay2label}")

    # reference lines
    ax_scatter.axvline(csv1cutoff, ls="--", lw=1, color="black")
    ax_scatter.axhline(csv2cutoff, ls="--", lw=1, color="black")

    ax_scatter.set_xlabel(f"{assay1label}")
    ax_scatter.set_ylabel(f"{assay2label}")
    xlim = ax_scatter.get_xlim()
    ylim = ax_scatter.get_ylim()


    #  make 'ydata', choose series for the hist
    y_data = negctrl2["value"]

    from matplotlib import cm

    from matplotlib.colors import Normalize
    y_series_for_hist = y_data


    y_series_for_hist = y_series_for_hist.dropna().astype(float).to_numpy()
    if y_series_for_hist.size == 0:
        print("[heatstrip] no data") # bail out cleanly
    else:
        # current axis limits
        xl = ax_scatter.get_xlim()
        yl = ax_scatter.get_ylim()
        y_increasing = (yl[1] > yl[0])

        # find effective vertical span for hist
        bins = 4
        counts, edges = np.histogram(y_series_for_hist, bins=bins)
        # indices where counts > 0
        nz = np.flatnonzero(counts > 0)
        if nz.size == 0:
            print("[heatstrip] all-zero histogram; try more data or fewer bins")
        else:
            i_lo, i_hi = nz[0], nz[-1]  # first/last non-zero bin
            y_lo, y_hi = edges[i_lo], edges[i_hi + 1]  # span of the histogram

            # keep orientation consistent with the current axis (handles inverted y)
            y_min_plot, y_max_plot = (y_lo, y_hi) if y_increasing else (y_hi, y_lo)

            # vertical profile (counts along y) to create a gradient
            centers = 0.5 * (edges[:-1] + edges[1:])
            y_samples = np.linspace(min(y_lo, y_hi), max(y_lo, y_hi), 400)
            vals = np.interp(y_samples, centers, counts.astype(float), left=0.0, right=0.0)

            # if constant, nudge so a colormap can show variation
            vmin, vmax = float(vals.min()), float(vals.max())
            if np.isclose(vmin, vmax):
                vmax = vmin + (abs(vmin) + 1e-9) * 1e-3
            norm = Normalize(vmin=vmin, vmax=vmax)
            vals_norm = norm(vals)

            #  vertical gradient stretched across full x-range
            grad_img = np.tile(vals_norm.reshape(-1, 1), (1, 200))  # (Ny x Nx), no smoothing

            ax_scatter.imshow(
                grad_img,
                extent=[xl[0], xl[1], y_min_plot, y_max_plot],  # full width, histogram’s y-span
                origin="lower",
                aspect="auto",
                cmap=cm.binary,
                alpha=0.8,  # opaque; reduce to see points through it
                zorder=1.1,  # under most scatter points (raise if needed)
                interpolation="nearest",
            )

            # restore original limits
            ax_scatter.set_xlim(xl)
            ax_scatter.set_ylim(yl)

    x_series_for_hist = negctrl1["value"]
    from matplotlib import cm
    from matplotlib.colors import Normalize

    x_series_for_hist = x_series_for_hist.dropna().astype(float).to_numpy()
    if x_series_for_hist.size == 0:
        print("[heatstrip] no data")
    else:
        #current axis limits
        xl = ax_scatter.get_xlim()
        yl = ax_scatter.get_ylim()
        x_increasing = (xl[1] > xl[0])

        # find  effective vertical span
        bins = 4
        counts, edges = np.histogram(x_series_for_hist, bins=bins)
        # indices where counts > 0
        nzx = np.flatnonzero(counts > 0)
        if nzx.size == 0:
            print("[heatstrip] all-zero histogram; try more data or fewer bins")
        else:
            i_lo, i_hi = nzx[0], nzx[-1]  # first/last non-zero bin
            x_lo, x_hi = edges[i_lo], edges[i_hi + 1]  # span of the histogram

            # keep orientation consistent with the current axis (handles inverted y)
            x_min_plot, x_max_plot = (x_lo, x_hi) if x_increasing else (x_hi, x_lo)

            # vertical profile (counts along y) to create a gradient
            centers = 0.5 * (edges[:-1] + edges[1:])
            x_samples = np.linspace(min(x_lo, x_hi), max(x_lo, x_hi), 400)
            vals = np.interp(x_samples, centers, counts.astype(float), left=0.0, right=0.0)

            # if constant, nudge so a colormap can show variation
            vmin, vmax = float(vals.min()), float(vals.max())
            if np.isclose(vmin, vmax):
                vmax = vmin + (abs(vmin) + 1e-9) * 1e-3
            norm = Normalize(vmin=vmin, vmax=vmax)
            vals_norm = norm(vals)
            # build a horizontal gradient image
            # vals_norm is 1D over x_samples, make it a single row
            grad_row2 = vals_norm.reshape(1, -1)
            grad_img2 = np.tile(grad_row2, (200, 1))

            # preserve current axis limits/orientation
            y_increasing = (yl[1] > yl[0])
            y0, y1 = (yl[0], yl[1]) if y_increasing else (yl[1], yl[0])

            # draw a vertical strip: x-span = histogram support, y-span = full plot
            im2 = ax_scatter.imshow(
                grad_img2,
                extent=[x_min_plot, x_max_plot, y0, y1],
                origin="lower",
                aspect="auto",
                cmap=cm.binary,
                alpha=0.8,
                zorder=1.1,
                interpolation="nearest",
            )
            #restore original limits
            ax_scatter.set_xlim(xl)
            ax_scatter.set_ylim(yl)

    ax_scatter.set_xlim(xlim)
    ax_scatter.set_ylim(ylim)


    plt.tight_layout()
    plt.show()

    best = combined[combined["segment"] == "x & y above"]


if __name__ == "__main__":
    dual_assay_violin(
        "EOS300008_confluence.csv",
        "EOS300008_inhibition.csv",
        10,
        20
    )