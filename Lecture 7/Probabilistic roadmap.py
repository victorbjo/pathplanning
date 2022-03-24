import matplotlib.pyplot as plt
import shapely.geometry as geo
map = geo.Polygon([(0,10),
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

polys = [map, polygon0, polygon1]
for polygon in polys:
    x,y = polygon.exterior.xy
    plt.plot(x,y)
plt.show()