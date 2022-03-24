import matplotlib.pyplot as plt
import shapely.geometry as geo
from scipy.stats import qmc

def halton(plot):
    plot.set_title("Halton")
    halton_sampler = qmc.Halton(d=2)
    halton_samples = halton_sampler.random(n=200)
    halton_samples = qmc.scale(halton_samples, [0,0], [10,10])
    plot.scatter(halton_samples[:,0], halton_samples[:,1], s=100, alpha=0.5)

def plotPolygons(polys, plot):
    for polygon in polys:
        x,y = polygon.exterior.xy
        plot.plot(x,y)

class environment:
    def __init__(self):
        fig, (self.mapPlot) = plt.subplots(1)
        self.map = geo.Polygon([(0,10),
                            (0,0),
                            (10,0),
                            (10, 10),
                            ])
        polygon0 = geo.Polygon([(3,5),
                            (1,1),
                            (3,2),
                            ])
        polygon1 = geo.Polygon([(4,6),
                            (7,8),
                            (9,9),
                            (3, 7),
                            ])
        self.polys = [self.map, polygon0, polygon1]
    def plot(self):
        plotPolygons(self.polys ,self.mapPlot)
    def drawHalton(self):
        halton(self.mapPlot)

env = environment()
env.plot()
env.drawHalton()

plt.show()