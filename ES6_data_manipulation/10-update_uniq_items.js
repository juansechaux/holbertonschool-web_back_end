export default function updateUniqueItems(mapData) {
  if (!(mapData instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const [key, value] of mapData) {
    if (value === 1) {
      mapData.set(key, 100);
    }
  }
  return mapData;
}
