import random
import plotly.figure_factory as ff

dice_result = []
count = []

for i in range(0, 100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    sum = dice1 + dice2

    dice_result.append(sum)
    count.append(i)

fig = ff.create_distplot([dice_result], ["result"])
fig.show()