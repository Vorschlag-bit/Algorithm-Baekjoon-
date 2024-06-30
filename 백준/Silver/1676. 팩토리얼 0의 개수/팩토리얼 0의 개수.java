import java.math.BigInteger;
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int cnt = 0;
        
        for(int i = 5; i <= n; i +=5) {
            int num = i;
            while(num % 5 == 0) {
                num /= 5;
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}