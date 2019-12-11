#!/usr/bin/env python3

import os
import shutil

SRC = "visualisation.ref"
DEST = "ref"

delta = int(200. / 2800. * 1400.)

for i in range(11, 2001):
    idx = 20300 + (i - 11) * delta
    shutil.copy(SRC + os.sep + "surf_{}.dat".format(i), DEST + os.sep + "surf_{}.dat".format(idx))
