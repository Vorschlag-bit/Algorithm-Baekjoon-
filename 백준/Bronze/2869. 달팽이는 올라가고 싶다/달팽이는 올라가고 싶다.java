import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());
        int days = 0;
        int ans = 0;
        // 몫
        days = (V - A) / (A - B);
        if((V - A) % (A - B) == 0){
            ans = days + 1;
        }
        else {
            ans = days + 2;
        }
        System.out.println(ans);
    }
}