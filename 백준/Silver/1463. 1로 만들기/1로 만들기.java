import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[n + 1];
        if(n == 1) {
            System.out.println(0);
            System.exit(0);
        }
        else if(n == 2) {
            System.out.println(1);
            System.exit(0);
        }
        dp[1] = 0;
        dp[2] = 1;
        dp[3] = 1;

        for (int i = 4; i <= n; i++) {
            dp[i] = dp[i - 1] + 1;
            if(i % 3 == 0) dp[i] = Math.min(dp[i], dp[i / 3] + 1);
            if(i % 2 == 0) dp[i] = Math.min(dp[i], dp[i / 2] + 1);
        }
        System.out.println(dp[n]);
    }
}