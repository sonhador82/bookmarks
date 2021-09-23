import React from "react"
import { Container, Form, Button } from "react-bootstrap"
import axios from "axios"
import BACKEND_URL from "./Config"

class LoginForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {username: "", password: ""}
        this.handleChangeUsername = this.handleChangeUsername.bind(this)
        this.handleChangePassword = this.handleChangePassword.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleChangeUsername(event) {
        this.setState({username: event.target.value})
    }

    handleChangePassword(event) {
        this.setState({password: event.target.value})
    }

    handleSubmit(event) {
        event.preventDefault()

        axios.post(`${BACKEND_URL}/login`, this.state, { withCredentials: true})
        .then(function (response) {
            console.log(response);
            console.log("ALLL OK")
        })
        .catch(function (error) {
            console.log("Error")
            console.log(error);
        });
        
    }

    render() {
        return (
            <Container>
                        <Form onSubmit={this.handleSubmit}>
                            <Form.Group className="mb-3" controlId="formLogin">
                                <Form.Label>Login</Form.Label>
                                <Form.Control type="text" value={this.state.username} onChange={this.handleChangeUsername} placeholder="Enter login" />
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formBasicPassword">
                                <Form.Label>Password</Form.Label>
                                <Form.Control type="password" placeholder="Password" value={this.state.password} onChange={this.handleChangePassword} />
                            </Form.Group>
                            <Button variant="primary" type="submit">Login</Button>
                        </Form>
            </Container>

        )
    }
}

export default LoginForm
