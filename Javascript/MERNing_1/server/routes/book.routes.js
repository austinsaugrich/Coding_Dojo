import { getAllBooks, createBook, deleteOneBook, updateOneBook, findOne } from "../controllers/book.controller.js";
import { Router } from "express";

const router = Router();


router.route("/books")
    .get(getAllBooks)
    .post(createBook)


router.route("/book/:id")
    .get(findOne)
    .put(updateOneBook)
    .delete(deleteOneBook)

export default router;