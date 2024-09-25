import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        // 구간합을 저장할 배열
        int[] sum = new int[n + 1];
        for(int i = 1; i <= n; i++) sum[i] = sum[i - 1] + arr[i];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            int ans = sum[end] - sum[start - 1];
            sb.append(ans).append("\n");
        }
        System.out.println(sb);
    }
}