# DigitalOcean Spaces Checkpoint Connector

A package that offers the following features:
- to save PyTorch checkpoints and upload to DO Spaces asynchronously.
- to load PyTorch checkpoints from DO Spaces


## Pre-requisite
- A DigitalOcean account with access to [DigitalOcean Spaces](https://www.digitalocean.com/products/spaces)
- Create Spaces Bucket - Instructions [here](https://docs.digitalocean.com/products/spaces/how-to/create/#:~:text=You%20can%20create%20a%20bucket,Create%20a%20Spaces%20Bucket%20page)
- An environment with Python 3.10+ with pip installed.
- Obtain Spaces Key for API Access (Access Key and Access Secret)

## Pre-setup (required step)
- Download this connector from GitHub using `git clone`
- Run `pip install -e .` within the directory where setup.py is
- Set environment variables **SPACES_KEY** and **SPACES_SECRET** in your current environment. Replace **XXXX** and **YYYY** with your **SPACES_KEY** and **SPACES_SECRET**:
```
export SPACES_KEY=XXXX
export SPACES_SECRET=YYYY
```

## Upload Pytorch checkpoints to DO Spaces
- Open **demo_upload.py** in demo directory and edit the following lines:
    - Edit line 29-31 **region_name, endpoint_url, and spaces_name** for your DO Spaces Storage. For **spaces_name**, it is the directory hame which you wish to store the checkpoints within your bucket.
    - Edit line 35 for the checkpoint file name. For example, if I name it as "test", then the filename would be checkpoint_test_epoch_x.pth, where x is the number of epoch.
- Run `python3 demo_upload.py`
- Wait for a few minutes, the terminal should print someething similar as below:
```
Epoch [1/5], Loss: 1.2148
saved checkpoint for epoch 1
process started
Epoch [2/5], Loss: 1.1188
saved checkpoint for epoch 2
process started
Epoch [3/5], Loss: 1.1260
saved checkpoint for epoch 3
process started
Epoch [4/5], Loss: 1.1074
saved checkpoint for epoch 4
process started
Epoch [5/5], Loss: 1.1166
saved checkpoint for epoch 5
process started
upload done for epoch 5
upload done for epoch 2
upload done for epoch 4
upload done for epoch 3
upload done for epoch 1
```
- Go to DO Spaces and you should see the checkpoints are there.
- Go to /tmp directory and you should see all the .pth files have been removed.


## Download Pytorch checkpoints from DO Spaces
- Note that it is required to run **demo_upload.py** before proceeding this step.
- Open **demo_download.py** in demo directory and edit the following lines:
    - Edit line 10-12 **region_name, endpoint_url, and spaces_name** for your DO Spaces Storage. For **spaces_name**, it is the directory hame which you stored the previous checkpoints within your bucket.
    - Notice that line 13 & 14 is filled out for you and it matches the demo_upload.py **model and optimizer**. The model and optimizer needs to match what's used in the checkpoints that were previously uploaded.
- Run `python3 demo_download.py`
- The terminal should print someething similar as below:
```
Loaded checkpoint from epoch 5 with loss 1.1410622596740723
Inference done in evaluation mode.
Training continued.
```

## Contributing Guidelines
- We welcome any contributes to this project. Feel free to issue pull request and we will review them.
- For any issues or concerns, please raise a GitHub Issue.
- This connector is still under development. It is your responsibility to review and test for production environment usages.

