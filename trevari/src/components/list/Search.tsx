import { Button, Form, Input } from "antd";
import useSearch from "hooks/useSearch";

const Search = () => {
  const { onFinish } = useSearch();

  return (
    <Form layout="inline" onFinish={onFinish}>
      <Form.Item label="검색어" name={"keyword"}>
        <Input placeholder="검색어를 입력하세요." />
      </Form.Item>
      <Form.Item>
        <Button type="primary">Search</Button>
      </Form.Item>
    </Form>
  );
};

export default Search;
