let num = process.argv[2];

function fiboEvenSum(n) {
  let i = 1;
  let x = 1;
  let y = 1;
  let sum = 0;
  while (i < n) {
    let z = x + y;
    if (z % 2 === 0) {
      sum += z;
    }
    x = y;
    y = z;
    i++;
  }
  return sum;
}

console.log(fiboEvenSum(num));
