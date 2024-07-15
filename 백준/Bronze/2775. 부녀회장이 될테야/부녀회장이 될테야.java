import java.util.*;
import java.io.*;

class Main{
    public static void main (String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        int t = Integer.parseInt(br.readLine());
        int[][] dp = new int[15][15];

        // 0층 채우기
        for (int i = 0; i < 15; i++) {
            dp[0][i] = i;
        }

        for (int i = 1; i < 15; i++) {
            for(int j = 1; j < 15; j++) {
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
            }
        }

        for (int i = 0; i < t; i++) {
            int floor = Integer.parseInt(br.readLine());
            int num = Integer.parseInt(br.readLine());
            sb.append(dp[floor][num]).append("\n");
        }
        System.out.println(sb);
    }
}

