import Header from "../components/Header";
import { useState } from "react";
import { useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const [books, setBooks] = useState([]);
  useEffect(() => {
    getBooks();
  }, []);
  console.log(books);
  async function getBooks() {
    try {
      const response = await axios.get("http://localhost:8000/api/books");
      setBooks(response.data);
    } catch (error) {
      console.log(error);
    }
  }
  return (
    <>
      <Header title='Book Catalog' />
      <Table books={books} />
    </>
  );
}

const Table = ({ books }) => {
  const navigate = useNavigate();
  function goTo(id) {
    navigate("/books/" + id);
  }
  return (
    <div className='tableContainer'>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Page Count</th>
            <th>Available</th>
            <th>Book Page</th>
          </tr>
        </thead>
        <tbody>
          {books.map((book, index) => (
            <tr key={index}>
              <td>{book.title}</td>
              <td>{book.author}</td>
              <td>{book.pages}</td>
              <td>{book.isAvailable ? "Yes" : "No"}</td>
              <td>
                <button onClick={() => goTo(book._id)}>Book Details</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
