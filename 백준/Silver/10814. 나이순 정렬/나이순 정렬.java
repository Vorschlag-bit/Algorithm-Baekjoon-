import java.io.*;
import java.util.*;

class Member {
    int pk;
    int age;
    String name;

    public Member(int age, String name, int pk) {
        this.age = age;
        this.name = name;
        this.pk = pk;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        Member[] members = new Member[n];
        int pk = 1;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            members[i] = new Member(age, name, pk++);
        }

        Arrays.sort(members, new Comparator<Member>() {
            @Override
            public int compare(Member a, Member b) {
                //나이가 같다면 가입순
                if (a.age == b.age)
                    return a.pk - b.pk;
                //아님 나이순
                return a.age - b.age;
            }
        });

        for (int i = 0; i < n; i++) {
            System.out.println(members[i].age + " " + members[i].name);
        }
    }
}