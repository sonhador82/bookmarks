import React, { useState, useEffect, useContext, createContext, Children } from "react";
import axios from "axios";
import BACKEND_URL from "../Config"

const authContext = createContext()

export function ProvideAuth({ children }) {
    const auth = useProvideAuth()
    return <authContext.Provider value={auth}>{children}</authContext.Provider>
}


export const useAuth = () => {
    return useContext(authContext)
}

function useProvideAuth() {
    const [user, setUser] = useState(null)

    const signin = (email, password) => {
        // make call to back, return user?
        axios.post(`${BACKEND_URL}/auth/signin`,
            { "email": email, "password": password },
            { withCredentials: true })
            .then(function (response) {
                console.log(response)
                //cookies.set('isLoggedIn', true, { path: '/' })
                //logged()
            })
            .catch(function (error) {
                console.log("Error")
                console.log(error);
            })
        return user
    }

    const signout = () => {
        setUser(false)
        // removte session from backend
    }

    return {
        user,
        signin,
        signout
    }
}
