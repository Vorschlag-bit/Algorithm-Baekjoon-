import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int l;
    public int solution(int[][] board) {
        l = board.length;
        int[][][] cost = new int[l][l][4];
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l; j++) {
                Arrays.fill(cost[i][j], Integer.MAX_VALUE);
            }
        }
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0,0,-1, 0});
        while(!q.isEmpty()) {
            int[] arr = q.poll();
            int cx = arr[0];
            int cy = arr[1];
            if(cx == l - 1 && cy == l - 1) continue;
            int dir = arr[2];
            int currentCost = arr[3];
            for(int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if(!Check(nx, ny) || board[nx][ny] == 1) continue;

                int newCost = currentCost + 100;
                if(dir != i && dir != -1) newCost += 500;
                
                if(cost[nx][ny][i] > newCost) {
                    cost[nx][ny][i] = newCost;
                    q.offer(new int[]{nx,ny,i,newCost});
                }
            }
        }
        int answer = Integer.MAX_VALUE;
        for(int i = 0; i < 4; i++)
            answer = Math.min(answer ,cost[l-1][l-1][i]);
        return answer;
    }
    public static boolean Check(int nx, int ny) {
        return 0 <= nx && nx < l && 0 <= ny && ny < l;
    }
}