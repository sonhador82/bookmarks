import { Route } from "react-router-dom"
import useSecurity from "./UseSecurity"
import SignIn from "./views/pages/SignIn"

const SecureRoute = (props) => {
    const { loggedIn } = useSecurity()

    return (
        <Route {...props}>{ loggedIn ? props.children : <SignIn /> }</Route>
    )
}

export default SecureRoute
