export default function appendToEachArrayValue(array, appendString) {
  for (let idx of value) {
    let value = array[idx];
    array[idx] = appendString + value;
  }

  return array
}
