import java.math.BigInteger;
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        BigInteger fac = BigInteger.ONE;

        for(int i = 2; i <= n; i++) {
            fac = fac.multiply(BigInteger.valueOf(i));
        }
        int ans = 0;
        while(fac.mod(BigInteger.TEN).equals(BigInteger.ZERO)) {
            ans++;
            fac = fac.divide(BigInteger.TEN);
        }
        System.out.println(ans);
    }
}