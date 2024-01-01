import java.util.*;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        String str = sc.next();
        
        str = str.toUpperCase();
        
        int[] arr = new int[26];
        
        for(int i = 0; i<str.length(); i++){
            arr[str.charAt(i)-65]++;
        }
        
        int Max = -1;
        char ch = '?';
        
        for(int i = 0; i<26; i++){
            if(arr[i]>Max){
                Max = arr[i];
                ch = (char)(i+65);
            }
            else if(arr[i]==Max)
                ch = '?';
        }
        System.out.println(ch);
    }
}