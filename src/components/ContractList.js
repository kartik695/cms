// src/components/ContractList.js
import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchContractsStart, fetchContractsSuccess, fetchContractsFailure } from '../features/contracts/contractSlice';
import axios from 'axios';

const ContractList = () => {
  const dispatch = useDispatch();
  const { contracts, loading, error } = useSelector((state) => state.contracts);

  useEffect(() => {
    const fetchContracts = async () => {
      dispatch(fetchContractsStart());
      try {
        const response = await axios.get('http://localhost:8888/api/contracts');
        dispatch(fetchContractsSuccess(response.data));
      } catch (err) {
        dispatch(fetchContractsFailure(err.message));
      }
    };

    fetchContracts();
  }, [dispatch]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h2>Contracts</h2>
      <ul>
        {contracts.map((contract) => (
          <li key={contract._id}>
            {contract.name} - {contract.status}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ContractList;