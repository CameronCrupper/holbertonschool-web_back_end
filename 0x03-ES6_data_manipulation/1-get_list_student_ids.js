const getListStudentIds = (ids) => {
  if (!Array.isArray(ids)) {
    return [];
  }
  const ids2 = ids.map((item) => item.id);

  return ids2;
};

export default getListStudentIds;
