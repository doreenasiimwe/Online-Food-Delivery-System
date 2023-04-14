import { Link } from "react-router-dom";
import "./menu.css";
export function Menu() {
  return (
    <div>
      <div className="menucontainer">
        <div className="menucolumn1">
          <Link to="/breakfast">
            <h2>Breakfast</h2>
            <img src="./images/breakfast.jpg" alt="white wines" />
          </Link>
        </div>

        <div className="menucolumn1">
          <Link to="/lunch">
            {" "}
            <h2>Lunch</h2>
            <img src="./img/buffetug.jfif" alt="lunch" />
          </Link>
        </div>

        <div className="menucolumn1">
          <Link to="/dinner">
            <h2>Dinner</h2>
            <img src="./img/cafech.jpg" alt="Dinner" />
          </Link>
        </div>
      </div>
    </div>
  );
}

// import React from "react";
// import { useState,useEffect } from "react";
// import "./menu.css"
// import { Link } from "react-router-dom";

// export function Menu() {
//       const [categories, setCategories] = useState([]);
//     // const [activeImageIndex, setActiveImageIndex] = useState(0);
//     console.log(categories,"categoryState");
//     const fetchAllCategories =()=>{
//         fetch('http://127.0.0.1:5000/categories')
//         .then(Response=>Response.json(),"api response")
//         .then(data=>setCategories(data.categories));
//     }

//     useEffect(()=>{
//         fetchAllCategories();
//     },[]);

//     return (
//       <div className='menucontainer'>
//         <div className='menucolumn1'>
//             {categories.map(food_category =>
//             <div>
//               <Link to="/breakfast">
//                 <h2>"name":{food_category.name}</h2>
//                 <img>"image":{food_category.image}</img>
//               </Link>
//                 {/* <span>"Title":{category.title}</span>
//                 <span>"Brand":{category.brand}</span> */}
//             </div>)}
//             {categories.map(food_category =>
//             <div>
//               <Link to="/breakfast">
//                 <h2>"name":{food_category.name}</h2>
//                 <img>"image":{food_category.image}</img>
//               </Link>
//                 {/* <span>"Title":{category.title}</span>
//                 <span>"Brand":{category.brand}</span> */}
//             </div>)}
//             {categories.map(food_category =>
//             <div>
//               <Link to="/breakfast">
//                 <h2>"name":{food_category.name}</h2>
//                 <img>"image":{food_category.image}</img>
//               </Link>
//                 {/* <span>"Title":{category.title}</span>
//                 <span>"Brand":{category.brand}</span> */}
//             </div>)}
//         </div>

//       </div>
//     );
//    }
