import torch
import torch.nn as nn
import torch.optim as optim
from do_spaces_checkpoint_connector import CheckpointManager
import torchvision.models as models
import os



# Example usage
if __name__ == "__main__":

    region_name = "ny3"
    endpoint_url = 'https://paperspace-test.nyc3.digitaloceanspaces.com'
    space_name = "checkpoint"
    model = models.resnet18(pretrained=False)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    manager = CheckpointManager(region_name, endpoint_url, space_name, model, optimizer)
    name = 'test'
    epoch = 5
    start_epoch, loss = manager.download_and_load(name, epoch)
    print(f'Loaded checkpoint from epoch {start_epoch} with loss {loss}')


    # # Set model to evaluation mode and use it for inference
    model.eval()
    inputs = torch.randn(10, 3, 224, 224)
    outputs = model(inputs)
    print('Inference done in evaluation mode.')


    # Set model back to training mode to continue training
    model.train()
    inputs = torch.randn(10, 3, 224, 224)
    targets = torch.randn(10, 1000)
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = nn.MSELoss()(outputs, targets)
    loss.backward()
    optimizer.step()
    print('Training continued.')







