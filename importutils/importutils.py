# Import torch
import lazy_import as lazy

def lazily(name):
    return lazy.lazy_module(name)

# lazy import neccessary module
torch = lazily('torch')
nn = lazily('torch.nn')
F = lazily('torch.nn.functional')
init = lazily('torch.nn.init')
models = lazily('torchvision.models')
optim = lazily('torch.optim')
torchvision = lazily('torchvision')
# Dataset = lazily('torch.utils.data.Dataset')
# DataLoader = lazily('torch.utils.data.DataLoader')

plt = lazily('matplotlib.pyplot')  
np = lazily('numpy')
pd = lazily('pandas')
cv2 = lazily('cv2')
Image = lazily('PIL.Image')

os = lazily('os')
shutil = lazily('shutil')
sys = lazily('sys')
glob = lazily('glob')
random = lazily('random')
pickle = lazily('pickle')
Path = lazily('pathlib.Path')
datetime = lazily('datetime')
time = lazily('time')


# ipython magic
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