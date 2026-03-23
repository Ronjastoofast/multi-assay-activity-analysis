# multi-assay-activity-analysis

Analysis of EU-OPENSCREEN data to compare activity of compounds as measured by two readouts.

---

## Overview
The dataset is from EU-OPENSCREEN database (EOS300008). The antiviral activity of a set of compounds was measured by two different readouts.
https://ecbd.eu/assays/EOS300008#scroll-nav__5

The goal is to identify active compounds and look for trends or interesting results.
---

## Dataset

- ~2400 compounds tested at 10 µM  
- Cells infected with a virus affecting:
  - cell count (death/growth)
  - cell morphology (damage)  
- 384-well plates with positive and negative controls  

### Readouts
- **Confluence** → cell area (damage)
- **Inhibition** → cell count (survival/growth)

### Activity thresholds (defined by the people who generated the data)
- Confluence > 10%  
- Inhibition > 20%  

---

## Objectives

- Identify lead compounds (those with the best activity across both readouts)  
- Identify trends in the data (does a good confluence correlate with a good inhibition?)
- look for any interesting results, and suggest ways to investigate them
- look for any ways to improve the experiment for next time
---

## Key Findings & Decisions

### 1. Some compounds had high inhibition and high confluence
- 3 compounds show >80% activity in both readouts, so are obvious lead candidate choices

**Interpretation:**  
-	They are the most active compounds! 

**Decision:**  
- Replicate the results, test at lower concentrations for more detailed dose response data
- Carry these compounds forward (more detailed biological assays, tox, pk/pd, etc.)
---
### 2. Control variability impacts interpretation
- Inhibition controls show high variance (30–140%)  

**Interpretation:**  
- compounds with apparently low inhibition might still be very active

**Decision:**  
- Treat inhibition values as a traffic light assay, anything in the >30% range is potentially ‘good’  
- Expand lead set to include borderline compounds 

**Impact:**  
- Adds ~4–5 additional potential lead compounds  

**Recommended actions:**  
- Replicate the results, test at different concentrations for more detailed dose response data
- If we need the inhibition value to differentiate between good and mediocre compounds:
- Look into whether this level of variation is normal for this readout
- If plate-specific data is available, see if plate-to-plate variation in inhibition is responsible for this variation (and if so, test out plate-by-plate normalisation)
- If repeated experiments are planned:
  - record plate-specific data (if this wasn’t done already)
  - try to reduce the variation
  - consider a different readout instead
  
### 3a. Some compounds had high confluence result but not high inhibition
- Cells retain morphology but die/fail to grow

**Interpretation:**  
- possible that either the compounds are directly (negatively) affecting growth, or are reducing the impact of the virus on cell area but not cell count


**Decision:**  
- Deprioritise as primary leads  
- retain as backups in case of issues with lead compounds (toxicity, poor pk/pd)
- keep structures in mind when designing future antiviral compounds and for SAR from this dataset

**Follow-up:**  
- If we need more leads or otherwise want to understand this activity:
- Test in uninfected cells to assess direct cytotoxicity vs antiviral effect  
- Test at higher concentrations to assess if this reflects a weaker activity

---

### 3b. Some compounds had high inhibition but not high confluence

- cell count is good, but cells morphology is different to the control  

**Interpretation:**  
- possible that either the compounds are directly (negatively) affecting cell morphology, or are reducing the impact of the virus on cell area but not cell count

**Decision:**  
- Deprioritise as primary leads, and these compounds are considered less good than compounds with high confluence and low inhibition.
- retain as backups (to the backups) in case of issues with lead compounds (toxicity, poor pk/pd)
- keep structures in mind when designing future antiviral compounds, and for SAR from this dataset

**Follow-up:**  
- If we need more leads or otherwise want to understand this activity:
- Test in uninfected cells to assess direct cytotoxicity of compounds  
- Test at higher concentrations to assess if this reflects a weaker activity

---

### 4. Relationship between readouts

- Weak correlation, but there is a general trend where high confluence compounds have higher inhibition (20-125%) and lower confluence compounds tend to have lower inhibition (-50 – 50% and one outlier at ~80%).

**Interpretation:**  
- the weak correlation could be due to the high variance in the inhibition
- if some compounds directly affect inhibition or confluence this could also explain the weak relationship.

**Decision:**  
- Prioritise compounds with consistent signals across both readouts  
- try to reduce inhibition variance in future runs

---

## Visualisations

### Readout Comparison

Scatter plot of confluence vs inhibition with activity thresholds:

<img src="images/DualAssay.png" width="500">

---

### Quadrant Classification

Quadrant-coloured scatter plot highlighting:
- inactive compounds  
- good activity in one readout or the other  
- good activity in both readouts  

<img src="images/DualAssay_QuadColour.png" width="500">

---

### Control Variability

**Confluence controls:**

<img src="images/Control_Histogram_Confluence.png" width="500">

**Inhibition controls:**

<img src="images/Control_Histogram_Inhibition.png" width="500">

---

### Interpretation

- Negative controls cluster near 0%  
- Positive controls cluster near 100%  
- Inhibition shows significantly higher variance  

---

### Combined View

Overlay of control distributions with experimental data:

<img src="images/DualAssay_hist.png" width="500">

---

Scatter plot with control distributions embedded:

<img src="images/DualAssay_bar.png" width="500">

---

## Limitations

- No plate-level metadata, so cannot assess batch effects  
- Single measurements per compound, so limited statistical confidence  
- Assay variability reduces reliability of threshold-based classification
- No control experiments on uninfected cells to differentiate direct effects of the compounds on the cells from their viral inhibition effect

---

## Key Takeaways

- The confluence data is more reliable than the inhibition data
- some compounds are active by both measures, and are good leads
- some compounds are active by only one measure, and might make good backups but should be tested against uninfected cells

---

## Next Steps
  
- Introduce plate-level metadata to assess batch effects  
- Replicate the measurements of lead compounds (and backup lead compounds, depending on the per-compound cost of further assays)
- look into the SAR of the active compounds
- carry out further testing of lead compounds 

---
