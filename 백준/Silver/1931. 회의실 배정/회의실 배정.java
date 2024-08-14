import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int ans = 0;
        int n = Integer.parseInt(br.readLine());
        ArrayList<Meeting> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            list.add(new Meeting(s, e));
        }
        list.sort((o1, o2) -> {
            if(o1.end == o2.end) return o1.start - o2.start;
            return o1.end - o2.end;
        });

        int end = 0;
        for(Meeting meeting : list) {

            if(end <= meeting.start) {
                end = meeting.end;
                ans++;
            }
        }
        System.out.println(ans);
    }
}
class Meeting{
    int start;
    int end;

    public Meeting(int start, int end) {
        this.start = start;
        this.end = end;
    }
}