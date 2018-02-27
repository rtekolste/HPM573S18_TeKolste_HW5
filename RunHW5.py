import HW5
import scr.FigureSupport as Fig

MySimulation=HW5.AllGames(odds_heads=.5, num_games=1000)
y=MySimulation.simulate()

#SamplePathSupport.graph_sample_path(
 #   sample_path=cohortoutcomes.get_sample_path(),
  #  title="Winnings Curve",
   # x_label="Amount Won",
    #y_label="Number of Times Won")

Fig.graph_histogram(
    observations=y.get_outcomes(),
    title ="Histogram of Patients",
    x_label="Amount Won",
    y_label="Number of Times Won")

##ANSWER TO QUESTION ONE:
#The minimum is -250 because that's what you pay to play. So if you win 0 times, you get $-250
#The maximum is $350 because the max times you can get the winning combination for
# 20 flips is 6 times so you can win $600 - $250 to play = $350

##Answer to QUESTION TWO:
print(y._losemoney/1000)



