import React, { useEffect, useState } from 'react';
import { Link } from "react-router-dom";
import AdminHeader from 'components/admin/AdminHeader';
import AdminFooter from 'components/admin/AdminFooter';
import { getAdminHomeData } from 'services/api.js';
import 'styles/tailwind.css';

function AdminHome() {
  const [data, setData] = useState({
    registeredPlayers: 0,
    matchesPlayedLastWeek: [],
    playerActivityTrends: [],
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await getAdminHomeData();
        setData(result);
      } catch (error) {
        console.error('Error fetching admin home data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <AdminHeader />
        <main className="container mx-auto px-4 py-8">
            {/* AdminDashboard Title */}
            <h1 className="text-3xl font-bold mb-4">Admin Dashboard</h1>

            {/* QuickAccess */}
            <section className="mb-8">
                <h2 className="text-2xl font-semibold mb-4">Quick Access</h2>
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div className="bg-blue-500 text-white rounded-lg shadow-lg p-6">
                        <div className="font-semibold text-lg mb-2">Manage Players</div>
                        <p className="text-sm mb-4">View, add, and edit player details.</p>
                        <Link to="/admin/players"
                              className="inline-block px-4 py-2 bg-white text-blue-500 rounded hover:bg-blue-100 transition">View
                            Players</Link>
                    </div>
                    <div className="bg-green-500 text-white rounded-lg shadow-lg p-6">
                        <div className="font-semibold text-lg mb-2">Manage Matches</div>
                        <p className="text-sm mb-4">Schedule and track match details.</p>
                        <Link to="/admin/matches"
                              className="inline-block px-4 py-2 bg-white text-green-500 rounded hover:bg-green-100 transition">View
                            Matches</Link>
                    </div>
                    <div className="bg-yellow-500 text-white rounded-lg shadow-lg p-6">
                        <div className="font-semibold text-lg mb-2">Manage Seasons</div>
                        <p className="text-sm mb-4">Manage system seasons.</p>
                        <Link to="/admin/seasons"
                              className="inline-block px-4 py-2 bg-white text-yellow-500 rounded hover:bg-yellow-100 transition">View
                            Seasons</Link>
                    </div>
                </div>
            </section>

            {/* Data Overview */}

            <section className="mb-8">
                <div className="bg-white shadow-md rounded-lg p-6">
                    <h2 className="text-2xl font-semibold mb-4">Registered Players</h2>
                    <p className="text-4xl">{data.registeredPlayers}</p>
                </div>
            </section>

            <section className="mb-8">
                <h2 className="text-2xl font-semibold mb-4">Matches Played in the Last Week</h2>
                {/* Add your graph component here */}
            </section>

            <section className="mb-8">
                <h2 className="text-2xl font-semibold mb-4">Player Activity Trends</h2>
                {/* Add your graph component here */}
            </section>
        </main>
        <AdminFooter/>
    </div>
  );
}

export default AdminHome;
