function push(array, value) {
    for (let i = array.length; i > 0; i--) {
        array[i] = array[i - 1]
    }
    array[0] = value
    return array
}

console.log(push([1, 2, 3, 4, 5], 6))

function insert(array, index, value) {
    for (let i = array.length; i > 0; i--) {
        array[i] = array[i - 1]
    }
    array[index] = value
    return array
}

console.log(insert([1, 2, 3, 4], 2, 21))

function remove(array, index) {
    const removedNumber = array[index]
    for (let i = index; i < array.length - 1; i++) {
        array[i] = array[i + 1]
    }
    array.length = array.length - 1;
    console.log(array)
    return removedNumber
}
console.log(remove([1, 2, 3, 4, 5], 1))