import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[5001];
        Arrays.fill(dp, -1);

        dp[3] = 1;
        dp[5] = 1;

        for (int i = 6; i < n + 1; i++) {
            if(dp[i - 3] != -1) dp[i] = dp[i - 3] + 1;
            if(dp[i - 5] != -1) dp[i] = dp[i - 5] + 1;
        }
        System.out.println(dp[n]);
    }
}