import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<>(); //스택 선언
        StringBuffer sb = new StringBuffer(); //스택에 따라 + -를 담을 StringBuffer선언
        int n = Integer.parseInt(br.readLine());
        boolean Check = true;
        //시작은 1부터
        int cur = 1;
        for(int i = 0; i < n; i++){
            int num = Integer.parseInt(br.readLine());

            while(cur <= num) {
                stack.push(cur);
                sb.append("+\n");
                cur++;
            }

            if(stack.peek() != num) {
                Check = false;
                break;
            }

            stack.pop();
            sb.append("-\n");
        }
        if(Check) {
            System.out.println(sb);
        }
        else System.out.println("NO");
    }
}