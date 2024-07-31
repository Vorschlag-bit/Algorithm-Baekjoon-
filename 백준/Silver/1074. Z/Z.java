import java.io.*;
import java.util.*;

class Main{
    static int n, r, c, ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        int size = (1 << n);
        solution(0,0,size);
        System.out.println(ans);
    }

    private static void solution(int x, int y, int size) {
        if(size == 1) return;
        int newsize = size / 2;

        // 1사분면
        if(c < x + newsize && r < y + newsize)
            solution(x, y, newsize);
        // 2사분면
        else if(c >= x + newsize && r < y + newsize) {
            ans += newsize * newsize;
            solution(x + newsize, y, newsize);
        }
        // 3사분면
        else if(c < x + newsize && r >= y + newsize) {
            ans += newsize * newsize * 2;
            solution(x, y + newsize, newsize);
        }
        // 4사분면
        else {
            ans += newsize * newsize * 3;
            solution(x+ newsize, y + newsize, newsize);
        }
    }
}