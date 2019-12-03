import torch.nn as nn
import torch.optim as optim
import torchvision
from torchvision import transforms
from collections import OrderedDict
from torch.autograd import Variable
from torchvision.datasets import ImageFolder
from model import vgg16
import torch
import numpy as np
import sys
import matplotlib.pyplot as plt
from model import vgg16
import cv2


use_cuda = torch.cuda.is_available()

net = vgg16()
if use_cuda:
	net = net.cuda()
net.load_state_dict(torch.load('vgg16.pt'))
net.eval()
criterion = nn.CrossEntropyLoss()
loss_list, acc_list = [], []


def test(image):
	h, w, c = image.shape
	transform1 = transforms.Compose([transforms.ToTensor(), ])
	images = transform1(image).view(1, c, h, w)
	print(images.numpy().shape)
	if use_cuda:
	 	images = images.cuda()
	print(images)
	output = net(images)
	pred = output.data.max(1)[1]
	print(pred.item())
	return pred
image = cv2.imread(sys.argv[1])
test(image)