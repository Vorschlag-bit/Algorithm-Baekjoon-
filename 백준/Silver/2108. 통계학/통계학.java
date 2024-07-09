import  java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuffer sb = new StringBuffer();
        int n = sc.nextInt();

        int[] arr = new int[n];
        Map<Integer, Integer> frequencymap = new HashMap<>();
        int sum = 0;
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        int maxfrequency = 0;

        for(int i = 0; i < n; i++){
            int num = sc.nextInt();
            arr[i] = num;
            sum += num;
            max = Math.max(max, num);
            min = Math.min(min, num);

            int frequency = frequencymap.getOrDefault(num, 0) + 1;
            frequencymap.put(num, frequency);
            maxfrequency = Math.max(maxfrequency, frequency);
        }

        //산술 평균
        sb.append(Math.round((double) sum / n)).append("\n");

        //중앙값
        Arrays.sort(arr);
        sb.append(arr[n / 2]).append("\n");

        //최빈값
        List<Integer> mode = new ArrayList<>();
        for(Map.Entry<Integer, Integer> entry : frequencymap.entrySet()){
            if(entry.getValue() == maxfrequency){
                mode.add(entry.getKey());
            }
        }
        Collections.sort(mode);
        sb.append(mode.size() > 1 ? mode.get(1) : mode.get(0)).append("\n");

        //범위
        sb.append(max - min);
        System.out.println(sb);
    }
}