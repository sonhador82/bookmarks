import React, { useState } from "react"
import { Container, Form, Button } from "react-bootstrap"
import axios from "axios"
import BACKEND_URL from "../../Config"
import Cookies from 'universal-cookie';
import useSecurity from "../../UseSecurity";

const cookies = new Cookies()


const SignIn = (props) => {
    const { logged } = useSecurity()
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    const handleSubmit = (event) => {
        event.preventDefault()
        axios.post(`${BACKEND_URL}/login`, 
            {"username": username, "password": password}, 
            { withCredentials: true})
        .then(function (response) {
            console.log(response);
            cookies.set('isLoggedIn', true, { path: '/' })
            logged()
        })
        .catch(function (error) {
            console.log("Error")
            console.log(error);
        })        
    }

    return (
        <Container>
            <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="formLogin">
                    <Form.Label>Login</Form.Label>
                    <Form.Control type="text" value={username} onChange={ e => setUsername(e.target.value)} placeholder="Enter login" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
                </Form.Group>
                <Button variant="primary" type="submit">Login</Button>
            </Form>
        </Container>
    )
}

export default SignIn
