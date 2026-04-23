import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  interactions: [],
  chatResponse: null,
  loading: false,
  error: null,
};

const interactionSlice = createSlice({
  name: "interaction",
  initialState,
  reducers: {
    setLoading: (state, action) => {
      state.loading = action.payload;
    },

    setChatResponse: (state, action) => {
      state.chatResponse = action.payload;
    },

    setInteractions: (state, action) => {
      state.interactions = action.payload;
    },

    addInteraction: (state, action) => {
      state.interactions.push(action.payload);
    },

    setError: (state, action) => {
      state.error = action.payload;
    },
  },
});

export const {
  setLoading,
  setChatResponse,
  setInteractions,
  addInteraction,
  setError,
} = interactionSlice.actions;

export default interactionSlice.reducer;
