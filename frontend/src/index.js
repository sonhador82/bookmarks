import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import BookmarkForm from "./Bookmark";
import reportWebVitals from './reportWebVitals';
import Page from './Page'

ReactDOM.render(
  <React.StrictMode>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons" />
    <meta name="viewport"  content="minimum-scale=1, initial-scale=1, width=device-width" />
    <Page />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
