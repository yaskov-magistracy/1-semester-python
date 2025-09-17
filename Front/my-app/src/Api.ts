import axios, { AxiosResponse } from "axios";


export type RegisterRequest = {
    login: string,
    email: string,
    password: string
}

export type LoginRequest = {
    login: string,
    password: string
}

export enum AccountRole{
    User = "User",
    Admin = "Admin"
}

export type LoginResponse = {
    id: string,
    role: AccountRole
}

export type AddNotificationRequest = {
    time: Date,
    text: string
}

export type RepeatNotificationRequest = {
    deltaTime?: Date
    newTime?: Date
}

export type Notification = {
    id: string,
    time: Date,
    text: string
}

export const api = {
    accounts: {
        register: async (request: RegisterRequest): Promise<AxiosResponse<LoginResponse>> => {
            const response = await axios.post<LoginResponse>('/accounts/register', request)
            return response
        },
        login: async (request: LoginRequest): Promise<AxiosResponse<LoginResponse>> => {
            const response = await axios.post<LoginResponse>('/accounts/login', request)
            return response
        },
        my: async (): Promise<AxiosResponse<LoginResponse>> => {
            const response = await axios.post<LoginResponse>('/accounts/my')
            return response
        },
        logout: async (): Promise<AxiosResponse> => {
            const response = await axios.post('/accounts/logout')
            return response
        },
        blockUser: async (accountId: string): Promise<AxiosResponse> => {
            const response = await axios.post(`/accounts/${accountId}/block`, )
            return response
        }
    },
    notifications: {
        add: async (request: AddNotificationRequest): Promise<AxiosResponse<Notification>> => {
            const response = await axios.post<Notification>('/notifications', request)
            return response
        },
        repeat: async (notificationId: string, request: RepeatNotificationRequest): Promise<AxiosResponse<Notification>> => {
            const response = await axios.post<Notification>(`/notifications/${notificationId}/repeat`, request)
            return response
        },
        remove: async (notificationId: string): Promise<AxiosResponse> => {
            const response = await axios.delete(`/notifications/${notificationId}`)
            return response
        }
    }
}