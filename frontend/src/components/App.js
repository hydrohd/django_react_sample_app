import React, { Component } from "react";
import { render } from "react-dom";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <h1>This is a sample application using React + DRF</h1>
        );
    }
}


const appDiv = document.getElementById("app")
//const root = createRoot(container)
render(<App />, appDiv)


