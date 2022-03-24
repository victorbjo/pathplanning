from cmath import pi, sqrt
from dataclasses import replace
from glob import has_magic
import numpy as np
from typing import overload
import matplotlib.pyplot as plt
import shapely.geometry as geo
from scipy.stats import qmc
from sklearn.neighbors import NearestNeighbors
def halton(plot, polys):
    plot.set_title("Halton")
    halton_sampler = qmc.Halton(d=2)
    halton_samples = halton_sampler.random(n=75)
    halton_samples = qmc.scale(halton_samples, [0,0], [10,10])
    halton_samples = removeOverlaps(polys, halton_samples)
    #print(halton_samples)
    plot.scatter(halton_samples[:,0], halton_samples[:,1], s=100, alpha=0.5)
    findNeighbor(plot, halton_samples, polys)

def plotPolygons(plot, polys):
    for polygon in polys:
        x,y = polygon.exterior.xy
        plot.plot(x,y)

def removeOverlaps(polys, haltonPoints):
    newPoints = haltonPoints.tolist()
    for point in haltonPoints:
        geoPoint = geo.Point(point[0], point[1])
        overlap = False
        for x in range(len(polys[1:])):
            if geoPoint.within(polys[x+1]):
                overlap = True
                newPoints.remove([point[0],point[1]])
    haltonPoints = np.array(newPoints)
    return haltonPoints

def findNeighbor(plot, points, polys):
    nbrs = NearestNeighbors(n_neighbors=4, algorithm='ball_tree').fit(points)
    distances, indices = nbrs.kneighbors(points)
    for index in indices:
        point0 = geo.Point(points[index[0]])
        point1 = geo.Point(points[index[1]])
        point2 = geo.Point(points[index[2]])
        point3 = geo.Point(points[index[3]])
        line0 = geo.LineString([point0, point1])
        line1 = geo.LineString([point0, point2])
        line2 = geo.LineString([point0, point3])
        lines=[line0, line1, line2]
        for line in lines:
            intersect = False
            for x in range(len(polys)-1):
                if line.intersects(polys[x+1]):
                    intersect = True
                    #print(line.intersects(poly))
            if not intersect:
                plot.plot(*line.xy)
            



            

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
        polygon2 = geo.Polygon([(4,3),
                            (7,6),
                            (7,5),
                            ])
        self.polys = [self.map, polygon0, polygon1, polygon2]
    def plot(self):
        plotPolygons(self.mapPlot, self.polys)
    def drawHalton(self):
        halton(self.mapPlot, self.polys)

env = environment()
env.plot()
env.drawHalton()

plt.show()