import SignUp from "./components/SignUp";
import Login from "./components/Login";
import Dashboard from "./components/Dashboard";
import AdminDashboard from "./components/AdminDashboard";
import {Routes, Route} from "react-router-dom"

export default function App(){
  return (

   <div>
    
    <Routes>
      <Route path="/" element={<Login/>}/>
      <Route path="/signup" element={<SignUp/>}/>
      <Route path="/homepage" element={<Dashboard/>}/>
      <Route path="/admin_dashboard" element={<AdminDashboard/>}/>
    </Routes>
   </div>
  )
}

// import { useState } from 'react';
// // import UserContext from './UserContext';
// import Profile from './components/Context';

// export function App() {
//   const [user, setUser] = useState({ name: 'Chidi', role: 'Developer' });
  
//   return (
//     <UserContext.Provider value={{user, setUser}}>
//       <Profile />
//       <Dashboard />
//     </UserContext.Provider>
//   );
// }