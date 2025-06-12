import java.util.*;
class Tuple {
    String head;
    int num;
    int idx;
    
    public Tuple(String h, int n, int i) {
        this.head = h;
        this.num = n;
        this.idx = i;
    }
}
class Solution {
    public String[] solution(String[] files) {
        String[] ans = new String[files.length];
        List<Tuple> dict = new ArrayList();
        for (int idx = 0; idx < files.length; idx++) {
            String file = files[idx];
            String low = file.toLowerCase();
            StringBuilder head = new StringBuilder();
            int n_s = 0;
            int n_e = 0;
            for (int i = 0; i < low.length(); i++) {
                char chr = low.charAt(i);
                if (Character.isDigit(chr)) {
                    n_s = i;
                    break;
                }
                head.append(chr);
            }
            for (int i = n_s; i < low.length(); i++) {
                if (Character.isDigit(low.charAt(i))) {
                    n_e = i;
                }
                else break;
            }
            Integer num = Integer.valueOf(low.substring(n_s,n_e+1));
            dict.add(new Tuple(head.toString(),num,idx));
        }
        Collections.sort(dict, (a,b) -> {
            int cmp = a.head.compareTo(b.head);
            if (cmp != 0) return cmp;
            return Integer.compare(a.num,b.num);
        });
        int cnt = 0;
        for (Tuple t : dict) {
            int idx = t.idx;
            ans[cnt] = files[idx];
            cnt++;
        }
        return ans;
    }
}