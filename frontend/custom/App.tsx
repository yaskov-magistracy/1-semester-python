'use client'
import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { AccountRole, api, Notification } from './Api';
import UserPage from './User';
import AdminPage from './Admin';


export type AccountState = {
  id: string,
  role: AccountRole
}

const App = () => {
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [account, setAccount] = useState<AccountState | null>(null);

  useEffect(() => {(async () => {
    const myResponse = await api.accounts.my();
    setAccount({
      id: myResponse.data.id,
      role: myResponse.data.role
    });
    setIsLoading(false);
  })()}, [])

  if (isLoading)
    return <Loading />;

  if (account === null)
    return <LoginPage />
  if (account?.role === AccountRole.User)
    return <UserPage account={account}/>
  if (account?.role === AccountRole.Admin)
    return <AdminPage account={account}/>

  {throw new Error("This is unprocessable state")}
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

type LoginPageProps = {
    
}

const LoginPage = (props: LoginPageProps) => {
    return (
        <>
          
        </>
    );
}

export default App;
