import statistics

dataSet = {}
with open("students.txt", "r", encoding="utf-8") as studentsFile:
    for line in studentsFile:
        name, scores = line.split()
        grades = list(map(int, scores.split(',')))
        dataSet[name] = grades

averPersonalScore = {}
allGrades = []
for name, scores in dataSet.items():
    averPersonalScore[name] = sum(scores) / len(scores)
    allGrades += scores
minGrade = min(allGrades)
maxGrade = max(allGrades)
modeGrade = statistics.mode(allGrades)

with open("statisticinfo.txt", "w", encoding="utf-8") as file:
    for name, scores in averPersonalScore.items():
        file.write(f"{name}: {scores:.2f}\n")
    file.write(f"maxGrade: {maxGrade}\n")
    file.write(f"minGrade: {minGrade}\n")
    file.write(f"modeGrade: {modeGrade}\n")
