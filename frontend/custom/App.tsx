'use client'
import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { AccountRole, api, Notification } from './Api';
import UserPage from './User';
import AdminPage from './Admin';
import AuthPage from './Auth';


export type AccountState = {
  id: string,
  role: AccountRole,
  email: string,
}

const App = () => {
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [account, setAccount] = useState<AccountState | null>(null);
  const [needReload, setNeedReload] = useState<boolean>(false);

  const reloadAcc = () => {
    setIsLoading(true);
    setNeedReload(!needReload);
  }

  const logout = async () => {
    await api.accounts.logout();
    setAccount(null);
    reloadAcc();
  }

  useEffect(() => {(async () => {
    const myResponse = await api.accounts.my();
    if (myResponse.data === null)
    {
      setIsLoading(false);
      return;
    }

    setAccount({
      id: myResponse.data.id,
      role: myResponse.data.role,
      email: myResponse.data.email,
    });
    setIsLoading(false);
  })()}, [needReload])

  if (isLoading)
    return <Loading />;

  const getContent = () => {
    if (account === null)
      return <AuthPage reloadAcc={reloadAcc}/>

    return (
      <div>
        <div>
          <p>Email: {account.email}</p>
          Вы {account?.role === AccountRole.User ? "User" : "Admin"} -
          <button
            style={{backgroundColor: "red"}}
            onClick={logout}
          >
            Logout
          </button>
        </div>
        {account?.role === AccountRole.User
          ? <UserPage account={account}/>
          : <AdminPage account={account}/>}
      </div>
    );
  }

  return (
    <div className="outer">
      <div className="middle">
        <div className="inner">
          {getContent()}
        </div>
      </div>
    </div>
  )
}

const Loading = () => {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Loading...
        </p>
      </header>
    </div>
  )
}


export default App;
