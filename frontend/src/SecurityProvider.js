import { useState } from "react"
import SecurityContext from "./SecurityContext"

const SecurityProvider = (props) => {
    const [loggedIn, setLoggedIn] = useState(false)

    return (
        <SecurityContext.Provider
            value={{
                logged: () => setLoggedIn(true),
                login: (username, password) => {
                    if(username === 'admin' && password === 'admin') {
                        setLoggedIn(true)
                    }
                },
                logout: () => setLoggedIn(false),
                loggedIn,
            }}
        >
            {props.children}
        </SecurityContext.Provider>
    )
}

export default SecurityProvider
