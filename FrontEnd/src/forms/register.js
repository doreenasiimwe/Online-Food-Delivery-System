// import { editableInputTypes } from "@testing-library/user-event/dist/utils";
import { useState } from "react";
import { Link } from "react-router-dom";
export function RegisterForm() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [contact, setContact] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();

    const errors = Validate();

    // set state to error
    setErrors(errors);
    if (errors === "") {
      alert(email);
    }
  };

  const Validate = () => {
    const error = {};
    if (!name) {
      error.name = "Name is required";
    } else if (name.length > 26) {
      error.name = "name should below 26 letters";
    } else {
      error.name = "";
    }
    if (!email) {
      error.email = "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      error.email = "Incorrect email format";
    } else {
      error.email = "";
    }

    if (!contact) {
      error.contact = "Contact is required";
    } else if (!contact.length === 10) {
      error.contact = "Contact is incorrect";
    } else if (isNaN(contact)) {
      error.contact = "Contact should include numbers";
    } else {
      error.contact = "";
    }

    if (!password) {
      error.password = "Password is required";
    } else {
      error.password = "";
    }
    return error;
  };
  return (
    <div className="container">
      <div className="form_container" id="register">
        <div className="imgp">
          <h2>Sign Up</h2>
        </div>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="name">Name</label>
            <input type="text" onChange={(e) => setName(e.target.value)} />
            {errors.name && <div className="error">{errors.name}</div>}
          </div>

          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input type="text" onChange={(e) => setEmail(e.target.value)} />
            {errors.email && <div className="error">{errors.email}</div>}
          </div>

          <div className="form-group">
            <label htmlFor="contact">Contact</label>
            <input type="text" onChange={(e) => setContact(e.target.value)} />
            {errors.contact && <div className="error">{errors.contact}</div>}
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              onChange={(e) => setPassword(e.target.value)}
            />
            {errors.password && <div className="error">{errors.password}</div>}
          </div>


          <button className="buttonlogin" type="submit" >Register</button>
        </form>
        <p>
          Already have an account?|<Link to="/login"> Log in</Link>
        </p>

        <Link to="/" className="back">
          Back
        </Link>
      </div>
    </div>
  );
}
