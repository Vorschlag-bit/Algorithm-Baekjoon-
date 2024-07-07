import java.util.*;

class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Queue<Integer> q = new LinkedList<>();
        int n = sc.nextInt();
        int num = 1;
        for(int i = 0; i < n; i++){
            q.offer(num);
            num++;
        }
        int cnt = 0;
        while(q.size() > 1){
            if(cnt%2 == 0){
                q.poll();
            }
            else {
                int m = q.poll();
                q.offer(m);
            }
            cnt++;
        }
        System.out.println(q.peek());
    }
}