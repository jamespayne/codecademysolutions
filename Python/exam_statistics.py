grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# --Print all the grades--

def print_grades(grades):
    for grade in grades:
        print grade

# print_grades(grades)

# --Get the sum of the grades/scores--

def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total
# print grades_sum(grades)
