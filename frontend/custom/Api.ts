import axios, { AxiosResponse } from "axios";


export const baseApi = axios.create({
    baseURL: 'api/v1',
    url: 'api/v1',
    withCredentials: true
})

export type RegisterRequest = {
    login: string,
    email: string,
    password: string,
    role?: AccountRole,
}

export type AccountResponse ={
    id: string
    login: string
    role: AccountRole
    blockReason?: string
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
    targetLogin: string,
    blockReason: string
}

export type AddNotificationRequest = {
    time: Date,
    text: string
}

export type RepeatNotificationRequest = {
    targetId: string
    newTime: Date
}

export type Notification = {
    id: string,
    time: Date,
    text: string
}

export type ApiResponse<T> = {
    data: T | null,
    status: number,
    message?: string
}

const getErr = (e: any) => ({
    data: null,
    status: e.response.status,
    message: e.response.data.detail[0].msg
      ?? e.response.data.detail
})

const getNotification = (e: Notification): Notification => ({
    id: e.id,
    time: new Date(e.time),
    text: e.text,
})

export const api = {
    accounts: {
        getAll: async (): Promise<ApiResponse<AccountResponse[]>> => {
            try {
                const response = await baseApi.get<AccountResponse[]>('/accounts')
                return {
                    data: response.data,
                    status: response.status,
                }
            } catch (e: any) {
                return getErr(e)
            }
        },
        register: async (request: RegisterRequest): Promise<ApiResponse<LoginResponse>> => {
            try {
                request.role = AccountRole.User;
                const response = await baseApi.post<LoginResponse>('/accounts/register', request)
                return {
                    data: response.data,
                    status: response.status,
                }
            } catch (e: any) {
                return getErr(e)
            }
        },
        login: async (request: LoginRequest): Promise<ApiResponse<LoginResponse>> => {
            try {
                const response = await baseApi.post<LoginResponse>('/accounts/login', request)
                return {
                    data: response.data,
                    status: response.status,
                }
            } catch (e: any) {
                return getErr(e)
            }
        },
        my: async (): Promise<ApiResponse<LoginResponse>> => {
            try {
                const response = await baseApi.get<LoginResponse>('/accounts/my')
                return {
                    data: response.data,
                    status: response.status,
                }
            } catch (e: any) {
                return getErr(e)
            }
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
        add: async (request: AddNotificationRequest): Promise<ApiResponse<Notification>> => {
            try {
                const response = await baseApi.post<Notification>('/notifications', request)
                return {
                    data: getNotification(response.data),
                    status: response.status,
                }
            } catch (e: any) {
                return getErr(e)
            }
        },
        getMy: async (): Promise<ApiResponse<Notification[]>> => {
            try {
                const response = await baseApi.get<Notification[]>('/notifications/my')
                return {
                    data: response.data.map(getNotification),
                    status: response.status,
                }
            } catch (e: any) {
                return getErr(e)
            }
        },
        repeat: async (request: RepeatNotificationRequest): Promise<ApiResponse<Notification>> => {
            try {
                const response = await baseApi.post<Notification>('/notifications/repeat', request)
                return {
                    data: getNotification(response.data),
                    status: response.status,
                }
            } catch (e: any) {
                return getErr(e)
            }
        },
    }
}