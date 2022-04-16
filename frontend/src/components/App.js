import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    //leaving this for future reminder of how to access variables through components in the future
    //render() {
    //    return <h1>{this.props.name}</h1>;
    //}

    render() {
        return <HomePage />;
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv)

//similar to above comment, leaving this for future reminder of how to access variables through components in the future
//render(<App name="jon" />, appDiv)