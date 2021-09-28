import { classes } from 'istanbul-lib-coverage'
import React from 'react'
import { Navbar, Container, Nav, Button } from 'react-bootstrap'
import { Link, NavLink } from 'react-router-dom'
import useSecurity from '../../UseSecurity'

const NavigationBar = () => {
    const { logout, loggedIn } = useSecurity()

    return (
        <Navbar bg="dark" variant="dark">
            <Container>
                <Navbar.Brand>Bookmarks</Navbar.Brand>
                <Nav className="me-auto">
                    <NavLink className="nav-link" exact to="/add">Add</NavLink>
                    <NavLink className="nav-link" exact to="/bookmark">Show</NavLink>
                    {loggedIn
                        ? <Button variant="danger" onClick={ () => logout()}>Sign out</Button>
                        : <NavLink className="nav-link" exact to="/signin">Sign in</NavLink>
                    }
                </Nav>
            </Container>
        </Navbar>            
    )
}
export default NavigationBar
