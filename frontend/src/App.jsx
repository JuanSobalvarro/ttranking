import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from 'pages/visitor/Home.jsx';
import PlayerList from "pages/visitor/players/PlayerList.jsx";
import PlayerDetail from "pages/visitor/players/PlayerDetail.jsx";

import ProtectedRoute from 'components/ProtectedRoute.jsx';
import AdminHome from 'pages/admin/Home.jsx';
import AdminLogin from 'pages/admin/AdminLogin.jsx';
import AdminPlayerList from 'pages/admin/players/PlayerList.jsx';
import AdminPlayerAdd from 'pages/admin/players/PlayerAdd.jsx';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          {/* Visitor views */}
          <Route path="/" element={<Home />} />
          <Route path="/players" element={<PlayerList />} />
          <Route path="/players/:id" element={<PlayerDetail />} />
          <Route path="/login" element={<AdminLogin />} />
          {/* Admin Views */}
          <Route path="/admin"
            element={
              <ProtectedRoute>
                <AdminHome />
              </ProtectedRoute>
            }
          />
          <Route path="/admin/players"
            element={
              <ProtectedRoute>
                <AdminPlayerList />
              </ProtectedRoute>
            }
          />
          <Route path="/admin/players/add"
            element={
              <ProtectedRoute>
                <AdminPlayerAdd />
              </ProtectedRoute>
            }
          />
          <Route path="/admin/matches"
            element={
              <ProtectedRoute>
                <AdminHome />
              </ProtectedRoute>
            }
          />
          <Route path="/admin/seasons"
            element={
              <ProtectedRoute>
                <AdminHome />
              </ProtectedRoute>
            }
          />

          <Route path="*" element={<h1>Not Found</h1>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;