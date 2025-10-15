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

    // Modified encrypt to RETURN the ciphertext instead of just printing
    String encrypt(String ms) {
        pt = new int[3][3];
        ct = new char[3][3];
        int k = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                pt[j][i] = ms.charAt(k++) - 'a';
            }
        }
        StringBuilder cipherText = new StringBuilder();
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int z = 0; z < 3; z++) {
                    ct[i][j] += ((key[i][z] * pt[z][j]));
                }
            }
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                cipherText.append((char) (ct[j][i] % 26 + 'a'));
            }
        }
        return cipherText.toString();
    }

    void decrypt(String ms) {
        int[][] ik = inverseKey(key);

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

        System.out.print("Decrypted: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print((char) (p[j][i] + 'a'));
            }
        }
    }

    // === Matrix functions remain unchanged ===

    int determinant(int[][] mat) { ... } // Keep same
    int detInv(int a, int b) { ... }
    int[][] adjoint(int mat[][]) { ... }
    int[][] inverseKey(int[][] matrix) { ... }
}

public class main {
    public static void main(String args[]) {
        HillCipher c = new HillCipher();
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the message\n");
        String msg = s.nextLine();

        String enc = c.encrypt(msg);
        System.out.println("Encrypted: " + enc);

        c.decrypt(enc); // ✅ Now decrypting the real encrypted text
    }
}