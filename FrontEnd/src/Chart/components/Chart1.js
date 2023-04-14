import React from 'react';
import '../styles/navbar.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {faCartPlus}  from '@fortawesome/free-solid-svg-icons';

const Navbar2 = ({size, setShow}) => {
  return (
    <nav>
        <div className="nav_box">
            <span className="my_shop" onClick={()=>setShow(true)}>
             <button>fooditems</button>
            </span>
            <div className="cart" onClick={()=>setShow(false)}>
                <span>
                    <FontAwesomeIcon icon={faCartPlus } className="fa-solid fa-cart-plus" />
                </span>
                <span>{size}</span>
            </div>
        </div>
    </nav>
  )
}

export default Navbar2;