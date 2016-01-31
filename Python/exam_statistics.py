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

def grades_average(grades):
    total = grades_sum(grades)
    return total/float(len(grades))
# print grades_average(grades)

# -- Calculates the grade variance --

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance/len(scores)
print grades_variance(grades)

# -- Calculate Standard Deviation --

def grades_std_deviation(variance):
    return float(variance) ** 0.5

variance = grades_variance(grades)
print grades_std_deviation(variance)
