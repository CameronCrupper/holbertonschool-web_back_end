const fs = require('fs');

module.exports = async function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'UTF-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const students = data.split('\n').map((student) => student.split(','));
      const field = {};
      students.shift();
      const message = [];
      message.push(`Number of students: ${students.length}`);
      students.forEach((student) => {
        if (!field[student[3]]) field[student[3]] = [];
        field[student[3]].push(student[0]);
      });
      Object.keys(field).forEach((key) => {
        message.push(`Number of students in ${key}: ${field[key].length}. List: ${field[key].join(', ')}`);
      });
      const result = message.join('\n');
      console.log(result);
      resolve(result);
    });
  });
};
