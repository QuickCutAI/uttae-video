import { useQuery } from "react-query";
import { getBookList } from "api/axios/books";

const useBookList = (keyword: string) => {
  return useQuery(keyword, () => {
    return getBookList({
      keyword,
      pageNumber: 10,
    });
  });
};
