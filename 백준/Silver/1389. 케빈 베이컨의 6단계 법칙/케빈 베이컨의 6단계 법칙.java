import java.util.*;
import java.io.*;

class Main{
    static boolean[] visit;
    static int[] dis;
    static int ans = Integer.MAX_VALUE;
    static Queue<Integer> q = new LinkedList<>();
    static int [][] arr;
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        arr = new int[n + 1][n + 1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = 1;
            arr[b][a] = 1;
        }
        int person = 0;
        for (int i = 1; i <= n; i++) {
            visit = new boolean[n + 1];
            dis = new int[n + 1];
            int sum = 0;
            bfs(i);
            for (int j = 1; j <= n; j++) {
                sum += dis[j];
            }
            if(ans > sum) {
                ans = sum;
                person = i;
            }
        }
        System.out.println(person);
    }

    private static void bfs(int i) {
        q.offer(i);
        visit[i] = true;

        while(!q.isEmpty()) {
            int num = q.poll();
            for (int j = 1; j <= n; j++) {
                if(arr[num][j] == 1 && !visit[j]) {
                    q.offer(j);
                    visit[j] = true;
                    dis[j] = dis[num] + 1;
                }
            }
        }
    }
}