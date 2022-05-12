const getStudentIdsSum = (students) => {
  const everyone = students
    .map((student) => student.id)
    .reduce((studentPrev, studentCurrent) => studentPrev + studentCurrent);
  return everyone;
};
export default getStudentIdsSum;
