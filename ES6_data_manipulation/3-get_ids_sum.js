export default function getStudentIdsSum(listStudents) {
  const sum = 0;
  if (Array.isArray(listStudents)) {
    const sum = listStudents.reduce((accumulator, currentVal) => accumulator + currentVal.id, 0);
    return sum;
  }
  return sum;
}
