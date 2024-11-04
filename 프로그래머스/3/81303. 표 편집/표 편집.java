import java.util.*;
class Solution {
    public String solution(int n, int k, String[] cmd) {
        TreeSet<Integer> set = new TreeSet<>();
        Deque<Integer> dq = new LinkedList<>();
        StringBuilder sb = new StringBuilder();
        boolean[] check = new boolean[n];
        for(int i = 0; i < n; i++)
            set.add(i);
        
        for(String c : cmd) {
            StringTokenizer st = new StringTokenizer(c);
            String s = st.nextToken();
            
            switch(s) {
                case "U":
                    int x = Integer.parseInt(st.nextToken());
                    for(int i = 0; i < x; i++)
                        k = set.lower(k);
                    break;
                case "D":
                    x = Integer.parseInt(st.nextToken());
                    for(int i = 0; i < x; i++)
                        k = set.higher(k);
                    break;
                case "C":
                    int last = set.last();
                    dq.offer(k);
                    set.remove(k);
                    check[k] = true;
                    if(last == k) {
                        k = set.lower(k);
                    }
                    else
                    k = set.higher(k);
                    break;
                case "Z":
                    x = dq.pollLast();
                    check[x] = false;
                    set.add(x);
                    break;
            }
        }
        for(int i = 0; i < n; i++) {
            sb.append((check[i] ? "X" : "O"));
        }
        return sb.toString();
    }
}