import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split(" ");
        int n = Integer.parseInt(arr[0]);
        int m = Integer.parseInt(arr[1]);

        int cnt = 0;
        StringBuilder sb = new StringBuilder();
        ArrayList<String> list = new ArrayList<>();
        Set<String> nonHeard = new HashSet<>();

        for (int i = 0; i < n; i++) {
            nonHeard.add(br.readLine());
        }

        for (int i = 0; i < m; i++) {
            String name = br.readLine();
            if(nonHeard.contains(name)) {
                cnt++;
                list.add(name);
            }
        }
        Collections.sort(list);
        
        for (String name : list) {
            sb.append(name).append("\n");
        }
        
        System.out.println(cnt);
        System.out.println(sb);
    }
}