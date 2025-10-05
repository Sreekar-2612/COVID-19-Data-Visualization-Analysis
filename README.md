# COVID-19 Data Analysis & Visualization

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 Overview
This project analyzes global COVID-19 data using Python, providing insights into **cases, deaths, and vaccination trends** across countries.  
Data source: [Kaggle COVID-19 Dataset by Bolkonsky](https://www.kaggle.com/datasets/bolkonsky/covid19)

---

## 🛠 Features

- **Data Cleaning & Preprocessing**
  - Handles missing or inconsistent data.
  - Converts dates to proper datetime format.
  - Fills missing numeric values and dynamically handles missing columns.

- **Exploratory Data Analysis**
  - Counts and summaries for total cases, deaths, and vaccinations per country.
  - Trend analysis over time for cases, deaths, and vaccinations.
  - Top 10 countries by cases, deaths, and vaccinations.

- **Visualizations**
  - Static plots with **Matplotlib & Seaborn** (bar charts, line plots)
  - Interactive visualizations with **Plotly Express** (scatter/bubble charts)
  - Annotated charts for better readability

- **Insight Summary**
  - Highlights countries with highest cases, deaths, and vaccinations.

---

## 📂 Dataset

- Kaggle: [Bolkonsky COVID-19 Dataset](https://www.kaggle.com/datasets/bolkonsky/covid19)
- Contains daily country-wise data:
  - `total_cases`, `new_cases`
  - `total_deaths`, `new_deaths`
  - `total_vaccinations`
  - `population`

---

## 💻 Technologies Used

- Python 3.8+
- Pandas, NumPy
- Matplotlib, Seaborn
- Plotly Express

---

## 📈 Key Insights

- Total countries tracked: `X`
- Country with highest total cases: `COUNTRY_NAME`
- Country with highest total deaths: `COUNTRY_NAME`
- Country with highest total vaccinations: `COUNTRY_NAME` (if available)

*(These values are dynamically calculated in the script.)*

---

