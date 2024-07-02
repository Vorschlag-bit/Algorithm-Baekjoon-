import java.util.*;
import java.io.*;

class Main {
    static long[] arr;
    static StringBuffer sb = new StringBuffer();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        arr = new long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }
        
        Arrays.sort(arr);

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        
        for (int i = 0; i < m; i++) {
            long num = Long.parseLong(st.nextToken());
            binary_search(0, n - 1, num);
        }
        
        System.out.print(sb);
    }

    public static void binary_search(int start, int end, long num) {
        if (start > end) {
            sb.append("0\n");
            return;
        }
        int mid = (start + end) / 2;
        if (num == arr[mid]) {
            sb.append("1\n");
            return;
        }
        if (arr[mid] > num) binary_search(start, mid - 1, num);
        else binary_search(mid + 1, end, num);
    }
}