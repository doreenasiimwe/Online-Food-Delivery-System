import React from "react";

function Soups() {
  return (
    <div>
      <div className="soupscontainer">
        <div className="soupscolumn1">
          <h3>Chicken Soup</h3>
          <img src="./images/chicken soup.jpg" alt="chicken soup" />
          <p>Price: 10000UGX</p>
          <button>Order</button>

          <h3>Vegetable Soup</h3>
          <img src="./images/vegetables.jpg" alt="vegetable soup" />
          <p>Price: 5000UGX</p>
          <button>Order</button>
        </div>
        <div className="soupcolumn2">
          <h3>Tomato Soup</h3>
          <img src="./images/tomato soup.jpg" alt="Tomato soup" />
          <p>Price: 8000UGX</p>
          <button>Order</button>

          <h3>Mushroom Soup</h3>
          <img src="./images/mushroom soup.jpg" alt="mushroom soup" />
          <p>Price: 5000UGX</p>
          <button>Order</button>
        </div>
      </div>
    </div>
  );
}
export default Soups;
