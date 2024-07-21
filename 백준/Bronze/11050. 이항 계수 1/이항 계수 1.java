import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        System.out.println(fac(n, k));
    }

    private static int fac(int n, int k) {
        if(n == k || k == 0) return 1;
        
        return fac(n - 1, k - 1) + fac(n - 1, k);
    }
}