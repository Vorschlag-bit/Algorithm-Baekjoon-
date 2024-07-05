import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        //주어지는 최대 수는 1000
        boolean[] Prime = new boolean[1001];
        Arrays.fill(Prime, true);
        //1은 소수 아님
        Prime[1] = false;
        int cnt = 0;
        int sqrt = (int) Math.sqrt(1000);
        //그냥 1000까지 소수판별
        for (int i = 2; i <= sqrt; i++) {
            if (Prime[i]) {
                for (int j = i * i; j <= 1000; j += i) {
                    Prime[j] = false;
                }
            }
        }
        for(int i = 0; i < n; i++) {
            int num = scanner.nextInt();
            if(Prime[num]) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}