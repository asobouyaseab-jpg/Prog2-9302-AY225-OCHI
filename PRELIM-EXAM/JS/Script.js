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
