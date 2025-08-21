import java.util.*;
class Solution {
    public int solution(String[][] book_time) {
        int ans = 0;
        int n = book_time.length;
        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] bt = book_time[i];
            arr[i][0] = s2t(bt[0]);
            arr[i][1] = s2t(bt[1]) + 10;
        }
        // 일찍 시작 기준으로 정렬
        Arrays.sort(arr,Comparator
                    .comparingInt((int[] a) -> a[0])
                   .thenComparingInt((int[] a) -> a[1]));
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int[] a : arr) {
            int st = a[0];
            int et = a[1];
            while(!pq.isEmpty() && pq.peek() <= st) {
                pq.poll();
            }
            pq.add(et);
            ans = Math.max(ans, pq.size());
        }
        return ans;
    }
    
    public int s2t(String str) {
        String[] s = str.split(":");
        return Integer.valueOf(s[0])*60 + Integer.valueOf(s[1]);
    }
}