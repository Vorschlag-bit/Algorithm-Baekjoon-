import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Long> q = new PriorityQueue<>((a, b) -> {
            long n1 = Math.abs(a);
            long n2 = Math.abs(b);
            if(n1 == n2) return Long.compare(a, b);
            return Long.compare(n1, n2);
        });
        for(int i = 0; i < n; i++) {
            long num = Long.parseLong(br.readLine());
            if(num == 0) {
                if(q.isEmpty()) {
                    sb.append(0).append("\n");
                }
                else {
                    sb.append(q.poll()).append("\n");
                }
            }
            else {
                q.offer(num);
            }
        }
        System.out.println(sb);
    }
}