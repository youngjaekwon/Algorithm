import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        Map<String, String> idMap = new HashMap<>();
        Map<String, String> recordMap = new HashMap<>();
        Map<String, String> changeRecordMap = new HashMap<>();

        for (int i = 0; i < record.length; i++) {
            String[] eachRecord = record[i].split(" ");
            String state = eachRecord[0];
            String id = eachRecord[1];
            if (state.equals("Enter")){
                String nick = eachRecord[2];
                idMap.put(id, nick);
            }

            if (state.equals("Change")){
                String nick = eachRecord[2];
                changeRecordMap.put(id, nick);
            }

            if (recordMap.get(id) == null){
                recordMap.put(id, state);
            } else {
                String states = recordMap.get(id);
                recordMap.put(id, states + " " + state);
            }
        }

        Iterator<String> ids = recordMap.keySet().iterator();
        while (ids.hasNext()){
            String id = ids.next();
            String[] states = recordMap.get(id).split(" ");

            if (states.length < 2) continue;

            for (int i = 0; i < states.length; i++) {
                if ((i + 1 < states.length)
                        && ((states[i].equals("Enter") && states[i + 1].equals("Change") && !states[states.length - 1].equals("Enter")))
                        && !(states[states.length - 2].equals("Enter") && states[states.length - 1].equals("Leave"))){
                    idMap.put(id, changeRecordMap.get(id));
                }
            }
        }

        List<String> answerList = new ArrayList<>();

        for (int i = 0; i < record.length; i++) {
            String[] eachRecord = record[i].split(" ");
            String state = eachRecord[0];
            String id = eachRecord[1];

            if (state.equals("Enter")){
                answerList.add(idMap.get(id) + "님이 들어왔습니다.");
            } else if (state.equals("Leave")){
                answerList.add(idMap.get(id) + "님이 나갔습니다.");
            }
        }

        String[] answer = new String[answerList.size()];
        answerList.toArray(answer);
        return answer;
    }
}