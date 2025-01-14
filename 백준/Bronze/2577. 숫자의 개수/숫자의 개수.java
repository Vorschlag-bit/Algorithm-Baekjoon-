import java.util.*;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        int n = A*B*C;

        String num = Integer.toString(n);

        int[] arr = new int[10];

        for(int i = 0; i<num.length(); i++){
            arr[num.charAt(i)-'0']++; 
        }

        for(int i = 0; i<10; i++){
            System.out.println(arr[i]);
        }
    }
}