import numpy
import torch
import torchvision

print("Torch:", torch.__version__)
print("Torchvision:", torchvision.__version__)
print("Numpy:", numpy.__version__)

try:
    import torchcam

    print("TorchCAM:", torchcam.__version__)
except ImportError:
    print("TorchCAM: not installed (optional)")
