import random
import pylab

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    scores = []
    for i in xrange(numTrials):
        term1 = random.randrange(50, 81)
        term2 = random.randrange(60, 91)
        final = random.randrange(55, 96)
        scores.append(0.25 * term1 + 0.25 * term2 + 0.5 * final)
    return scores

def plotQuizzes():
    ntrials = 10000
    scores = generateScores(ntrials)
    pylab.figure()
    pylab.hist(scores, bins = 7)
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()