from enum import Enum
import numpy as np
import matplotlib.pyplot as plt
from scr import FigureSupport as Fig
import scr.SamplePathClass as SamplePathSupport
import SamplePath as SamplePath

class FlipState(Enum):
    HEADS=1
    TAILS=2
    TWOTAILS=3
    WIN=4
# This is actually a Markov process model
# because you're either in the state where you just got heads and you need
# two tails then a heads to win or you're in the state where you just got
#one tails and you need one tails and one heads to win or you're in the state where
#you've gotten 2, 3, 4, etc. etc. tails in a row and you just need one heads to win
#and by extension start over.

class Game:
    def __init__(self, id, odds_heads):
        self._rnd=np.random
        self._rnd.seed(id)
        self.odds_heads=odds_heads
        self._wins=0
        self._flipstate=FlipState.HEADS

    def one_game(self):
        t=0
        while t<20:
            #This first one is the "heads" state. You need 2 tails followed by 1 heads to win
            #You either get heads and stay in the "heads" state or you get tails and then
            #move into the place where you need one more tails followed by a heads to win.
            if self._flipstate==FlipState.HEADS:
                if self._rnd.sample() < self.odds_heads:
                    self._flipstate=FlipState.HEADS
                else:
                    self._flipstate=FlipState.TAILS
            #This is the tails state. You've gotten one tails already and you need o
            #one more followed by a heads to win. If you flip heads on this one, you
            #move back to the previous "heads" state.
            elif self._flipstate==FlipState.TAILS:
                if self._rnd.sample() < self.odds_heads:
                    self._flipstate=FlipState.HEADS
                else:
                    self._flipstate=FlipState.TWOTAILS
            #This is the two tails flipstate. In this state you either flip heads (and win)
            #Or you flip tails and you've already got 2 tails built up so you stay in the
            #two tails state.
            elif self._flipstate==FlipState.TWOTAILS:
                if self._rnd.sample() < self.odds_heads:
                    self._flipstate=FlipState.WIN
                    self._wins+=1
                else:
                    self._flipstate=FlipState.TWOTAILS

            #Now imagine you've just won. Your flipstate is Win,
            # which is the same as the Heads flipstate so we're going to give it the same syntax
            #and push it back into the loop.
            elif self._flipstate==FlipState.WIN:
                if self._rnd.sample() < self.odds_heads:
                    self._flipstate=FlipState.HEADS
                else:
                    self._flipstate=FlipState.TAILS
            else:
                print (["Error at", t])
            t += 1

        ##we need to count the times that it gets tails, tails, heads in a 20 flip sequence
    def Get_x(self):
        return self._wins*100-250


class AllGames:
    def __init__(self, odds_heads, num_games):
        self.odds_heads=odds_heads
        self._num_games=num_games
        self._outcomes=[]
        self._losemoney = []

    def simulate(self):
        for i in range(self._num_games):
            game = Game(i, self.odds_heads)
            game.one_game()
            x=game.Get_x()
            self._outcomes.append(x)
        return CohortOutcomes(self)

    def get_average_x(self):
        return sum(self._outcomes)/self._num_games

    def get_num_games(self):
        return self._num_games

    def get_outcomes(self):
        return self._outcomes

    def LoseMoney(self):
        for i in len(self._outcomes):
            if (self._outcomes[i]<1):
                self._losemoney=1
            else:
                self._losemoney=0
        return self._losemoney

class CohortOutcomes:
    def __init(self, simulated_cohort):
        self._simulatedCohort=simulated_cohort

    #def get_sample_path(self):
     #   n_games=self._simulatedCohort.get_num_games()
      #  winnings=SamplePathSupport.SamplePathBatchUpdate("Amount of Winnings", 0, 0)

       # for obs in self._simulatedCohort.get_outcomes():
        #    winnings.record(time=obs, increment=1)

        #return winnings

