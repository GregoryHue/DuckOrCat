
<h1>Duck or Cat</h1>

Duck or Cat is a binary classification model. It classifies pictures of ducks and cats. 

<h1>Table of Contents</h1>

- [Content of this project](#content-of-this-project)
- [Dataset](#dataset)
- [The model](#the-model)
- [Result](#result)
- [Project setup](#project-setup)
  - [Install CUDA drivers on Windows 11:](#install-cuda-drivers-on-windows-11)
  - [Install CuDNN on WSL2:](#install-cudnn-on-wsl2)
  - [Install CUDA on WSL2:](#install-cuda-on-wsl2)
  - [Install Miniconda:](#install-miniconda)
  - [Disable Miniconda on start-up (optional):](#disable-miniconda-on-start-up-optional)
  - [Create a conda environement:](#create-a-conda-environement)
  - [Install librairies:](#install-librairies)
- [Usage](#usage)
  - [Scrapy](#scrapy)
  - [Jupyter](#jupyter)
  - [Flask](#flask)
- [Versions](#versions)
- [Structure](#structure)
- [References](#references)

# Content of this project

This project is split into 3 differents folders:

- `scrapy`: Scrapy project that helps with the creation of a dataset. It massively download pictures of cats and ducks.
- `jupyter`: Jupyter project that trains and validates the model.
- `flask`: Flask project that alows the user to try the model.

# Dataset

The balance of the dataset is the following:

* train: 9000 cats and 9000 ducks
* test: 2000 cats and 9000 ducks

# The model

The model is a CNN classification model, it has the following structure:

![Structure of the model](https://i.imgur.com/ebkMGGu.jpg)

# Result

Here is the evolution of the accuracy over 25 epochs:

![Accuracy and loss over epochs](https://github.com/GregoryHue/DuckOrCat/blob/main/flask/static/loss_and_acc.png)

Here is the predictions of cats and ducks:

![Cats](https://github.com/GregoryHue/DuckOrCat/blob/main/flask/static/cat_prediction.png?raw=true)
![Ducks](https://github.com/GregoryHue/DuckOrCat/blob/main/flask/static/duck_prediction.png?raw=true)

And here is the confusion matrix:

![Confusion matrix](https://github.com/GregoryHue/DuckOrCat/blob/main/flask/static/confusion_matrix.png?raw=true)

The model has an accuracy of 98.21%, ***which seems to be very different for the deployed model***.

# Project setup

## Install CUDA drivers on Windows 11:

[Here.](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local)

## Install CuDNN on WSL2:

Find the correct version of cuDNN [here](https://developer.nvidia.com/rdp/cudnn-download) then run:

```bash
wget https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.0/local_installers/12.x/cudnn-local-repo-ubuntu2204-8.9.0.131_1.0-1_amd64.deb/
sudo dpkg -i cudnn-local-repo-ubuntu2204-8.9.0.131_1.0-1_amd64.deb
sudo cp /var/cudnn-local-repo-ubuntu2204-8.9.0.131/cudnn-local-D7522631-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install libcudnn8 libcudnn8-dev
```

## Install CUDA on WSL2:

Delete the old key:

```bash
sudo apt-key del 7fa2af80
```

Find the correct version of CUDA [here](https://developer.nvidia.com/cuda-downloads) then run:

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
bsudo apt-get update
sudo apt-get -y install cuda
```

## Install Miniconda:

Get the correct version of Miniconda [here](https://docs.conda.io/en/latest/miniconda.html) and install it:

```bash
wget wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sudo bash Miniconda3-latest-Linux-x86_64.sh -p /usr/bin/miniconda3
```

## Disable Miniconda on start-up (optional):

Get into the Miniconda environement if you aren't already:

```bash
source /usr/bin/miniconda3/bin/activate
```

Turn off conda on start-up:
```bash
conda config --set auto_activate_base false
```

## Create a conda environement:

Get into the Miniconda environement if you aren't already:

```bash
source /usr/bin/miniconda3/bin/activate
```

Create a new conda environement:

```bash
conda create --name env python=3.9
```

## Install librairies:

Get in the environement:

```bash
conda activate env
```

Install cudatoolkit:

```bash
conda install -c conda-forge cudatoolkit=11.8.0
```

Install required librairies:
```bash
cd dev/DuckOrCat/ && pip install -r scrapy/requirements.txt
```

Set the path variables:
```bash
CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
```

# Usage

This project is supposed to be used in this order :

1. Scrapy to download/generate the dataset
2. Jupyter to create and train the model 
3. Flask to deploy the model in real conditions.

But since the model is already built and stored on github at `flask/static/model.h5`, it is possible to skip step 1 and 2.

## Scrapy

Get into the Miniconda environement if you aren't already:

```bash
source /usr/bin/miniconda3/bin/activate
```

To download picture of ducks or cats, get into the `scrapy/` folder and run:

```bash
scrapy crawl [duck|cat]
```

Some scripts are available in `scrapy/tools/`:

* `delete_duplicate.py`: delete every picture duplicates in the dataset folder.
* `rename.py`: rename every pictures of a folder following a pattern.
* `resize.py`: to save on storage and ressources during the training, resize every pictures to be a maximum of 1024 pixels of width and height.

To use any of them, get into the `scrapy/tools/` and run:

```bash
python3 [script_name]
```

## Jupyter

Get into the Miniconda environement if you aren't already:

```bash
source /usr/bin/miniconda3/bin/activate
```

To develop on the model, get into the `jupyter/` folder and run:

```bash
jupyter-lab
```

## Flask

Get into the Miniconda environement if you aren't already:

```bash
source /usr/bin/miniconda3/bin/activate
```

To develop the web interface, get into the `flask/` folder and run:

```bash
flask --app  main.py --debug run
```

If you want to run the production version on Docker instead, you can run:

```bash
docker build -f Dockerfile -t flask . && docker run -p 8000:8000 -it flask
```

Then open [http://localhost:8000/](http://localhost:8000/).

# Versions

* Windows 11 and WSL2 (Ubuntu 22.04.2 LTS)
* Python 3.9
* Flask 2.2.3
* Scrapy 2.7.1
* Tensorflow 2.12
* CUDA tool kit 11.8
* Docker version 20.10.24 (optional)

# Structure

```
flask/
scrapy/
jupyter/
env/
.gitignore
README.md
```

# References

* [Scrapy](https://scrapy.org/)
* [Item Pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html)
* [Pillow + scrapy = sometimes cannot identify image file](https://stackoverflow.com/questions/30114305/pillow-scrapy-sometimes-cannot-identify-image-file)
* [Dst tensor is not initialized #38](https://github.com/aymericdamien/TensorFlow-Examples/issues/38)
* [Install Tensorflow/Keras in WSL2 for Windows with NVIDIA GPU](https://www.youtube.com/watch?v=0S81koZpwPA)
* [CUDA - Installation](https://www.tutorialspoint.com/cuda/cuda_installation.htm)
* [Image Recognition Guide](https://www.fritz.ai/image-recognition/)
* [Binary Classification](https://www.kaggle.com/code/ryanholbrook/binary-classification)
* [🐈🐕 Cat and Dog Classification](https://www.kaggle.com/code/gcdatkin/cat-and-dog-classification)
* [Keras CNN Dog or Cat Classification](https://www.kaggle.com/code/uysimty/keras-cnn-dog-or-cat-classification)
* [TF2 - Tutorials - Keras - Save and Restore Models](https://www.kaggle.com/code/vikramtiwari/tf2-tutorials-keras-save-and-restore-models)
* [How To Make a Web Application Using Flask in Python 3](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
* [How Can You Use TensorFlow with Docker?](https://www.run.ai/guides/tensorflow/tensorflow-with-docker)
