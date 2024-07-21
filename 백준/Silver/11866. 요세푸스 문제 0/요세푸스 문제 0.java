import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            q.offer(i);
        }
        StringBuilder sb = new StringBuilder("<");

        while(q.size() > 1){

            for(int i = 0; i < k - 1; i++) {
                int num = q.poll();
                q.offer(num);
            }
            // k번째 수는 뺀다
            sb.append(q.poll()).append(", ");
        }
        // 마지막은 닫는 괄호로
        sb.append(q.poll()).append(">");
        System.out.println(sb);
    }
}