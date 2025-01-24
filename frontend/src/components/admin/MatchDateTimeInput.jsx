import React from 'react';

const MatchDateTimeInput = ({ matchDateTime, setMatchDateTime }) => (
  <div className="mb-8 z-10">
    <label htmlFor="matchDateTime" className="block mb-2 font-bold text-white">
      Fecha y Hora del Partido
    </label>
    <input
      type="datetime-local"
      id="matchDateTime"
      value={matchDateTime}
      onChange={(e) => setMatchDateTime(e.target.value)}
      className="bg-white text-gray-700 px-4 py-2 rounded w-full max-w-md shadow-md"
    />
  </div>
);

export default MatchDateTimeInput;
