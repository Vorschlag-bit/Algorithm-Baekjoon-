import java.io.*;
import java.util.*;

class Main {
    static int[][] map;
    static boolean[] visit;
    static int ans = 0;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        map = new int[n + 1][n + 1];
        visit = new boolean[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());

            map[n1][n2] = 1;
            map[n2][n1] = 1;
        }
        for (int i = 1; i <= n; i++) {
            if(!visit[i]) {
                bfs(i);
                ans++;
        }
        }
        System.out.println(ans);
    }

    private static void bfs(int i) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(i);
        visit[i] = true;
        while (!q.isEmpty()) {
            int num = q.poll();
            for (int k = 1; k <= n; k++) {
                if (map[num][k] == 1 && !visit[k]) {
                    visit[k] = true;
                    q.offer(k);
                }
            }
        }
    }
}