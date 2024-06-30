import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int X = scanner.nextInt();

        ArrayList<Integer> stick = new ArrayList<>();
        stick.add(64);
        int total = 64;

        while(total > X) {
            //총 합이 x보다 긴 경우 가장 짧은 막대를 반갈
            int shortest = stick.get(stick.size() - 1);
            int half = shortest / 2;
            //반갈내고 바로 버려보고
            stick.remove(stick.size() - 1);
            stick.add(half);
            //반갈 1쪽만으로도 X보다 길다면 총 길이를 반갈로 바꾸고
            if (total - half >= X) total -= half;
            //아니라면 반갈은 붙여준다
            else stick.add(half);
        }
        System.out.println(stick.size());
    }
}