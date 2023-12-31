import java.util.*;
class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        
        int nnum = sc.nextInt();
        
        int[] arr = new int[nnum];
        
        int len = arr.length;
        
        for(int i = 0; i<len; i++){
            arr[i] = sc.nextInt();
        }
        
        int max = 0;
        int min = 1000000;
        
        for(int i = 0 ; i<len; i++){
            if(arr[i]>max){
                max = arr[i];
            }
            if(arr[i]<min)
                min = arr[i];
        }
        if(len == 1)
            System.out.println(arr[0]*arr[0]);
        else
        System.out.println(max*min);
    }
}