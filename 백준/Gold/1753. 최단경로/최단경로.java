import java.io.*;
import java.util.*;

class Main{
    static List<Node>[] list;
    static int max = Integer.MAX_VALUE;
    static int[] distance;
    static PriorityQueue<Node> pq;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        list = new List[v + 1];
        distance = new int[v + 1];

        for(int i = 1; i <= v; i++)
            list[i] = new ArrayList<>();

        int start = Integer.parseInt(br.readLine());

        for(int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());

            int num = Integer.parseInt(st.nextToken());
            int node = Integer.parseInt(st.nextToken());
            int dis = Integer.parseInt(st.nextToken());

            list[num].add(new Node(node, dis));
        }

        StringBuilder sb = new StringBuilder();
        distance = dijkstra(start, v);
        for(int i = 1; i <= v; i++) {
            int dis = distance[i];
            sb.append(dis != max ? dis : "INF").append("\n");
        }
        System.out.println(sb);
    }

    private static int[] dijkstra(int start, int end) {
        pq = new PriorityQueue<>((a, b) -> a.dis - b.dis);
        Arrays.fill(distance, max);

        distance[start] = 0;
        pq.offer(new Node(start, 0));

        while(!pq.isEmpty()) {
            Node current = pq.poll();
            int idx = current.idx;
            int dis = current.dis;

            if(distance[idx] < dis) continue;

            for(Node next : list[idx]) {
                int cost = distance[idx] + next.dis;

                if(cost < distance[next.idx]) {
                    distance[next.idx] = cost;
                    pq.offer(new Node(next.idx, cost));
                }
            }
        }
        return distance;
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