import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const sendChat = (message) =>
  axios.post(`${BASE_URL}/chat-log`, { message });

export const logForm = (data) =>
  axios.post(`${BASE_URL}/log-interaction`, data);

export const getHistory = (name) =>
  axios.get(`${BASE_URL}/history/${name}`);
