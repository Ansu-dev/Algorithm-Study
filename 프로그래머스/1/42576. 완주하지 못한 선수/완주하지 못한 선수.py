def solution(participant, completion):
    answer = ''
    hashDict = {}
    sumHash = 0
    # 1명 찾기 -> participant엔 있고 completion에는 없는 사람 찾기

    # 해시를 사용 하여 품
    # 1. Hash를 Key로 갖고, participant의 이름을 Value로 갖는 Dictionary를 만들고 합을 구함
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    # 2. 합에서 completion의 hash들의 합을 뺀다.
    for comp in completion:
        sumHash -= hash(comp)
    # 3. 마지막에 남은 hash가 완주하지 못한 선수의 hash이다.
    return hashDict[sumHash]