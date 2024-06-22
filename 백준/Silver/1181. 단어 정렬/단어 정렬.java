import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        String[] arr = new String[n];
        
        for(int i = 0; i < n; i++)
            arr[i] = br.readLine();
        
        Arrays.sort(arr, new Comparator<String>() {
            @Override //길이 순서 정렬
            public int compare(String s1, String s2) {
                if(s1.length() != s2.length())
                    return s1.length() - s2.length();
                //길이가 같다면 알파벳순서로 정렬
                return s1.compareTo(s2);
            }
        });
        for(int i = 0; i < n; i++){
            if(i == 0 || !arr[i].equals(arr[i - 1])) 
            System.out.println(arr[i]);
        }
    }
}