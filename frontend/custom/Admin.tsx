import React, {useEffect, useState} from 'react';
import { AccountState } from "./App";
import {AccountResponse, api} from "@/custom/Api";
import Notifications from "@/custom/Notifications";

type Props = {
  account: AccountState;
}

const AdminPage = (props: Props) => {
  const [isNotifications, setIsNotifications] = useState<boolean>(true);

  const getContent = () => {
    if (isNotifications)
      return <Notifications {...props} />

    return <Users />
  }

  return (
    <div>
      Таблица -{" "}{isNotifications ? "Уведомления" : "Пользователи"}
      <button
        style={{backgroundColor: "bisque"}}
        onClick={() => setIsNotifications(!isNotifications)}
      >
        Переключить
      </button>
      {getContent()}
    </div>
  );
}

type UsersProps = {

}

const Users = (props: UsersProps) => {
  const [users, setUsers] = useState<AccountResponse[]>([]);
  const [needReload, setNeedReload] = useState(false);

  const reload = () => setNeedReload(!needReload);

  useEffect(() => {(async () => {
    const myResponse = await api.accounts.getAll();
    if (!!myResponse.message)
    {
      return;
    }

    const data = myResponse.data ?? [];
    setUsers(data);
  })()}, [needReload])

  return (
    <div style={{ margin: '20px 0' }}>
      <h2>Пользователи</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse', border: '1px solid #ccc' }}>
        <thead>
        <tr style={{ backgroundColor: '#f5f5f5' }}>
          <th style={{ border: '1px solid #ccc', padding: '8px', width: '10%' }}>ИД</th>
          <th style={{ border: '1px solid #ccc', padding: '8px', width: '20%' }}>Логин</th>
          <th style={{ border: '1px solid #ccc', padding: '8px' }}>Блокировка</th>
        </tr>
        </thead>
        <tbody>
        {users.map((e) => (
          <tr key={e.id}>
            <td style={{ border: '1px solid #ccc', padding: '8px' }}>{e.id}</td>
            <td style={{ border: '1px solid #ccc', padding: '8px' }}>{e.login}</td>
            <td style={{ border: '1px solid #ccc', padding: '8px' }}>
              <Block login={e.login} blockReason={e.blockReason} onBlock={reload}/>
            </td>
          </tr>
        ))}
        </tbody>
      </table>
    </div>
  )
}

const Block = (props: {login: string, blockReason?: string, onBlock: () => void}) => {
  const [blockReason, setBlockReason] = useState<string>("");

  if (!!props.blockReason)
    return <>Заблокирован. Причина -{` ${props.blockReason}`}</>

  const block = async () => {
      await api.accounts.blockUser({
        targetLogin: props.login,
        blockReason: blockReason,
      })
    props.onBlock();
  }

  return (
    <>
      <input
        placeholder={"Причина блокировки"}
        value={blockReason}
        onChange={e => setBlockReason(e.target.value)}
      />
      <button style={{backgroundColor: "red"}} onClick={block}>Заблокировать</button>
    </>
  )
}

export default AdminPage