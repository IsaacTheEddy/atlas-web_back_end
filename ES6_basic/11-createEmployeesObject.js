export default function createEmployeeObject(departmentName, employees) {
  const Obj = {
    [`${departmentName}`]: Array.isArray(employees) ? employees.map(emp => emp.name || emp) : []
  }
  return Obj;
}
