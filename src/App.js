// src/App.js
import React from 'react';
import { useSelector } from 'react-redux';
import ContractList from './components/ContractList';
import LogoutButton from './components/LogoutButton'; // Import the LogoutButton

function App() {
  const { isAuthenticated } = useSelector((state) => state.auth);

  return (
    <div className="App">
      <h1>Contract Management System</h1>
      {isAuthenticated && <LogoutButton />} {/* Render the LogoutButton if authenticated */}
      {isAuthenticated ? (
        <ContractList />
      ) : (
        <p>Please log in to view contracts.</p>
      )}
    </div>
  );
}

export default App;