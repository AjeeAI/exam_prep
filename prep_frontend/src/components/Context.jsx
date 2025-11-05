import { useContext } from 'react';
import UserContext from './UserContext';

function Profile() {
  const user = useContext(UserContext);
  function handlePromote(){
    setUser({...user, role: "Senior Developer"})
  }
  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.role}</p>
      <button onClick={handlePromote}>Change role</button>
    </div>
  );
}

export default Profile;