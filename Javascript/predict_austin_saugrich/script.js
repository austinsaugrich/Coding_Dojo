const cars = ['Tesla', 'Mercedes', 'Honda']
const [randomCar] = cars
const [, otherRandomCar] = cars
const [, , other] = cars
//Predict the output
console.log(randomCar)
console.log(otherRandomCar)
console.log(other)

// tesla mercedes
// tesla mercedes
//I think it doesnt print out the 3rd value because there is no comma to seperate it. It looks like the second value is being printed due to the , before the variable name.
// To get it to print, youd need another variable and add a second comma has seen above.


const employee = {
    employeeName: 'Elon',
    age: 47,
    company: 'Tesla'
}
const { employeeName } = employee;
//Predict the output
console.log(employeeName);

// there would be an error
// there was an error because employeeName is not defined.
//to fix it id have to deconstruct it as done above

const person = {
    name: 'Phil Smith',
    age: 47,
    height: '6 feet'
}
const password = '12345';
const { password: hashedPassword } = person;
//Predict the output
console.log(password);
console.log(hashedPassword);

//it should print 12345 and undefined 
//it printed 12345 and undefined 
// if we wanted to do line 35, we would have too add password to the person object instead of outside of it. 

const numbers = [8, 2, 3, 5, 6, 1, 67, 12, 2];
const [, first] = numbers;
const [, , , second] = numbers;
const [, , , , , , , , third] = numbers;
const [, , , , forth] = numbers;
//Predict the output
console.log(first === second);
console.log(first === third);
console.log(forth)

// it should print false and true
// it printed false and true

const lastTest = {
    key: 'value',
    secondKey: [1, 5, 1, 8, 3, 3]
}
const { key } = lastTest;
const { secondKey } = lastTest;
const [, willThisWork] = secondKey;
//Predict the output
console.log(key);
console.log(secondKey);
console.log(secondKey[0]);
console.log(willThisWork);
console.log(secondKey[5])

//it should print, value, the array of numbers, 1, and 5.
// printed what i said

var beatles = ['Paul', 'George', 'John', 'Ringo'];
function printNames(names) {
    function actuallyPrintingNames() {
        for (var index = 0; index < names.length; index++) {
            var name = names[index];
            console.log(name + ' was found at index ' + index);
        }
        console.log('name and index after loop is ' + name + ':' + index);
    }
    actuallyPrintingNames();
}
printNames(beatles);

//there are 3 scopes, and it should print out all the names of the beatles with the index of each name


function actuallyPrintingNames() {
    for (let index = 0; index < names.length; index++) {
        let name = names[index];
        console.log(name + ' was found at index ' + index);
    }
    console.log('name and index after loop is ' + name + ':' + index);
}

// it produces the output refrenceerror because name and index are outside of the loop

const beatles = ['Paul', 'George', 'John', 'Ringo'];
function printNames(names) {
    function actuallyPrintingNames() {
        for (let index = 0; index < names.length; index++) {
            const name = names[index];
            console.log(name + ' was found at index ' + index);
        }
    }
    actuallyPrintingNames();
}
printNames(beatles);

// it prints out each index of beatles with the index of each one. const is used to make sure the value stays the same and let is used so its block scoped


const planet = {
    name: "Jupiter",
    milesFromSun: 49849,
    mass: 393983,
    composition: ["gas", "liquid", "oxygen"]
}
const planetCopy = { ...planet }
console.log(planet.composition[0] === planetCopy.composition[0])
console.log(planet === planetCopy)

// it should print out true and false, the reason for this is because the object planet and its copy are using the same array but they are still sepreate objects. 
