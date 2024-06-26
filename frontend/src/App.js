import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import AuthForm from "./components/auth";
import Categories from "./components/categories";
import Category from "./components/category";
import UserContext from "./utils/context";
import UserAccess from "./components/user_access";
import Messages from "./components/messages";


const App = () => {
  const [user, setUser] = useState(JSON.parse(localStorage.getItem("user")) || {});

  useEffect(() => {
    localStorage.setItem("user", JSON.stringify(user));
  }, [user]);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      <Router>
        <Routes>
          <Route path="/" element={<AuthForm />} />
          <Route path="/categories" element={<Categories />} />
          <Route path="/categories/:id" element={<Category />} />
          <Route path="/user-access" element={<UserAccess />} />
          <Route path="/messages" element={<Messages />} />
        </Routes>
      </Router>
    </UserContext.Provider>
  );
}

export default App;