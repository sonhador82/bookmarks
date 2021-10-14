import { Route } from "react-router-dom"
import { useAuth } from "./hooks/UseAuth"
import SignIn from "./views/pages/SignIn"

const SecureRoute = (props) => {
    const { user } = useAuth()

    return (
        <Route {...props}>{ user ? props.children : <SignIn /> }</Route>
    )
}

export default SecureRoute
