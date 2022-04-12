import axios from "axios";
import { QueryFunction } from "react-query";

export const queryFn: QueryFunction = async ({ queryKey }) => {
  const { data } = await axios.get(`http://localhost:8000/${queryKey[0]}`);
  return data;
};
