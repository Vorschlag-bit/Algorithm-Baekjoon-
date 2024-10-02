import java.io.*;

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[]dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        if(n == 1) {
            System.out.println(1);
            System.exit(0);
        }
        for (int i = 2; i <= n; i++) {
            dp[i] = (dp[i-2] * 2 + dp[i-1]) % 10007;
        }
        System.out.println(dp[n]);
    }
}