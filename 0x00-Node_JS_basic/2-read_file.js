const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    const field = {};
    const data = fs.readFileSync(path, 'UTF-8');
    const students = data.split('\n').map((student) => student.split(','));
    students.shift();
    console.log(`Number of students: ${students.length}`);
    students.forEach((student) => {
      if (!field[student[3]]) field[student[3]] = [];
      field[student[3]].push(student[0]);
    });
    Object.keys(field).forEach((key) => {
      console.log(`Number of students in ${key}: ${field[key].length}. List: ${field[key].join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};
