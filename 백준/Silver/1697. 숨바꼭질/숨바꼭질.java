import java.io.*;
import java.util.*;

class Main{
    static int n;
    static int m;
    static int[] arr = new int[100001];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        Arrays.fill(arr, - 1);
        arr[n] = 0;
        bfs(n);

        System.out.println(arr[m]);
    }

    private static void bfs(int n) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(n);

        while(!q.isEmpty()) {
            int num = q.poll();
            if(num == m) break;
            int d1 = num * 2;
            int d2 = num - 1;
            int d3 = num + 1;

            if(d2 >= 0 && arr[d2] == -1) {
                arr[d2] = arr[num] + 1; q.offer(d2);
            }
            if(d3 <= 100000 && arr[d3] == -1) {
                arr[d3] = arr[num] + 1; q.offer(d3);
            }
            if(d1 <= 100000 && arr[d1] == -1) {
              arr[d1] = arr[num] + 1; q.offer(d1);
            }
        }
    }
}