Matrix Determinant Solver — Midterm Lab 2

Name: Nobutoshi Ochi
Student ID: 24-1786-978
Course Code: Programming2-LAB (Prog2-9302-AY225)
Assignment: Midterm Lab 2 — Matrix Determinant Solver
Date: March 18, 2026

Objective
The purpose of this assignment is to understand how to compute the determinant of a 3×3 matrix using cofactor expansion and to implement the process in code.
- Hard-code the given fixed matrix in the program
- Use cofactor expansion to calculate the determinant
- Display step-by-step output (minor → cofactor → determinant)
- If the determinant equals 0, classify the matrix as SINGULAR

Languages
Java — DeterminantSolver.java
JavaScript — determinant_solver.js
Both programs implement the same algorithm and operate on the same matrix.

How to Run
Java:
javac DeterminantSolver.java
java DeterminantSolver

JavaScript (using Node.js):
node determinant_solver.js

Assigned Matrix
| 1   2   4 |
| 3   5   6 |
| 2   4   8 |

Output Flow
1. Display the matrix
2. Perform cofactor expansion along Row 1
3. Compute each minor
4. Compute each cofactor
5. Calculate the determinant
6. If determinant = 0, output SINGULAR

Final Result
Determinant = 0
The matrix is SINGULAR and does not have an inverse.