import React from "react";

function Fruits() {
  return (
    <div>
      <div className="fruitscontainer">
        <div className="fruitcolumn1">
          <h2>Bananas</h2>
          <img src="./images/bananas.jpg" alt="Bananas" />
          <p>Price: 2000UGX</p>
          <button>Order</button>

          <h2>Oranges</h2>
          <img src="./images/oranges.jpg" alt="Oranges" />
          <p>Price: 2000UGX</p>
          <button>Order</button>
        </div>
        <div className="fruitcolumn2">
          <h2>Apples</h2>
          <img src="./images/apples.jpg" alt="Apples" />
          <p>Price: 2000UGX</p>
          <button>Order</button>

          <h2>Mangoes</h2>
          <img src="./images/mangoes.jpg" alt="Mangoes" />
          <p>Price: 2000UGX</p>
          <button>Order</button>
        </div>
      </div>
    </div>
  );
}
export default Fruits;
