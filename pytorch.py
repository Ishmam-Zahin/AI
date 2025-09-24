import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from torchvision.models import vgg16, VGG16_Weights

model = vgg16(pretrained=True)
VGG16_Weights.DEFAULT