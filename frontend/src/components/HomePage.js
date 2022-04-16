import React, { Component } from "react";
import BeastsPage from "./BeastsPage";
import CharacterPage from "./CharacterPage";
import ItemsPage from "./ItemsPage";
import SkillsPage from "./SkillsPage";
import { BrowserRouter as Router, Switch, Route, Link, Redirect,} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path='/'><p>This is the homepage.</p></Route>
          <Route path='/beasts' component={BeastsPage} />
          <Route path='/character' component={CharacterPage} />
          <Route path='/items' component={ItemsPage} />
          <Route path='/skills' component={SkillsPage} />
        </Switch>
      </Router>
    );
  }
}