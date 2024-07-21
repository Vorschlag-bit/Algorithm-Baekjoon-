import java.io.*;
import java.math.BigInteger;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();

        BigInteger M = new BigInteger("1234567891");
        BigInteger ans = BigInteger.ZERO;
        BigInteger pow = BigInteger.ONE;
        BigInteger r = new BigInteger("31");

        for (int i = 0; i < str.length(); i++) {
            BigInteger charValue = BigInteger.valueOf(str.charAt(i) - 'a' + 1);
            ans = ans.add(charValue.multiply(pow)).mod(M);
            pow = pow.multiply(r).mod(M);
        }

        System.out.println(ans);
    }
}