import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        //나눈 몫을 저장할 리스트
        ArrayList<Integer> arr = new ArrayList<>();
        //나머지 저장할 변수
        int BIG = Math.max(N, M);
        int SMALL = Math.min(N, M);
        int GCD = GCD(BIG, SMALL);
        int LCM = N * M / GCD;
        System.out.println(GCD);
        System.out.println(LCM);
    }
    public static int GCD(int big, int small) {
        if(small == 0) return big;

        return GCD(small, big % small);
    }
}