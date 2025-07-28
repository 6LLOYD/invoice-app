import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000/api',
});

export const getDocuments = async () => {
  const response = await api.get('/documents');
  return response.data;
};

export const createDocument = async (data: { numero: string; date: string; total: number; type_document: string; client_id: number }) => {
  const response = await api.post('/documents', data);
  return response.data;
};