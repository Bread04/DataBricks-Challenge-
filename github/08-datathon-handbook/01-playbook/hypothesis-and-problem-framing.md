# 🔬 The Hypothesis-Driven Framework for Datathons

<!-- markdownlint-disable MD013 -->

> 🟢 **In plain English:** The secret of teams that win premier datathons (like the Citadel Data Open or Harvard/MIT datathons) is that **they never open a Jupyter notebook to start blindly coding**. They begin by asking: *"What are the 3–5 hypotheses about human or operational behavior that could explain this data?"* This guide shows you how to frame problems like a winning team.

---

## 🏛️ Why Hypotheses Win Over Raw Algorithms

Judges at competitive datathons are usually senior data leaders, enterprise sponsors, or quantitative researchers. When a team opens their presentation saying:
> *"We trained an XGBoost model with 500 trees and got 0.84 AUC..."*

Judges tune out. But when a winning team says:
> *"We identified that shipping delays aren't caused by transit distance, but by weekend customs backlog. We formulated 3 behavioral hypotheses, proved them using the data, built a model to quantify the risk, and created an operational scheduling tool that saves 18 hours per container."*

Judges lean forward. That team wins.

---

## 📝 The 3-Step Problem Framing Recipe

When the competition prompt is released at Hour 0, gather your team around a whiteboard or shared Google Doc and execute these three steps:

### Step 1: Find the "Economic / Operational Bottleneck"
Translate the organizer's prompt into a real-world bottleneck:
- **Organizer prompt:** *"Predict patient hospital readmissions within 30 days."*
- **Real-world bottleneck:** *"Hospital beds are blocked by patients who relapse because they lacked follow-up care instructions. If we identify high-risk patients 24 hours before discharge, care coordinators can schedule home visits and prevent costly readmissions."*
- **The Metric that matters:** It's not just accuracy; it's **False Negatives** (missing a sick patient costs $15,000; an unnecessary nurse follow-up call costs $20).

### Step 2: Formulate 3–5 Structured Hypotheses
A good datathon hypothesis connects **Domain Logic** to **Measurable Features**:

```text
Hypothesis Template:
"We hypothesize that [DOMAIN FACTOR] significantly increases [TARGET OUTCOME] 
because [REAL-WORLD MECHANISM]. 
We will test this by measuring [FEATURE OR RATIO]."
```

#### Example Set (Logistics / Supply Chain Datathon):
1. **The Weekend Backlog Hypothesis ($H_1$):** Shipments arriving at ports on Friday evening experience disproportionately higher delays because customs clearance operates with skeleton crews over weekends.
   - *Testable feature:* `is_friday_arrival` paired with `port_congestion_index`.
2. **The Fragility & Weather Interaction Hypothesis ($H_2$):** Temperature fluctuations above $5^\circ\text{C}$ cause perishable goods spoilage only when transit duration exceeds 48 hours.
   - *Testable feature:* Interaction term `temp_variance * transit_hours`.
3. **The Multi-Hop Transfer Lag Hypothesis ($H_3$):** Delays do not accumulate linearly; routes with $\ge 3$ carrier handoffs experience exponential scheduling slippage.
   - *Testable feature:* Non-linear polynomial / bucketed feature `transfer_count ** 2`.

### Step 3: Map Hypotheses to Your Technical Architecture

```text
┌─────────────────────────────────┐
│     Hypothesis Formulation      │  Hour 0–2: Define H1, H2, H3
└─────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│ Targeted Feature Engineering    │  Hour 4–10: Build specific columns 
│ (Test & Validate Signals)       │  designed to prove or disprove H1-H3
└─────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│ Machine Learning Modeling       │  Hour 10–18: Train LightGBM / CatBoost
│ (Quantify Feature Importance)   │  Use SHAP to verify if H1-H3 drove predictions
└─────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│ Interactive Solution & Pitch    │  Hour 24–42: Build simulator sliders around H1-H3
│ (Actionable Human Decisions)    │  Tell judges the complete hypothesis story
└─────────────────────────────────┘
```

---

## 🎯 How to Pitch Hypotheses to Judges

During your 3-minute pitch, structure your narrative around your hypotheses:

1. **Slide 2 (The Problem):** State the real-world operational bottleneck.
2. **Slide 3 (Our Core Hypotheses):** Show the 3 hypotheses you set out to test.
3. **Slide 4 (The Data Findings):** Show 2 clean charts proving $H_1$ and $H_2$ were correct (and honestly mention if $H_3$ was disproven—judges love scientific honesty!).
4. **Slide 5 (The ML Model):** Show that the top features chosen by the model align directly with these validated behavioral hypotheses.
5. **Slide 7 (Live Demo):** Use your Streamlit sliders to adjust the exact variables from $H_1$ and $H_2$ and watch the risk score update live!

This narrative gives your project an intellectual backbone that 95% of competitor teams lack.
