import React from 'react';
import { AccountState } from "./App";


type Props = {
    account: AccountState
}

const UserPage = (props: Props) => {
    return (
        <>
            Вы User
        </>
    );
}

export default UserPage