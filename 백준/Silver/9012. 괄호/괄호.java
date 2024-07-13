import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            // '('과 ')'개수를 세기 위한 변수 
            int cnt = 0;
            // 괄호가 한 쌍을 이루는지, 짝이 없느 괄호가 있는지 판단
            boolean flag = true;
            for (int j = 0; j < s.length(); j++) {
                // ')'로 시작하는 예외
                if(cnt < 0) {
                    flag = false;
                    break;
                }
                // 한 문장에서 cnt 개수를 카운팅
                if(s.charAt(j) == '(') cnt++;
                if(s.charAt(j) == ')') cnt--;
            }
            // 다 짝 지어지지 않는 예외
            if(cnt != 0) flag = false;
            if(!flag) sb.append("NO").append("\n");
            else sb.append("YES").append("\n");
        }
        System.out.println(sb);
    }
}