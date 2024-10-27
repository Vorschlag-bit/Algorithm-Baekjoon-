import java.io.*;
import java.util.*;

class Main{
    static List<Node>[] list;
    static int dist[];
    static int v1;
    static int v2;
    static int max = Integer.MAX_VALUE;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        list = new List[n + 1];
        dist = new int[n + 1];

        for(int i = 1; i <= n; i++)
            list[i] = new ArrayList<>();

        for(int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int current = Integer.parseInt(st.nextToken());
            int next = Integer.parseInt(st.nextToken());
            int dis = Integer.parseInt(st.nextToken());

            list[current].add(new Node(next, dis));
            list[next].add(new Node(current, dis));
        }

        st = new StringTokenizer(br.readLine());
        v1 = Integer.parseInt(st.nextToken());
        v2 = Integer.parseInt(st.nextToken());

        int ans = -1;
        // case 1
        int d1 = dijkstra(1, v1);
        if(d1 != max) {
            int d2 = dijkstra(v1, v2);
            if(d2 != max) {
                int d3 = dijkstra(v2, n);
                if(d3 != max) {
                    ans = d1 + d2 + d3;
                }
            }
        }
        // case 2
        d1 = dijkstra(1, v2);
        if(d1 != max) {
            int d2 = dijkstra(v2, v1);
            if(d2 != max) {
                int d3 = dijkstra(v1, n);
                if(d3 != max) {
                    // case1에서도 정상 경로라면
                    ans = (ans == -1) ? d1 + d2 + d2 : Math.min(ans, (d1 + d2 + d3));
                }
            }
        }
        System.out.println(ans);
    }

    private static int dijkstra(int start, int end) {
        Arrays.fill(dist, max);
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.dis - b.dis);
        dist[start] = 0;

        pq.offer(new Node(start, 0));

        while(!pq.isEmpty()){
            Node current = pq.poll();
            int idx = current.idx;
            int dis = current.dis;

            if(dis > dist[idx]) continue;

            for(Node next : list[idx]) {
                int cost = next.dis + dist[idx]; // 다음 노드까지 최소 비용

                if(cost < dist[next.idx]) {
                    dist[next.idx] = cost;
                    pq.offer(new Node(next.idx, cost));
                }
            }
        }
        return dist[end];
    }
}

class Node{
    public int idx;
    public int dis;

    public Node(int idx, int dis) {
        this.idx = idx;
        this.dis = dis;
    }
}