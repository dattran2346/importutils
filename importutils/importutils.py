# Import torch
try:
    import torch
    from torch import nn
    from torch.nn import init
    import torch.nn.functional as F
    from torchvision.models import * # import all model
    from torch import optim
    from torch.utils.data import Dataset, DataLoader
    import torchvision
    from torchvision import transforms
    print('import torch and torchvision')
except:
    print('torch module not found ')


def get_env_name():
    try:
        cls = get_ipython().__class__.__name__
        if cls == 'ZMQInteractiveShell':
            return 'Jupyter'
        elif cls == 'TerminalInteractiveShell':
            return 'Terminal'
    except NameError:
        return "Script"

# run default ipython magic
env = get_env_name()
if env != "Script":
    ipython = get_ipython()
    ipython.magic('reload_ext autoreload')
    ipython.magic('autoreload 2')

    if env == 'Jupyter':
        ipython.magic('matplotlib inline')
    else:
        ipython.magic('matplotlib tk')

    
# Import matplotlib
try:
    import matplotlib.pyplot as plt
    print('import matplotlib.pyplot as plt')
except:
    print('matplotlib module not found')

# Import numpy
try:
    import numpy as np
    print('import numpy as np')
except:
    print('numpy module not found')

# Import pandas
try:
    import pandas as pd
    print('import pandas as pd')
except:
    print('pandas module not found')

# Import cv2
try:
    import cv2
    print('import cv2')
except:
    print('cv2 module not found')

try:
    from PIL import Image
    print('Import PIL')
except:
    print('PIL module not found')


# import default python library
import os
import sys
import glob
import random
import pickle
from pathlib import Path
import datetime
import time
import shutil