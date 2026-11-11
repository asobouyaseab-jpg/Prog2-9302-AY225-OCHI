/*
 * Name: Nobutoshi Ochi
 * Student ID: 24-1786-978
 * Course Code: Programming2-LAB
 * Assignment: Midterm Lab 2 - Matrix Determinant Solver
 * Date: March 18, 2026
 * Description: Computes the determinant of a fixed 3x3 matrix using cofactor expansion.
 */

public class DeterminantSolver {
    // 固定行列を先に提示
    static double[][] M = {
        {1, 2, 4},
        {3, 5, 6},
        {2, 4, 8}
    };

    // 2x2 minor を計算
    public static double computeMinor(double a, double b, double c, double d) {
        return a * d - b * c;
    }

    // 行列を表示
    public static void printMatrix(double[][] M) {
        for (int i = 0; i < 3; i++) {
            System.out.printf("  | %2.0f  %2.0f  %2.0f |\n", M[i][0], M[i][1], M[i][2]);
        }
    }

    // 余因子展開で行列式を計算
    public static double solveDeterminant(double[][] M) {
        System.out.println("===================================================");
        System.out.println("  3x3 MATRIX DETERMINANT SOLVER");
        System.out.println("  Student: Nobutoshi Ochi");
        System.out.println("  Assigned Matrix:");
        System.out.println("===================================================");
        printMatrix(M);
        System.out.println("===================================================\n");

        System.out.println("Expanding along Row 1 (cofactor expansion):\n");

        double minor1 = computeMinor(M[1][1], M[1][2], M[2][1], M[2][2]);
        System.out.println("  Step 1 — Minor M₁₁ = " + minor1);

        double minor2 = computeMinor(M[1][0], M[1][2], M[2][0], M[2][2]);
        System.out.println("  Step 2 — Minor M₁₂ = " + minor2);

        double minor3 = computeMinor(M[1][0], M[1][1], M[2][0], M[2][1]);
        System.out.println("  Step 3 — Minor M₁₃ = " + minor3);

        double c11 = M[0][0] * minor1;
        double c12 = -M[0][1] * minor2;
        double c13 = M[0][2] * minor3;

        System.out.println("\n  Cofactor C₁₁ = " + c11);
        System.out.println("  Cofactor C₁₂ = " + c12);
        System.out.println("  Cofactor C₁₃ = " + c13);

        double det = c11 + c12 + c13;
        System.out.println("\n  det(M) = " + det);
        System.out.println("===================================================");
        System.out.println("  ✓  DETERMINANT = " + det);
        System.out.println("===================================================");

        if (det == 0) {
            System.out.println("The matrix is SINGULAR — it has no inverse.");
        }
        return det;
    }

    public static void main(String[] args) {
        solveDeterminant(M);
    }
}
