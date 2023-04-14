import React from "react";

function TeaItems() {
  return (
    <div>
      <div className="teacontainer">
        <div className="teacolumn1">
          <h2>Milk</h2>
          <img src="./images/milktea.jpeg" alt="milk" />
          <p>Price: 3000UGX</p>
          <button>Order</button>

          <h2>Cappiccino</h2>
          <img src="./images/cappiccino.webp" alt="cappiccino" />
          <p>Price: 10000UGX</p>
          <button>Order</button>
        </div>

        <div className="teacolumn1">
          <h2>African Tea</h2>
          <img src="./images/africantea.jpeg" alt="African tea" />
          <p>Price: 3000UGX</p>
          <button>Order</button>

          <h2>Turkisk coffee</h2>
          <img src="./images/turkishcoffee.jpg" alt="turkish coffee" />
          <p>Price: 10000UGX</p>
          <button>Order</button>
        </div>
      </div>
    </div>
  );
}
export default TeaItems;
