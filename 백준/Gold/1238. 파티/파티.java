import java.io.*;
import java.util.*;

class Main{
    static List<Node> list[];
    static int minT1;
    static int minT2;
    static int dist[];
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        list = new List[n + 1];
        dist = new int[n + 1];

        for(int i = 1; i <= n; i++)
            list[i] = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            int next = Integer.parseInt(st.nextToken());
            int dis = Integer.parseInt(st.nextToken());

            list[num].add(new Node(next, dis));
        }
        
        int ans = 0;
        
        for(int i = 1; i <= n; i++) {
            minT1 = dijkstra(i, x);
            minT2 = dijkstra(x, i);
            ans = Math.max(ans, minT1 + minT2);
        }
        System.out.println(ans);
    }

    private static int dijkstra(int start, int end) {
        Arrays.fill(dist, Integer.MAX_VALUE);
        PriorityQueue<Node> pq = new PriorityQueue<>((d1, d2) -> d1.dis - d2.dis);
        dist[start] = 0;
        pq.offer(new Node(start, 0));

        while(!pq.isEmpty()) {
            Node current = pq.poll();
            int idx = current.next;
            int distance = current.dis;

            if(distance > dist[idx]) continue; // 현재 최소 거리보다 누적 거리가 길다면 스킵

            for(Node next : list[idx]) {
                int cost = dist[idx] + next.dis;

                if(cost < dist[next.next]) {
                    dist[next.next] = cost;
                    pq.offer(new Node(next.next, cost));
                }
            }
        }
        return dist[end];
    }
}

class Node {
    public int next;
    public int dis;

    public Node(int next, int dis) {
        this.next = next;
        this.dis = dis;
    }
}