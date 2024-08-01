import java.io.*;
import java.util.*;

class Main{
    static StringBuilder sb = new StringBuilder();
    static boolean[] visit;
    static int[][] map;
    static int n, m, v;
    static Queue<Integer> q = new LinkedList<>();
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        map = new int[n + 1][n + 1];
        visit = new boolean[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            map[a][b] = map[b][a] = 1;
        }

        dfs(v);
        sb.append("\n");
        visit = new boolean[n + 1];
        bfs(v);
        System.out.println(sb);
    }

    private static void bfs(int v) {
        q.offer(v);
        visit[v] = true;
        while(!q.isEmpty()) {
            int num = q.poll();
            sb.append(num+"").append(" ");
            for (int i = 1; i <= n; i++) {
                if(map[num][i] == 1 && !visit[i]) {
                    q.offer(i);
                    visit[i] = true;
                }
            }
        }
    }

    private static void dfs(int v) {
        sb.append(v+"").append(" ");
        visit[v] = true;

        for (int i = 1; i <= n; i++) {
            if(map[v][i] == 1 && !visit[i]) dfs(i);
        }
    }
}