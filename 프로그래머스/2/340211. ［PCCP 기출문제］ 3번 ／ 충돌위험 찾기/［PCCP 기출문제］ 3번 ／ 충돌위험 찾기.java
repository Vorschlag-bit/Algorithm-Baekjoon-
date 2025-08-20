import java.util.*;

class Solution {
    class Robot {
        int x;
        int y;
        List<int[]> path = new ArrayList<>();
        boolean goal = false;

        public Robot(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public int solution(int[][] points, int[][] routes) {
        int ans = 0;
        List<Robot> robots = new ArrayList<>();
        int[][] dir = {{1,0},{-1,0},{0,1},{0,-1}};

        // robots 초기화
        for (int i = 0; i < routes.length; i++) {
            int x = points[routes[i][0] - 1][0] - 1;
            int y = points[routes[i][0] - 1][1] - 1;

            Robot r = new Robot(x, y);
            for (int j = 1; j < routes[i].length; j++) {
                int nx = points[routes[i][j] - 1][0] - 1;
                int ny = points[routes[i][j] - 1][1] - 1;
                r.path.add(new int[]{nx, ny});
            }
            robots.add(r);
        }

        // 출발 전 충돌 감지
        Map<List<Integer>, Integer> visit = new HashMap<>();
        for (Robot r : robots) {
            List<Integer> key = Arrays.asList(r.x, r.y);
            visit.put(key, visit.getOrDefault(key, 0) + 1);
        }
        for (int v : visit.values()) {
            if (v > 1) ans += 1;
        }

        // 시뮬레이션
        while (true) {
            boolean flag = true;
            for (Robot r : robots) {
                if (!r.goal) { flag = false; break; }
            }
            if (flag) break;

            List<Robot> moved = new ArrayList<>();

            // 한 칸씩 이동
            for (Robot r : robots) {
                if (r.goal) continue;
                int tx = r.path.get(0)[0];
                int ty = r.path.get(0)[1];
                int curDist = Math.abs(tx - r.x) + Math.abs(ty - r.y);

                for (int[] d : dir) {
                    int nx = r.x + d[0];
                    int ny = r.y + d[1];
                    int nxtDist = Math.abs(tx - nx) + Math.abs(ty - ny);
                    if (0 <= nx && 0 <= ny && nxtDist < curDist) {
                        r.x = nx;
                        r.y = ny;
                        moved.add(r);
                        break;
                    }
                }
            }

            // 이동한 로봇들의 충돌/도착 처리
            Map<List<Integer>, Integer> v = new HashMap<>();
            for (Robot r : moved) {
                List<Integer> key = Arrays.asList(r.x, r.y);
                v.put(key, v.getOrDefault(key, 0) + 1);

                int tx = r.path.get(0)[0];
                int ty = r.path.get(0)[1];

                if (tx == r.x && ty == r.y) {
                    r.path.remove(0);        // 다음 목적지로
                    if (r.path.isEmpty()) {  // 더 이상 목적지 없으면 완료
                        r.goal = true;
                    }
                }
            }

            // 충돌 집계
            for (int va : v.values()) {
                if (va > 1) ans += 1;
            }
        }

        return ans;
    }
}