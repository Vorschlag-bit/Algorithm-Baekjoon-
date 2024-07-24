import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int[][] dp = new int[41][2];
            // 0은 0번째에 1개, 1은 1번째에 1개가 들어간다.
            dp[0][0] = 1;
            dp[1][1] = 1;
            int n = Integer.parseInt(br.readLine());
            int cnt1 = 0;
            int cnt0 = 0;
            for (int j = 2; j <= n; j++) {
               dp[j][0] = dp[j-1][0] + dp[j - 2][0];
               dp[j][1] = dp[j-1][1] + dp[j - 2][1];
            }
            StringBuilder sb = new StringBuilder();
            sb.append(dp[n][0] + " ").append(dp[n][1]);
            System.out.println(sb);
        }
    }
}