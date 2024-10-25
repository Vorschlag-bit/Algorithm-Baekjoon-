import java.io.*;
import java.util.*;

class Main{
    static int n;
    static List<Node>[] list;
    static int maxDis = 0;
    static int maxNode = 0;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        list = new List[n + 1];

        for(int i = 1; i <= n; i++) {
            list[i] = new ArrayList<>();
        }

        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());

            while(true) {
                int node = Integer.parseInt(st.nextToken());
                if(node == -1) break;
                int dis = Integer.parseInt(st.nextToken());
                list[num].add(new Node(node, dis));
            }
        }
        bfs(1);
        bfs(maxNode);
        System.out.println(maxDis);
    }

    private static void bfs(int start) {
        Queue<Node> q = new LinkedList<>();
        boolean[] visit = new boolean[n + 1];
        visit[start] = true;
        for(Node node : list[start]) {
            q.offer(node);
            visit[node.next] = true;
        }
        maxDis = 0;

        while(!q.isEmpty()) {
            Node current = q.poll();
            int next = current.next;
            int dis = current.dis;

            if(maxDis < dis) {
                maxDis = dis;
                maxNode = next;
            }
            for(Node node : list[next]) {
                if(!visit[node.next]) {
                    visit[node.next] = true;
                    q.offer(new Node(node.next, dis + node.dis));
                }
            }
        }

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