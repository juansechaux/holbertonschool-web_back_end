import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const arrayOfClassrooms = [];
  /* eslint-disable no-plusplus */
  for (let x = 19; x < 21; x++) {
    arrayOfClassrooms.push(new ClassRoom(x));
  }
  arrayOfClassrooms.push(new ClassRoom(34));
  return arrayOfClassrooms;
}
