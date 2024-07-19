import java.io.*;
import java.util.*;
class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> list = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            switch(str) {
                //push
                case "push" :
                    int num = Integer.parseInt(st.nextToken());
                    list.add(num);
                    break;
                //pop
                case "pop" :
                    if(list.isEmpty()) sb.append(-1).append("\n");
                    else {
                        sb.append(list.get(0)).append("\n");
                        list.remove(0);
                    }
                    break;
                //size
                case "size" :
                    sb.append(list.size()).append("\n");
                    break;
                //empty
                case "empty" :
                    if(list.isEmpty()) sb.append(1).append("\n");
                    else sb.append(0).append("\n");
                    break;
                //front
                case "front" :
                    if(list.isEmpty()) sb.append(-1).append("\n");
                    else sb.append(list.get(0)).append("\n");
                    break;
                //back
                case "back" :
                    if(list.isEmpty()) sb.append(-1).append("\n");
                    else sb.append(list.get(list.size() - 1)).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}