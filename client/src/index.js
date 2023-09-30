
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import reportWebVitals from './reportWebVitals';
import Root from "./routes/root";
import SignUp from './signup';
import Thanks from './Components/Thanks';
import Shop from './shop';
import Login from './Components/Login';


const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/>,
  },
  {
    path: "/sign",
    element: <SignUp />,
  },
  
  {
    path: "/thank",
    element: <Thanks />
  },
  {
    path: "/shop",
    element: < Shop/>
  },
  {
    path: "/login",
    element: < Login/>
  },

]);
const root = ReactDOM.createRoot(document.getElementById('root'));


root.render(
  <React.StrictMode>
     <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
