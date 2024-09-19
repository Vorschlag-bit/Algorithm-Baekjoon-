import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Deque<Integer> q = new LinkedList<>();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int price = Integer.parseInt(br.readLine());
            if (price <= k) q.add(price);
        }
        int sum = 0;

        while(sum < k) {
            if(q.getLast() + sum > k) {
                q.removeLast();
                continue;
            }
            sum += q.getLast();
            ans++;
        }
        System.out.println(ans);
        }
    }