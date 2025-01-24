import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import AdminHeader from "components/admin/AdminHeader";
import AdminFooter from "components/admin/AdminFooter";
import { addPlayer, getCountryChoices } from "services/api.js";
import { Button, Label, Select, TextInput, FileInput, Card } from "flowbite-react";
import "styles/tailwind.css";

function PlayerAdd() {
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    alias: "",
    gender: "",
    date_of_birth: "",
    nationality: "",
    photo: null,
  });
  const [countryChoices, setCountryChoices] = useState([]);
  const [photoPreview, setPhotoPreview] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCountryChoices = async () => {
      try {
        const choices = await getCountryChoices();
        setCountryChoices(choices);
      } catch (error) {
        console.error("Error fetching country choices:", error);
      }
    };
    fetchCountryChoices();
  }, []);

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    if (name === "photo") {
      const file = files[0];
      setFormData({ ...formData, photo: file });
      setPhotoPreview(URL.createObjectURL(file));
    } else {
      setFormData({ ...formData, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new FormData();
    for (const key in formData) {
      data.append(key, formData[key]);
    }
    try {
      await addPlayer(data);
      navigate("/admin/players");
    } catch (error) {
      console.error("Error adding player:", error);
    }
  };

  return (
    <div>
      <AdminHeader />
      <main className="container mx-auto px-4 py-8">
        <h2 className="text-3xl font-bold text-gray-900 mb-6">Añadir Nuevo Jugador</h2>
        <Card>
          <form
            onSubmit={handleSubmit}
            className="flex flex-col gap-4"
            encType="multipart/form-data"
          >
            {/* First Name */}
            <div>
              <Label htmlFor="first_name" value="Nombre" />
              <TextInput
                id="first_name"
                name="first_name"
                value={formData.first_name}
                onChange={handleChange}
                placeholder="Nombre del jugador"
                required
              />
            </div>

            {/* Last Name */}
            <div>
              <Label htmlFor="last_name" value="Apellido" />
              <TextInput
                id="last_name"
                name="last_name"
                value={formData.last_name}
                onChange={handleChange}
                placeholder="Apellido del jugador"
                required
              />
            </div>

            {/* Alias */}
            <div>
              <Label htmlFor="alias" value="Alias (Opcional)" />
              <TextInput
                id="alias"
                name="alias"
                value={formData.alias}
                onChange={handleChange}
                placeholder="Alias del jugador (opcional)"
              />
            </div>

            {/* Gender */}
            <div>
              <Label htmlFor="gender" value="Género" />
              <Select
                id="gender"
                name="gender"
                value={formData.gender}
                onChange={handleChange}
                required
              >
                <option value="">Seleccione</option>
                <option value="M">Masculino</option>
                <option value="F">Femenino</option>
              </Select>
            </div>

            {/* Date of Birth */}
            <div>
              <Label htmlFor="date_of_birth" value="Fecha de nacimiento" />
              <TextInput
                id="date_of_birth"
                name="date_of_birth"
                type="date"
                value={formData.date_of_birth}
                onChange={handleChange}
                required
              />
            </div>

            {/* Nationality */}
            <div>
              <Label htmlFor="nationality" value="Nacionalidad" />
              <Select
                id="nationality"
                name="nationality"
                value={formData.nationality}
                onChange={handleChange}
                required
              >
                <option value="">Seleccione</option>
                {countryChoices.map(([code, name]) => (
                  <option key={code} value={code}>
                    {name}
                  </option>
                ))}
              </Select>
            </div>

            {/* Photo Upload */}
            <div>
              <Label htmlFor="photo" value="Foto" />
              <FileInput
                id="photo"
                name="photo"
                accept="image/*"
                onChange={handleChange}
              />
              {photoPreview && (
                <img
                  src={photoPreview}
                  alt="Vista previa de la foto"
                  className="mt-4 w-32 h-32 object-cover rounded-lg shadow"
                />
              )}
            </div>

            {/* Actions */}
            <div className="flex justify-between mt-6">
              <Button type="submit" color="success">
                Guardar
              </Button>
              <Button color="gray" onClick={() => navigate("/admin/players")}>
                Volver a la Lista
              </Button>
            </div>
          </form>
        </Card>
      </main>
      <AdminFooter />
    </div>
  );
}

export default PlayerAdd;
