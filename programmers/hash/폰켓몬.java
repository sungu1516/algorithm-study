import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0; 
        int totalLen = nums.length;
        int pickLen = totalLen / 2;
        
        // 1. nums 배열 중 중복값 제거
        // 자료구조 - hash
        HashSet<Integer> set = new HashSet<>();
        for(int num : nums) {
            set.add(num);
        }
        
        // 2. 최대값은 pickLen 이므로, nums의 길이와 pickLen을 비교 후 결정
        int setSize = set.size();
        
        // 2-1. 만약 pickLen이 더 짧거나 같은 경우
        if(pickLen <= setSize) {
            answer = pickLen;
        } else {
            // 2-2. pickLen이 더 긴 경우
            answer = setSize;
        }
        
        return answer;
    }
}