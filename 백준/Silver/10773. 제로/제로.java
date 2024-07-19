import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int k = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();

        for(int i = 0; i < k; i++){
            int num = Integer.parseInt(br.readLine());

            if(num == 0) stack.pop();
            else stack.push(num);
        }
        int ans = 0;
        while(!stack.isEmpty()){
            ans += stack.pop();
        }
        System.out.println(ans);
    }
}