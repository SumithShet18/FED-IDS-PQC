import { useState } from "react";
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
    // Dummy feature vector (same length as backend expects)
    const dummyFeatures = new Array(78).fill(0.01);

    const res = await detectIntrusion(dummyFeatures);
    setResult(res);
  }

  async function runPQC() {
    const res = await pqcDemo();
    setPqc(res);
  }

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Federated IDS Dashboard</h1>

      <button onClick={checkBackend}>Check Backend</button>
      <p>{status}</p>

      <hr />

      <button onClick={runDetection}>Run Intrusion Detection</button>
      {result && (
        <div>
          <p><b>Prediction:</b> {result.prediction}</p>
          <p><b>Error:</b> {result.reconstruction_error}</p>
          <p><b>Threshold:</b> {result.threshold}</p>
        </div>
      )}

      <hr />

      <button onClick={runPQC}>Run PQC Demo</button>
      {pqc && (
        <div>
          <p>{pqc.kyber}</p>
          <p>{pqc.encryption}</p>
          <p>{pqc.signature}</p>
        </div>
      )}
    </div>
  );
}

export default App;
