import java.util.*;

class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        boolean Check = false;
        int ans = 0;
        for(int i = 1; i < n ; i++){
            int m = i + (i/1000000) % 10 + (i/100000) % 10
                    + (i/10000) % 10 + (i/1000) % 10 + (i/100) % 10 + (i/10) % 10 + i%10;
            if(m == n) {
                Check = true;
                ans = i;
                break;
            }
        }
        if(Check)
        System.out.println(ans);
        else System.out.println(0);
    }
}