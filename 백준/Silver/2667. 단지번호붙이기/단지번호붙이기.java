import java.io.*;
import java.util.*;

class Main{
    static int[][] map;
    static boolean[][] visit;
    static int n;
    static int[] dx = new int[] {0, 0, 1, -1};
    static int[] dy = new int[] {1, -1, 0, 0};
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        visit = new boolean[n][n];
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < n; j++) {
                map[i][j] = str.charAt(j) - '0';
            }
        }
        int cnt = 0;
        for(int i  = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(map[i][j] == 1 && !visit[i][j]) {
                    list.add((bfs(i, j)));
                    cnt++;
                }
            }
        }
        Collections.sort(list);
        for (int n : list) sb.append(n).append("\n");
        System.out.println(cnt);
        System.out.println(sb);
    }

    private static int bfs(int c, int r) {
        Queue<int[]> q = new LinkedList<>();
        visit[c][r] = true;
        q.offer(new int[]{c, r});
        int cnt = 1;
        while(!q.isEmpty()){
            int[] arr = q.poll();
            int px = arr[0];
            int py = arr[1];
            for(int i = 0; i < 4; i++) {
                int cx = px + dx[i];
                int cy = py + dy[i];
                if(Check(cx, cy) && !visit[cx][cy] && map[cx][cy] == 1) {
                    visit[cx][cy] = true;
                    cnt++;
                    q.offer(new int[] {cx, cy});
                }
            }
        }
        return cnt;
    }

    private static boolean Check(int cx, int cy) {
        return cx >= 0 && cx < n && cy >= 0 && cy < n;
    }
}