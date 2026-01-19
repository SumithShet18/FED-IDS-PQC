const BACKEND_URL = "http://127.0.0.1:5000";

export async function healthCheck() {
  const res = await fetch(`${BACKEND_URL}/health`);
  return res.json();
}

export async function detectIntrusion(features) {
  const res = await fetch(`${BACKEND_URL}/detect`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ features }),
  });
  return res.json();
}

export async function pqcDemo() {
  const res = await fetch(`${BACKEND_URL}/pqc`);
  return res.json();
}
