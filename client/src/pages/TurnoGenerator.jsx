import React, { useState } from "react";
import axios from "axios";
import "./TurnoGenerator.css";
import { Link } from "react-router-dom";
import Swal from "sweetalert2";

export function TurnoGenerator() {
  const [codigo, setCodigo] = useState("");

  const handleGenerarTurno = async () => {
    const codigoTrimmed = codigo.trim();

    // Validar si el campo está vacío
    if (!codigoTrimmed) {
      Swal.fire({
        title: "Campo vacío",
        text: "Por favor, ingresa tu código antes de continuar.",
        icon: "warning",
        confirmButtonText: "Entendido",
      });
      return; // Evita que siga el proceso si está vacío
    }

    try {
      const response = await axios.post(
        "http://localhost:8000/stva/api/v1/generar_turno/",
        { codigo: codigoTrimmed }
      );

      Swal.fire({
        title: "Turno generado",
        text: response.data.mensaje,
        icon: "success",
        confirmButtonText: "OK",
      });
    } catch (error) {
      let mensajeError = "Error de conexión con el servidor.";
      if (error.response && error.response.data.error) {
        mensajeError = error.response.data.error;
      }

      Swal.fire({
        title: "Error",
        text: mensajeError,
        icon: "error",
        confirmButtonText: "Entendido",
      });
    }
  };

  return (
    <div className="turno-container">
      <img src="/src/assets/logo_unimag.png" alt="Logo" className="logo" />
      <h1 className="titulo">Generador de turnos</h1>

      <input
        type="number"
        placeholder="Código"
        value={codigo}
        onChange={(e) => setCodigo(e.target.value)}
        className="input-codigo"
      />

      <button onClick={handleGenerarTurno} className="boton-turno">
        Generar turno
      </button>

      <Link to="/stva_qr" className="enlace-qr">
        Genera tu turno con QR aquí.
      </Link>
    </div>
  );
}
