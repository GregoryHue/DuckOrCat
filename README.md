# DuckOrCat

Duck or Cat is a binary classification model. It classifies pictures of ducks and cats. A Scrapy project is available to download picture for your dataset and modify them if needed.

## Project setup

### Miniconda installation:

Get the correct version of Miniconda [here](https://docs.conda.io/en/latest/miniconda.html) and install it:

```bash
wget wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sudo bash Miniconda3-latest-Linux-x86_64.sh -p /usr/bin/miniconda3
```

### Disable Miniconda on start-up (optionnal):

Get into the Miniconda environement if you aren't already:

```bash
source /usr/bin/miniconda3/bin/activate
```

Turn off conda on start-up:
```bash
conda config --set auto_activate_base false
```

### Create a conda environement:

Get into the Miniconda environement if you aren't already:

```bash
source /usr/bin/miniconda3/bin/activate
```

Create a new conda environement:

```bash
conda create --name env python=3.9
```

### Install librairies:

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
pip install -r requirements.txt
```

Set the path variables:
```bash
CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
```

## Usage

### Jupyter

To develop on the model, get into the `jupyter` folder and run `jupyter-lab`:

```bash
cd jupyter && jupyter-lab
```

### Scrapy

To download picture of ducks or cats, get into the `scrapy` folder and make a crawl:

```bash
cd scrapy && scrapy crawl [duck|cat]
```

Some scripts are available in `scrapy/tools/`:

* `delete_duplicate.py`: delete every picture duplicates in the dataset folder.
* `rename.py`: rename every pictures of a folder following a pattern.
* `resize.py`: to save on storage and RAM, resize every pictures to be a maximum of 1024 pixels of width and height.

To use any of them :

```bash
cd scrapy/tools/ && python3 [script_name]
```

## Versions

* Windows 11 and WSL2 (Ubuntu 20.04.5)
* Python 3.9
* Scrapy 2.7.1
* Tensorflow 2.12
* CUDA tool kit 11.8

## Structure

```
scrapy/
jupyter/
env/
.gitignore
README.md
requirements.txt
```

## References

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
* [3 Ways to Deploy Machine Learning Models in Production](https://towardsdatascience.com/3-ways-to-deploy-machine-learning-models-in-production-cdba15b00e)
* [How to Deploy Machine Learning Models](https://towardsdatascience.com/how-to-deploy-machine-learning-models-601f8c13ff45)
* [A faster way to build and share data apps](https://streamlit.io/)
* [Quickstart - Installing MLflow](https://mlflow.org/docs/latest/quickstart.html)
