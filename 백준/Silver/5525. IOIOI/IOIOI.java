import java.io.*;

class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int s = Integer.parseInt(br.readLine());
        String str = br.readLine();
        int ans = 0;
        int pCnt = 0;
        for(int i = 1; i < s - 1; i++) {
            if(str.charAt(i - 1) == 'I' && str.charAt(i) == 'O' && str.charAt(i + 1) == 'I') {
                pCnt++;
                if(pCnt == n) {
                    ans++;
                    pCnt--;
                }
                // ioi패턴일 경우만 2칸 점프
                i++;
            }
            else pCnt = 0;
        }
        System.out.println(ans);
    }
}