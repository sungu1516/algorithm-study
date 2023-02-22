from collections import deque

def get_diff_cnt(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt

def solution(begin, target, words):
    words.append(begin)
    visited = [0] * len(words)

    # bfs 정의
    def bfs(graph, st_idx, visited):
        # que 초기화
        que = deque([st_idx])
        # 첫 방문 처리
        visited[st_idx] = 1

        while que:
            # que - popleft
            idx = que.popleft()
            for i in range(len(words)):
                # 조건1 - 방문하지 않은 경우
                # 조건2 - 두 알파벳의 다른 char의 개수가 1개인 경우
                if not visited[i] and get_diff_cnt(words[idx], words[i]) == 1:
                    # 방문처리 - 횟수 기록
                    visited[i] = visited[idx] + 1
                    # 만약 target 이라면
                    if words[i] == target:
                        return visited[i] - 1
                    # que 삽입
                    que.append(i)

    # bfs 실행
    result = bfs(words, len(words) - 1, visited)
    if result:
        return result
    else:
        return 0