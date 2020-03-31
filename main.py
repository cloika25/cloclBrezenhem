from core import *
import time
import matplotlib
from matplotlib.animation import FuncAnimation, ArtistAnimation
import numpy as np

image=prepare_image()


vertexes_catmul=np.array([[0.0,0.3],[0.1,0.1],[0.5,0.2], [0.7,0.4], [0.9,0.0], [1.,1.]])

derivatives=np.array([0,1,2, -1])


            #zero
digitals = [[np.array([[231.0, 75.0],[365.0, 81.0], [369.0, 201.0], [369.0, 275.0]]),
            np.array([[369.0, 275.0],[369.0, 349.0], [345.0, 447.0], [256.0, 446.0]]),
            np.array([[256.0, 446.0],[167.0, 445.0], [139.0, 358.0], [131.0, 258.0]]),
            np.array([[131.0, 258.0],[123.0, 158.0], [159.0, 84.0], [254.0, 47.0]])],
            #one
            [np.array([[255.0, 424.0],[254.0, 361.0], [256.0, 412.0], [255.0, 303.0]]),
            np.array([[255.0, 303.0],[254.0, 194.0], [254.0, 234.0], [253.0, 167.0]]),
            np.array([[253.0, 167.0],[252.0, 100.0], [256.0, 28.0], [243.0, 43.0]]),
            np.array([[243.0, 43.0],[230.0, 58.0], [226.0, 99.0], [138., 180.]])],
            #two
            [np.array([[373.0, 414.0], [327.0, 393.0], [104.0, 356.0], [120.0, 405.0]]),
             np.array([[120.0, 405.0], [136.0, 454.0], [312.0, 323.0], [336.0, 241.0]]),
             np.array([[336.0, 241.0], [360.0, 159.0], [334.0, 74.0], [271.0, 50.0]]),
             np.array([[271.0, 50.0], [208.0, 26.0], [152.0, 55.0], [104, 111]])]
            ]
vertexes_ermit = digitals[2]
#build_catmul_rom(vertexes_catmul, 200)
build_kasteljo(vertexes_ermit,200)
#build_ermit_spline(image, vertexes_ermit, derivatives, 200)