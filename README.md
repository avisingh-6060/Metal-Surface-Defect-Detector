# AI-Based Metal Surface Defect Inspection System

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Project Overview

The **AI-Based Metal Surface Defect Inspection System** is a Deep Learning-powered web application that automatically detects defects on steel surfaces using the **EfficientNetB0** convolutional neural network.

Users can upload a steel surface image, and the application performs real-time defect classification while providing confidence scores, prediction reliability, defect descriptions, maintenance recommendations, interactive visualizations, and a professional PDF inspection report.

This project demonstrates an end-to-end industrial AI workflow by combining **TensorFlow**, **Streamlit**, **Plotly**, and **ReportLab** into a modern web application.

---

# Key Features

- AI-powered steel surface defect detection
- EfficientNetB0 Transfer Learning model
- Real-time image classification
- Professional Streamlit dashboard
- Confidence score analysis
- Prediction reliability indicator
- Detailed defect description
- Intelligent maintenance recommendations
- Interactive probability visualization
- Prediction summary table
- Professional PDF inspection report
- Hindalco-branded inspection report
- Clean and responsive user interface

---

# Detectable Defects

The model detects six different steel surface defects:

- Crazing
- Inclusion
- Patches
- Pitted Surface
- Rolled-in Scale
- Scratches

---

# Deep Learning Model

| Property | Value |
|-----------|-------|
| Model | EfficientNetB0 |
| Framework | TensorFlow / Keras |
| Learning Technique | Transfer Learning |
| Classification Type | Multi-Class |
| Number of Classes | 6 |
| Input Size | 224 × 224 |
| Model Accuracy | 99.2% |

---

# Technology Stack

## Programming Language

- Python

## Deep Learning

- TensorFlow
- Keras
- EfficientNetB0
- Transfer Learning
- Convolutional Neural Network (CNN)

## Web Framework

- Streamlit

## Data Processing

- Pandas
- NumPy

## Visualization

- Plotly

## PDF Generation

- ReportLab

## Image Processing

- Pillow (PIL)

---

# Dataset

This project is trained using the **NEU Metal Surface Defect Dataset**, a benchmark dataset widely used for steel surface defect classification.

The dataset contains six categories of steel surface defects and is commonly used to evaluate deep learning models for industrial quality inspection.

---

# Project Workflow

```text
Steel Surface Image
        │
        ▼
Image Preprocessing
        │
        ▼
EfficientNetB0 Model
        │
        ▼
Defect Prediction
        │
        ▼
Confidence Score
        │
        ▼
Reliability Analysis
        │
        ▼
Defect Description
        │
        ▼
Maintenance Recommendation
        │
        ▼
Interactive Dashboard
        │
        ▼
PDF Inspection Report
```

---

# Project Structure

```text
Metal-Surface-Defect-Detector/
│
├── app.py
├── steel_defect_model.keras
├── class_names.json
├── hindalco_logo.png
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-github-username/Metal-Surface-Defect-Detector.git
```

Move into the project directory

```bash
cd Metal-Surface-Defect-Detector
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# Application Output

The application provides:

- Predicted Defect
- Confidence Score
- Prediction Reliability
- Defect Description
- Maintenance Recommendation
- Interactive Probability Chart
- Prediction Summary Table
- Professional PDF Inspection Report

---

# PDF Inspection Report

The application automatically generates a professional inspection report containing:

- Hindalco Logo
- Report ID
- Inspection Date & Time
- Predicted Defect
- Confidence Score
- Prediction Reliability
- Model Information
- Overall Model Accuracy
- Defect Description
- Maintenance Recommendation
- Professional Footer

---

# Industrial Applications

This project can be applied in:

- Steel Manufacturing
- Surface Quality Inspection
- Industrial Automation
- AI-based Visual Inspection
- Smart Manufacturing
- Quality Control Systems
- Manufacturing Analytics

---

# Future Enhancements

Possible improvements include:

- Live camera-based defect inspection
- Video defect detection
- Grad-CAM explainability
- REST API integration
- Database support
- Cloud deployment
- Industrial IoT integration
- Multi-defect localization

---

# Author

**Avi Singh**

BCA Student | AI & Machine Learning Enthusiast

Developed using **Python**, **TensorFlow**, **EfficientNetB0**, **Streamlit**, **Plotly**, and **ReportLab**.

---

# License

This project is licensed under the **MIT License**.

---

## Support

If you found this project useful, consider giving it a ⭐ on GitHub.