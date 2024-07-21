import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);
        int start = (int) Math.round(n * 0.15);
        int end = n - start;
        double sum = 0;
        for (int i = start; i < end; i++) {
            sum += arr[i];
        }
        int ans = (int) Math.round(sum / (end - start));
        System.out.println(ans);
    }
}