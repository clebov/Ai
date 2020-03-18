import torch
from torch.autograd.variable import Variable
from torch.nn.functional import binary_cross_entropy_with_logits as bce_loss
dtype = torch.cuda.FloatTensor

def discriminator_loss(logits_real, logits_fake):
    """
    Computes the discriminator loss.
    
    You should use the stable torch.nn.functional.binary_cross_entropy_with_logits 
    loss rather than using a separate softmax function followed by the binary cross
    entropy loss.
    
    Inputs:
    - logits_real: PyTorch Tensor of shape (N,) giving scores for the real data.
    - logits_fake: PyTorch Tensor of shape (N,) giving scores for the fake data.
    
    Returns:
    - loss: PyTorch Tensor containing (scalar) the loss for the discriminator.
    """
    
    loss = None
    
    ####################################
    #          YOUR CODE HERE          #
    ####################################
    N = logits_real.size()
    true_labels = Variable(torch.ones(N)).type(dtype)
    real_image_loss = bce_loss(logits_real, true_labels)
    fake_image_loss = bce_loss(logits_fake, 1 - true_labels)
    
    loss = real_image_loss + fake_image_loss
    
    ##########       END      ##########
    
    return loss

def generator_loss(logits_fake):
    """
    Computes the generator loss.
    
    You should use the stable torch.nn.functional.binary_cross_entropy_with_logits 
    loss rather than using a separate softmax function followed by the binary cross
    entropy loss.

    Inputs:
    - logits_fake: PyTorch Tensor of shape (N,) giving scores for the fake data.
    
    Returns:
    - loss: PyTorch Tensor containing the (scalar) loss for the generator.
    """
    
    loss = None
    
    ####################################
    #          YOUR CODE HERE          #
    ####################################
    N = logits_fake.size()
    true_labels = Variable(torch.ones(N)).type(dtype)
    loss = bce_loss(logits_fake, true_labels)
    
    ##########       END      ##########
    
    return loss


def ls_discriminator_loss(scores_real, scores_fake):
    """
    Compute the Least-Squares GAN loss for the discriminator.
    
    Inputs:
    - scores_real: PyTorch Tensor of shape (N,) giving scores for the real data.
    - scores_fake: PyTorch Tensor of shape (N,) giving scores for the fake data.
    
    Outputs:
    - loss: A PyTorch Tensor containing the loss.
    """
    
    loss = None
    
    ####################################
    #          YOUR CODE HERE          #
    ####################################
    N = scores_real.size()
    loss_real = 0.5*torch.mean(torch.pow(scores_real-Variable(torch.ones(N)).type(dtype), 2))
    loss_fake = 0.5*torch.mean(torch.pow(scores_fake, 2))
    loss = loss_real + loss_fake
    
    ##########       END      ##########
    
    return loss

def ls_generator_loss(scores_fake):
    """
    Computes the Least-Squares GAN loss for the generator.
    
    Inputs:
    - scores_fake: PyTorch Tensor of shape (N,) giving scores for the fake data.
    
    Outputs:
    - loss: A PyTorch Tensor containing the loss.
    """
    
    loss = None
    
    ####################################
    #          YOUR CODE HERE          #
    ####################################
    N = scores_fake.size()
    loss = 0.5*torch.mean(torch.pow(scores_fake-Variable(torch.ones(N)).type(dtype), 2))
    return loss
    
    ##########       END      ##########
    
    return loss
