import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        String[] arr = new String[n];
        
        for(int i = 0; i < n; i++)
            arr[i] = br.readLine();
        
        int ans = 1000; //대충 많은 수로 설정
        for(int i = 0; i <= n - 8; i++) {
            for(int j = 0; j <= m - 8; j++) {
                int c = Check(arr, i , j);
                ans = Math.min(ans, c);
            }
        }
        System.out.println(ans);
    }
    public static int Check(String[] arr, int row, int col) {
        //체스판은 흑색으로 시작하거나 백색으로 시작함
        //우선, 흑색으로 시작하는 걸 기준으로 최소 개수를 구해보기
        String[] Chess = {"BWBWBWBW", "WBWBWBWB"};
        
        int cnt = 0;
        for(int i = 0; i < 8; i++) {
            for(int j = 0; j < 8; j++){
                if(arr[row + i].charAt(col + j) != Chess[i % 2].charAt(j))
                    cnt++;
            }
        }
        return Math.min(cnt, 64 - cnt);
    }
}