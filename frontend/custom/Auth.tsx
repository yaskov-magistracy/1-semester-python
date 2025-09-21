import React, {useState} from "react";
import {api} from "@/custom/Api";

type AuthPageProps = {
  reloadAcc: () => void;
}

const AuthPage = (props: AuthPageProps) => {
  const [isLogging, setIsLogging] = useState<boolean>(true);

  const getContent = () => {
    if (isLogging)
      return <LoginPage {...props} />
    else
      return <RegisterPage {...props} />
  }

  return (
    <>
      <div>
        <button
          onClick={() => {setIsLogging(!isLogging)}}
        >
          {isLogging ? "Зарегистрироваться" : "Войти"}
        </button>
      </div>
      {getContent()}
    </>
  )
}



const LoginPage = (props: AuthPageProps) => {
  const [login, setLogin] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [error, setError] = useState<string | null>(null);

  const onAuth = async () => {
    const response = await api.accounts.login({
      login: login,
      password: password,
    });
    if (response.data === null) {
      setError(response.message!);
      return;
    }

    setError(null);
    props.reloadAcc();
  }

  return (
    <div style={{width: "300px", height:"300px", margin:"auto", verticalAlign: "middle", textAlign: "center"}}>
      <h3>Login</h3>
      <div>
        <input
          placeholder={"login"}
          value={login}
          onChange={e => setLogin(e.target.value)}
        />
      </div>
      <div>
        <input
          placeholder={"password"}
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
      </div>
      <div>
        <button
          onClick={onAuth}
          style={{backgroundColor: "bisque", borderColor: "black"}}
        >
          enter
        </button>
      </div>
      {error && <div style={{backgroundColor: "red"}}>{error}</div>}
    </div>
  );
}

const RegisterPage = (props: AuthPageProps) => {
  const [login, setLogin] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [error, setError] = useState<string | null>(null);

  const onReg = async () => {
    const response = await api.accounts.register({
      login: login,
      email: email,
      password: password,
    });
    if (response.data === null) {
      setError(response.message!);
      return;
    }

    setError(null);
    props.reloadAcc();
  }

  return (
    <div style={{width: "300px", height:"300px", margin:"auto", verticalAlign: "middle", textAlign: "center"}}>
      <h3>Registration</h3>
      <div>
        <input
          placeholder={"login"}
          value={login}
          onChange={e => setLogin(e.target.value)}
        />
      </div>
      <div>
        <input
          placeholder={"email"}
          value={email}
          onChange={e => setEmail(e.target.value)}
        />
      </div>
      <div>
        <input
          placeholder={"password"}
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
      </div>
      <div>
        <button
          onClick={onReg}
          style={{backgroundColor: "bisque", borderColor: "black"}}
        >
          enter
        </button>
      </div>
      {error && <div style={{backgroundColor: "red"}}>{error}</div>}
    </div>
  );
}

export default AuthPage;