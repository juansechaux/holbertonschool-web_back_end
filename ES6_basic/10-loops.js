export default function appendToEachArrayValue(array, appendString) {
  let index = 0;
  for (const str of array) {
    array[index] = appendString + str;
    index += 1;
  }

  return array;
}
