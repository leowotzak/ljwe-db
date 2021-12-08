import {Container} from "react-bootstrap";
import {PageLayout, RegisterForm} from '../components'
import 'holderjs';

export default () => {

    return (
        <PageLayout>
            <img src="holder.js/300x200" />
            <h1>This is the register page</h1>
            <p>You should be able to create an account here.</p>
            <p>Should go into some details about what benefits this affords</p>
            <RegisterForm />
        </PageLayout>
    )
}