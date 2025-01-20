import React, { useState, useEffect } from "react";
import { Link, useLocation } from "react-router-dom";
import "styles/tailwind.css";
import { Button } from "flowbite-react";

function Header() {
  const location = useLocation(); // Get current route
  const [isSidebarOpen, setIsSidebarOpen] = useState(false); // Sidebar state
  const [opacity, setOpacity] = useState(1); // Opacity state for scroll effect

  const toggleSidebar = () => {
    setIsSidebarOpen((prev) => !prev); // Toggle sidebar
  };

  useEffect(() => {
    const handleScroll = () => {
      setOpacity(window.scrollY > 50 ? 0.9 : 1); // Adjust opacity on scroll
    };

    window.addEventListener("scroll", handleScroll);

    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <div>
      {/* Header */}
      {!isSidebarOpen && (
        <header
          className={`sticky top-0 z-50 bg-green-700 shadow-md transition-opacity duration-300`}
          style={{ opacity }}
        >
          <div className="container mx-auto flex items-center justify-between px-4 sm:px-6 lg:px-10 py-3 sm:py-4">
            {/* Logo */}
            <Link to="/" className="flex items-center text-white no-underline space-x-3">
              <img
                src="/src/assets/images/logo-white-48.png"
                alt="Logo"
                className="h-10 sm:h-12"
              />
              <span className="text-lg sm:text-2xl font-semibold">
                Clasificación de Tenis de Mesa
              </span>
            </Link>

            {/* Desktop Navigation */}
            <nav className="hidden sm:flex items-center space-x-6 lg:space-x-8 text-sm sm:text-base text-white font-medium">
              <Link
                to="/"
                className={`hover:text-gray-300 ${location.pathname === "/" ? "font-bold text-white" : ""}`}
              >
                Inicio
              </Link>
              <Link
                to="/players/"
                className={`hover:text-gray-300 ${location.pathname === "/players/" ? "font-bold text-white" : ""}`}
              >
                Jugadores
              </Link>
              <Link
                to="/matches/"
                className={`hover:text-gray-300 ${location.pathname === "/matches/" ? "font-bold text-white" : ""}`}
              >
                Partidos
              </Link>
              <Link
                to="/seasons/"
                className={`hover:text-gray-300 ${location.pathname === "/seasons/" ? "font-bold text-white" : ""}`}
              >
                Temporadas
              </Link>
              <Link
                to="/login/"
                className="text-green-700 bg-white border-2 border-white rounded-md py-2 px-4 hover:bg-green-700 hover:text-white transition-all"
              >
                Iniciar Sesión
              </Link>
            </nav>


            {/* Hamburger Icon (Mobile) */}
            <Button
              className="text-white sm:hidden"
              onClick={toggleSidebar}
              aria-label="Toggle menu"
            >
              <i className="fas fa-bars text-2xl"></i>
            </Button>
          </div>
        </header>
      )}

      {/* Sidebar (Mobile) */}
      <div
        className={`fixed top-0 left-0 h-full w-64 bg-green-700 transform ${
          isSidebarOpen ? "translate-x-0" : "-translate-x-full"
        } transition-transform duration-300 shadow-lg z-40`}
      >
        <div className="flex items-center justify-between px-4 py-4">
          <span className="text-white text-lg font-semibold">Menú</span>
          <Button
            className="text-white"
            onClick={toggleSidebar}
            aria-label="Close menu"
          >
            <i className="fas fa-times text-2xl"></i>
          </Button>
        </div>
        <nav>
          <ul className="flex flex-col space-y-6 px-4 text-white font-medium text-sm">
            <li>
              <Link
                to="/"
                className={`block hover:text-gray-300 ${location.pathname === "/" ? "font-bold text-white" : ""}`}
                onClick={toggleSidebar}
              >
                Inicio
              </Link>
            </li>
            <li>
              <Link
                to="/players/"
                className={`block hover:text-gray-300 ${location.pathname === "/players/" ? "font-bold text-white" : ""}`}
                onClick={toggleSidebar}
              >
                Jugadores
              </Link>
            </li>
            <li>
              <Link
                to="/matches/"
                className={`block hover:text-gray-300 ${location.pathname === "/matches/" ? "font-bold text-white" : ""}`}
                onClick={toggleSidebar}
              >
                Partidos
              </Link>
            </li>
            <li>
              <Link
                to="/seasons/"
                className={`block hover:text-gray-300 ${location.pathname === "/seasons/" ? "font-bold text-white" : ""}`}
                onClick={toggleSidebar}
              >
                Temporadas
              </Link>
            </li>
            <li>
              <Link
                to="/login/"
                className="block text-green-700 bg-white border-2 border-white rounded-md px-4 text-center hover:bg-green-700 hover:text-white transition-all"
                onClick={toggleSidebar}
              >
                Iniciar Sesión
              </Link>
            </li>
          </ul>
        </nav>
      </div>

      {/* Overlay for Sidebar */}
      {isSidebarOpen && (
        <div
          className="fixed inset-0 bg-black opacity-50 z-30"
          onClick={toggleSidebar}
        ></div>
      )}
    </div>
  );
}

export default Header;
