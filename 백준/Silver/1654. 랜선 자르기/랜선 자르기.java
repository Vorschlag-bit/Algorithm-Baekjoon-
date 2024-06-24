import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        
        int[] arr = new int[k];
        long start = 1;
        long end = 0;
        
        for(int i = 0; i < k; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            end = Math.max(arr[i], end);
        }
        
        long result = 0;
        while(start <= end) {
            int cnt = 0;
            long mid = (start + end)/2;
            
            for(int i = 0; i < k; i++) {
                //랜선이 이진탐색으로 찾은 값보다 크면 자를 수 있는
                //몫과 나머지 랜선 길이 모으기
                if(arr[i] >= mid) {
                    cnt += arr[i] / mid;
                }
            }
            if(cnt < n) {//자른 횟수가 n보다 적다면 끝을 한 칸 뒤로
                    end = mid - 1;
                }
                else {//크다면 최댓값을 찾고 시작범위를 앞으로 한 칸
                    result = mid;
                    start = mid + 1;
                }
        }
        System.out.println(result);
    }
}