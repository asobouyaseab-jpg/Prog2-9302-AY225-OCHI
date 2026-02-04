Papa.parse("MOCK_DATA.csv", {
  download: true,
  header: true,
  skipEmptyLines: true,
  complete: function(results) {
    renderTable(results.data);
  }
});

function calculateGrade(student) {
  // LAB WORK 1〜3 の平均
  const lab1 = Number(student["LAB WORK 1"]);
  const lab2 = Number(student["LAB WORK 2"]);
  const lab3 = Number(student["LAB WORK 3"]);
  const labAvg = (lab1 + lab2 + lab3) / 3;

  // PRELIM EXAM
  const exam = Number(student["PRELIM EXAM"]);

  // 加重平均: LAB 40%, EXAM 60% → 整数に丸める
  return Math.round(labAvg * 0.4 + exam * 0.6);
}

function renderTable(students) {
  const tableBody = document.getElementById("studentTable");
  tableBody.innerHTML = "";

  students.forEach((student, index) => {
    const grade = calculateGrade(student);
    const row = `
      <tr>
        <td>${student.StudentID}</td>
        <td>${student.first_name} ${student.last_name}</td>
        <td>${grade}</td>
        <td><button onclick="deleteStudent(${index})">Delete</button></td>
      </tr>
    `;
    tableBody.innerHTML += row;
  });
}

function deleteStudent(index) {
  const tableBody = document.getElementById("studentTable");
  tableBody.deleteRow(index);
}
