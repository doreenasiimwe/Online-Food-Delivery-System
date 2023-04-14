import React from "react";

function Appetizers() {
  return (
    <div>
      <div className="appetizercontainer">
        <div className="appetizercolumn1">
          <h2>Cocktails</h2>
          <img src="./images/cocktails.jpg" alt="Cocktails" />
          <p>Price: 10000UGX</p>
          <button>Order</button>
        </div>

        <div className="appetizercolumn2">
          <h2>Chips and Dips</h2>
          <img src="./images/chips and dips.jpg" alt="Chips and Dips" />
          <p>Price: 15000UGX</p>
          <button>Order</button>
        </div>

        <div className="appetizercolumn3">
          <h2>Salads</h2>
          <img src="./images/salads.jpg" alt="Salads" />
          <p>Price: 5000UGX</p>
          <button>Order</button>
        </div>
      </div>
    </div>
  );
}
export default Appetizers;
