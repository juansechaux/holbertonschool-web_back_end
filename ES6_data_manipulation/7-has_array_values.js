export default function hasValuesFromArray(set, array) {
  let flag = true;
  for (const data of array) {
    if (set.has(data) === false) {
      flag = false;
    }
  }
  return flag;
}
