import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            arr[i] = num;
        }

        int start = 0;
        int ans = 0;
        for(int end = 0; end < arr.length; end++) {
            map.put(arr[end], map.getOrDefault(arr[end], 0) + 1);

            while(map.size() > 2) {
                map.put(arr[start], map.get(arr[start]) - 1);
                if(map.get(arr[start]) == 0) map.remove(arr[start]);
                start++;
            }

            ans = Math.max(ans, end - start + 1);
        }
        System.out.println(ans);
    }
}