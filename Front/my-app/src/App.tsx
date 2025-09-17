import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { AccountRole, api, Notification } from './Api';

type AccountState = {
  id: string,
  role: AccountRole
}

type State = {
  account?: AccountState
  notifications: Notification[]
}

const defaultState: State = {
  account: undefined,
  notifications: []
}

const App = () => {
  const [account, setAccount] = useState<AccountState | null>(null);
  const [notification, setNotifications] = useState<Notification[]>([]);

  useEffect(() => {(async () => {
    const myResponse = await api.accounts.my();
    
  })()}, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
