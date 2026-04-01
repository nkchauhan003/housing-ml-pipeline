# End-to-End Machine Learning Pipeline (House Price Prediction)

## Project Overview

This project demonstrates a complete **end-to-end machine learning pipeline** in Python to predict house prices using structured CSV data. 

---

## Problem Statement

Build a regression model that predicts **house prices** based on features such as:

* Area
* Bedrooms
* Bathrooms
* Stories
* Parking
* Age

---

## Tech Stack

* **pandas:** Data loading & manipulation
* **numpy:** Numerical operations
* **scikit-learn:** ML pipeline, preprocessing, modeling
* **matplotlib:** Visualization
* **seaborn:** Statistical plots & EDA
* **flask:** Model deployment as API

---

## Project Structure

```
housing-ml-pipeline/
│
├── data/
│   ├── raw/
│   │   └── housing.csv
│   └── processed/
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── pipeline/
│   └── utils/
│
├── models/
│   └── housing_model.pkl
│
├── app/
│   └── app.py
│
├── config/
│   └── config.yaml
│
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nkchauhan003/housing-ml-pipeline.git
cd housing-ml-pipeline
```

---

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Dataset

The dataset is a CSV file (`housing.csv`) containing housing features and target price.

Example:

```
area,bedrooms,bathrooms,stories,parking,age,price
1500,3,2,2,1,5,400000
```

---

## Workflow

### 1. Data Loading

* Load CSV using pandas

### 2. Data Cleaning

* Handle missing values
* Remove duplicates

### 3. Exploratory Data Analysis (EDA)

* Correlation heatmap
* Distribution plots

### 4. Feature Engineering

* Feature selection
* Feature scaling

### 5. Model Training

* Linear Regression model
* Pipeline with StandardScaler

### 6. Evaluation

* RMSE
* R² Score

### 7. Model Saving

* Save model using pickle

### 8. Deployment

* Serve predictions via Flask API

---

## Running the Project

### Train Model

```bash
python src/models/train_model.py
```

---

### Run API

```bash
python app/app.py
```

---

## API Usage

### Endpoint:

```
POST /predict
```

### Sample Request:

```curl
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"input": [2500, 4, 3, 2, 2, 5]}'
```

### Sample Response:

```json
{
  "prediction": [
    555462.6865671641
  ]
}
```
