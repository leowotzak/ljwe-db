import {Container} from "react-bootstrap";
import {PageLayout, LoginForm} from '../components'
import 'holderjs'

export default () => {

    return (
        <PageLayout>
            <img src="holder.js/300x200" />
            <h1>This is the login page</h1>
            <p>If you log in you should be able to access the web tools</p>
            <LoginForm />
        </PageLayout>
    )
}