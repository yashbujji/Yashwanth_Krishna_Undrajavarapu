import React, { useState, useEffect } from "react";
import { Chart } from "./Dashboard";
import "./App.css";

function App() {
  const [tempData, setTempData] = useState([]);
  const [phData, setPhData] = useState([]);
  const [oxygenData, setOxygenData] = useState([]);
  const [pressureData, setPressureData] = useState([]);
  const [isRefreshing, setIsRefreshing] = useState(false);

  const handleRefresh = async () => {
    setIsRefreshing(true);
    const tempResponse = await fetch("http://localhost:8888/temp");
    const tempData = await tempResponse.json();
    setTempData(tempData);

    const phResponse = await fetch("http://localhost:8888/ph");
    const phData = await phResponse.json();
    setPhData(phData);

    const oxygenResponse = await fetch("http://localhost:8888/oxygen");
    const oxygenData = await oxygenResponse.json();
    setOxygenData(oxygenData);

    const pressureResponse = await fetch("http://localhost:8888/pressure");
    const pressureData = await pressureResponse.json();
    setPressureData(pressureData);

    setIsRefreshing(false);
  };

  useEffect(() => {
    async function fetchData() {
      const tempResponse = await fetch("http://localhost:8888/temp");
      const tempData = await tempResponse.json();
      setTempData(tempData);

      const phResponse = await fetch("http://localhost:8888/ph");
      const phData = await phResponse.json();
      setPhData(phData);

      const oxygenResponse = await fetch("http://localhost:8888/oxygen");
      const oxygenData = await oxygenResponse.json();
      setOxygenData(oxygenData);

      const pressureResponse = await fetch("http://localhost:8888/pressure");
      const pressureData = await pressureResponse.json();
      setPressureData(pressureData);
    }

    fetchData();
  }, []);

  return (
    <div>
      <div>
      </div>
      <div className="container">
        <h1>MINIMUM VIABLE PROJECT</h1>
        <button onClick={handleRefresh}>Refresh</button>
        <span>{isRefreshing ? "Data is being refreshed..." : "Data is upto date."}</span>
        <h3>Temperature</h3>
        <Chart data={tempData} val={"Temperature (Celsius)"}/>
        {console.log(tempData, "temp")}
        <h3>pH</h3>
        <Chart data={phData} val={"pH Values"}/>

        <h3>Distilled Oxygen</h3>
        <Chart data={oxygenData} val={"Distilled Oxygen Percentage (%)"} />

        <h3>Pressure</h3>
        <Chart data={pressureData} val={"Pressure (psi)"}/>
      </div>
    </div>
  );
}

export default App;
