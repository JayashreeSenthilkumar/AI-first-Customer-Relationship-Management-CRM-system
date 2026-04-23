import { useState } from "react";
import { logForm } from "../services/api";

export default function InteractionForm() {
  const [form, setForm] = useState({
    hcp_name: "",
    topic: "",
    follow_up: ""
  });

  const handleSubmit = async () => {
    await logForm(form);
    alert("Saved!");
  };

  return (
    <div>
      <h3>Manual Log</h3>
      <input
        placeholder="HCP Name"
        onChange={(e) => setForm({ ...form, hcp_name: e.target.value })}
      />
      <input
        placeholder="Topic"
        onChange={(e) => setForm({ ...form, topic: e.target.value })}
      />
      <input
        placeholder="Follow Up"
        onChange={(e) => setForm({ ...form, follow_up: e.target.value })}
      />

      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}
