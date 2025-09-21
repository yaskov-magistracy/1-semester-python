import React, {ReactNode} from "react";
import { Notification } from "./Api";

type Props = {
    Notifications: Notification[],
    Title: string,
    ActionColumnTitle: string,
    ActionColumn?: (notification: Notification) => ReactNode
}

const NotificationsTable = (props: Props) => {
    return (
    <div style={{ margin: '20px 0' }}>
      <h2>{props.Title}</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse', border: '1px solid #ccc' }}>
        <thead>
          <tr style={{ backgroundColor: '#f5f5f5' }}>
            <th style={{ border: '1px solid #ccc', padding: '8px', width: '10%' }}>ИД</th>
            <th style={{ border: '1px solid #ccc', padding: '8px', width: '20%' }}>Время</th>
            <th style={{ border: '1px solid #ccc', padding: '8px', width: '' }}>Текст</th>
            {!!props.ActionColumn
              && <th style={{ border: '1px solid #ccc', padding: '8px', width: '40%' }}>{props.ActionColumnTitle}</th>}
          </tr>
        </thead>
        <tbody>
          {props.Notifications.map((e) => (
            <tr key={e.id}>
              <td style={{ border: '1px solid #ccc', padding: '8px' }}>{e.id}</td>
              <td style={{ border: '1px solid #ccc', padding: '8px' }}>
                {e.time.toLocaleString()}{" "}
                ({e.time.toUTCString().substring(e.time.toUTCString().length - 12)})
              </td>
              <td style={{ border: '1px solid #ccc', padding: '8px' }}>{e.text}</td>
              {!!props.ActionColumn && <td style={{ border: '1px solid #ccc', padding: '8px' }}>
                {props.ActionColumn(e)}
              </td>}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default NotificationsTable;