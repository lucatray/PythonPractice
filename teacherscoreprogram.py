def main():

    list_of_scores = get_scores()

    total_of_scores = total_scores(list_of_scores)

    lowest = min(list_of_scores)

    new_total = total_of_scores - lowest

    average = new_total / (len(list_of_scores) - 1)

    print('The average of these scores after moving the '
          'lowest is: ', format(average, '.2f'), sep='')

def get_scores():

    another = 'yes'

    scores = []

    while another == 'yes':

        test_score = float(input('Please enter the score (out of 100): '))

        scores.append(test_score)

        another = str(input('Would you like to add another score (yes or no): '))

    print('This is the list of scores: ', scores)

    return scores


def total_scores(list_of_scores):

    total = 0.0

    for num in list_of_scores:

        total += num

    print('This is the total of the scores:', total)

    return total




main()