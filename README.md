# multi-assay-activity-analysis

Dual-assay analysis of EU-OPENSCREEN data to compare biological readouts, identify misleading signals, and guide compound selection decisions.

---

## Overview

This project analyses two biological assay readouts (confluence and inhibition) from the EU-OPENSCREEN dataset (EOS300008):

https://ecbd.eu/assays/EOS300008#scroll-nav__5

The goal is not only to identify active compounds, but to determine:
- which signals are reliable
- which are misleading or assay-specific
- how this affects compound selection and follow-up strategy

---

## Dataset

- ~2400 compounds tested at 10 µM  
- Cells infected with a virus affecting:
  - cell count (death/growth)
  - cell morphology (damage)  
- 384-well plates with positive and negative controls  

### Readouts
- **Confluence** → cell area (morphology)
- **Inhibition** → cell count (survival/growth)

### Activity thresholds (defined concurrently with data generation)
- Confluence > 10%  
- Inhibition > 20%  

---

## Objectives

- Identify high-confidence lead compounds with consistent activity across both readouts  
- Identify discordant compounds and determine whether differences reflect biology or assay artefact  
- Evaluate reliability of each readout and its impact on compound classification  
- Define decision criteria for prioritising compounds and designing follow-up experiments  

---

## Key Findings & Decisions

### 1. High-confidence lead compounds

- 3 compounds show >80% activity in both readouts  

**Decision:**  
- Prioritise these as lead candidates  
- Suitable for follow-up optimisation and validation  

---

### 2. Confluence-active, inhibition-inactive compounds

- High confluence, low inhibition  

**Interpretation:**  
- Cells retain morphology but die/fail to grow → compounds likely not preventing cytotoxicity  
- May reflect assay-specific or indirect effects  

**Decision:**  
- Deprioritise as primary leads  
- Only pursue if supported by orthogonal assays  

**Follow-up:**  
- Test in uninfected cells to assess direct cytotoxicity vs antiviral effect  
- Test at higher concentrations to assess if this reflects a weaker activity

---

### 3. Inhibition-active, confluence-inactive compounds

- High inhibition, low confluence  

**Interpretation:**  
- Cells survive but remain morphologically damaged  
- Suggests partial biological effect or insufficient potency  

**Decision:**  
- Treat as secondary candidates  
- Potential starting points for optimisation  

**Follow-up:**  
- Test at higher concentrations  
- Assess whether increased potency improves confluence  
- Test in uninfected cells to see if compounds are directly affecting cell morphology

---

### 4. Control variability impacts interpretation

- Inhibition controls show high variance (30–140%)  

**Interpretation:**  
- Reduced confidence in inhibition readout  
- Increased risk of misclassifying compounds near threshold  

**Decision:**  
- Treat inhibition values in the >30% range as uncertain  
- Expand lead set to include borderline compounds  

**Impact:**  
- Adds ~4–5 additional potential lead compounds  

**Recommended actions:**  
- Investigate plate-level effects (batch variability)  on inhibition readout
- Review control normalisation methods  
- If repeated experiments are planned:
  - improve assay robustness  
  - reduce variance before relying on inhibition readout for decisions  

---

### 5. Relationship between readouts

- Weak overall correlation between confluence and inhibition  

**Interpretation:**  
- Readouts capture different biological effects  
- Agreement between them increases confidence  
- Disagreement highlights potential artefacts or distinct mechanisms  

**Decision:**  
- Prioritise compounds with consistent signals across both readouts  
- Use discordant results to guide targeted follow-up experiments  

---

## Visualisations

### Readout Comparison

Scatter plot of confluence vs inhibition with activity thresholds:

<img src="images/DualAssay.png" width="500">

---

### Quadrant Classification

Quadrant-coloured scatter plot highlighting:
- inactive compounds  
- readout-specific activity  
- concordant activity  

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

**Implication:**  
- Lower precision in inhibition readout  
- Reduced confidence in marginal activity calls  

---

### Combined View

Overlay of control distributions with experimental data:

<img src="images/DualAssay_hist.png" width="500">

---

Enhanced scatter plot with control distributions embedded:

<img src="images/DualAssay_bar.png" width="500">

---

## Limitations

- No plate-level metadata → cannot assess batch effects  
- Single measurements per compound → limited statistical confidence  
- Assay variability reduces reliability of threshold-based classification  

---

## Key Takeaways

- Not all activity signals are equally reliable  
- Control variability can directly impact decision-making  
- Discordant readouts are not noise — they provide insight into mechanism or assay limitations  
- Structuring experimental data around reliability and interpretation improves compound prioritisation  

---

## Next Steps

- Improve assay consistency (especially inhibition readout)  
- Incorporate replicate measurements to increase confidence  
- Introduce plate-level metadata to assess batch effects  
- Develop more robust criteria for defining activity beyond simple thresholds  

---
