# Exercise 1 – Course Duration Analysis
# You are given data about the duration of various online courses (in hours). The current course has a duration of 1.5 hours,
# while other courses range from a minimum of 2.5h to a maximum of 7h, with an average of 4h.

# a) Calculate the percentage difference between the current course and:

# The fastest (shortest) course among the others
# The slowest (longest) course among the others
# The average duration of all other courses

# b) Calculate the percentage of unusable/filler material reduced when comparing:

# The average of the other courses vs. the current course
# The current course itself (as a self-referential baseline)

# c) If a student watches 10 hours of this course, 
# how many hours of any other course would that be equivalent to? And conversely, how many hours of this course equal 10 hours of another course?

course1 = 7
course2 = 2.5
courseAverage = 4
currentCourse = 1.5
#a)
diffFastest = ((currentCourse - course2) / course2) * 100
diffSlowest = ((currentCourse - course1) / course1) * 100
diffAverage = ((currentCourse - courseAverage) / courseAverage) * 100
print("Percentage difference between current course and fastest course: ", f"{diffFastest:.2f}", "%")
print("Percentage difference between current course and slowest course: ", f"{diffSlowest:.2f}", "%")
print("Percentage difference between current course and average course: ", f"{diffAverage:.2f}", "%")
#b)
noEditOtherCourses = 5
noEditCurrentCourse = 3.5
reductionOtherCourses = 100 -( courseAverage * 100) / noEditOtherCourses
reductionCurrentCourse = 100 -( currentCourse* 100) / noEditCurrentCourse 
print("Percentage of unusable/filler material reduced when comparing the average of the other courses: ", f"{reductionOtherCourses:.2f}", "%")
print("Percentage of unusable/filler material reduced when comparing the current course itself (as a self-referential baseline): ", f"{reductionCurrentCourse:.2f}", "%")
#c)
currentCourseHours = 10 * 100 / currentCourse
otherCoursehours = courseAverage * currentCourseHours / 100
print("If a student watches 10 hours of this course, it would be equivalent to ", f"{otherCoursehours:.2f}", " hours of any other course.")
otherCourseHours = 10 * 100 / courseAverage
currentCourseHours = currentCourse * otherCourseHours / 100
print("Conversely, how many hours of this course equal 10 hours of another course: ", f"{currentCourseHours:.2f}", " hours of this course.")