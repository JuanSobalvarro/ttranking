import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Update this line
import { postSeason } from "src/services/api.js";
import { Button, TextInput, Label, Textarea, Datepicker, Tooltip } from 'flowbite-react';
import 'styles/tailwind.css';
import AdminFooter from "components/admin/AdminFooter.jsx";
import AdminHeader from "components/admin/AdminHeader.jsx";

function SeasonAdd() {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    start_date: '',
    end_date: '',
    singles_points_for_win: '',
    singles_points_for_loss: '',
    doubles_points_for_win: '',
    doubles_points_for_loss: ''
  });

  const [errors, setErrors] = useState({});
  const navigate = useNavigate(); // Update this line

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const validateForm = () => {
    const newErrors = {};
    if (!formData.name) newErrors.name = 'El nombre es requerido';
    if (!formData.start_date) newErrors.start_date = 'La fecha de inicio es requerida';
    if (!formData.end_date) newErrors.end_date = 'La fecha de fin es requerida';
    // Data type conversion to YYYY-MM-DD format
    if (formData.start_date) formData.start_date = formData.start_date.toISOString().split('T')[0];
    if (formData.end_date) formData.end_date = formData.end_date.toISOString().split('T')[0];
    formData.singles_points_for_win = Number(formData.singles_points_for_win);
    formData.singles_points_for_loss = Number(formData.singles_points_for_loss);
    formData.doubles_points_for_loss = Number(formData.doubles_points_for_loss);
    formData.doubles_points_for_win = Number(formData.doubles_points_for_win);
    return newErrors;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const validationErrors = validateForm();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }
    // Submit the form data to API
    try {
      console.log('Form data:', formData);
      await postSeason(formData);
      navigate('/admin/seasons'); // Updated method to navigate
    } catch (error) {
      console.error('Error creating season:', error);
    }
  };

  return (
    <div className="bg-white min-h-screen text-gray-800 flex flex-col">
        <AdminHeader />
      <main className="container mx-auto px-4 py-8 flex-grow">
        <h2 className="text-center text-4xl font-bold mb-8">Crear Nueva Temporada</h2>
        <form onSubmit={handleSubmit} className="space-y-6 max-w-xl mx-auto">
          {/* Name */}
          <div>
            <Label htmlFor="name" value="Nombre de la Temporada" />
            <TextInput
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              type="text"
              required
              className={`w-full mt-2 ${errors.name ? 'border-red-500' : ''}`}
            />
            {errors.name && <span className="text-red-500 text-sm">{errors.name}</span>}
          </div>

          {/* Description */}
          <div>
            <Label htmlFor="description" value="Descripción" />
            <Textarea
              id="description"
              name="description"
              value={formData.description}
              onChange={handleChange}
              className="w-full mt-2"
              placeholder="Agrega una descripción opcional de la temporada"
            />
          </div>

          {/* Start Date */}
          <div>
            <Label htmlFor="start_date" value="Fecha de Inicio" />
            <Datepicker
              id="start_date"
              name="start_date"
              selected={formData.start_date}
              onChange={(date) => setFormData({ ...formData, start_date: date })}
              required
              className={`w-full mt-2 ${errors.start_date ? 'border-red-500' : ''}`}
            />
            {errors.start_date && <span className="text-red-500 text-sm">{errors.start_date}</span>}
          </div>

          {/* End Date */}
          <div>
            <Label htmlFor="end_date" value="Fecha de Fin" />
            <Datepicker
              id="end_date"
              name="end_date"
              selected={formData.end_date}
              onChange={(date) => setFormData({ ...formData, end_date: date })}
              required
              className={`w-full mt-2 ${errors.end_date ? 'border-red-500' : ''}`}
            />
            {errors.end_date && <span className="text-red-500 text-sm">{errors.end_date}</span>}
          </div>

          {/* Points for Singles Matches */}
          <div>
            <Label htmlFor="singles_points_for_win" value="Puntos para ganar en Singles" />
            <TextInput
              id="singles_points_for_win"
              name="singles_points_for_win"
              value={formData.singles_points_for_win}
              onChange={handleChange}
              type="number"
              className="w-full mt-2"
              placeholder="Ejemplo: 10"
            />
          </div>

          <div>
            <Label htmlFor="singles_points_for_loss" value="Puntos para perder en Singles" />
            <TextInput
              id="singles_points_for_loss"
              name="singles_points_for_loss"
              value={formData.singles_points_for_loss}
              onChange={handleChange}
              type="number"
              className="w-full mt-2"
              placeholder="Ejemplo: 5"
            />
          </div>

          {/* Points for Doubles Matches */}
          <div>
            <Label htmlFor="doubles_points_for_win" value="Puntos para ganar en Dobles" />
            <TextInput
              id="doubles_points_for_win"
              name="doubles_points_for_win"
              value={formData.doubles_points_for_win}
              onChange={handleChange}
              type="number"
              className="w-full mt-2"
              placeholder="Ejemplo: 15"
            />
          </div>

          <div>
            <Label htmlFor="doubles_points_for_loss" value="Puntos para perder en Dobles" />
            <TextInput
              id="doubles_points_for_loss"
              name="doubles_points_for_loss"
              value={formData.doubles_points_for_loss}
              onChange={handleChange}
              type="number"
              className="w-full mt-2"
              placeholder="Ejemplo: 8"
            />
          </div>

          {/* Submit Button */}
          <div className="text-center">
            <Button type="submit" className="bg-blue-600 hover:bg-blue-700 w-full py-2 text-white">
              Crear Temporada
            </Button>
          </div>
        </form>
      </main>
        <AdminFooter />
    </div>
  );
}

export default SeasonAdd;
