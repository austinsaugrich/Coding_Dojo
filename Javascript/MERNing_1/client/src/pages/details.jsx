/* eslint-disable react/prop-types */
import Header from "../components/Header";
import { useParams } from "react-router-dom";
import axios from "axios";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Details() {
  const { id } = useParams();
  useEffect(() => {
    getABook(id);
  }, []);
  const [book, setBook] = useState([]);
  console.log(book);
  async function getABook(id) {
    try {
      const response = await axios.get("http://localhost:8000/api/book/" + id);
      setBook(response.data);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <>
      <Header title={book.title} />
      <BookDetails book={book} />
    </>
  );
}

const BookDetails = ({ book }) => {
  const navigate = useNavigate();
  async function HandleDelete(event) {
    event.preventDefault();
    try {
      await axios.delete("http://localhost:8000/api/book/" + book._id, {});
      navigate("/");
    } catch (error) {
      console.log(error);
    }
  }
  return (
    <div className='contentContainer'>
      <div className='content'>
        <div>
          <h1>{book.title}</h1>
          <h3>By {book.author}</h3>
        </div>
        <div>
          <h3>Page Count {book.pages}</h3>
          <h2>
            {book.isAvailable
              ? "Available for borrowing"
              : "Not available for borrowing"}
          </h2>
        </div>
        <div>
          <button onClick={HandleDelete}>Borrow</button>
        </div>
      </div>
    </div>
  );
};
