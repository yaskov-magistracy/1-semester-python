import NotificationsTable from "@/custom/NotificationsTable";
import React, {useEffect, useState} from "react";
import {AccountState} from "@/custom/App";
import {api, Notification as Notification} from "@/custom/Api";
import notificationsTable from "@/custom/NotificationsTable";

type Props = {
  account: AccountState,
  isAdmin?: boolean
}

const Notifications = (props: Props) => {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [curDate, setCurDate] = useState<Date>(new Date());
  const [error, setError] = useState<string | null>(null);
  const [needReload, setNeedReload] = useState<boolean | null>(null);

  const reload = () => {setNeedReload(!needReload)};
  const sortFunc = (a: Notification, b: Notification) =>
    a.time.getUTCDate() >= b.time.getUTCDate()
      ? -1
      : 1;

  useEffect(() => {(async () => {
    const myResponse = props.isAdmin
      ? await api.notifications.getAll()
      : await api.notifications.getMy();
    if (!!myResponse.message)
    {
      setError(myResponse.message);
      return;
    }

    const data = myResponse.data ?? [];
    setCurDate(new Date())
    setNotifications(data.sort(sortFunc));
  })()}, [needReload])

  if (!!error){
    return (<div>{error}</div>)
  }

  return (
    <div>
      <NotificationsTable
        Notifications={notifications
          .filter(e => e.time > curDate)}
        Title={"Уведомления"}
        ActionColumnTitle={""}
      />
      {!props.isAdmin && <AddEl reloadCallback={reload}/>}
      <NotificationsTable
        Notifications={notifications
          .filter(e => e.time <= curDate)}
        Title={"Архив"}
        ActionColumnTitle={"Повторить. Дата в формате dd.MM.yyyy HH:mm:ss или кнопки снизу"}
        ActionColumn={
        props.isAdmin
          ? undefined
          : (e) => <RepeatEl notification={e} reloadCallback={reload} />}
      />
    </div>
  );
}

type AddElProps = {
  reloadCallback: () => void;
}

const AddEl = (props: AddElProps) => {
  const [date, setDate] = useState("");
  const [text, setText] = useState("");
  const [error, setError] = useState<string | null>(null);

  const addNotification = async () => {
    const parsedTime = parseDate(date)
    if (isNaN(parsedTime.getTime())){
      setError("Некорректный формат даты");
      return;
    }
    setError(null);

    const response = await api.notifications.add({
      time: parsedTime,
      text: text,
    });
    if (response.data === null) {
      setError(response.message!);
      return;
    }
    setError(null);
    props.reloadCallback();
  }

  return (
    <div>
      <input
        placeholder={"Дата в формате dd.MM.yyyy HH:mm:ss"}
        value={date}
        onChange={e => setDate(e.target.value)}
      />
      <input
        placeholder={"Текст уведомления"}
        value={text}
        onChange={e => setText(e.target.value)}
      />
      <button
        onClick={addNotification}
      >
        Добавить
      </button>
      <div>
        <button
          style={{backgroundColor: "aqua"}}
          onClick={() => setDate(new Date().toLocaleString("ru-RU"))}>Текущее время</button>
      </div>
      {!!error
        && <div
              style={{backgroundColor: "red"}}>
          {error}
          </div>}
    </div>
  )
}

type RepeatProps = {
  reloadCallback: () => void;
  notification: Notification;
}

const RepeatEl = (props: RepeatProps) => {
  const [time, setTime] = useState("");
  const [error, setError] = useState<string | null>(null)

  const repeat = async () => {
    if (time.length < 10)
    {
      setError("Некорректный формат даты");
      return;
    }

    const parsedTime = parseDate(time)
    if (isNaN(parsedTime.getTime())){
      setError("Некорректный формат даты");
      return;
    }
    setError(null);

    const response = await api.notifications.repeat({
      targetId: props.notification.id,
      newTime: parsedTime,
    });
    if (response.data === null){
      setError(response.message!);
      return;
    }

    props.reloadCallback();
  }

  const addTime = (timeInMinutes: number) => {
    setTime(
      new Date(props.notification.time.getTime() + timeInMinutes * 1000 * 60)
        .toLocaleString("ru-RU"))
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


const parseDate = (time: string): Date => {
  const usTime = time.substring(3, 6) + time.substring(0, 3) + time.substring(6);
  return new Date(usTime)
}

export default Notifications;