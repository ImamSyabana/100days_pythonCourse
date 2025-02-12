# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again."}
#
# # cara manggil dictionary
# print(programming_dictionary["Bug"])
#
# # cara nambahin dictionary
# programming_dictionary["loop"] = "Di dunia programming ini maksudnya adalah mengeksekusi kode berulang-ulang"
#
# print(programming_dictionary)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for x in student_scores:

    if student_scores[x] >= 91 and student_scores[x] <= 100:
        student_grades[x] = "Outstanding"
    elif student_scores[x] >= 81 and student_scores[x] <= 90:
        student_grades[x] = "Exceeds Expectations"
    elif student_scores[x] >= 71 and student_scores[x] <= 80:
        student_grades[x] = "Acceptable"
    else:
        student_grades[x] = "Fail"


