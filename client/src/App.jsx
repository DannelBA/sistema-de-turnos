import { BrowserRouter, Routes, Route } from "react-router-dom";
import { TurnoGenerator } from "./pages/TurnoGenerator";
import { TurnoGeneratorQr } from "./pages/TurnoGeneratorQr";

export function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/stva" element={<TurnoGenerator />} />
        <Route path="/stva_Qr" element={<TurnoGeneratorQr />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
