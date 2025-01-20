import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import AdminHeader from '../../../components/admin/AdminHeader';
import AdminFooter from '../../../components/admin/AdminFooter';
import { addPlayer, getCountryChoices } from '../../../services/api.js';
import '../../../styles/tailwind.css';

function PlayerAdd() {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    alias: '',
    gender: '',
    date_of_birth: '',
    nationality: '',
    ranking: '',
    photo: '',
  });
  const [countryChoices, setCountryChoices] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCountryChoices = async () => {
      try {
        const choices = await getCountryChoices();
        setCountryChoices(choices);
      } catch (error) {
        console.error('Error fetching country choices:', error);
      }
    };

    fetchCountryChoices();
  }, []);

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    setFormData({
      ...formData,
      [name]: files ? files[0] : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new FormData();
    for (const key in formData) {
      data.append(key, formData[key]);
    }
    try {
      await addPlayer(data);
      navigate('/admin/players');
    } catch (error) {
      console.error('Error adding player:', error);
    }
  };

  return (
    <div>
      <AdminHeader />
      <main className="container mx-auto px-4 py-8">
        <h2 className="text-3xl font-bold mb-6">Añadir Nuevo Jugador</h2>
        <form onSubmit={handleSubmit} className="bg-white p-8 rounded-lg shadow-md" encType="multipart/form-data">
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="first_name">Nombre</label>
            <input
              type="text"
              name="first_name"
              id="first_name"
              value={formData.first_name}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="last_name">Apellido</label>
            <input
              type="text"
              name="last_name"
              id="last_name"
              value={formData.last_name}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="alias">Alias</label>
            <input
              type="text"
              name="alias"
              id="alias"
              value={formData.alias}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="gender">Género</label>
            <select
              name="gender"
              id="gender"
              value={formData.gender}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              required
            >
              <option value="">Seleccione</option>
              <option value="M">Masculino</option>
              <option value="F">Femenino</option>
            </select>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="date_of_birth">Fecha de nacimiento</label>
            <input
              type="date"
              name="date_of_birth"
              id="date_of_birth"
              value={formData.date_of_birth}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="nationality">Nacionalidad</label>
            <select
              name="nationality"
              id="nationality"
              value={formData.nationality}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              required
            >
              <option value="">Seleccione</option>
              {countryChoices.map((country) => (
                <option key={country[0]} value={country[0]}>{country[1]}</option>
              ))}
            </select>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="ranking">Ranking</label>
            <input
              type="number"
              name="ranking"
              id="ranking"
              value={formData.ranking}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="photo">Foto</label>
            <input
              type="file"
              name="photo"
              id="photo"
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <button type="submit" className="bg-blue-500 text-white px-6 py-3 rounded hover:bg-blue-600">Guardar</button>
          <button type="button" onClick={() => navigate('/admin/players')} className="bg-gray-300 text-black px-6 py-3 rounded hover:bg-gray-400 ml-4">Volver a la Lista</button>
        </form>
      </main>
      <AdminFooter />
    </div>
  );
}

export default PlayerAdd;
