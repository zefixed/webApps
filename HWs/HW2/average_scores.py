def compute_average_scores(scores: list[list[float]]) -> list[float]:
    studentsNumber = len(scores[0])
    sbjNumber = len(scores)
    avg = []
    
    for i in range(studentsNumber):
        studentSum = 0
        for j in range(sbjNumber):
            studentSum += scores[j][i]
        avg.append(studentSum / sbjNumber)
    
    return avg

if __name__ == "__main__":
    scores = [list(map(float, input().split())) for _ in range(int(input().split()[1]))]
    print("\n".join(list(map(str, compute_average_scores(scores)))))
