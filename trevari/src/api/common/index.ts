import axios from "axios";

export const Api = axios.create({
  baseURL: "https://api/itbook.store/1.0",
});
