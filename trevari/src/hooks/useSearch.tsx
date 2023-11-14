import { useRecoilState } from "recoil";
import { searchWordState } from "recoil/search";

interface iSearchForm {
  keyword: string;
}

const useSearch = () => {
  const [, setSearchWord] = useRecoilState(searchWordState);
  const onFinish = (values: iSearchForm) => {
    setSearchWord(values.keyword);
  };

  return {
    onFinish,
  };
};

export default useSearch;
