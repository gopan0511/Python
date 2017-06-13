def checkGrade(students):
	grades = []
	for student in students:
		grades.append(student[1])

	grades.sort()#on sorting we get the lowest grade in the beginning
	sort_grades = grades
	low_grade = sort_grades[0]#You obtain the lowest grade in the beginning(if there are no duplications) else you still obtain the lowest value and you can take that as a reference as the least value(in case of diplication)
	for grade in sort_grades:
		if grade != low_grade:
			low_grade = grade#To obtain the second lowest grade among the list and then it breaks
			break
	
	low_student = []
	for student in students:
		if student[1] == low_grade:
			low_student.append(student[0])

	low_student.sort()
	for name in low_student:
		print name


if __name__ == "__main__":#This is my way of using main function
	students = []
	N = input()
	for s in range(N):
		stud = [raw_input(),input()]#first field in the list is for name and second field is for marks.
		students.append(stud)#This makes a nested list like -> [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
	checkGrade(students)



