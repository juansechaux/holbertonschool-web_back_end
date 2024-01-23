export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = "";
    this._length = 0;
    this._students = [];

    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }

  set length(newLength) {
    if (typeof newLength !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = newLength;
  }

  set students(newStudents) {
    if (!Array.isArray(newStudents) || !newStudents.every(item => typeof item === 'string')) {
      throw new TypeError('newStudents must be an array of strings');
    }
    this._students = newStudents;
  }
}
