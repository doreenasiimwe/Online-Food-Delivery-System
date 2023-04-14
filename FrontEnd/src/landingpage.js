import "./landingpage.css";
import React, { useEffect } from "react";
import { useState } from "react";
import { Link } from "react-router-dom";
import "./navbar.js";

const Images = [
  "./img/fish.jpg",
  "./img/pasta.jpg",
  "./img/dinner4.jpg",
  "./img/cafech.jpg",
];
function LandingPage() {
  const [currentImage, setCurrentImage] = useState(null);
  useEffect(() => {
    const intervalId = setInterval(() => {
      setCurrentImage(Images[Math.floor(Math.random() * Images.length)]);
    }, 2000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <div className="landing">
        <img src={currentImage} alt="lunch" />
        <h2 className="welcome">Welcome to Fast and Yummy</h2>
        <Link to="menu">
          {" "}
          <button className="orderbtn">ORDER NOW</button>
        </Link>
      </div>
      <div className="popular">
        <h2>Popular Foods</h2>
        <div className="popularfood">
          <div className="winescolumn1">
            <img src="./img/cafech.jpg" alt="foods" />
          </div>

          <div className="winescolumn2">
            <img src="./img/waffles.jpg" alt="foods" />
          </div>

          <div className="winescolumn3">
            <img src="./img/dinner4.jpg" alt="foods" />
          </div>

          <div className="winescolumn3">
            <img src="./img/fish.jpg" alt="foods" />
          </div>
        </div>
      </div>
    </div>
  );
}
export default LandingPage;
