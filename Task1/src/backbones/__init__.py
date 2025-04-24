
from .resnet import r50, r101

def get_model(name, **kwargs):
    # resnet

    if  name == 'r50':
        return r50()
    elif name == 'r101':
        return r101()
    else:
        raise ValueError()

