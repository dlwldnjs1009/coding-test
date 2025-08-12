import java.io.*;

public class Main {
    static final char[] P = {'A','B','C','D'};
    static BufferedWriter w;

    public static void main(String[] args) throws Exception {
        BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
        w = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(r.readLine().trim());

        long[] dp = new long[Math.max(3, n + 1)];
        dp[0] = 0; dp[1] = 1; dp[2] = 3;
        for (int i = 3; i <= n; i++) dp[i] = dp[i - 2] + ((1L << (i - 2)) - 1) + 3;

        w.write(Long.toString(dp[n]));
        w.newLine();

        solve(n);
        w.flush();
    }

    static void solve(int n) throws IOException {
        int s = 0;
        while (n >= 2) {
            move3(n - 2, s, 2 - s);
            out(s, 1);
            out(s, 3);
            out(1, 3);
            n -= 2;
            s = 2 - s;
        }
        if (n == 1) out(s, 3);
    }

    static void move3(int k, int s, int e) throws IOException {
        if (k <= 0) return;
        int a = 3 - s - e;
        move3(k - 1, s, a);
        out(s, e);
        move3(k - 1, a, e);
    }

    static void out(int x, int y) throws IOException {
        w.write(P[x]); w.write(' '); w.write(P[y]); w.newLine();
    }
}
