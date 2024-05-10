function removeBlanks(string) {
    let noSpace = "";
    for (let i = 0; i < string.length; i++) {
        if (string[i] !== ' ') {
            noSpace += string[i]
        }
    }
    return noSpace
}
console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "));

function getDigits(string) {
    let numbers = ""
    for (let i = 0; i < string.length; i++) {
        if (!isNaN(Number(string[i])))
            numbers += string[i]
    }
    return Number(numbers)
}
console.log(getDigits("abc8c0d1ngd0j0!8"));

function acronym(string) {
    let words = string.split(' ');
    let acronym = "";
    for (let i = 0; i < words.length; i++) {
        if (words[i] !== '') {
            acronym += words[i][0].toUpperCase();
        }
    }
    return acronym;
}
console.log(acronym(" there's no free lunch - gotta pay yer way. "));

function countNonSpaces(string) {
    let count = 0;
    for (let i = 0; i < string.length; i++) {
        if (string[i] !== ' ') {
            count++;
        }
    }
    return count;
}

console.log(countNonSpaces("Honey pie, you are driving me crazy"));

function removeShorterStrings(array, num) {
    let result = [];
    let resultIndex = 0;
    for (let i = 0; i < array.length; i++) {
        if (array[i].length >= num) {
            result[resultIndex] = array[i];
            resultIndex++;
        }
    }
    return result;
}

console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4));