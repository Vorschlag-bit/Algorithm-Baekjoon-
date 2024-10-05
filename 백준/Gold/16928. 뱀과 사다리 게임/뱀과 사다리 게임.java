import java.io.*;
import java.util.*;

class Main{
    static int n;
    static int m;
    static int ans = 0;
    static int[]map = new int[101];
    static int[] Check = new int[101];;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= 100; i++) {
            map[i] = i;
        }

        // 사다리 map 등록
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int in = Integer.parseInt(st.nextToken());
            int out = Integer.parseInt(st.nextToken());
            map[in] = out;
        }

        // 뱀 map 등록
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int in = Integer.parseInt(st.nextToken());
            int out = Integer.parseInt(st.nextToken());
            map[in] = out;
        }
        bfs(1);
        System.out.println(ans);
    }

    private static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();

        q.offer(start);

        while(!q.isEmpty()) {
            int num = q.poll();
            if(num == 100) {
                ans = Check[100];
                break;
            }

            for (int i = 1; i <= 6; i++) {
                if(num + i < 101 && Check[map[num + i]] == 0) {
                    q.offer(map[num + i]);
                    Check[map[num + i]] = Check[map[num]] + 1;
                }
            }
        }
    }
}