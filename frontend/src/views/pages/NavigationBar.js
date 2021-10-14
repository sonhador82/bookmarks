import React from 'react'
import { Navbar, Container, Nav, Button } from 'react-bootstrap'
import { Link, NavLink } from 'react-router-dom'
import { useAuth } from '../../hooks/UseAuth'

const NavigationBar = () => {
    const auth = useAuth()

    return (
        <Navbar bg="dark" variant="dark">
            <Container>
                <Navbar.Brand>Bookmarks</Navbar.Brand>
                <Nav className="me-auto">
                    <NavLink className="nav-link" exact to="/add">Add</NavLink>
                    <NavLink className="nav-link" exact to="/bookmarks">Show</NavLink>
                    {auth.user ? (
                        <div>
                            <p>Account: ({auth.user.email})</p>
                            <Button variant="danger" onClick={() => auth.signout()}>Sign out</Button>
                        </div>
                    ) : (
                        <NavLink className="nav-link" exact to="/signin">Sign in</NavLink>
                    )}
                </Nav>
            </Container>
        </Navbar>            
    )
}
export default NavigationBar
