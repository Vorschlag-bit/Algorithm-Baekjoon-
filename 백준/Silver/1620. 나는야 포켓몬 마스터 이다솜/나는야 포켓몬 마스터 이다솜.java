import java.io.*;
import java.util.*;
class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        ArrayList<String> numbers = new ArrayList<>();
        HashMap<String, Integer> names = new HashMap<>();
        StringBuilder sb = new StringBuilder();
        numbers.add("");
        for (int i = 1; i <= n; i++) {
            String name = br.readLine();
            numbers.add(name);
            names.put(name, i);
        }

        for (int i = 0; i < m; i++) {
            String guess = br.readLine();
            char c = guess.charAt(0);
            // 숫자 입력 받을 경우
            if(Character.isDigit(c)) {
                int idx = Integer.parseInt(guess);
                sb.append(numbers.get(idx)).append("\n");
            } // 문자 입력 받을 경우
            else {
                sb.append(names.get(guess)).append("\n");
            }
        }
        System.out.println(sb);
    }
}