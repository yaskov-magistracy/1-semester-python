import NotificationsTable from "@/custom/NotificationsTable";
import React, {useEffect, useState} from "react";
import {AccountState} from "@/custom/App";
import {api, Notification as Notification} from "@/custom/Api";
import notificationsTable from "@/custom/NotificationsTable";

type Props = {
  account: AccountState
}

const Notifications = (props: Props) => {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const curDate = new Date().getUTCDate();
  const [error, setError] = useState<string | null>(null);
  const [needReload, setNeedReload] = useState<boolean | null>(null);

  const reload = () => {setNeedReload(!needReload)};

  useEffect(() => {(async () => {
    const myResponse = await api.notifications.getMy();
    if (!!myResponse.message)
    {
      setError(myResponse.message);
      return;
    }

    const data = myResponse.data ?? [];
    setNotifications(data)
  })()}, [needReload])

  if (!!error){
    return (<div>{error}</div>)
  }

  return (
    <div>
      <NotificationsTable
        Notifications={notifications.filter(e => e.time.getUTCDate() >= curDate)}
        Title={"Уведомления"}
        ActionColumnTitle={""}
      />
      <NotificationsTable
        Notifications={notifications.filter(e => e.time.getUTCDate() > curDate)}
        Title={"Архив"}
        ActionColumnTitle={"Повторить. Дата в формате dd.MM.yyyy HH:mm:ss или кнопки снизу"}
        ActionColumn={(e) =>
        <RepeatEl notification={e} reloadCallback={reload} />}
      />
    </div>
  );
}

type RepeatProps = {
  reloadCallback: () => void;
  notification: Notification;
}

const RepeatEl = (props: RepeatProps) => {
  const [time, setTime] = useState("");
  const [error, setError] = useState<string | null>(null)

  const repeat = async () => {
    const parsedTime = new Date(time)
    if (isNaN(parsedTime.getTime())){
      setError("Некорректный формат даты");
      return;
    }
    setError(null);
    debugger;
    return;

    const response = await api.notifications.repeat({
      targetId: props.notification.id,
      newTime: parsedTime,
    });
    props.reloadCallback();
  }

  const addTime = (timeInMinutes: number) => {
    setTime(
      new Date(props.notification.time.getTime() + timeInMinutes * 1000)
        .toLocaleString("ru", {}))
  }

  return (
    <>
      <div>
     <input
      placeholder={"Введите дату"}
      value={time}
      onChange={e => setTime(e.target.value)}
     />
        <button style={{backgroundColor: "coral"}} onClick={() => repeat()}>
          повторить
        </button>
        {!!error && <p style={{backgroundColor: "red"}}>{error}</p>}
      </div>
      <div>
        <button
          style={{backgroundColor: "bisque"}}
          onClick={() => addTime(5)}
        >
          +5 мин
        </button>
        <button
          style={{backgroundColor: "aliceblue"}}
          onClick={() => addTime(60)}
        >
          +60 мин
        </button>
        <button
          style={{backgroundColor: "aqua"}}
          onClick={() => addTime(60 * 24)}
        >
          +1 день
        </button>
      </div>

    </>
  )
}

export default Notifications;