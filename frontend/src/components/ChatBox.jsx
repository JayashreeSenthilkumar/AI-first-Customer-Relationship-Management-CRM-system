import { useState } from "react";
import { sendChat } from "../services/api";

export default function ChatBox() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState(null);

  const handleSend = async () => {
    const res = await sendChat(message);
    setResponse(res.data);
  };

  return (
    <div>
      <h3>Chat Log</h3>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Enter interaction..."
      />
      <button onClick={handleSend}>Send</button>

      {response && <pre>{JSON.stringify(response, null, 2)}</pre>}
    </div>
  );
}
