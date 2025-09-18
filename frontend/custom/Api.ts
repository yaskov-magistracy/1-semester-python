import axios, { AxiosResponse } from "axios";


export const baseApi = axios.create({
    baseURL: 'api/v1',
    url: 'api/v1',
    withCredentials: true
})

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

export type BlockRequest = {
    targetId: string,
    blockReason: string
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
            try{
                const response = await baseApi.post<LoginResponse>('/accounts/register', request)
                return response
            } catch(e: any) {
                return e.response
            }
        },
        login: async (request: LoginRequest): Promise<AxiosResponse<LoginResponse>> => {
            const response = await baseApi.post<LoginResponse>('/accounts/login', request)
            return response
        },
        my: async (): Promise<AxiosResponse<LoginResponse>> => {
            const response = await baseApi.post<LoginResponse>('/accounts/my')
            return response
        },
        logout: async (): Promise<AxiosResponse> => {
            const response = await baseApi.post('/accounts/logout')
            return response
        },
        blockUser: async (request: BlockRequest): Promise<AxiosResponse> => {
            const response = await baseApi.post(`/accounts/block`, request)
            return response
        }
    },
    notifications: {
        add: async (request: AddNotificationRequest): Promise<AxiosResponse<Notification>> => {
            const response = await baseApi.post<Notification>('/notifications', request)
            return response
        },
        getMy: async (): Promise<AxiosResponse<Notification[]>> => {

        },
        getAll: async (): Promise<AxiosResponse<Notification[]>> => {

        },
        repeat: async (notificationId: string, request: RepeatNotificationRequest): Promise<AxiosResponse<Notification>> => {
            const response = await baseApi.post<Notification>(`/notifications/${notificationId}/repeat`, request)
            return response
        },
        remove: async (notificationId: string): Promise<AxiosResponse> => {
            const response = await baseApi.delete(`/notifications/${notificationId}`)
            return response
        }
    }
}