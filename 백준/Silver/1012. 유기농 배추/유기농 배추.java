import java.io.*;
import java.util.*;

class Main{
    static int M;
    static int N;
    static int K;
    static int[]dx = {0,-1,0,1};
    static int[]dy = {1,0,-1,0};
    static int[][]visited;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            visited = new int [M][N];
            // 배추 입력 받기
            for (int j = 0; j < K; j++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                visited[x][y] = 1;
            }

            int ans = 0;
            for (int j = 0; j < M; j++) {
                for (int k = 0; k < N; k++) {
                    if(visited[j][k] == 1) {
                        bfs(j, k);
                        ans++;
                    }
                }
            }
            sb.append(ans).append("\n");
        }
        System.out.println(sb);
    }

    private static void bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x,y});
        visited[x][y] = 2;

        while(!q.isEmpty()) {
            int[] now = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];

                if(nx >= 0 && nx < M && ny >= 0 && ny < N && visited[nx][ny] == 1) {
                    visited[nx][ny] = 2;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
    }
}