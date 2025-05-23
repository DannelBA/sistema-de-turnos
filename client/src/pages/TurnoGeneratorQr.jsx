import React from 'react';
import './TurnoGeneratorQr.css'; // 
import { Link } from 'react-router-dom';
//import qr from './assets/qr.png';     // Asegúrate de que esta ruta es correcta

export function TurnoGeneratorQr() {
  return (
    <div className="container">
      <img src="\src\assets\logo_unimag.png" alt="Logo Universidad" className="logo" />
      <h1>Generador de turnos</h1>
      <p className="subtitulo">Escanéame con tu app de UID</p>

      <div className="qr-container">
        <img src="\src\assets\logo_unimag.png" alt="Código QR" className="qr" />
      </div>

      <div className="link-container">
        <Link to="/stva">
        <strong>¿No tienes la app?</strong><br />
          Géneralo con tu código aquí.
        </Link>
      </div>
    </div>
  );
}

