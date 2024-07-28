import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int sum = 0;

        while(st.hasMoreTokens()) {
            int n = Integer.parseInt(st.nextToken());
            sum += n * n;
        }

        sum %= 10;
        System.out.println(sum);
    }
}