import boto3
import multiprocessing
import os


class S3Uploader:
    def __init__(self, region_name, endpoint_url, space_name):
        self.endpoint_url =endpoint_url
        self.region_name = region_name
        self.aws_access_key_id=os.getenv('SPACES_KEY')
        self.aws_secret_access_key=os.getenv('SPACES_SECRET')
        self.space_name = space_name
    

    def upload_to_s3(self, filename, local_filepath, epoch):
        session = boto3.session.Session()
        s3_client = session.client('s3', region_name=self.region_name, endpoint_url=self.endpoint_url, aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key)
        s3_client.upload_file(local_filepath, self.space_name, filename)
        os.remove(local_filepath)
        print("upload done for epoch " + str(epoch))

    def download_from_s3(self, filename):
        session = boto3.session.Session()
        s3_client = session.client('s3', region_name=self.region_name, endpoint_url=self.endpoint_url, aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key)
        local_filepath = '/tmp/' + filename
        s3_client.download_file(self.space_name, filename, local_filepath)
        print("download complete")


    def upload_in_background(self, filename, local_filepath, epoch):
        process = multiprocessing.Process(target=self.upload_to_s3, args=(filename, local_filepath, epoch))
        process.start()
        print("process started")
        
