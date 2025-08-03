# Ash Bhuiyan                              07-19-2025
# Lab 8 - Computes grades from scores and student info and writes to grades.txt

def readStudents():
    students = {}
    with open("students.txt", 'r') as file:
        next(file)
        for line in file:
            sid, name = line.strip().split(", ")
            students[sid] = name
    return students

def readScores():

    scores = {}
    with open("scores.txt", 'r') as file:
        next(file)
        for line in file:
            sid, _, score = line.strip().split(", ")
            scores.setdefault(sid, []).append(int(score))
    return scores

def writeGrades(students, scores):
    with open("grades.txt", 'w') as file:
        file.write("Student ID,Name,Total Scores,Sum of All Scores,Score Average\n")
        for sid in students:
            student_scores = scores.get(sid, [])
            total = len(student_scores)
            total_sum = sum(student_scores)
            average = round(total_sum / total, 1) if total > 0 else 0
            file.write(f"{sid},{students[sid]},{total},{total_sum},{average}\n")

def main():
    
    students = readStudents()
    scores = readScores()
    writeGrades(students, scores)

if __name__ == "__main__":
    main()