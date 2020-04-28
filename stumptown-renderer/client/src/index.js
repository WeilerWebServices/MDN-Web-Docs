import React from "react";
import ReactDOM from "react-dom";
import "./index.scss";
import "typeface-zilla-slab";
import { App } from "./app";
// import * as serviceWorker from './serviceWorker';

const container = document.getElementById("root");
let docData = null;
const documentDataElement = document.getElementById("documentdata");
if (documentDataElement) {
  docData = JSON.parse(documentDataElement.text);
}
const app = (
  <React.StrictMode>
    <App doc={docData} />
  </React.StrictMode>
);
if (container.firstElementChild) {
  ReactDOM.hydrate(app, container);
} else {
  ReactDOM.render(app, container);
}

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();
