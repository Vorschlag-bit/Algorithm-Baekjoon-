import java.util.*;
import java.io.*;
public class Main {
    static int[][] dp = new int[30][30];
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        //문제는 m에서 n개를 뽑기만 하면 알아서 선이 연결된다고 생각하면 된다
        //또한 조합은 중복을 고려하지 않으므로 서쪽(1,2,3) 동쪽(1,2,3,4,5)가 있을 경우
        //동쪽에서 3개를 뽑는 (1,2,3)이나 (3,2,1)이나 (2,1,3) 모두 하나의 경우의 수가 된다
        for(int i = 1; i <= T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int ans = CB(M, N);
            System.out.println(ans);
        }
    }
    private static int CB(int M, int N) {
        //이전에 탐색한 조합이라면 그대로 출력
        if(dp[M][N] > 0) return dp[M][N];

        if(M == N || N == 0) return dp[M][N] = 1;

        //점화식은 파스칼의 법칙을 이용하자
        return dp[M][N] = CB(M - 1, N - 1) + CB(M - 1, N);
    }
}