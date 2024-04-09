import express from "express";
const app = express();
const port = 8000;

// make sure these lines are above any app.get or app.post code blocks
app.use(express.json());

import { faker } from "@faker-js/faker";
const createUser = () => {
    const newUser = {
        firstName: faker.person.firstName(),
        lastName: faker.person.lastName(),
        phoneNumber: faker.phone.number(),
        email: faker.internet.email(),
        password: faker.internet.password(),
        _id: faker.number.int()
    }
    return newUser
}

const createCompany = () => {
    const newCompany = {
        name: faker.company.name(),
        _id: faker.number.int(),
        address: {
            street: faker.location.street(),
            city: faker.location.city(),
            zipcode: faker.location.zipCode(),
            state: faker.location.state(),
            country: faker.location.country()
        }
    }
    return newCompany
}





app.get("/api/users/new", (req, res) => {
    res.json(createUser());
});

app.get("/api/companies/new", (req, res) => {
    res.json(createCompany());
});

app.get("/api/user/company", (req, res) => {
    const company = createCompany()
    company['users'] = [createUser()]
    res.json(company)
});












app.post("/api/users", (req, res) => {
    // req.body will contain the form data from Postman or from React later
    console.log(req.body);
    // we can push it into the users array for now...
    // later on this will be inserted into a database using a database method
    users.push(req.body);
    // the updated users array
    res.json(users);
});




// this needs to be below the other code blocks
app.listen(port, () => console.log(`Listening on port: ${port}`));
