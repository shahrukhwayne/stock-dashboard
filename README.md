# 📊 Stock Data Intelligence Dashboard

## 🚀 Overview

This project is a full-stack financial data platform that fetches, analyzes, and visualizes stock market data in real-time. It provides users with interactive charts, key insights, and a simple machine learning-based price prediction system.

The application demonstrates end-to-end development including data handling, API design, frontend visualization, and deployment.

---

## 🧠 Key Features

* 📈 Real-time stock data using yFinance
* 📊 Interactive charts using React + Chart.js
* 🔍 Company selection (INFY, TCS, RELIANCE)
* 📉 52-week summary (high, low, average)
* ⚖️ Stock comparison API
* 🔮 Machine Learning-based price prediction
* ⚡ API caching for better performance
* 🌐 Fully deployed backend and frontend

---

## 🏗️ Tech Stack

### Backend

* FastAPI
* Pandas, NumPy
* yFinance
* Scikit-learn (ML prediction)
* FastAPI Cache

### Frontend

* React.js
* Chart.js

### Deployment

* Backend: Render
* Frontend: Served via FastAPI (Static Build)

---

## 📡 API Endpoints

### 1. Get Companies

```
/companies
```

### 2. Get Stock Data (Last 30 Days)

```
/data/{symbol}
```

### 3. Get Summary

```
/summary/{symbol}
```

### 4. Compare Stocks

```
/compare?symbol1=INFY&symbol2=TCS
```

### 5. Predict Price (ML)

```
/predict/{symbol}
```

---

## ▶️ How to Run Locally

### 1. Clone Repository

```
git clone https://github.com/your-username/stock-dashboard.git
cd stock-dashboard
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Backend

```
uvicorn main:app --reload
```

### 4. Run Frontend

```
cd frontend
npm install
npm run dev
```

---

## 🌐 Live Demo

🔗 Live App: https://your-app.onrender.com
🔗 API Docs: https://your-app.onrender.com/docs

---

## 📊 How It Works

1. Fetches stock data using yFinance
2. Cleans and processes data using Pandas
3. Serves data via FastAPI APIs
4. React frontend fetches and displays charts
5. Machine learning model predicts next-day price
6. Caching improves performance for repeated requests

---

## 🔮 Machine Learning Model

A simple Linear Regression model is used to predict the next day's stock price based on historical trends.

---

## ⚡ Performance Optimization

* API caching implemented using FastAPI Cache
* Reduced redundant API calls
* Improved response time for frequent requests

---


## 👨‍💻 Author

Mohd Shahrukh

---

## 💡 Future Improvements

* Multi-day prediction
* Advanced ML models (LSTM)
* Better UI/UX design
* Authentication system
* More stock coverage

---

## ⭐ Conclusion

This project demonstrates a complete full-stack data application with real-world financial data, API design, machine learning integration, and deployment.

---
