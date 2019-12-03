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

use_cuda = torch.cuda.is_available()


train_dataset = ImageFolder(
    root=(sys.argv[1] + '/train'),
    transform=transforms.ToTensor()
)
valid_dataset = ImageFolder(
    root=(sys.argv[1] + '/valid'),
    transform=transforms.ToTensor()
)
batch_size = 32
train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size = batch_size, shuffle = True
)
valid_loader = torch.utils.data.DataLoader(
    valid_dataset, batch_size = 1
)



net = vgg16(pretrained = False)
if use_cuda:
	net = net.cuda()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=1e-4)
loss_list, acc_list = [], []

def train(epoch):
	net.train()
	for i, (images, labels) in enumerate(train_loader):
		if use_cuda:
			images, labels = images.cuda(), labels.cuda()
		#print(images, labels)
		optimizer.zero_grad()

		output = net(images)

		loss = criterion(output, labels)

		#loss_list.append(loss.data[0])
        #batch_list.append(i+1)

		if i % 10 == 0:
			print('Train - Epoch %d, Batch: %d, Loss: %f' % (epoch, i, loss.data.item()))

		loss.backward()
		optimizer.step()
def valid():
	net.eval()
	total_correct = 0
	avg_loss = 0.0
	for i, (images, labels) in enumerate(valid_loader):
		if use_cuda:
		 	images, labels = images.cuda(), labels.cuda()
		output = net(images)
		pred = output.data.max(1)[1]
		total_correct += pred.eq(labels.data.view_as(pred)).sum()

	acc = float(total_correct) / len(valid_dataset)
	print('Accuracy: %f' % (float(total_correct) / len(valid_dataset)))
	acc_list.append(acc)
	'''
	#train_acc
	total_correct = 0
	avg_loss = 0.0

	for i, (images, labels) in enumerate(train_loader):
	    images, labels = Variable(images), Variable(labels)
	    output = net(images)
	    avg_loss += criterion(output, labels).sum()
	    pred = output.data.max(1)[1]
	    total_correct += pred.eq(labels.data.view_as(pred)).sum()

	avg_loss /= len(train_dataset)
	acc = float(total_correct) / len(train_dataset)
	print('Train Avg. Loss: %f, Accuracy: %f' % (avg_loss.data.item(), acc))
	acc_list.append(acc)
	loss_list.append(avg_loss.data.item())
	'''

def train_and_test(epoch):
	train(epoch)
	valid()

for e in range(1, 10):
	train_and_test(e)
torch.save(net.state_dict(), 'vgg16_1.pt')
epoch_list = list(range(1, 5))

'''
def plotData(plt, x_data, y_data, y_label):
  x = [p for p in x_data]
  y = [q for q in y_data]
  plt.title('Learning Curve')
  plt.xlabel('Epoch')
  plt.ylabel(y_label)
  plt.plot(x, y, '-o')
  plt.show()
plotData(plt, epoch_list, acc_list, 'Training accuracy')
plotData(plt, epoch_list, loss_list, 'Training loss')
'''
