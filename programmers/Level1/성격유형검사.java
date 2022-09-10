import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        
        // 자료구조 : HashMap
        HashMap<String, Integer> map = new HashMap<>();
        map.put("R", 0);
        map.put("T", 0);
        map.put("C", 0);
        map.put("F", 0);
        map.put("J", 0);
        map.put("M", 0);
        map.put("A", 0);
        map.put("N", 0);
        
        // 1. survey, choices 순회하며 점수 기록
        
        for(int i = 0; i < choices.length; i ++) {
            // 1-1. choices[i]의 점수가 3점 이하인 경우, survey[i]의 첫 번째 캐릭터에 |x-4|점 더하기
            if(choices[i] <= 3) {
                map.put(survey[i].substring(0, 1), map.get(survey[i].substring(0, 1)) + Math.abs(choices[i] - 4));
            }
            // 1-2. choices[i]의 점수가 5점 이상인 경우, survey[i]의 첫 번째 캐릭터에 x-4점 더하기
            else if (choices[i] >= 5) {
                map.put(survey[i].substring(1, 2), map.get(survey[i].substring(1, 2)) + (choices[i] - 4));
            }
            // 1-3. 그 외의 경우, (점수가 4점인 경우), pass
            else {
                continue;
            }
        }
        
        System.out.println(map);
        // 2. 지표별 성격유형 결정
        // 만약 점수가 같을 시, 알파벳 우선
        // 2-1. 1번 지표
        if(map.get("R") >= map.get("T")) {
            answer += "R";
        } else {
            answer += "T";
        }
        
        // 2-2. 2번 지표
        if(map.get("C") >= map.get("F")) {
            answer += "C";
        } else {
            answer += "F";
        }
        
        
        // 2-3. 3번 지표
        if(map.get("J") >= map.get("M")) {
            answer += "J";
        } else {
            answer += "M";
        }
        
        
        // 2-4. 4번 지표
        if(map.get("A") >= map.get("N")) {
            answer += "A";
        } else {
            answer += "N";
        }
        
        return answer;
    }
}