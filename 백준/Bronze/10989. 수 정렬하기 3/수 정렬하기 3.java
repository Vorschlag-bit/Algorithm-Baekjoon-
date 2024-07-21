import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int[] cnt = new int[10000 + 1];
        // counting sort
        for (int i = 0; i < n; i++) {
            cnt[Integer.parseInt(br.readLine())]++;
        }
        br.close();
        for (int i = 1; i < 10000 + 1; i++) {
            while(cnt[i] > 0) {
                sb.append(i).append('\n');
                cnt[i]--;
            }
        }
        System.out.println(sb);
    }
}