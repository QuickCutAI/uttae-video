import { css } from "@emotion/css";
import { Layout } from "antd";
import { Content, Header } from "antd/es/layout/layout";
import { Route, Routes } from "react-router-dom";

const App = () => {
  return (
    <div>
      <Layout>
        <Header
          className={css`
            color: #fff;
            text-align: center;
          `}
        >
          ItBook
        </Header>
        <Content
          className={css`
            padding: 0 24px;
          `}
        >
          <Routes>
            <Route path="/books" />
            <Route path="/books/:id" />
          </Routes>
        </Content>
      </Layout>
    </div>
  );
};

export default App;
