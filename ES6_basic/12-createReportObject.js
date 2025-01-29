import createEmployeeObject from "./11-createEmployeesObject";

export default function createReportObject(employeesList) {
  employeesList = createEmployeeObject();
  console.log(employeesList)
}
