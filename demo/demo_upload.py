# This is a simple Demo which includes training a simple model and using checkpoint manager
import torch
import torch.nn as nn
import torch.optim as optim
from do_spaces_checkpoint_connector import CheckpointManager
import torchvision.models as models

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(2, 2)

    def forward(self, x):
        return self.fc(x)
    

# Example usage
if __name__ == "__main__":

    # Initialize the model and optimizer
    model = models.resnet18(pretrained=False)
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Define loss function
    criterion = nn.MSELoss()

    # Initialize CheckpointManager 
    region_name = "ny3"
    endpoint_url = 'https://paperspace-test.nyc3.digitaloceanspaces.com'
    space_name = "checkpoint"
    manager = CheckpointManager(region_name, endpoint_url, space_name, model, optimizer )

    # checkpoint name
    name = 'test'

    # Dummy training loop
    num_epochs = 5
    for epoch in range(num_epochs):
        # Dummy data
        inputs = torch.randn(10, 3, 224, 224)
        targets = torch.randn(10, 1000)
        
        # Zero the gradients
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(inputs)
        loss = nn.MSELoss()(outputs, targets)
        
        # Backward pass and optimize
        loss.backward()
        optimizer.step()
        
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
        
     
        # Save and upload checkpoint at the end of each epoch
        manager.save_and_upload(epoch+1, loss.item(), name)
    



