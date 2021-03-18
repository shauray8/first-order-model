from setuptools import setup, find_packages

sys.path[0:0] = ['First Order Model']
#from version import __version__

setup(
  name = 'First Order Model',
  packages = find_packages(),
  #version = __version__,
  license='MIT',
  description = 'This repository contains the source code for the paper First Order Motion Model for Image Animation',
  author = 'Shauray Singh',
  author_email = 'shauray9@gmail.com',
  url = 'https://github.com/shauray8/first-order-model',
  keywords = ['generative adversarial networks', 'machine learning'],
  install_requires=[
      'numpy',
      'tqdm',
      'torch',
      'torchvision',
      'pillow',
  ],
)

