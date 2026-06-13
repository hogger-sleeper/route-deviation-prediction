# Route Deviation Prediction Framework

## Overview

This project implements a Route Deviation Prediction Framework based on machine learning and deep learning techniques.

The framework reconstructs delivery routes, computes route quality metrics, generates route deviation labels, and compares multiple predictive models for route deviation detection and regression.

---

## Objectives

- Reconstruct planned and actual delivery routes
- Compute route quality metrics
  - RQS (Route Quality Score)
  - EDS (Edit Distance Score)
  - DDS (Distance Deviation Score)
- Generate route deviation labels
- Train and evaluate multiple machine learning and deep learning models
- Compare model performance against the reference research paper

---

## Dataset Features

| Feature | Description |
|----------|------------|
| Route ID | Route identifier |
| Driver ID | Driver identifier |
| Country | Country code |
| Week ID | Week identifier |
| Day of Week | Day number |
| Planned Route | Planned stop sequence |
| Actual Route | Actual stop sequence |
| Planned Stop Count | Number of planned stops |
| Actual Stop Count | Number of actual stops |
| Planned Distance | Planned route distance |
| Actual Distance | Actual route distance |
| RQS | Route Quality Score |
| EDS | Edit Distance Score |
| DDS | Distance Deviation Score |
| Label | D (Deviation) / ND (No Deviation) |

---

## Project Structure

```text
route_deviation_project
│
├── notebook
│   ├── 01_dataset_exploration.ipynb
│   ├── 02_route_reconstruction.ipynb
│   ├── 03_ml_processing.ipynb
│   ├── 04_random_forest_classifier.ipynb
│   ├── 05_random_forest_regressor.ipynb
│   ├── 06_mlp_benchmark.ipynb
│   ├── 07_lstm_regression.ipynb
│   ├── 08_attention_regression.ipynb
│   ├── 09_cnn_regression.ipynb
│   ├── 10_lstm_classification.ipynb
│   ├── 11_attention_classification.ipynb
│   ├── 12_model_comparison.ipynb
│   ├── 13_results_analysis.ipynb
│   └── 14_hyperparameter_tuning.ipynb
│
├── src
│   ├── metrics
│   ├── preprocessing
│   ├── models
│   └── utils
│
├── outputs
├── requirements.txt
└── README.md
```

---

## Models Implemented

### Classification Models

- Random Forest Classifier
- MLP Classifier
- LSTM Classifier
- Attention-based Classifier

### Regression Models

- Random Forest Regressor
- LSTM Regressor
- Attention-based Regressor
- CNN Regressor

---

## Classification Results

| Model | Accuracy |
|---------|---------|
| Random Forest | 0.7780 |
| MLP | 0.7148 |
| LSTM | 0.7644 |
| Attention | 0.7265 |

---

## Regression Results

| Model | R² Score |
|---------|---------|
| Random Forest | 0.4225 |
| LSTM | 0.3558 |
| Attention | 0.3312 |
| CNN | 0.4153 |

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- TensorFlow / Keras
- Matplotlib
- Jupyter Notebook

---

## Installation

```bash
git clone https://github.com/hogger-sleeper/route-deviation-prediction.git

cd route-deviation-prediction

pip install -r requirements.txt
```

---

## Key Findings

- Random Forest achieved the highest classification accuracy.
- Random Forest achieved the highest regression performance.
- Deep learning models produced competitive results.
- The implementation successfully reproduces the route deviation prediction pipeline described in the reference paper.

---

## Author

Vaibhav Mahesh

B.Tech Computer Science and Business Systems

SASTRA Deemed University
