import { useState } from "react";
import { getHistory } from "../services/api";

export default function History() {
  const [name, setName] = useState("");
  const [data, setData] = useState([]);

  const fetchHistory = async () => {
    const res = await getHistory(name);
    setData(res.data.data);
  };

  return (
    <div>
      <h3>History</h3>
      <input
        placeholder="HCP Name"
        onChange={(e) => setName(e.target.value)}
      />
      <button onClick={fetchHistory}>Fetch</button>

      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
