import React from "react";
import "./footer.css";
import TwitterIcon from "@mui/icons-material/Twitter";
import FacebookIcon from "@mui/icons-material/Facebook";
import MarkunreadIcon from "@mui/icons-material/Markunread";

function Footer() {
  return (
    <>
      <div className="footer">
        <div className="footer_container">
          <div className="locate">
            <h3>LOCATIONS</h3>
            <h4>Kampala</h4>
            <p>Kira Road</p>
            <p>Parliamentary Avenue</p>
            <p>Equatorial mall</p>
            <p>Namugongo</p>
            <p>Kamwokya</p>
            <h4>Mukono</h4>
          </div>

          <div>
            <h3>CONTACTS</h3>
            <p>info@fastandyummy.co.ug</p>

            <p>+256 706517066</p>
            <p>+256 741099846</p>
            <p>Toll free: +008 8004 537</p>

            <TwitterIcon />
            <span> @fastandyummy1.com</span>
            <div>
              <FacebookIcon />
              <span> fastandyummy1</span>
            </div>
            <div>
              <MarkunreadIcon />
              <span> fastandyummy@gmail.com</span>
            </div>
          </div>

          <div>
            <h3>MENU</h3>
            <p>Breakfast</p>
            <p>Lunch</p>
            <p>Dinner</p>
            <p>Breakfast</p>
            <p>Lunch</p>
            <p>Dinner</p>
            <p>Breakfast</p>
          </div>
        </div>
        <p>
          Fast and yummy is an online delivery restaurant offers you the best
          dinning experience. We are open 24/7 from Monday to Sunday and you can
          place your orders via email or by contacting us directly. You can also
          visit our social platforms for more information.
        </p>
        <p className="copy">&copy; 2023 Fast and Yummy. All rights reserved</p>
      </div>
    </>
  );
}

export default Footer;
