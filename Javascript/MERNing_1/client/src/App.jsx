import { Routes, Route, BrowserRouter } from "react-router-dom";
import "./App.css";
import Home from "./pages/home";
import CreateBook from "./pages/createbook";
import Details from "./pages/details";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Home />} path='/'></Route>
        <Route element={<CreateBook />} path='/create'></Route>
        <Route element={<Details />} path='/books/:id'></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
