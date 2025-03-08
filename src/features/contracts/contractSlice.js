// src/features/contracts/contractSlice.js
import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  contracts: [],
  loading: false,
  error: null,
};

const contractSlice = createSlice({
  name: 'contracts',
  initialState,
  reducers: {
    fetchContractsStart: (state) => {
      state.loading = true;
      state.error = null;
    },
    fetchContractsSuccess: (state, action) => {
      state.contracts = action.payload;
      state.loading = false;
      state.error = null;
    },
    fetchContractsFailure: (state, action) => {
      state.loading = false;
      state.error = action.payload;
    },
  },
});

export const { fetchContractsStart, fetchContractsSuccess, fetchContractsFailure } = contractSlice.actions;

export default contractSlice.reducer;