import React, { useState, useEffect } from 'react';
import PlotWidget from 'react-pyqtgraph';

function RealTimePlot() {
  const [data, setData] = useState({ x: [], y: [] });

  useEffect(() => {
    // create a WebSocket connection to the backend server
    const ws = new WebSocket('ws://localhost:8000/ws/realtime-plot/');
    // receive the data from the server
    ws.onmessage = (event) => {
      setData(JSON.parse(event.data));
    };
    // clean up the WebSocket connection when the component is unmounted
    return () => ws.close();
  }, []);

  const options = {
    title: "Real-Time Plot",
    labels: { left: "Y-axis", bottom: "X-axis" },
    width: 800,
    height: 600,
    margin: { left: 50, bottom: 50 }
  };

  return (
    <PlotWidget
      data={[{ x: data.x, y: data.y }]}
      options={options}
    />
  );
}

export default RealTimePlot;