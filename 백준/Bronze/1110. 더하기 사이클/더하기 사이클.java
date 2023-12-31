import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int cnt = 0;

        int[] arr = new int[2];

        arr[0] = n / 10;
        arr[1] = n % 10;

        int sum = 0;

        for (int i = 0; i < Integer.MAX_VALUE; i++) {  // Infinite loop
            int ill = arr[0] + arr[1];
            if(ill>=10)
            ill= ill%10;
            sum = arr[1] * 10 + ill;
            cnt++;
            arr[0] = sum / 10;
            arr[1] = sum % 10;
            if (sum == n)
            break;
        }
        System.out.println(cnt);
    }
}