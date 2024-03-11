//problem 1
const checkAge = age => age >= 18 ? "You are good to go!" : "Sorry! You must be 18 or older!";


console.log(checkAge(20));
console.log(checkAge(16));


//problem 2
const checkWeather = isRaining => isRaining ? "Get your rain jacket!" : "No rain on today's forecast!";


console.log(checkWeather(true));
console.log(checkWeather(false));


// problem 3
const checkEvenOdd = num => num % 2 === 0 ? "That's an even number!" : "That's an odd number!";


console.log(checkEvenOdd(4));
console.log(checkEvenOdd(7));

//problem 4
const compareNumbers = (num1, num2) => num1 > num2 ? `${num1} is more than ${num2}!` : `${num1} is less than ${num2}!`;


console.log(compareNumbers(10, 5));
console.log(compareNumbers(3, 9));

