export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  const array = [];
  set.forEach((value) => {
    if (value.startsWith(startString)) {
      array.push(value.replace(startString, ''));
    }
  });
  return String(array).replace(/,/g, '-');
}
