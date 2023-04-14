import React from "react";

function KatogoItems() {
  return (
    <div>
      <div className="katogocontainer">
        <div className="katogocolumn1">
          <h2>Matooke/Offals</h2>
          <img src="./images/offals.jpeg" alt="" />
          <p>Price: 8000UGX</p>
          <button>Order</button>
        </div>

        <div className="katogocolumn2">
          <h2>Matooke/Gnuts</h2>
          <img src="./images/gnuts.jpeg" alt="" />
          <p>Price: 5000UGX</p>
          <button>Order</button>
        </div>

        <div className="katogocolumn3">
          <h2>Irish/Beef</h2>
          <img src="./images/irish.jpeg" alt="irish/beef" />
          <p>Price: 8000UGX</p>
          <button>Order</button>
        </div>

        <div className="katogocolumn4">
          <h2>Cassava/Beans</h2>
          <img src="./images/cassava.jpg" alt="cassava/beans" />
          <p>Price: 5000UGX</p>
          <button>Order</button>
        </div>
      </div>
    </div>
  );
}
export default KatogoItems;
