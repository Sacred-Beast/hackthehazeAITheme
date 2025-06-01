import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000'; // or use http://localhost:8000

export const fetchExampleData = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/your-endpoint`);
    return response.data;
  } catch (error) {
    console.error('API call failed:', error);
    throw error;
  }
};
