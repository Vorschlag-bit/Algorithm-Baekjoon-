import java.io.*;
import java.util.*;

class Main {
    static int n;
    static int m;
    static int[] arr = new int[100001];
    static int[] visit = new int[100001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        Arrays.fill(arr, Integer.MAX_VALUE);
        arr[n] = 0;
        visit[n] = 1;  // 시작점의 방문 횟수를 1로 설정
        bfs(n);

        System.out.println(arr[m]);
        System.out.println(visit[m]);
    }

    private static void bfs(int n) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(n);

        while (!q.isEmpty()) {
            int now = q.poll();

            for (int next : new int[]{now - 1, now + 1, now * 2}) {
                if (Rangecheck(next)) {
                    if (arr[next] > arr[now] + 1) {
                        arr[next] = arr[now] + 1;
                        visit[next] = visit[now];  // 방문 횟수를 현재 위치의 방문 횟수로 설정
                        q.offer(next);
                    }
                    else if(arr[next] == arr[now] + 1) {
                        visit[next] += visit[now];  // 방문 횟수를 현재 위치의 방문 횟수만큼 증가
                    }
                }
            }
        }
    }

    private static boolean Rangecheck(int number) {
        return 0 <= number && number < 100001;
    }
}