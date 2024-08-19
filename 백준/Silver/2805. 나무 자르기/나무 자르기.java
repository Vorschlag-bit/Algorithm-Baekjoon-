import java.util.*;
import java.io.*;

class Main {
    static int n;
    static long m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        long[] trees = new long[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(trees);
        long start = 1;
        long end = trees[n - 1];

        while(start <= end) {
            long mid = (start + end) / 2;
            long sum = 0;
            for (int i = 0; i < n; i++) {
                if(trees[i] > mid) sum += (trees[i] - mid);
            }

            if(sum >= m) start = mid + 1;
            else end = mid - 1;
        }
        System.out.println(end);
    }
}