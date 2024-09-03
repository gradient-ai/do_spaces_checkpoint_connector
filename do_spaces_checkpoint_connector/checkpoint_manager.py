import time
from .checkpoint_saver import CheckpointSaver
from .s3_uploader import S3Uploader
import os

class CheckpointManager:
    def __init__(self, region_name, endpoint_url, space_name, model, optimizer=None):
        self.saver = CheckpointSaver(model, optimizer)
        self.uploader = S3Uploader(region_name, endpoint_url, space_name)

    def save_and_upload(self, epoch, loss, name):
        file_name=  f'checkpoint_{name}_epoch_{epoch}.pth'
        local_filepath = '/tmp/checkpoint' + file_name
        self.saver.save_checkpoint(epoch, loss, local_filepath)
        print("saved checkpoint for epoch " + str(epoch))
        self.uploader.upload_in_background(file_name, local_filepath, epoch)
        
    def download_and_load(self, name, epoch):
        file_name=  f'checkpoint_{name}_epoch_{epoch}.pth'
        local_filepath = '/tmp/' + file_name
        self.uploader.download_from_s3(file_name)
        epoch, loss = self.saver.load_checkpoint(local_filepath)
        os.remove(local_filepath)
        return epoch, loss
    
    
    

