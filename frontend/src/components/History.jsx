import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getHistory } from "../services/api";
import { setInteractions } from "../redux/interactionSlice";

export default function History() {
  const [name, setName] = useState("");
  const dispatch = useDispatch();

  const { interactions } = useSelector((state) => state.interaction);

  const fetchHistory = async () => {
    const res = await getHistory(name);
    dispatch(setInteractions(res.data.data));
  };

  return (
    <div>
      <h3>History</h3>

      <input
        placeholder="HCP Name"
        onChange={(e) => setName(e.target.value)}
      />

      <button onClick={fetchHistory}>Fetch</button>

      <pre>{JSON.stringify(interactions, null, 2)}</pre>
    </div>
  );
}
