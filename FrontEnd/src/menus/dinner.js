import React from "react";
import { Link } from "react-router-dom";
import "./menu.css";

export function Dinner() {
  return (
    <div className="dinnerContainer">
      <div className="dinnerCategories">
        <div className="dinnercolumn1">
          <Link to="/wines">
            <h2>Wines</h2>
            <img src="./images/breakfast.jpg" alt="tea" />
          </Link>
        </div>

        <div className="dinnercolumn2">
          <Link to="/desserts">
            <h2>Desserts</h2>
            <img src="./img/buffetug.jfif" alt="snacks" />
          </Link>
        </div>

        <div className="dinnercolumn3">
          <Link to="/appetizers">
            <h2>Appetizers</h2>
            <img src="./img/cafech.jpg" alt="katogo" />
          </Link>
        </div>
      </div>
    </div>
  );
}
export default Dinner;
