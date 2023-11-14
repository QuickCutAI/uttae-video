import { Api } from "api/common";
import { iSearchParams } from "types/search";

export const getBookList = async (params: iSearchParams) => {
  const { keyword, pageNumber } = params;
  const response = await Api.get(`/search/${keyword}/${pageNumber}`);
  return response.data;
};
