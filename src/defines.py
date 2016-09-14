#!/usr/bin/env python
# -*- coding: ascii -*-
"""defines.py - this file contains meta data and program parameters"""

# Meta data
__author__ = "Nicolai Spicher"
__credits__ = ["Nicolai Spicher", "Stefan Maderwald", "Markus Kukuk", "Mark E. Ladd"]
__license__ = "GPL v3"
__version__ = "v0.1-beta"
__maintainer__ = "Nicolai Spicher"
__email__ = "nicolai[dot]spicher[at]fh-dortmund[dot]de"
__status__ = "Beta"
__url__ = "https://github.com/nspi/vbcg"
__description__ = "A real-time application for video-based estimation of the heart rate" \
                  " frequency and the phase of the cardiac cycle."

# Indices of parameters
IDX_WEBCAM = 0
IDX_CAMERA = 1
IDX_ALGORITHM = 2
IDX_CURVES = 3
IDX_FRAMES = 4
IDX_FACE = 5
IDX_FPS = 6
IDX_COLORCHANNEL = 7
IDX_ZERO_PADDING = 8
IDX_TRIGGER = 9

# Standard values of parameters
VAL_WEBCAM = 1
VAL_CAMERA = 1
VAL_ALGORITHM = 0
VAL_CURVES = 1
VAL_FRAMES = 0
VAL_FACE = 0
VAL_FPS = 25
VAL_COLORCHANNEL = 1
VAL_ZERO_PADDING = 1
VAL_TRIGGER = 1

# Labels of algorithms in GUI
LABEL_ALGORITHM_1 = "Estimate HR"
LABEL_ALGORITHM_2 = "Filter signal"
LABEL_ALGORITHM_3 = "Trigger MRI"
