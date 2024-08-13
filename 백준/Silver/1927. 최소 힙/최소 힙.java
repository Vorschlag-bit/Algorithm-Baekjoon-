import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Integer> q = new PriorityQueue<>();
    
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int m = Integer.parseInt(br.readLine());

            if(m == 0) {
                if(!q.isEmpty()){
                    int Min = q.poll();
                    sb.append(Min).append("\n");
                }
                else sb.append(0).append("\n");
            }
            else {
                q.offer(m);
            }
        }
        System.out.println(sb);
    }
}