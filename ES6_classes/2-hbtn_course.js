export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string' || name.trim().length === 0) {
      throw new Error('Name must be a non-empty string');
    }

    if (typeof length !== 'number' || length <= 0) {
      throw new Error('Length must be a positive number');
    }

    if (!Array.isArray(students) || students.some((student) => typeof student !== 'string' || student.trim().length === 0)) {
      throw new Error('Students must be a non-empty array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string' || value.trim().length === 0) {
      throw new Error('Name must be a non-empty string');
    }
    this._name = value;
  }

  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'number' || value <= 0) {
      throw new Error('Length must be a positive number');
    }
    this._length = value;
  }

  get students() {
    return this._students;
  }

  set students(value) {
    if (!Array.isArray(value) || value.some((student) => typeof student !== 'string' || student.trim().length === 0)) {
      throw new Error('Students must be an array with non empty strings');
    }
    this._students = value;
  }
}
