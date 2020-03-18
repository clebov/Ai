import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import ImageFolder
import numpy as np
from models import Discriminator, Generator
from utils import show_images
from train import train
from losses import discriminator_loss, generator_loss,ls_discriminator_loss,ls_generator_loss
import matplotlib.pyplot as plt

#%matplotlib inline
plt.rcParams['figure.figsize'] = (10.0, 8.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'
#%load_ext autoreload
#%autoreload 2


device = torch.device("cuda:0")
batch_size = 128
scale_size = 64 # We resize the images to 64x64 for training
NOISE_DIM = 100
NUM_EPOCHS = 50
learning_rate = 0.0002
celeba_root = 'celeb'

celeba_train = ImageFolder(root=celeba_root, transform=transforms.Compose([
transforms.Resize(scale_size),
transforms.ToTensor(),
]))


celeba_loader_train = DataLoader(celeba_train, batch_size=batch_size, drop_last=True)

imgs = celeba_loader_train.__iter__().next()[0].numpy().squeeze()
show_images(imgs, color=True)

# =============================================================================
print("Vanilla GAN")
D = Discriminator().to(device)
G = Generator(noise_dim=NOISE_DIM).to(device)
D_optimizer = torch.optim.Adam(D.parameters(), lr=learning_rate, betas = (0.5,
0.999))
G_optimizer = torch.optim.Adam(G.parameters(), lr=learning_rate, betas = (0.5,
0.999))
#original gan
train(D, G, D_optimizer, G_optimizer, discriminator_loss,
generator_loss, num_epochs=NUM_EPOCHS, show_every=250,
train_loader=celeba_loader_train, device=device)
# =============================================================================
torch.cuda.empty_cache()

# =============================================================================
# print("LSGAN")
# D = Discriminator().to(device)
# G = Generator(noise_dim=NOISE_DIM).to(device)
# D_optimizer = torch.optim.Adam(D.parameters(), lr=learning_rate, betas = (0.5,
# 0.999))
# G_optimizer = torch.optim.Adam(G.parameters(), lr=learning_rate, betas = (0.5,
# 0.999))
# # ls-gan
# train(D, G, D_optimizer, G_optimizer, ls_discriminator_loss,ls_generator_loss, num_epochs=NUM_EPOCHS, show_every=200,
# train_loader=celeba_loader_train, device=device)
# torch.cuda.empty_cache()
# =============================================================================
