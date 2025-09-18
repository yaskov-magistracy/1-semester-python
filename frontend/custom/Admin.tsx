import React from 'react';
import { AccountState } from "./App";


type Props = {
    account: AccountState
}

const AdminPage = (props: Props) => {
    return (
        <>
            Вы Admin
        </>
    );
}

export default AdminPage