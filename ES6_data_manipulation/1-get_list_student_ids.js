export default function getListStudentIds(arrayData) {
  const arrayIds = [];
  if (typeof arrayData !== typeof arrayIds) {
    return arrayIds;
  }
  const items = arrayData.keys();
  for (const obj of items) {
    arrayIds.push(arrayData[obj].id);
  }
  return arrayIds;
}
