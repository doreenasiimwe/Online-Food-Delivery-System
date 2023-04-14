import React from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "./navbar.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCartPlus } from "@fortawesome/free-solid-svg-icons";

function Navbar() {
  return (
    <div className="overall_nav">
      <div className="rrr">
        <img src="logoo.png" className="my_logo" alt="logo"></img>
        <h5>
          Fast <br></br>And <br></br>Yummy
        </h5>
      </div>
      <div className="buttonlink">
        <div className="nav_link1">
          <Link to="/" className="home">
            Home
          </Link>
        </div>

        <div className="nav_link2">
          <Link to="/menu" className="menu">
            Menu
          </Link>
        </div>

        <Link to="/login">
          <button id="btns">LogIn</button>
        </Link>
        <Link to="/register">
          <button id="btn-r">Register</button>
        </Link>
        <Link to="/chart">
          <div className="cart">
            <span>
              <FontAwesomeIcon
                icon={faCartPlus}
                className="fa-solid fa-cart-plus"
                id="chart"
              />
            </span>
          </div>
        </Link>
      </div>
    </div>
  );
}

export default Navbar;
