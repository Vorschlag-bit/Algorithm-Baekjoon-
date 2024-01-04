import java.util.*;

class Main{
    public static int reverse (int a) {
        String s = Integer.toString(a);
        char[] arr = s.toCharArray();
        char[] rsa = new char[arr.length];
        
        for(int i = 0; i<arr.length; i++){
            rsa[arr.length - 1 - i] = arr[i];
        }
        
        String rs = new String(rsa);
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