import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        String[] nums = str.split("-");
        ArrayList<Integer> sums = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            StringTokenizer st = new StringTokenizer(nums[i], "+");
            int sum = 0;
            while(st.hasMoreTokens()) {
                sum += Integer.valueOf(st.nextToken());
            }
            sums.add(sum);
        }
        int answer = sums.remove(0);
        for(int sum : sums) {
            answer -= sum;
        }
        System.out.println(answer);
    }
}