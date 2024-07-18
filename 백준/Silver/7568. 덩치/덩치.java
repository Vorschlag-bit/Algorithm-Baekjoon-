import java.io.*;
import java.util.*;
class Human {
    int height;
    int weight;
    int rank;

    public Human(int weight, int height) {
        this.weight = weight;
        this.height = height;
        rank = 1;
    }
}

class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        Human[] humans = new Human[n + 1];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            humans[i] = new Human(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                //자기 자신은 패스
                if(i == j) continue;

                if(humans[i].height < humans[j].height && humans[i].weight < humans[j].weight) {
                    humans[i].rank++;
                }
            }
            sb.append(humans[i].rank).append(" ");
        }
        System.out.println(sb);
    }
}