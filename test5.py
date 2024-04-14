import torch
from torch import nn
from torchvision import models

class VGGLoss_ESRGAN(nn.Module):
    def __init__(self):
        super().__init__()
        vgg19_model = models.vgg19(pretrained=True)
        # print(vgg19_model)
        self.vgg19_54 = nn.Sequential(*list(vgg19_model.features.children())[:35])
        self.criterion = nn.L1Loss()

    def forward(self, real, fake):
        return self.criterion(self.vgg19_54(real), self.vgg19_54(fake))

def main():
    vgg = VGGLoss_ESRGAN()
    x = torch.randn(1,3,256,256)
    y = torch.randn(1,3,256,256)
    m = vgg(x,y)
    print(m)

if __name__ == '__main__':
    main()