import { useState } from "react";
import Header from "./components/Header";
import Card from "./components/Card";
import { healthCheck, detectIntrusion, pqcDemo } from "./api";

function App() {
  const [status, setStatus] = useState("");
  const [result, setResult] = useState(null);
  const [pqc, setPqc] = useState(null);

  async function checkBackend() {
    const res = await healthCheck();
    setStatus(res.status);
  }

  async function runDetection() {
    const dummyFeatures = new Array(78).fill(0.01);
    const res = await detectIntrusion(dummyFeatures);
    setResult(res);
  }

  async function runPQC() {
    const res = await pqcDemo();
    setPqc(res);
  }

  return (
    <div className="app">
      <Header />

      <div className="dashboard">

        <Card title="System Status">
          <button onClick={checkBackend}>Check Backend</button>
          <p className="status">{status || "Unknown"}</p>
        </Card>

        <Card title="Intrusion Detection">
          <button onClick={runDetection}>Run Detection</button>

          {result && (
            <>
              <p><b>Prediction:</b> {result.prediction}</p>
              <p><b>Error:</b> {result.reconstruction_error.toFixed(6)}</p>
              <p><b>Threshold:</b> {result.threshold.toFixed(6)}</p>
            </>
          )}
        </Card>

        <Card title="Post-Quantum Security">
          <button onClick={runPQC}>Run PQC Demo</button>

          {pqc && (
            <>
              <p>🔐 {pqc.kyber}</p>
              <p>📦 {pqc.encryption}</p>
              <p>✅ {pqc.signature}</p>
            </>
          )}
        </Card>

      </div>
    </div>
  );
}

export default App;
