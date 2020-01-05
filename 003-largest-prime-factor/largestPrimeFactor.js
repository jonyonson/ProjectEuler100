function largestPrimeFactor(number) {
  let i = 2;
  let max = 1;
  while (i <= number) {
    if (number % i === 0) {
      max = i;
      number /= i;
    } else {
      i++;
    }
  }
  return max;
}
