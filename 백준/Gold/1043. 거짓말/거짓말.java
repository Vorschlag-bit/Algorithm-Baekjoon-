import java.io.*;
import java.util.*;

class Main {
    static int[][] map;
    static int n; // 사람 수
    static int m; // 파티 수
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static Set<Integer> truth = new HashSet<>();
    static List<Set<Integer>> party = new ArrayList<>();
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n + 1][n + 1];
        st = new StringTokenizer(br.readLine());
        int ans = m;
        if(Integer.parseInt(st.nextToken()) == 0) {
            System.out.println(ans);
            System.exit(0);
        }
        else {
            while(st.hasMoreTokens()) {
                truth.add(Integer.parseInt(st.nextToken()));
            }
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            TreeMap<Integer, Integer> tm = new TreeMap<>();
            Set<Integer> set = new HashSet<>();
            while(st.hasMoreTokens()) {
                int p = Integer.parseInt(st.nextToken());
                tm.put(p, 0);
                set.add(p);
            }
            party.add(set);
            for(int key : tm.keySet()) {
                map[key][tm.higherKey(key) == null ? 0 : tm.higherKey(key)] = 1;
                map[tm.higherKey(key) == null ? 0 : tm.higherKey(key)][key] = 1;
            }
        }
        for(Set<Integer> s : party) {
            for(int p : s) {
                if(truth.contains(p)) {
                    bfs(p);
                }
            }
        }
        for(Set<Integer> s : party) {
            for(int p : s) {
                if(truth.contains(p)) {
                    ans--;
                    break;
                }
            }
        }
        System.out.println(ans);
    }

    private static void bfs(int t) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(t);
        while(!q.isEmpty()) {
            int num = q.poll();
            for(int i = 1; i <= n; i++) {
                if(map[num][i] == 1) {
                    q.offer(i);
                    truth.add(i);
                    map[num][i] = 2;
                    map[i][num] = 2;
                }
            }
        }
    }
}