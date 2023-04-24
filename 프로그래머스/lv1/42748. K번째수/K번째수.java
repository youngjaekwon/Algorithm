import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        int i = 0;

        for (int[] command:commands){
            List<Integer> list = new ArrayList<>();

            for (int num : array){
                list.add(num);
            }

            int startIndex = command[0] - 1;
            int endIndex = command[1];
            int k = command[2] - 1;

            List<Integer> arrayByCommand = list.subList(startIndex, endIndex);
            arrayByCommand.sort(new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    return o1.compareTo(o2);
                }
            });
            int targetNum = arrayByCommand.get(k);
            answer[i++] = targetNum;
        }

        return answer;
    }
}