import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api';

// Axios instances for different purposes
const publicApi = axios.create({
  baseURL: BASE_URL,
});

const adminApi = axios.create({
  baseURL: BASE_URL,
});

// Refresh token function
const refreshToken = async () => {
  const refresh = localStorage.getItem('refreshToken');
  if (!refresh) {
    throw new Error('No refresh token found');
  }

  try {
    const response = await adminApi.post('/token-refresh/', { refresh });
    localStorage.setItem('token', response.data.access);
    console.log('Token refreshed:', response.data.access);
    return response.data.access;
  } catch (error) {
    console.error('Error refreshing token:', error);
    throw error; // Handle this in your app (e.g., redirect to login)
  }
};

// Attach interceptor to adminApi for automatic token refresh
adminApi.interceptors.request.use(
  async (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

adminApi.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      try {
        const newToken = await refreshToken();
        error.config.headers.Authorization = `Bearer ${newToken}`;
        return adminApi.request(error.config); // Retry the original request
      } catch (refreshError) {
        console.error('Token refresh failed, redirecting to login:', refreshError);
        // Handle token refresh failure (e.g., redirect to login page)
      }
    }
    return Promise.reject(error);
  }
);

// API functions
export const getHomeData = async () => {
  try {
    const response = await publicApi.get('/home/');
    return response.data;
  } catch (error) {
    console.error('Error fetching home data:', error);
    throw error;
  }
};

export const getAdminHomeData = async () => {
  try {
    const response = await adminApi.get('/admin/home/');
    return response.data;
  } catch (error) {
    console.error('Error fetching admin home data:', error);
    throw error;
  }
};

export const adminLogin = async (username, password) => {
  const payload = { username, password };

  try {
    const response = await publicApi.post('/token/', payload);
    localStorage.setItem('token', response.data.access);
    localStorage.setItem('refreshToken', response.data.refresh); // Store refresh token
    return response.data;
  } catch (error) {
    console.error('Error logging in:', error);
    throw error;
  }
};

// Rankings

export const getRanking = async () => {
    try {
        const response = await publicApi.get('/players/rankings/');
        return response.data;
    } catch (error) {
        console.error('Error fetching rankings:', error);
        throw error;
    }
}

// Players

export const getPlayers = async (page = 1, pageSize = 10) => {
  try {
    const response = await publicApi.get('/players/', {
      params: { page, page_size: pageSize },
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching players:', error);
    throw error;
  }
};

export const getPlayer = async (id) => {
    try {
        if (!id) {
          throw new Error('Player ID is required');
        }
        const response = await publicApi.get(`/players/${id}/`);
        return response.data;
    } catch (error) {
        console.error('Error fetching player:', error);
        throw error;
    }
}


export const addPlayer = async (data) => {
  try {
    const response = await adminApi.post('/players/', data, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    return response.data;
  } catch (error) {
    console.error('Error adding player:', error);
    throw error;
  }
};

export const deletePlayer = async (id) => {
    try {
        if (!id) {
        throw new Error('Player ID is required');
        }
        const response = await adminApi.delete(`/players/${id}/`);
        return response.data;
    } catch (error) {
        console.error('Error deleting player:', error);
        throw error;
    }
}

export const getCountryChoices = async () => {
  try {
    const response = await publicApi.get('/players/country-choices/');
    return response.data;
  } catch (error) {
    console.error('Error fetching country choices:', error);
    throw error;
  }
};


// Matches

export const getSingleMatches = async (page = 1, pageSize = 10) => {
    try {
        const response = await publicApi.get('/matches/singles/', {
            params: { page, page_size: pageSize },
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching matches:', error);
        throw error;
    }
}

export const getDoubleMatches = async (page = 1, pageSize = 10) => {
    try {
        const response = await publicApi.get('/matches/doubles/',
            {params: { page, page_size: pageSize },
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching matches:', error);
        throw error;
    }
}

export const getSingleMatch = async (id) => {
    try {
        if (!id) {
          throw new Error('Match ID is required');
        }
        const response = await publicApi.get(`/matches/singles/${id}/`);
        return response.data;
    } catch (error) {
      console.error('Error fetching match:', error);
      throw error;
    }
}

export const postSingleMatch = async (data) => {
    try {
        const response = await adminApi.post('/matches/singles/', data);
        return response.data;
    } catch (error) {
        console.error('Error adding match:', error);
        throw error;
    }
}

export const deleteMatch = async (id, type) => {
    try {
        if (!id) {
          throw new Error('Match ID is required');
        }
        const response = await adminApi.delete(`/matches/${type}/${id}/`);
        return response.data;
    } catch (error) {
      console.error('Error deleting match:', error);
      throw error;
    }
}

export const postSingleGame = async (data) => {
    try {
        const response = await adminApi.post('/matches/singles-games/', data);
        return response.data;
    } catch (error) {
        console.error('Error adding games:', error);
        throw error;
    }
}

export const getDoubleMatch = async (id) => {
    try {
        if (!id) {
          throw new Error('Match ID is required');
        }
        const response = await publicApi.get(`/matches/doubles/${id}/`);
        return response.data;
    } catch (error) {
      console.error('Error fetching match:', error);
      throw error;
    }
}

export const postDoubleMatch = async (data) => {
    try {
        const response = await adminApi.post('/matches/doubles/', data);
        return response.data;
    } catch (error) {
        console.error('Error adding match:', error);
        throw error;
    }
}

export const postDoubleGame = async (data) => {
    try {
        const response = await adminApi.post('/matches/doubles-games/', data);
        return response.data;
    } catch (error) {
        console.error('Error adding games:', error);
        throw error;
    }
}

// Seasons

export const getSeasons = async (page = 1, pageSize = 10) => {
    try {
        const response = await publicApi.get('/seasons/', {
            params: { page, page_size: pageSize },
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching seasons:', error);
        throw error;
    }
}

export const getSeason = async (id) => {
    try {
        if (!id) {
          throw new Error('Season ID is required');
        }
        const response = await publicApi.get(`/seasons/${id}/`);
        return response.data;
    } catch (error) {
      console.error('Error fetching season:', error);
      throw error;
    }
}

export const postSeason = async (data) => {
    try {
        const response = await adminApi.post('/seasons/', data);
        return response.data;
    } catch (error) {
        console.error('Error adding season:', error);
        throw error;
    }
}

export const deleteSeason = async (id) => {
    try {
        if (!id) {
          throw new Error('Season ID is required');
        }
        const response = await adminApi.delete(`/seasons/${id}/`);
        return response.data;
    } catch (error) {
      console.error('Error deleting season:', error);
      throw error;
    }
}