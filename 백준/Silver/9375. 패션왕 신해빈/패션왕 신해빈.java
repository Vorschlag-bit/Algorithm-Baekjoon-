import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException {
        // n개의 자리수에 넣을 수 있는 숫자가 주어지고 0을 포함해서 생길 수 있는 조합의 가짓수
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            HashMap<String, Integer> map = new HashMap<>();
            for(int j = 0; j < n; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String cloth = st.nextToken();
                String key = st.nextToken();
                map.put(key, map.getOrDefault(key, 0) + 1);
            }
            int count = 1;
            for(int cnt : map.values()) {
                count *= (cnt + 1);
            }
            sb.append(count - 1).append("\n");
        }
        System.out.println(sb);
    }
}