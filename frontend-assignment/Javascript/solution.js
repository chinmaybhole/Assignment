function toCase(str) {
  return str.toLowerCase() + "-" + str.toUpperCase();
}

function firstChar(str) {
  for (let i = 0; i < str.length; i++) {
    if (str[i] !== " ") {
      return str[i];
    }
  }
  return "";
}

function rotate(arr) {
  let firstElement = arr.shift();
  arr.push(firstElement);
  return arr;
}

let str = "Mthatha";
let result = toCase(str);
console.log(result);

let result1 = firstChar(str);
console.log(result1);

let arr = ["a", "b", "c"];
let result2 = rotate(arr);
console.log(result2); // Output: ['b', 'c', 'a']
