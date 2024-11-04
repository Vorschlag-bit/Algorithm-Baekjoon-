import java.util.*;
class Solution {
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static char[][] map;
    public List<Integer> solution(String[][] places) {
        List<Integer> list = new ArrayList<>();
        
        for(String[] arr : places) {
            map = new char[5][5];
            int cnt = 0;
            for(String str : arr) {
                for(int i = 0; i < str.length(); i++) {
                    map[cnt][i] = str.charAt(i);
                }
                cnt++;
            }
            boolean check = true;
            for(int i = 0; i < 5 && check; i++) {
                for(int j = 0; j < 5 && check; j++) {
                    if(map[i][j] == 'P') {
                        check = bfs(i, j);
                    }
                }
            }
            list.add(check ? 1 : 0);
        }
        return list;
    }
    public boolean bfs(int x, int y) {
        
        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(!Check(nx, ny)) continue;
            
            // 거리 1에 대한 검사
            if(map[nx][ny] == 'P') return false;
            
            // 거리 1에 'X'가 있을 경우, 그 너머에 대한 bfs를 실행할 필요 없다.
            // P O
            // X P 같은 경우 O에서 검증
            if(map[nx][ny] == 'X') continue;
            
            for(int j = 0; j < 4; j++) {
                int nx2 = nx + dx[j];
                int ny2 = ny + dy[j];
                
                // 유효성 검사 및 bfs 시작점 아닌지 판단
                if(!Check(nx2, ny2) || nx2 == x && ny2 == y) continue;
                
                if(map[nx2][ny2] == 'P') {
                    // case 1: x, y로부터 상하좌우로 맨하튼 거리 2인데 사이에 파티션이 없음
                    if(Math.abs(nx2 - x) + Math.abs(ny2 - y) == 2 &&
                       map[nx][ny] != 'X') return false;
                    // case 2: x, y로부터 대각선
                    if(Math.abs(nx2 - x) == 1 && Math.abs(ny2 - y) == 1) {
                        if(map[x][ny2] != 'X' || map[nx2][y] != 'X')
                            return false;
                    }
                }
            }
        }
        return true;
    }
    public boolean Check(int x, int y) {
        return 0 <= x && x < 5 && 0 <= y && y < 5;
    }
}