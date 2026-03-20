# multi-assay-activity-analysis
Dual-assay analysis of EU-OPENSCREEN data to compare biological readouts and identify misleading or assay-specific activity signals

## Overview
This project analyses two biological assay readouts (confluence and inhibition) from the EU-OPENSCREEN dataset (EOS300008, https://ecbd.eu/assays/EOS300008#scroll-nav__5) 

## Dataset
~2400 compounds tested at 10 µM on cells infected with a virus (which affects cell count by killing and cell morphology by harming cells). Tested in 384 well plates with positive and negative controls on each plate. 

- Two assay readouts:
  - Confluence (cell area)
  - Inhibition (cell count)
- Activity defined as:
  - Confluence >10% OR Inhibition >20%
  

## Objectives
-	Identify the most potent compounds (perform well in both readouts)
- Identify other compounds of interest (differ from any trends, perform well in one readout but not the other)
- Evaluate how control variability affects interpretation
- Look for trends between the two readouts

## Key Findings
### 1. 3 compounds perform very well (>80%) in both readouts:
- These are lead candidates
### 2. Some compounds perform well in the confluence readout but not the inhibition readout:
- This implies that many cells died, but those remaining had normal morphology.
- Further Experiments: test with uninfected cells to see if the compounds themselves reduce cell count without affecting morphology

### 3. Some compounds perform well in the inhibition readout (cell count) but not the confluence readout (cell surface area).
-	This implies that the cells did not die but were still harmed
- Further Experiments: test with uninfected cells to determine if these compounds are directly affecting confluence.
- Further Experiments: test higher concentration to determine if compounds are active enough to reduce death but not potent enough to prevent the virus from harming the cells.

### 4. Large variance in the control values for the inhibition readout (30-140%). 
- This implies the results from this readout are less precise. A compound with a readout of 30% may be as effective as the positive control
- - This adds 4-5 other compounds to our lead candidate list
- Ask the people doing the experiment: is this sort of variance normal for this measurement?
- Ask the people doing the experiment: does the raw data specify which 384-well plate each datapoint is from?
- Ask the people doing the experiment: 'normalising' the controls was mentioned, how specifically was this done?
- - if NO: it would be nice to record this information in future experiments
- - if YES: lets examine this data for trends between plates (do some plates have significantly higher or lower cell counts? if so, can we take this into account or reduce the plate-to-plate variance)
### 5. There is weak correlation, but a broad trend exists between the two readouts:
- As confluence increases, the proportion of compounds with an inhibition readout <20% decreases.
- Almost all compounds that are inactive in the confluence readout have an inhibition readout <50%.
- one compound has very low confluence but high inhibition, which could be worth looking into more
- if the variance of the inhibition controls was reduced, perhaps a higher correlation would be seen

## Results:
## Readout Comparison
Scatter plot of confluence vs inhibition with activity thresholds.
<img src="images/DualAssay.png" width="500">
### Observation
There is weak correlation between the two readouts. Most compounds are inactive in both readouts. Most compounds with low confluence (0-10%) have inhibition <20%, and all compounds with high confluence (>80%) have inhibition >20%.
## Improved Visualisation
Quadrant-coloured scatter plot highlighting readout-specific vs concordant activity.
<img src="images/DualAssay_QuadColour.png" width="500">
## Control Variability
Histogram plot of the control results for the confluence readout:
<img src="images/Control_Histogram_Confluence.png" width="500">

Histogram plot of the control results for the inhibition readout:
<img src="images/Control_Histogram_Inhibition.png" width="500">

### Observation
Negative controls cluster around 0% activity, while positive controls cluster near 100%, but the inhibition assay shows higher variance.
### Implication
Higher variability in the inhibition readout, which increases the risk of misclassifying compounds near the activity threshold, and makes any trend between the two readouts less clear.

## Combining the control and experimental Data
Visualisations incorporating control distributions highlight overlap between experimental signals and negative controls.

<img src="images/DualAssay_hist.png" width="500">

Scatter plot of confluence vs inhibition with activity thresholds, with quadrant colouring, incorporating the negative control histograms as a shaded bar in the actual plot.
<img src="images/DualAssay_bar.png" width="500">

## Limitations
- Plate-level information is not available, preventing assessment of batch effects (did some plates overall have higher or lower inhibition values)
- Single measurements per compound limit statistical confidence


  
