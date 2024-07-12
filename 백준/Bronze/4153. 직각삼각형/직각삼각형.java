import java.util.*;
import java.io.*;

class Main{
    public static void main (String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = 1, b = 1, c = 1;

        while(true){
            StringTokenizer st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            if(a == 0 && b == 0 && c == 0) break;
            boolean Check = false;
            if(a * a == b * b + c * c || b * b == c * c + a * a || c * c == b * b + a * a){
                Check = true;
            }
            if(Check){
                System.out.println("right");
            }
            else System.out.println("wrong");
        }
    }
}