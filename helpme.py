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
        
def above_below_classify(grade):
    """
    Function to classify students into above avg or below avg
    """
    if grade >= 12:
        return 1
    else:
        return 0

