import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> q = new PriorityQueue<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            q.offer(Integer.parseInt(st.nextToken()));
        }
        int[] arr = new int[n];
        arr[0] = q.poll();
        for(int i = 1; i < n; i++) {
            arr[i] = arr[i - 1] + q.poll();
        }
        int ans = 0;
        for(int i = 0; i < n; i++)
            ans += arr[i];
        System.out.println(ans);
    }
}