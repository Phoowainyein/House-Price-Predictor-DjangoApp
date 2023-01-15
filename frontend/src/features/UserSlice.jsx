import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'
import customFetch from '../utils/Axios'
import { toast } from 'react-toastify'
import {
  addUserToLocalStorage,
  getUserFromLocalStorage
} from '../utils/LocalStorage'

const initialState = {
  isLoading: false,
  userInfo: getUserFromLocalStorage()
}

export const registerUser = createAsyncThunk(
  'user/registerUser',
  async ({ name, email, password }, thunkAPI) => {
    try {
      const resp = await customFetch.post('/api/auth/register', {
        email,
        name,
        password
      })
      console.log(resp)
      return resp.data
    } catch (error) {
      console.log('ERROR: response.status: ' + error.response.status)
      console.log(error.response.data)
      return thunkAPI.rejectWithValue(error.response.data)
    }
  }
)

export const loginUser = createAsyncThunk(
  'user/loginUser',
  async ({ email, password }, thunkAPI) => {
    try {
      const resp = await customFetch.post('/api/auth/login', {
        email,
        password
      })
      console.log(resp)
      return resp.data
    } catch (error) {
      console.log('ERROR: response.status: ' + error.response.status)
      console.log(error.response.data)
      return thunkAPI.rejectWithValue(error.response.data)
    }
  }
)
const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(registerUser.pending, (state) => {
        state.isLoading = true
      })
      .addCase(registerUser.fulfilled, (state, { payload }) => {
        const { userInfo } = payload
        state.isLoading = false
        state.user = userInfo
        addUserToLocalStorage(userInfo)
        toast.success(`Hello there ${userInfo.name}.`)
      })
      .addCase(registerUser.rejected, (state, { payload }) => {
        const { error } = payload
        state.isLoading = false
        toast.error(error)
      })
      .addCase(loginUser.pending, (state) => {
        state.isLoading = true
      })
      .addCase(loginUser.fulfilled, (state, { payload }) => {
        const { userInfo } = payload
        state.isLoading = false
        state.user = userInfo
        addUserToLocalStorage(userInfo)
        toast.success(`Welcome back ${userInfo.name}!`)
      })
      .addCase(loginUser.rejected, (state, { payload }) => {
        const { error } = payload
        state.isLoading = false
        toast.error(error)
      })
  }
})

export default userSlice.reducer
