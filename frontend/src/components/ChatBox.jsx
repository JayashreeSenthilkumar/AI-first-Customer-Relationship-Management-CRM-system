import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { sendChat } from "../services/api";
import { setChatResponse, setLoading, setError } from "../redux/interactionSlice";

export default function ChatBox() {
  const [message, setMessage] = useState("");
  const dispatch = useDispatch();

  const { chatResponse, loading } = useSelector(
    (state) => state.interaction
  );

  const handleSend = async () => {
    try {
      dispatch(setLoading(true));

      const res = await sendChat(message);

      dispatch(setChatResponse(res.data));
      dispatch(setLoading(false));
    } catch (err) {
      dispatch(setError("Something went wrong"));
      dispatch(setLoading(false));
    }
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

      {loading && <p>Loading...</p>}

      {chatResponse && (
        <pre>{JSON.stringify(chatResponse, null, 2)}</pre>
      )}
    </div>
  );
}
