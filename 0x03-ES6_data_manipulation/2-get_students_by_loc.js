const getStudentsByLocation = (students, city) => {
  const stewsLok = students.filter(
    (student) => student.location === city,
  );
  return stewsLok;
};
export default getStudentsByLocation;
