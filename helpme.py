def classify_student_performance(grade):
    """
    Function to classify students into classes (Good, Average, and Poor) based on performance
    """
    if grade >= 15:
        return 2
    elif grade <= 9:
        return 0
    else:
        return 1
