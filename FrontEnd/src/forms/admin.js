import { useState } from "react";
import { Link } from "react-router-dom";

export function AdminLogin() {
  const [email, setEmail] = useState("");
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

    if (!email) {
      error.email = "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      error.email = "Incorrect email format";
    } else {
      error.email = "";
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
      <div className="form_container" id="login">
        <div className="imgp">
          <h2>Admin</h2>
        </div>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input type="text" onChange={(e) => setEmail(e.target.value)} />
            {errors.email && <div className="error">{errors.email}</div>}
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              onChange={(e) => setPassword(e.target.value)}
            />
            {errors.password && <div className="error">{errors.password}</div>}
          </div>

          <button className="buttonlogin">Log in</button>
        </form>
        <p>
          Login as customer| <Link to="/login">Login</Link>
        </p>
        <Link to="/" className="back">
          Back
        </Link>
      </div>
    </div>
  );
}
