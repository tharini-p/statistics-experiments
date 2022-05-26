#import packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from wand.image import Image
from wand.display import display
%matplotlib notebook

# 10000 simulations of die roll
n = 10000

#averages of die rolls
avg = []
for i in range(2,n):
    a = np.random.randint(1,7,i)
    avg.append(np.average(a))

def clt(current):
    plt.cla()
    if current == n:
        a.event_source.stop()

    plt.hist(avg[0:current])

    plt.gca().set_title('Expected value of die rolls')
    plt.gca().set_xlabel('Average of die rolls')
    plt.gca().set_ylabel('Frequency of rolls')

    plt.annotate('Die roll = {}'.format(current), [3,27])

#animation
fig = plt.figure()
a = animation.FuncAnimation(fig, clt, interval=1)

#save animation as gif
a.save('C:/Users/Desktop/statistics-experiments/clt-die-roll.gif', writer='imagemagick', fps=10)