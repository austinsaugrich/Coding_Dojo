import { model, Schema } from 'mongoose';
const BookSchema = new Schema(
    {
        title: {
            type: String,
            required: [true, "Title is required!"],
            minlength: [2, "The title must be at least 2 characters long!"],
            maxlength: [255, "The title must be less than 255 characters long!"]
        },
        author: {
            type: String,
            required: [true, "Author is required!"],
            minlength: [5, "The Authors name must be at least 5 characters long!"],
            maxlength: [255, "The Authors name must be less than 255 characters long!"]
        },
        pages: {
            type: Number,
            required: [true, "Number of pages is required!"],
            minlength: [1, "The book needs to have at least 1 page!"],
        },
        isAvailable: {
            type: Boolean,
            default: false
        }
    },
    { timestamps: true }
);
const Book = model("Book", BookSchema);
export default Book;