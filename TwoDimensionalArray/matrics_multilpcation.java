package TwoDimensionalArray;

public class matrics_multilpcation {
    public static void main(String[] args) {
        int[][] a = {{1, 2, 1}, {2, 1, 2}};
        int[][] b = {{1, 0, 1, 2}, {2, 10, 0, 0}, {0, 3, 1, 1}};

        if (a[0].length != b.length) {
            System.out.println("Matrix multiplication is not possible.");
        } else {
            int[][] c = new int[a.length][b[0].length];

            for (int i = 0; i < c.length; i++) {
                for (int j = 0; j < c[0].length; j++) {
                    for (int k = 0; k < b.length; k++) {
                        c[i][j] += a[i][k] * b[k][j];
                    }
                }
            }

            // Printing the result matrix
            System.out.println("Resultant Matrix:");
            for (int i = 0; i < c.length; i++) {
                for (int j = 0; j < c[0].length; j++) {
                    System.out.print(c[i][j] + " ");
                }
                System.out.println(); // Move to the next line for the next row
            }
        }
    }
}
