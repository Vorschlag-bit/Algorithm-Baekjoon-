import java.io.*;
import java.util.*;

class Main{
    static int time = Integer.MAX_VALUE;
    static int h = 0;
    static int n;
    static int m;
    static int[][] map;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        int min = Integer.MAX_VALUE;
        int max = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if(max < map[i][j]) max = map[i][j];
                if(min > map[i][j]) min = map[i][j];
            }
        }

        for(int i = min; i <= max; i++) {
            int tree = b;
            int t = 0;
            for (int x = 0; x < n; x++) {
                for (int y = 0; y < m; y++) {
                    int height = map[x][y];
                    // map이 목표 나무보다 길 경우
                    if(height > i) {
                        tree += (height - i);
                        t += ((height - i) * 2);
                    }
                    // map이 목표 나무보다 짧은 경우
                    else {
                        tree -= (i - height);
                        t += (i - height);
                    }
                }
            }
            // 목재가 부족한 경우, 이 이상의 높이는 볼 필요 없음
            if(tree < 0) break;
            if(t <= time) {
                time = t;
                h = i;
            }
        }
        System.out.println(time + " " + h);
    }
}