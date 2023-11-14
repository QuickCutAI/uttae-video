import { List } from "antd";
import VirtualList from "rc-virtual-list";
import { CSSProperties, ReactNode } from "react";

const ListBody = () => {
  const data = [];

  return (
    <List>
      <VirtualList data={[]} itemKey={""}>
        {(item: any) => <div />}
      </VirtualList>
    </List>
  );
};

export default ListBody;
