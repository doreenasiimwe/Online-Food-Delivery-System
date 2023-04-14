import { Link } from "react-router-dom";
import "./menu.css";

export function Breakfast() {
  return (
    <div class="breakfastContainer">
      <div className="breakfastcontainer">
        <div className="breakfastcolumn1">
          <Link to="/teaitems">
            <h2>Tea</h2>
            <img src="./images/breakfast.jpg" alt="tea" />
          </Link>
        </div>
        <div className="breakfastcolumn1">
          <Link to="/snackitems">
            {" "}
            <h2>Snacks</h2>
            <img src="./img/buffetug.jfif" alt="snacks" />
          </Link>
        </div>

        <div className="breakfastcolumn1">
          <Link to="/katogoitems">
            <h2>Katogo</h2>
            <img src="./img/cafech.jpg" alt="katogo" />
          </Link>
        </div>
        <div className="breakfastcolumn1">
          <Link to="/drinkitems">
            <h2>Drinks and Beverages</h2>
            <img src="./img/cafech.jpg" alt="Drinks" />
          </Link>
        </div>
      </div>
    </div>
  );
}
