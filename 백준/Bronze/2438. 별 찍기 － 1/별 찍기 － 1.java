import java.util.*;

class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 1;
        while(n >= cnt) {
            for(int i = 1; i <= cnt; i++){
                System.out.print("*");
            }
            cnt++;
            System.out.println();
        }
    }
}