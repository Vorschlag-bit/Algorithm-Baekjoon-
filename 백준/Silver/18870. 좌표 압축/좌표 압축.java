import java.io.*;
import java.util.StringTokenizer;
import java.util.TreeMap;

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];

        TreeMap<Integer, Integer> map = new TreeMap<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            arr[i] = num;
            map.put(num, 0);
        }
        int cnt = 0;
        for (int key : map.keySet()) {
            map.put(key, cnt);
            cnt++;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(map.get(arr[i])).append(" ");
        }
        System.out.println(sb);
    }
}