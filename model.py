import torch.nn as nn
from torchvision import models

class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        self.feature_extractor = models.vgg16(pretrained = True).features
        self.classifier = nn.Sequential(
                nn.Linear(25088, 4096, bias = True),
                nn.ReLU(inplace = True),
                nn.Linear(4096, 4096, bias = True),
                nn.ReLU(inplace = True),
                nn.Linear(4096, 3, bias = True)
                )
        
    def forward(self, x):
        features = self.feature_extractor(x)
        features = features.view(features.shape[0], -1)
        return self.classifier(features)
def vgg16(pretrained=False, **kwargs):
    """VGG 16-layer model (configuration "D")
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = Network()
    return model
