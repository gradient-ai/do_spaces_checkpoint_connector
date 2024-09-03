import torch

class CheckpointSaver:
    def __init__(self, model, optimizer=None):
        self.model = model
        self.optimizer = optimizer

    def save_checkpoint(self, epoch, loss, file_path):
        checkpoint = {
            'epoch': epoch,
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict() if self.optimizer else None,
            'loss': loss,
        }
        torch.save(checkpoint, file_path)


    def load_checkpoint(self, filepath):
        checkpoint = torch.load(filepath)
        self.model.load_state_dict(checkpoint['model_state_dict'])
        if self.optimizer and checkpoint['optimizer_state_dict']:
            self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        return checkpoint['epoch'], checkpoint['loss']
