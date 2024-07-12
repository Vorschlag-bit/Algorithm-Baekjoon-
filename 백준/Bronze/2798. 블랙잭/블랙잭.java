import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        ArrayList<Integer> list = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            list.add(Integer.parseInt(st.nextToken()));
        }
        int ans = 0;
        Collections.sort(list);
        int a = 0, b = 0, c = 0;
        for (int i = 0; i < N; i++) {
            a = list.get(i);
            for (int j = i + 1; j < N; j++) {
                b = list.get(j);
                for (int k = j + 1; k < N; k++) {
                    c = list.get(k);
                    if(a + b + c <= M) {
                        ans = Math.max(ans, a + b + c);
                    }
                }
            }
        }
        System.out.println(ans);
    }
}