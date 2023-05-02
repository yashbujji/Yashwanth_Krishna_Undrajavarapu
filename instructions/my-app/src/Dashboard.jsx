
import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import { CSVLink } from 'react-csv';

export const Chart = ({ data, val }) => {
  const isLoading = data.length === 0;

  if (isLoading) {
    return <div>Loading chart...</div>;
  }

  
  const headers = [
    { label: 'Time', key: 'time' },
    { label: val, key: 'value' },
  ];
  
  return (
    <div>
      <LineChart width={800} height={400} data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
        <XAxis dataKey="time" tick={false} label={{ value: 'Time', position: 'insideBottomRight' }}/>
        <YAxis label={{ value: val, angle: -90, position: 'insideLeft' }}/>
        <CartesianGrid strokeDasharray="3 3"/>
        <Tooltip/>
        <Legend />
        <Line type="monotone" dataKey="value" stroke="#00556f" activeDot={{ r: 8 }}/>
      </LineChart>
      <CSVLink data={data} headers={headers} filename={`${val}-data.csv`}>
        Download {val} data
      </CSVLink>
    </div>
  );
};
