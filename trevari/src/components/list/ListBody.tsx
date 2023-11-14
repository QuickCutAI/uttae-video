import { List } from "antd";
import VirtualList from "rc-virtual-list";
import { CSSProperties, ReactNode } from "react";
import Search from "./Search";

const ListBody = () => {
  return (
    <>
      <Search />
      <List>
        <VirtualList data={[]} itemKey={""}>
          {(item: any) => <div />}
        </VirtualList>
      </List>
    </>
  );
};

export default ListBody;
