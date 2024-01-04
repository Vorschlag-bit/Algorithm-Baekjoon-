import java.util.*;

class Main{
    public static int reverse (int a) {
        String s = Integer.toString(a);
        StringBuffer sb = new StringBuffer(s);
        String rs = sb.reverse().toString();
        
        a = Integer.parseInt(rs);
        
        return a;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        System.out.print(reverse(reverse(n)+reverse(m)));
    }
}