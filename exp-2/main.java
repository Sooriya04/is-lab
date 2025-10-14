import java.util.*;
import java.math.*;

class HillCipher {
    char[][] ct;
    static int[][] pt;
    static int[][] key = {
            { 17, 17, 5 },
            { 21, 18, 21 },
            { 2, 2, 19 }
    };

    void encrypt(String ms) {
        pt = new int[3][3];
        ct = new char[3][3];
        int k = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                pt[j][i] = ms.charAt(k++) - 'a';
            }
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int z = 0; z < 3; z++) {
                    ct[i][j] += ((key[i][z] * pt[z][j]));
                }

            }

        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print((char) (ct[j][i] % 26 + 'a') + " ");
            }
        }

    }

    void decrypt(String ms) {
        int[][] ik = new int[3][3];
        ik = inverseKey(key);

        System.out.println();
        int p[][] = new int[3][3];
        int k = 0;

        int mj[][] = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                mj[j][i] = ms.charAt(k++) - 'a';
            }
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                p[i][j] = 0;
                for (int z = 0; z < 3; z++) {
                    p[i][j] += ((ik[i][z] * mj[z][j]));
                }
                p[i][j] = (p[i][j] % 26 + 26) % 26;
            }
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print((char) (p[j][i] + 'a'));
            }
        }

    }

    int determinant(int[][] mat) {
        int x = (mat[0][0] * ((mat[1][1] * mat[2][2]) - (mat[2][1] * mat[1][2])))
                - (mat[0][1] * ((mat[1][0] * mat[2][2]) - (mat[2][0] * mat[1][2])))
                + (mat[0][2] * ((mat[1][0] * mat[2][1]) - (mat[2][0] * mat[1][1])));
        return (x % 26 + 26) % 26;

    }

    int detInv(int a, int b) {
        BigInteger az = BigInteger.valueOf(a);
        BigInteger bz = BigInteger.valueOf(b);
        return (az.modInverse(bz)).intValue();
    }

    int[][] adjoint(int mat[][]) {
        int res[][] = new int[3][3];
        res[0][0] = (mat[1][1] * mat[2][2]) - (mat[2][1] * mat[1][2]);
        res[0][1] = -((mat[1][0] * mat[2][2]) - (mat[2][0] * mat[1][2]));
        res[0][2] = (mat[1][0] * mat[2][1]) - (mat[2][0] * mat[1][1]);

        res[1][0] = -((mat[0][1] * mat[2][2]) - (mat[0][2] * mat[2][1]));
        res[1][1] = (mat[0][0] * mat[2][2]) - (mat[2][0] * mat[0][2]);
        res[1][2] = -((mat[0][0] * mat[2][1]) - (mat[2][0] * mat[0][1]));

        res[2][0] = (mat[0][1] * mat[1][2]) - (mat[1][1] * mat[0][2]);
        res[2][1] = -((mat[0][0] * mat[1][2]) - (mat[1][0] * mat[0][2]));
        res[2][2] = (mat[0][0] * mat[1][1]) - (mat[1][0] * mat[0][1]);

        int resT[][] = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                resT[i][j] = (res[j][i] % 26 + 26) % 26;
            }
        }
        return resT;
    }

    int[][] inverseKey(int[][] matrix) {
        int det = determinant(matrix);
        int detInverse = detInv(det, 26);
        int[][] adj = adjoint(matrix);
        int[][] kInverse = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                kInverse[i][j] = (detInverse * adj[i][j]) % 26;
            }
        }
        return kInverse;
    }
}

public class main {
    public static void main(String args[]) {
        HillCipher c = new HillCipher();
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the message\n");
        String msg = s.nextLine();
        c.encrypt(msg);
        c.decrypt("nlitjvrnd");
    }
}