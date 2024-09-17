import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int cnt = 0;
            cnt += bfs(1, n);
            cnt += bfs(2, n);
            cnt += bfs(3, n);
            sb.append(cnt + "\n");
        }
        System.out.println(sb);
    }

    private static int bfs(int i, int n) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(i);
        int cnt = 0;
        while(!q.isEmpty()) {
            int current = q.poll();
            if(current == n) cnt ++;

            if(current + 1 <= n) {
                q.offer(current + 1);
            }
            if(current + 2 <= n) {
                q.offer(current + 2);
            }
            if(current + 3 <= n) {
                q.offer(current + 3);
            }
        }
        return cnt;
    }
}