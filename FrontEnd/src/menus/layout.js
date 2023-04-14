import React from "react";
import { Outlet, Link } from "react-router-dom";

const Layout = () => {
  return (
    <>
      <nav className="categories">
        <h2>
          <Link id="menuCategories" to="/">
            Breakfast
          </Link>
        </h2>

        <h2>
          <Link id="menuCategories" to="/lunch">
            Lunch
          </Link>
        </h2>

        <h2>
          <Link id="menuCategories" to="/dinner">
            Dinner
          </Link>
        </h2>
      </nav>

      <Outlet />
    </>
  );
};

export default Layout;
