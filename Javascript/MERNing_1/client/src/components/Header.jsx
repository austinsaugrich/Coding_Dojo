import { useNavigate } from "react-router-dom";

function Header({ title }) {
  const navigate = useNavigate();
  function goTo(page) {
    navigate(page);
  }
  return (
    <div className='header'>
      <div className='buttonContainer'>
        <button className='button' onClick={() => goTo("/")}>
          Catalog
        </button>
        <button className='button' onClick={() => goTo("/create")}>
          Add book
        </button>
      </div>
      <div className='title'>
        <h1>{title}</h1>
      </div>
    </div>
  );
}
export default Header;
