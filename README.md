# Car Price Prediction Model

An end-to-end Machine Learning project that predicts the price of used cars based on various vehicle attributes. The project covers data preprocessing, feature engineering, model training, evaluation, and deployment using Streamlit for an interactive web application.

---

## Overview

This project aims to estimate the selling price of a used car using Machine Learning. The model analyzes important vehicle features such as brand, model, manufacturing year, fuel type, transmission, and kilometers driven to generate accurate price predictions.

---

## Features

* Predicts used car prices based on user inputs
* Interactive web application built with Streamlit
* Data preprocessing and feature encoding
* Machine Learning regression model
* Fast and efficient predictions
* Simple and easy-to-use interface

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

---

## Project Structure

```text
Car_price_prediction_model/
│── Car_price_predictor/
│   ├── app.py
│   ├── model.pkl
│   └── car_price_model.ipynb
│
│── Cardetails.csv
│── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/pveeramaniteja-ux/car_price_prediction_model.git
```

### Navigate to the project directory

```bash
cd car_price_prediction_model
```

### Install the required dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Model Serialization using Pickle
9. Streamlit Deployment

---

## Input Features

The model predicts car prices using features such as:

* Brand
* Model
* Manufacturing Year
* Fuel Type
* Transmission
* Kilometers Driven
* Engine Size (if applicable)
* Other vehicle specifications

---

## Output

The application predicts the estimated selling price of a used car based on the information provided by the user.

---

## Future Improvements

* Improve prediction accuracy using advanced regression models.
* Deploy the application on Streamlit Cloud.
* Include additional vehicle specifications.
* Integrate real-time market price data.
* Enhance the user interface and add visualizations.

---

## Author

**Veeramaniteja Pasupuleti**

GitHub: https://github.com/pveeramaniteja-ux

LinkedIn: https://www.linkedin.com/in/veeramaniteja-pasupuleti

---

## License

This project is available for educational and learning purposes.
