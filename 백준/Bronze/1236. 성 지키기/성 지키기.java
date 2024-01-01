import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int col = 0;
        int row = 0;

        char[][] arr = new char[n][m];

        int len = arr.length;

        for (int i = 0; i < len; i++) {
            String str = sc.next();
            for(int j = 0; j < arr[i].length; j++){
                arr[i][j] = str.charAt(j);
            }
        }

        int cnt = 0;
        //행 검사
        for (int i = 0; i < n; i++) {
            boolean check = true;
            for (int j = 0; j < m; j++) {
                if (arr[i][j]=='X') {
                    check = false;
                    break;
                }
            }
            if(check == true)
            col++;
        }
        //열 검사
        for(int i = 0; i < m; i++){
            boolean check = true;
            for(int j = 0; j< n; j++){
                if(arr[j][i]=='X'){
                    check = false;
                    break;
                }
            }
            if(check == true)
            row++;
        }

        System.out.println(Math.max(row,col));
    }
}