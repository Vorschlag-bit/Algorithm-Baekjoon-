import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        Map<String, String> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String url = st.nextToken();
            String pwd = st.nextToken();
            map.put(url, pwd);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            String url = br.readLine();
            sb.append(map.get(url)).append("\n");
        }
        System.out.println(sb);
    }
}