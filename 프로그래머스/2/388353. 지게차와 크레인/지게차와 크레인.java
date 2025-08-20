import java.util.*;

class Solution {
    static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    static final char EMPTY = '.';
    static int n, m;

    public int solution(String[] storage, String[] req) {
        int ans = 0;
        n = storage.length;
        m = storage[0].length();

        char[][] arr = new char[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = storage[i].charAt(j);
            }
        }

        // 요청 처리
        for (String r : req) {
            if (r.length() == 1) {
                // 외부와 접촉 가능한 경로(EMPTY 또는 target)만 따라가며 target 제거
                char target = r.charAt(0);
                // 비교할 map(깊은 복사)
                char[][] map = new char[n][m];
                for (int i = 0; i < n; i++) map[i] = arr[i].clone();
                // 지점 판단
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < m; j++) {
                        if (arr[i][j] == target) {
                            if (bfs(i,j,target,arr,map)) arr[i][j] = EMPTY;
                        }
                    }
                }

            } else {
                // 해당 문자를 전부 제거
                char target = r.charAt(0);
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < m; j++) {
                        if (arr[i][j] == target) {
                            arr[i][j] = EMPTY;
                        }
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] != EMPTY) ans++;
            }
        }
        return ans;
    }

    static boolean bfs(int x, int y, char target, char[][] arr, char[][] map) {
        Deque<int[]> q = new ArrayDeque<>();
        boolean[][] visit = new boolean[n][m];
        q.add(new int[]{x,y});
        visit[x][y] = true;
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int cx = cur[0];
            int cy = cur[1];
            for (int[] d : dir) {
                int nx = cx + d[0];
                int ny = cy + d[1];
                if (!check(nx,ny)) return true;
                if (!visit[nx][ny] && map[nx][ny] == EMPTY) {
                    visit[nx][ny] = true;
                    q.add(new int[] {nx,ny});
                }
            }
        }
        return false;
    }
    
    public static boolean check(int x,int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }
}