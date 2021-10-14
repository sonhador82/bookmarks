import React from 'react'
import { Route, Switch } from 'react-router'
import SecureRoute from './SecureRoute'
// import AddBookmark from './views/pages/AddBookmark'
import AddBookmark from './views/pages/bookmarks/Add'
import ShowBookmarks from './views/pages/Bookmarks'
import Home from './views/pages/Home'
import SignIn from './views/pages/SignIn'

const Routes = () => {
    return (
        <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/signin" component={SignIn} />
            <SecureRoute path="/add"><AddBookmark /></SecureRoute>
            <Route path="/bookmarks" component={ShowBookmarks} />
        </Switch>
    )
}

export default Routes
