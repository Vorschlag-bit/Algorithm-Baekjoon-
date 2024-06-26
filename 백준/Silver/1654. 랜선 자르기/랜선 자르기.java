import java.io.*;
import java.util.*;

class Main{
    static int[] arr;
    static int n;
    static int k;
    //이진탐색 재귀ver
    public static long binary_search(long s, long e) {
        //재귀문에선 최종 end값이 정답이다
        if(s > e) return e;
        
        long mid = (s + e) / 2;
        int cnt = 0;
        for(int i = 0; i < k; i++)
            //작은 경우는 어차피 0이 나오므로 조건절 필요없음
            cnt += arr[i] / mid;
        //1. 너무 많이 잘랐음
        if(cnt < n) return binary_search(s, mid - 1);
        //2. 너무 적게 잘랐음
        else return binary_search(mid + 1, e);
    }  
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        
        arr = new int[k];
        long start = 1;
        long end = 0;
        
        for(int i = 0; i < k; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            end = Math.max(arr[i], end);
        }
        long result = binary_search(start, end);
        System.out.println(result);
    }
}