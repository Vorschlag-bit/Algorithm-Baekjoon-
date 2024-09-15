import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        for(int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            Queue<Integer> q = new LinkedList<>();
            boolean[] visit = new boolean[10000];
            String[] path = new String[10000];

            q.offer(a);
            visit[a] = true;
            Arrays.fill(path, "");

            while(!q.isEmpty() && !visit[b]) {
                int n = q.poll();

                int D = (n * 2) % 10000;
                int S = n == 0 ? 9999 : n - 1;
                int L = (n % 1000) * 10 + n / 1000;
                int R = (n % 10) * 1000 + n / 10;

                if(!visit[D]) {
                    q.offer(D);
                    visit[D] = true;
                    path[D] = path[n] + "D";
                }
                if(!visit[S]) {
                    q.offer(S);
                    visit[S] = true;
                    path[S] = path[n] + "S";
                }
                if(!visit[L]) {
                    q.offer(L);
                    visit[L] = true;
                    path[L] = path[n] + "L";
                }
                if(!visit[R]) {
                    q.offer(R);
                    visit[R] = true;
                    path[R] = path[n] + "R";
                }
            }
            sb.append(path[b]).append("\n");
        }
        System.out.println(sb);
    }
}