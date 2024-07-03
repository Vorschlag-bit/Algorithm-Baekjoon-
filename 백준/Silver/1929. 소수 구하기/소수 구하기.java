import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        StringBuffer sb = new StringBuffer();
        //소수체크배열 생성 후 true로 초기화
        boolean[] Prime = new boolean[n + 1];
        Arrays.fill(Prime, true);
        //1은 소수아님
        Prime[1] = false;
        int sqrt = (int)Math.sqrt(n);
        //2부터 n제곱근으로 n까지 나누면 된다.
        for(int i = 2; i <= sqrt; i++) {
            if(Prime[i]) {
                //i의 배수만큼 지워나가기
                for(int j = i * i; j <= n; j += i) {
                    Prime[j] = false;
                }
            }
            }
        for(int i = m; i <= n; i++) {
            if(Prime[i]) {
                sb.append(i).append("\n");
            }
        }
        System.out.println(sb);
    }
}