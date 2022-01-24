var words = require('an-array-of-french-words')

final_arr = []
start = "."
words.forEach((item,index)=>{
    if(item[0] != start) {
        console.log(item)
        final_arr.push(index)
        start = item[0]
    }
})

const alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];

for (const [i, v] of alphabet.entries()) {
    console.log("\""+ v + "\" : " + final_arr[i])
}

let myDictionary = {
    "a" : 0,
    "b" : 24298,
    "c" : 39404,
    "d" : 73612,
    "e" : 114106,
    "f" : 135159,
    "g" : 147643,
    "h" : 157832,
    "i" : 163673,
    "j" : 175370,
    "k" : 177768,
    "l" : 178259,
    "m" : 185336,
    "n" : 201628,
    "o" : 205516,
    "p" : 210849,
    "q" : 237924,
    "r" : 239055,
    "s" : 274886,
    "t" : 297250,
    "u" : 313222,
    "v" : 314213,
    "w" : 321430,
    "x" : 321622,
    "y" : 321685,
    "z" : 321777,
}

const fs = require('fs');
const writeStream = fs.createWriteStream('WordList.txt');
const pathName = writeStream.path;

// for (const [key, value] of Object.entries(myDictionary)) {
//     writeStream.write(`${value} : ${key}\n`);
// }

words.forEach(value => writeStream.write(`${value}\n`));


writeStream.on('finish', () => {
   console.log(`wrote all the array data to file ${pathName}`);
});

writeStream.on('error', (err) => {
    console.error(`There is an error writing the file ${pathName} => ${err}`)
});

writeStream.end();