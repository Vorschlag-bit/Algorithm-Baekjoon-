import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int[] arr = new int[n]; // 원 성적 담을 배열
        
        double m = 0;//최대 점수
        for(int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            m = Math.max(arr[i], m);
        }
        
        double ans = 0; //조작된 성적 평균
        for(int i = 0; i < n; i++) {
            double score = (arr[i]/m) * 100;
            ans += score;
        }
        
        System.out.println(ans/n);
    }
}