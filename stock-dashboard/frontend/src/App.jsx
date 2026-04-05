import React, { useState } from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend
);

function App() {
  const [activeTab, setActiveTab] = useState("data");
  const [chartData, setChartData] = useState({});
  const [symbol, setSymbol] = useState("INFY");
  const [loading, setLoading] = useState(false);

  // 📊 Normal data
  const loadData = async () => {
    setLoading(true);

    try {
      const res = await fetch(`http://127.0.0.1:8000/data/${symbol}`);
      const data = await res.json();

      const labels = data.map(i => i.Date.split("T")[0]);
      const prices = data.map(i => i.Close);

      setChartData({
        labels,
        datasets: [
          {
            label: `${symbol} Price`,
            data: prices,
            borderColor: "#00ffcc",
            tension: 0.4,
            borderWidth: 3
          }
        ]
      });
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  // 🔮 Prediction view
  const loadPrediction = async () => {
    setLoading(true);

    try {
      const res = await fetch(`http://127.0.0.1:8000/data/${symbol}`);
      const data = await res.json();

      const predRes = await fetch(`http://127.0.0.1:8000/predict/${symbol}`);
      const predData = await predRes.json();

      const labels = data.map(i => i.Date.split("T")[0]);
      const prices = data.map(i => i.Close);

      const predictedPrice = predData.prediction;

      setChartData({
        labels: [...labels, "Next Day"],
        datasets: [
          {
            label: "Actual",
            data: prices,
            borderColor: "#00ffcc",
            borderWidth: 3,
            tension: 0.4
          },
          {
            label: "Prediction",
            data: [...prices, predictedPrice],
            borderColor: "#ff4d4d",
            borderDash: [6, 6],
            borderWidth: 3,
            tension: 0.4
          }
        ]
      });
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div
      style={{
        padding: "20px",
        background: "#0f172a",
        color: "white",
        minHeight: "100vh"
      }}
    >
      <h2>📊 Stock Dashboard</h2>

      {/* 🔘 Tabs */}
      <div style={{ marginBottom: "15px" }}>
        <button
          onClick={() => setActiveTab("data")}
          style={{
            marginRight: "10px",
            background: activeTab === "data" ? "#00ffcc" : "#222",
            color: activeTab === "data" ? "#000" : "#fff"
          }}
        >
          📊 Data
        </button>

        <button
          onClick={() => setActiveTab("prediction")}
          style={{
            background: activeTab === "prediction" ? "#ff4d4d" : "#222",
            color: "#fff"
          }}
        >
          🔮 Prediction
        </button>
      </div>

      {/* 🔽 Symbol select */}
      <select onChange={(e) => setSymbol(e.target.value)}>
        <option value="INFY">INFY</option>
        <option value="TCS">TCS</option>
        <option value="RELIANCE">RELIANCE</option>
      </select>

      {/* 🔘 Action button */}
      <div style={{ marginTop: "10px" }}>
        {activeTab === "data" ? (
          <button onClick={loadData} disabled={loading}>
            {loading ? "Loading..." : "Load Data"}
          </button>
        ) : (
          <button onClick={loadPrediction} disabled={loading}>
            {loading ? "Predicting..." : "Predict Price"}
          </button>
        )}
      </div>

      {/* 📈 Chart */}
      <div style={{ marginTop: "20px" }}>
        {chartData.labels && <Line data={chartData} />}
      </div>
    </div>
  );
}

export default App;