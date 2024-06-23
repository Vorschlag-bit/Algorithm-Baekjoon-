import java.util.*;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        
        int cnt = 0;
        for(int i = 666; i <= 100000000; i++) {
            //범위 돌면서 맞는 수 찾기, 문자열로 변환 후 666이 있는지 확인 후 cnt를 1씩 증가
            //cnt가 n과 같다면 그 수를 출력하고 종료
            String str = Integer.toString(i);
            if(str.contains("666")) {
                cnt++;
                if(cnt == n) {
                    int ans = Integer.parseInt(str);
                    System.out.println(ans);
                    break;
                }
            }
        }
    }
}