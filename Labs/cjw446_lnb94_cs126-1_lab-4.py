# Lab 4 Grade Calculator
# Carter Wrobel, Laura Ball
# cjw446, lnb94
# 10/9/17
# Section 1


def main():
    # Homework functions are defined here and the variables for the homework score
    homework_weight = .20
    homework_scores = [39, 40, 29, 40, 0, 5]
    homework_max = [40, 40, 40, 40, 40, 5]
    homework_total = sum(homework_scores)
    homework_total_max = sum(homework_max)
    total_homework_score = round(average(homework_total, homework_total_max))
    percent_total_homework_score = total_homework_score/100
    weighted_total_homework = round(average_weighted(homework_total, homework_total_max, homework_weight),2)

    # Quiz functions are defined here and the vaibles for the quiz score
    quiz_weight = .20
    quiz_scores = [10, 10, 9, 2, 10, 10, 10]
    quiz_max = [10, 10, 10, 10, 10, 10, 10]
    quiz_total = sum(quiz_scores)
    quiz_total_max = sum(quiz_max)
    total_quiz_score = round(average(quiz_total , quiz_total_max))
    percent_total_quiz_score = total_quiz_score/100
    weighted_total_quiz = round(average_weighted(quiz_total, quiz_total_max, quiz_weight),2)
    
    # Test functions are definered here and the variables for the qiiz score
    test_weight = .60
    test_scores = [293, 284, 300]
    test_max = [300, 300, 300]
    test_total = sum(test_scores)
    test_total_max = sum(test_max)
    total_test_score = round(average(test_total, test_total_max))
    percent_total_test_score = total_test_score/100
    weighted_total_test_score = round(average_weighted(test_total, test_total_max, test_weight),2)
    
    # Total Grade scores and functions are defined here
    sum_total_scores = (total_homework_score + total_test_score + total_quiz_score)/3
    final_score = round(average(sum_total_scores,100))
    percent_final_score = final_score/100
    weighted_total = round((weighted_total_homework + weighted_total_quiz + weighted_total_test_score)*100)
    percent_weighted_total = weighted_total/100

    # The answers to each of the functions will be printed out here
    print ("Homework Grade:" , total_homework_score , ":" , letter_grade(percent_total_homework_score))
    print("Quiz Grade:" , total_quiz_score  , ":" , letter_grade(percent_total_quiz_score))
    print("Test Grade:" , total_test_score , ":"  , letter_grade(percent_total_test_score))
    # print("Final Score Unweighted:" , final_score  , ":" , letter_grade(percent_final_score))
    print ("Final Score:", weighted_total, ":", letter_grade(percent_weighted_total))
# The average function takes the total scores acheived and divides it by the
# total score possible to get the grade as a percentage
def average(score_list, max_list):
    avg = (score_list / max_list) * 100
    return avg

# The letter_grade function takes the scores of each and converts the percentage
# to an actaul letter grade to be printed out
def letter_grade(percent):
    if (percent <= 1 and percent >= .90):
        return "A"
    elif (percent < .9 and percent >=.80):
        return "B"
    elif (percent < .8 and percent >=.7):
        return "C"
    elif (percent < .7 and percent >=.6):
        return "D"
    else:
        return "F"

# The average_weighted function takes the weight percentage of each function
# and then spits out the weighted percent of it which will be added later to
# give the final grade total
def average_weighted(score_list, max_list, weight):
    avg_weighted = (score_list / max_list) * (weight)
    return avg_weighted

print (main())







