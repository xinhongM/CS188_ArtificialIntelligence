# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2a():
    """
      Prefer the close exit (+1), risking the cliff (-10).
    """
    chosenDiscount = .8
    chosenNoise = 0
    chosenLivingReward = -4
    return chosenDiscount, chosenNoise, chosenLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2b():
    """
      Prefer the close exit (+1), but avoiding the cliff (-10).
    """
    chosenDiscount = .2
    chosenNoise = .21
    chosenLivingReward = .6
    return chosenDiscount, chosenNoise, chosenLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2c():
    """
      Prefer the distant exit (+10), risking the cliff (-10).
    """
    chosenDiscount = 1
    chosenNoise = 0
    chosenLivingReward = -1
    return chosenDiscount, chosenNoise, chosenLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2d():
    """
      Prefer the distant exit (+10), avoiding the cliff (-10).
    """
    chosenDiscount = .7
    chosenNoise = .4
    chosenLivingReward = 2
    return chosenDiscount, chosenNoise, chosenLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2e():
    """
      Avoid both exits and the cliff (so an episode should never terminate).
    """
    chosenDiscount = 0
    chosenNoise = 1
    chosenLivingReward = 0
    return chosenDiscount, chosenNoise, chosenLivingReward
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
