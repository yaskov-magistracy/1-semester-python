import React from 'react';
import { AccountState } from "./App";
import NotificationsTable from "@/custom/NotificationsTable";
import Notifications from "@/custom/Notifications";


type Props = {
    account: AccountState
}

const UserPage = (props: Props) => {
  return (
    <>
      <Notifications {...props} />
    </>
  );
}

export default UserPage