import { css } from "@emotion/css";
import { Layout } from "antd";
import { Content, Header } from "antd/es/layout/layout";
import { Route, Routes } from "react-router-dom";
import BookList from "./pages/BookList";
import { RecoilRoot } from "recoil";

const App = () => {
  return (
    <RecoilRoot>
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
            <Route path="/books" element={<BookList />} />
            <Route path="/books/:id" />
          </Routes>
        </Content>
      </Layout>
    </RecoilRoot>
  );
};

export default App;
