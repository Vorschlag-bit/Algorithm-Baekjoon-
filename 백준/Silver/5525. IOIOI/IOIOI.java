import java.io.*;

class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int s = Integer.parseInt(br.readLine());
        String str = br.readLine();
        int ans = 0;
        String ioi ="";
        for (int i = 0; i < 2 * n + 1; i++) {
            if(i % 2 == 0) ioi += "I";
            else ioi += "O";
        }
        int l = ioi.length();
        for(int i = 0; i <= s - l; i++) {
            if(str.charAt(i) == 'I') {
                boolean Check = true;
                String sub = str.substring(i);
                for(int j = 0; j < l; j++) {
                    if(sub.charAt(j) != ioi.charAt(j)) {
                        Check = !Check;
                        break;
                    }
                }
                if(Check) {
                    ans++;
                    if(i + 2 < s)
                    i += 1;
                }
            }
        }
        System.out.println(ans);
    }
}