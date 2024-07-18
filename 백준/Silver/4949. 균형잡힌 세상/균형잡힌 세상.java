import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while(true) {
            String s = br.readLine();
            if(s.equals(".")) {
                br.close();
                break;
            }
            sb.append(Balance(s)? "yes\n" : "no\n");
        }
        System.out.println(sb);
    }
    private static boolean Balance(String s){
        Stack<Character> stack = new Stack<>();

        for(char c : s.toCharArray()) {
            if(c == '(' || c == '[') stack.push(c);
            else if(c == ')' || c == ']') {
                if(stack.isEmpty()) return false;
                char top = stack.pop();
                if(c == ')' && top != '(' || c == ']' && top != '[') return false;
            }
        }
        return stack.isEmpty();
    }
}