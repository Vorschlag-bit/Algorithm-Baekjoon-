import java.util.*;

class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        String num = Integer.toString(n);
        
        int cnt = 0;
        int i = 1;
        
        while(true){
            int front = 1;
            int back = 1;
            if(num.length()==1)
                break;
            for(int j = 0; j < i; j++){
                front *= num.charAt(j) - '0';
            }
            
            for(int j = i; j < num.length(); j++){
                back *= num.charAt(j) - '0';
            }
            
            if(back == front){
                cnt = 1;
                break;
            }
            
            if(i == num.length() - 1)
                break;
            
            i++;
        }
        String result = (cnt == 1) ? "YES" : "NO";
        System.out.print(result);
    }
}