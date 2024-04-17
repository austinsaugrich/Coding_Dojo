import Header from "../components/Header";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useState } from "react";

export default function CreateBook() {
  return (
    <>
      <Header title='Add a book' />
      <AddForm />
    </>
  );
}

function AddForm() {
  const navigate = useNavigate();
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [pageCount, setPageCount] = useState(0);
  const [availability, setAvailability] = useState(false);
  function handleTitle(event) {
    setTitle(event.target.value);
  }
  function handleAuthor(event) {
    setAuthor(event.target.value);
  }
  function handlePageCount(event) {
    setPageCount(event.target.value);
  }
  function handleAvailability(event) {
    setAvailability(event.target.checked);
  }

  async function handleSubmit(event) {
    event.preventDefault();
    try {
      await axios.post("http://localhost:8000/api/books", {
        title: title,
        author: author,
        pages: pageCount,
        isAvailable: availability,
      });
      navigate("/");
    } catch (error) {
      console.log(error);
    }
  }
  return (
    <div className='contentContainer'>
      <form>
        <div className='content'>
          <label>Title</label>
          <input type='text' onChange={handleTitle} value={title} />
          <label>Authors Name</label>
          <input type='text' onChange={handleAuthor} value={author} />
          <label>Page Count</label>
          <input type='number' onChange={handlePageCount} value={pageCount} />
          <div>
            <label>Is it Available</label>
            <input
              type='checkbox'
              onChange={handleAvailability}
              value={availability}
              checked={availability}
            />
          </div>
          <button className='button' type='submit' onClick={handleSubmit}>
            Add A Book
          </button>
        </div>
      </form>
    </div>
  );
}
