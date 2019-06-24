# A minimal package module to kick-start Deep Learning project

Deep Learning is fun, but developing it is quite intimidating, especially when you missed some package. I found myself have to go back and forth in a Jupyter Notebook to import yet another package I want to use. However, this approach has 2 drawbacks. First, this interrupts the thinking process, and second, import modules are scattered across the code, which made it's hard to manage. This project aims to provide a minimal set of packages to kickstart a new project.

### Installation

```
pip install importutils
```

### Usage

Squeeze all of these
```
import numpy as np
import pandas as pd
import whatsoever
```

Into a single line 
```
from importutils import *
```

## Include package

### Install package
- common pytorch module
- numpy as np
- pandas as pd
- matplotlib.pyplot as plt
- cv2
- PIL Image

### Default python package
- os
- sys
- glob
- random
- pickle
- pathlib.Path
- datetime
- time
- shutil

## Note

- This package is intented to use in development environment, do not include in your production.

- The above list is my common usage list, if you think what I might be missing, feel free to send a PR. Cheers :)


