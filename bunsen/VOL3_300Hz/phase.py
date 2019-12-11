#!/usr/bin/env python3

import os
import shutil

SRC = "visualisation.ref"
DEST = "ref"

delta = int(300. / 2800. * 700.)

for i in range(2, 2001):
    idx = 20650 + (i - 2) * delta
    shutil.copy(SRC + os.sep + "surf_{}.dat".format(i), DEST + os.sep + "surf_{}.dat".format(idx))
