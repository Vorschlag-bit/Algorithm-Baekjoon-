import java.io.*;
import java.util.*;

class Main{
    static List<Node>[] list;
    static int[] distance;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        list = new List[n + 1];
        distance = new int[n + 1];

        for(int i = 1; i <= n; i++)
            list[i] = new ArrayList<>();

        for(int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());

            list[s].add(new Node(e, t));
        }
        StringTokenizer st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        int ans = dijkstra(start, end);
        System.out.println(ans);
    }

    private static int dijkstra(int start, int end) {
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.cost - b.cost);
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[start] = 0;
        pq.offer(new Node(start, 0));

        while(!pq.isEmpty()) {
            Node current = pq.poll();
            int idx = current.idx;
            int cost = current.cost;

            if(distance[idx] < cost) continue;

            for(Node next : list[idx]) {
                int nextIdx = next.idx;
                int nextCost = next.cost;
                int total = distance[idx] + nextCost;

                if(total < distance[nextIdx]) {
                    distance[nextIdx] = total;
                    pq.offer(new Node(nextIdx, total));
                }
            }
        }
        return distance[end];
    }
}

class Node{
    public int idx;
    public int cost;

    public Node(int idx, int cost) {
        this.idx = idx;
        this.cost = cost;
    }
}