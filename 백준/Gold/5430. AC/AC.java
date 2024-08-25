import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            String method = br.readLine();
            int n = Integer.parseInt(br.readLine());
            Deque<Integer> dq = new ArrayDeque<>();

            StringTokenizer st = new StringTokenizer(br.readLine(), "[],");
            for(int j = 0; j < n; j++)
                dq.offer(Integer.parseInt(st.nextToken()));

            boolean error = false;
            boolean left = true;

            for (char c : method.toCharArray()) {
                if (c == 'R') {
                    left = !left;
                } else {
                    if (left) {
                        if (dq.poll() == null) {
                            answer.append("error\n");
                            error = true;
                            break;
                        }
                    } else {
                        if (dq.pollLast() == null) {
                            error = true;
                            answer.append("error\n");
                            break;
                        }
                    }
                }
            }
            if(error) continue;
            answer.append("[");
            if(dq.size() > 0) {
                if(left) {
                    answer.append(dq.poll());
                    while(!dq.isEmpty()) answer.append(",").append(dq.poll());
                }
                else {
                    answer.append(dq.pollLast());
                    while(!dq.isEmpty()) answer.append(",").append(dq.pollLast());
                }
            }
            answer.append("]\n");
        }
        System.out.println(answer);
    }
}
