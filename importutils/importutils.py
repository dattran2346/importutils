import lazy_import as lazy

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

def lazily_module(name):
    module = lazy.lazy_module(name)
    try: 
        get_ipython().magic('aimport -%s' % name)
        print('Not autoreload %s' % name)
    except: pass
    return module

def lazily_class(name):
    module = lazy.lazy_class(name)
    try: 
        get_ipython().magic('aimport -%s' % name)
        print('Not autoreload %s' % name)
    except: pass
    return module

# lazy import neccsessary module
# torch = lazily_module('torch')
# nn = lazily_module('torch.nn')
# F = lazily_module('torch.nn.functional')
# init = lazily_module('torch.nn.init')
# models = lazily_module('torchvision.models')
# optim = lazily_module('torch.optim')
# torchvision = lazily_module('torchvision')
# Dataset = lazily_class('torch.utils.data.Dataset')
# DataLoader = lazily_class('torch.utils.data.DataLoader')

plt = lazily_module('matplotlib.pyplot')  
np = lazily_module('numpy')
# pd = lazily_module('pandas')
cv2 = lazily_module('cv2')
Image = lazily_module('PIL.Image')

# builtin lib > import anyway
os = lazily_module('os')
shutil = lazily_module('shutil')
sys = lazily_module('sys')
glob = lazily_module('glob')
random = lazily_module('random')
pickle = lazily_module('pickle')
Path = lazily_class('pathlib.Path')
datetime = lazily_module('datetime')
time = lazily_module('time')



# run default ipython magic
# env = get_env_name()
# if env != "Script":
#     ipython = get_ipython()
#     ipython.magic('reload_ext autoreload')
#     # ipython.run_cell_magic('reload_ext', 'autoreload')
#     ipython.magic('autoreload 2')
#     # ipython.run_cell_magic('autoreload', '2')

#     if env == 'Jupyter':
#         ipython.magic('matplotlib inline')
#     else:
#         ipython.magic('matplotlib tk')