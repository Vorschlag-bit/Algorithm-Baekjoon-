import java.util.*;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();
        int b = sc.nextInt();
        int[] arr = new int[2000];
        int cnt = 1;
        
        for(int i = 1; i <= 45; i++){
            for(int j = 1; j <= i; j++){
                arr[cnt] = i;
                cnt++;
            }
        }
        
        int sum = 0;
        
        for(int i = a; i<= b; i++){
            sum += arr[i];
        }
        System.out.print(sum);
    }
}