import React from "react";
import { Notification } from "./Api";

type Props = {
    Notifications: Notification[],
    Title: string,
    ActionColumnTitle: string,
    ActionColumnText: string,
    ActionColumnCallback: (notification: Notification) => void,
}

const NotificationsTable = (props: Props) => {
    return (
    <div style={{ margin: '20px 0' }}>
      <h2>{props.Title}</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse', border: '1px solid #ccc' }}>
        <thead>
          <tr style={{ backgroundColor: '#f5f5f5' }}>
            <th style={{ border: '1px solid #ccc', padding: '8px' }}>ИД</th>
            <th style={{ border: '1px solid #ccc', padding: '8px' }}>Время</th>
            <th style={{ border: '1px solid #ccc', padding: '8px' }}>Текст</th>
            <th style={{ border: '1px solid #ccc', padding: '8px' }}>{props.ActionColumnTitle}</th>
          </tr>
        </thead>
        <tbody>
          {props.Notifications.map((e) => (
            <tr key={e.id}>
              <td style={{ border: '1px solid #ccc', padding: '8px' }}>{e.id}</td>
              <td style={{ border: '1px solid #ccc', padding: '8px' }}>{e.time.toString()}</td>
              <td style={{ border: '1px solid #ccc', padding: '8px' }}>{e.text}</td>
              <td style={{ border: '1px solid #ccc', padding: '8px' }}>
                  <button 
                    onClick={() => props.ActionColumnCallback(e)}
                    style={{ padding: '5px 10px', margin: '0 5px' }}
                  >
                    {props.ActionColumnText}
                  </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default NotificationsTable;