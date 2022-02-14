import { Container } from "react-bootstrap";
import { PageLayout, LoginForm } from "../components";

export default () => {
  return (
    <PageLayout>
      <h1>This is the login page</h1>
      <p>If you log in you should be able to access the web tools</p>
      <LoginForm />
    </PageLayout>
  );
};
