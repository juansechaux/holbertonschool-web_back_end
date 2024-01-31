export default function getStudentsByLocation(listStudents, city) {
  const newArray = [];
  if (Array.isArray(listStudents)) {
    const newArray = listStudents.filter((value) => value.location === city);
    return newArray;
  }
  return newArray;
}
