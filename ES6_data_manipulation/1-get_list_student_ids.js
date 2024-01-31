export default function getListStudentIds(arrayData) {
  const newArray = [];
  if (Array.isArray(arrayData)) {
    const newArray = arrayData.map((value) => value.id);
    return newArray;
  }
  return newArray;
}
