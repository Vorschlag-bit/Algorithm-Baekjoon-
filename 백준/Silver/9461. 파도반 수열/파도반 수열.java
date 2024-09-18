import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for(int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            long[] dp = new long[200];
            if(n == 1) {
                sb.append(1).append("\n");
                continue;
            }
            if(n == 2) {
                sb.append(1).append("\n");
                continue;
            }
            dp[0] = 0;
            dp[1] = 1;
            dp[2] = 1;
            for(int j = 3; j <= n; j++) {
                dp[j] = dp[j - 3] + dp[j - 2];
            }
            sb.append(dp[n]).append("\n");
        }
        System.out.println(sb);
    }
}
