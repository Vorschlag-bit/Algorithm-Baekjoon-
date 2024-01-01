import java.util.*;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int[] arr = new int[5];
        
        for(int i = 0; i<5; i++){
            arr[i] = sc.nextInt();
        }
        
        int val = 1;
        int cnt = 0;
        
        while(true){
            for(int i = 0; i<5; i++){
                if(val%arr[i]==0){
                    cnt++;
                }
            }
            if(cnt>=3){
                System.out.println(val);
                return;
            }
            val++;
            cnt = 0;
        }
    }
}