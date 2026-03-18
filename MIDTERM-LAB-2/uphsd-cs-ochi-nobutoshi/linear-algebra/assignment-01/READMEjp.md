Name: Nobutoshi Ochi
Student ID: 24-1786-978
Course Code: Programming2-LAB Prog2-9302-AY225
Assignment: Midterm Lab 2 — Matrix Determinant Solver
Date: March 18, 2026

課題の目的
この課題の目的は、余因子展開 (cofactor expansion) を用いて 3×3 行列の行列式を計算する方法を理解し、プログラムとして実装することです。
固定行列をハードコードする
余因子展開を使って計算する
ステップごとの出力を行う（minor → cofactor → determinant）
determinant が 0 の場合は「SINGULAR」と判定する

使用言語

Java — DeterminantSolver.java
JavaScript — determinant_solver.js
両方とも同じアルゴリズムを実装し、同じ行列を対象にしています。

実行方法（概要）

Java
javac DeterminantSolver.java
java DeterminantSolver

Java Script
node determinant_solver.js

割り当て行列
コード
| 1   2   4 |
| 3   5   6 |
| 2   4   8 |


出力の流れ

行列を表示
Row 1 に沿って余因子展開
各 minor を計算
各 cofactor を計算
determinant を算出
det = 0 の場合は「SINGULAR」と判定

最終結果

Determinant = 0
この行列は SINGULAR であり、逆行列を持ちません。