import React from "react";

function Grains() {
  return (
    <div>
      <div className="grainscontainer">
        <div className="grainscolumn1">
          <h2> Brown Rice</h2>
          <img src="./images/rice.jpg" alt="Rice" />
          <p>Price: 5000UGX</p>
          <button>Order</button>

          <h2>Chips</h2>
          <img src="./images/chips.jpg" alt="" />
          <p>Price: 5000UGX</p>
          <button>Order</button>
        </div>
        <div className="grainscolumn2">
          <h2>Pasta</h2>
          <img src="./images/pasta.jpg" alt="" />
          <p>Price: 5000UGX</p>
          <button>Order</button>

          <h2> White Rice</h2>
          <img src="./images/whiterice.jpg" alt="white rice" />
          <p>Price: 5000UGX</p>
          <button>Order</button>
        </div>
      </div>
    </div>
  );
}
export default Grains;
