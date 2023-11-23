def solution(alp, cop, problems):
    max_alp = max(max(problem[0] for problem in problems), alp)
    max_cop = max(max(problem[1] for problem in problems), cop)
    
    # DP 테이블 초기화
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 알고력 또는 코딩력을 늘리는 경우
            if i < max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            # 문제를 푸는 경우
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp = min(max_alp, i + alp_rwd)
                    next_cop = min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

    # 최종적으로 필요한 알고력과 코딩력에 도달하기 위한 최소 시간
    return dp[max_alp][max_cop]