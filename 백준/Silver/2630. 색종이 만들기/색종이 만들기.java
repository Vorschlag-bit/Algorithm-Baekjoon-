import java.io.*;
import java.util.*;

class Main {
    static int[][] arr;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new int[n + 1][n + 1];

        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(whitecheck(1, 1, n));
        System.out.println(bluecheck(1, 1, n));
    }
    private static int bluecheck(int col, int row, int n) {
        if(n==1) return arr[col][row];
        int cnt = 0;
        for (int i = col; i < col + n; i++) {
            for (int j = row; j < row + n; j++) {
                if(arr[i][j] == 1) cnt++;
            }
        }

        if(cnt == n * n) return 1;
        if(cnt == 0) return 0;

        return  bluecheck(col, row, n/2) +
                bluecheck(col + n/2, row, n/2) +
                bluecheck(col, row + n/2, n/2) +
                bluecheck(col + n/2, row + n/2, n/2);
    }
    private static int whitecheck(int col, int row, int n) {
        if(n==1 && arr[col][row] == 0) return 1;
        int cnt = 0;
        for (int i = col; i < col + n; i++) {
            for (int j = row; j < row + n; j++) {
                if(arr[i][j] == 0) cnt++;
            }
        }

        if(cnt == n * n) return 1;
        if(cnt == 0) return 0;

        return  whitecheck(col, row, n/2) +
                whitecheck(col + n/2, row, n/2) +
                whitecheck(col, row + n/2, n/2) +
                whitecheck(col + n/2, row + n/2, n/2);
    }
}