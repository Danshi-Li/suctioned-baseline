import numpy as np


INTRINSICS = np.array([
            [
                [455.209, 0.0,     317.772],
                [0.0    , 454.941, 179.729],
                [0.0    , 0.0,     1.0    ] # left
            ],
            [
                [455.449, 0.0,     319.373],
                [0.0    , 454.540, 180.585],
                [0.0    , 0.0,     1.0    ] # right
            ]
        ])

EXTRINSICS = self.poses_ori = np.array(
            [[[-0.3506,   -0.6968,    0.6257,  0.4617873],
              [ 0.9308,   -0.1859,    0.3146,  0.1960991],
              [-0.1029,    0.6928,    0.7138,  0.4683795],
              [ 0.    ,    0.    ,    0.    ,  1.        ]], # left

             [[ 0.3849,    0.6775,   -0.6267,   -0.471459 ],
              [-0.9181,    0.2113,   -0.3354,   -0.1985267],
              [-0.0948,    0.7045,    0.7033,   0.4687329],
              [ 0.    ,    0.    ,    0.    ,   1.       ]]] # right
        ) # hard code