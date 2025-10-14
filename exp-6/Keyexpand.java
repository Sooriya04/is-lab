import java.util.Scanner;

public class Keyexpand {
    private static final int[] Rcon = {
            0x00, 0x01, 0x02, 0x04, 0x08,
            0x10, 0x20, 0x40, 0x80, 0x1B, 0x36
    };

    private static int[] rotword(int[] word) {
        return new int[] { word[1], word[2], word[3], word[0] };
    }

    private static int[] subword(int[] word) {
        int[] sub = new int[4];
        for (int i = 0; i < 4; i++) {
            sub[i] = sbox[word[i]];
        }
        return sub;
    }

    public static int[] keyexp(int[] key) {
        int[] R = new int[44 * 4];
        System.arraycopy(key, 0, R, 0, 16);
        int[] temp = new int[4];

        for (int i = 4; i < 44; i++) {
            for (int j = 0; j < 4; j++) {
                temp[j] = R[(i - 1) * 4 + j];
            }
            if (i % 4 == 0) {
                temp = rotword(temp);
                temp = subword(temp);
                temp[0] ^= Rcon[i / 4];
            }
            for (int j = 0; j < 4; j++) {
                R[i * 4 + j] = R[(i - 4) * 4 + j] ^ temp[j];
            }
        }
        return R;
    }

    public static void main(String[] s) {
        Scanner sc = new Scanner(System.in);
        int[] key = new int[16];
        System.out.println("Enter 16 key bytes in hex (one by one):");
        for (int i = 0; i < 16; i++) {
            System.out.printf("Byte %d: ", i);
            key[i] = Integer.parseInt(sc.next(), 16);
        }

        int[] expanded = keyexp(key);
        System.out.println("\nExpanded Keys:");
        for (int round = 0; round <= 10; round++) {
            System.out.printf("Round %d Key: ", round);
            for (int j = 0; j < 4; j++) {
                int base = (round * 4 + j) * 4;
                System.out.printf("%02x %02x %02x %02x ",
                        expanded[base], expanded[base + 1],
                        expanded[base + 2], expanded[base + 3]);
            }
            System.out.println();
        }
        sc.close();
    }
}