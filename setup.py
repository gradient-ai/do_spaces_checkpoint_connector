from setuptools import setup, find_packages

setup(
    name='do_spaces_checkpoint_connector',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch',
        'boto3'
    ],
    author='Jason Peng',
    author_email='ypeng@digitalocean.com',
    description='A package to save PyTorch checkpoints and upload to DO Spaces asynchronously',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gradient-ai/do_spaces_checkpoint_connector',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
