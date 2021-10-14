import React, { useState } from "react"
import axios from "axios"
import BACKEND_URL from "../../Config"
import Cookies from 'universal-cookie';
import { useAuth } from "../../hooks/UseAuth";

const cookies = new Cookies()


const SignIn = (props) => {
    const { user, signin } = useAuth()
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    const handleSubmit = (event) => {
        event.preventDefault()
        console.log(`User: ${user}`)
        signin(username, password)
    }

    const divStyle = {
        display: 'block',
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <div>
                    <label controlId="formLogin">Login</label>
                    <input type="text" value={username} onChange={ e => setUsername(e.target.value)} placeholder="Enter login" /> 
                </div>
                <div>
                <label controlId="formBasicPassword">Password</label>
                <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
                </div>
                <button variant="primary" type="submit">Login</button>
            </form>
        </div>
    )
}

export default SignIn
