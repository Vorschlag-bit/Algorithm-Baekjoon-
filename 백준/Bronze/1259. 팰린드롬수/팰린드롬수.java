import java.util.*;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n;
       
        
        for(int k = 0; k < 3000; k++){
            n = sc.nextInt();
            boolean pcheck = true;
            if(n==0)
            break;
            String num = Integer.toString(n);
            int len = num.length();
            char[] arr = new char[len];

            for(int i = 0; i < len; i++){
                arr[i] = num.charAt(i);
            }
        
            for(int i = 0; i<len/2; i++){
                if(arr[i]!=arr[len-1-i])
                pcheck = false;
            }

            if(pcheck == true)
            System.out.println("yes");
            else
            System.out.println("no");
        }
    }
}