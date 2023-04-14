import React from "react";
import { Link } from "react-router-dom";

export function NoPage() {
  return (
    <div className="page">
     <p>Redirect | <Link to="/"> <span>Click here to return to homepage</span></Link></p>
      <img src="nopage.png"></img>
    </div>
  );
}
