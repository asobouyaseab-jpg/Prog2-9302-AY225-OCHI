<<<<<<< HEAD
// Programmer Identifier: Nobutoshi [24-1786-978]

// CSVを外部ファイルから読み込む
async function loadCSV() {
  try {
    const response = await fetch("MOCK_DATA.csv"); // 同じフォルダにあるCSVを取得
    const text = await response.text();
    parseCSV(text);
  } catch (error) {
    console.error("CSV読み込みエラー:", error);
  }
}

let students = [];

function parseCSV(csvText) {
  const lines = csvText.trim().split("\n");
  const headers = lines[0].split(",");

  students = lines.slice(1).map(line => {
    const values = line.split(",");
    return {
      id: values[0],
      name: values[1] + " " + values[2], // first_name + last_name
      grade: values[3]                   // LAB WORK 1 を例として表示
    };
  });

  render();
}

function render() {
  const table = document.getElementById("studentTable");
  table.innerHTML = `
    <tr><th>ID</th><th>Name</th><th>Grade</th><th>Action</th></tr>
    ${students.map((s, index) => `
      <tr>
        <td>${s.id}</td>
        <td>${s.name}</td>
        <td>${s.grade}</td>
        <td><button onclick="deleteStudent(${index})">Delete</button></td>
      </tr>
    `).join("")}
  `;
}

function deleteStudent(index) {
  students.splice(index, 1);
  render();
}

document.getElementById("addForm").addEventListener("submit", e => {
  e.preventDefault();
  const id = document.getElementById("idInput").value;
  const name = document.getElementById("nameInput").value;
  const grade = document.getElementById("gradeInput").value;
  students.push({ id, name, grade });
  render();
});

// ページ読み込み時にCSVを読み込む
loadCSV();
=======
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
>>>>>>> adb71b09c10cf060179503bd37fe3cbb9774f921
