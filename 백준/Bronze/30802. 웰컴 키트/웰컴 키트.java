import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt((br.readLine()));
        int num = 0;
        int pens = 0;
        int pen = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] sizes = new int[6];
        for (int i = 0; i < 6; i++) {
            sizes[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        br.close();
        for (int i = 0; i < 6; i++) {
            num += (sizes[i] + t - 1) / t;
        }
        pens = (n / p);
        pen = (n % p);  
        System.out.println(num);
        System.out.println(pens + " " + pen);
    }
}