import matplotlib.pyplot as plt
import random
from scipy.stats import qmc

fig, (halton_axes) = plt.subplots(1)
halton_axes.set_title("Halton")
halton_sampler = qmc.Halton(d=2)
halton_samples = halton_sampler.random(n=200)
halton_samples = qmc.scale(halton_samples, [0,0], [10,10])
halton_axes.scatter(halton_samples[:,0], halton_samples[:,1], s=100, alpha=0.5)
plt.show()