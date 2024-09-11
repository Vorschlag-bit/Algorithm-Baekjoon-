import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < t; i++) {
            int k = Integer.parseInt(br.readLine());
            TreeMap<Integer, Integer> map = new TreeMap<>();
            for (int j = 0; j < k; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                char c = st.nextToken().charAt(0);
                int number = Integer.parseInt(st.nextToken());
                if(c == 'I') {
                    map.put(number, map.getOrDefault(number,0) + 1);
                }
                else {
                    if(!map.isEmpty() && c == 'D') {
                        int key = number == 1 ? map.lastKey() : map.firstKey();
                        if(map.get(key) == 1) map.remove(key);
                        else map.put(key, map.get(key) - 1);
                    }
                }
            }
            if(map.isEmpty()) sb.append("EMPTY\n");
            else sb.append(map.lastKey() + " ").append(map.firstKey()).append("\n");
        }
        System.out.println(sb);
    }
}