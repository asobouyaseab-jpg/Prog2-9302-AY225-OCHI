/*
 * Name: Nobutoshi Ochi
 * Student ID: 24-1786-978
 * Course Code: Programming2-LAB
 * Assignment: Midterm Lab 2 - Matrix Determinant Solver
 * Date: March 18, 2026
 * Description: Computes the determinant of a fixed 3x3 matrix using cofactor expansion.
 */

// 固定行列を先に提示
const matrix = [
    [1, 2, 4],
    [3, 5, 6],
    [2, 4, 8]
];

// 2x2 minor を計算
function computeMinor(a, b, c, d) {
    return (a * d) - (b * c);
}

// 行列を表示
function printMatrix(m) {
    m.forEach(row => {
        console.log(`  | ${row[0]}  ${row[1]}  ${row[2]} |`);
    });
}

// 余因子展開で行列式を計算
function solveDeterminant(m) {
    const line = "=".repeat(50);

    console.log(line);
    console.log("  3x3 MATRIX DETERMINANT SOLVER");
    console.log("  Student: Nobutoshi Ochi");
    console.log("  Assigned Matrix:");
    console.log(line);
    printMatrix(m);
    console.log(line + "\n");

    console.log("Expanding along Row 1 (cofactor expansion):\n");

    const minor11 = computeMinor(m[1][1], m[1][2], m[2][1], m[2][2]);
    console.log(`  Step 1 — Minor M₁₁ = ${minor11}`);

    const minor12 = computeMinor(m[1][0], m[1][2], m[2][0], m[2][2]);
    console.log(`  Step 2 — Minor M₁₂ = ${minor12}`);

    const minor13 = computeMinor(m[1][0], m[1][1], m[2][0], m[2][1]);
    console.log(`  Step 3 — Minor M₁₃ = ${minor13}`);

    const c11 = m[0][0] * minor11;
    const c12 = -m[0][1] * minor12;
    const c13 = m[0][2] * minor13;

    console.log(`\n  Cofactor C₁₁ = ${c11}`);
    console.log(`  Cofactor C₁₂ = ${c12}`);
    console.log(`  Cofactor C₁₃ = ${c13}`);

    const det = c11 + c12 + c13;
    console.log(`\n  det(M) = ${det}`);
    console.log(line);
    console.log(`  ✓  DETERMINANT = ${det}`);
    console.log(line);

    if (det === 0) {
        console.log("The matrix is SINGULAR — it has no inverse.");
    }
}

// 実行
solveDeterminant(matrix);
