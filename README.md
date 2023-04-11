# DOCDatasetManager

Duck or Cat is a binary classification model. It classifies pictures of ducks and cats. A Scrapy project is available to manage your dataset.

## Project setup

Get into the project folder:
```bash
cd DuckOrCat
```

Create a new environment:

```bash
virtualenv --python="/usr/bin/python3" env
```

Get into that environment:

```bash
source env/bin/activate 
```

Install the librairies:
```bash
pip install -r requirements.txt
```

## Usage

Run:

```bash
cd app && scrapy crawl [duck|cat]
```

This will download pictures, depending which website you have put in `app/downloader/spiders/ducks.py` in `allowed_domains` and `start_urls`. You can try with `https://unsplash.com/s/photos/duck`. The pictures will be available in `app/images/`.

Some scripts are available in `app/tools/`:

* ``delete_duplicate.py``: delete every picture duplicates in a folder.
* ``rename.py``: rename every pictures of a folder following a pattern.
* ``resize.py``: to save on storage and RAM, resize every pictures to be maximum 1024 pixels of width and height.

To use any of them :

```bash
cd app/tools/ && python3 [script_name]
```

## Versions

* Python 3.10.6
* Ubuntu 20.04.5

## Structure

```
app/
dataset/
env/
.gitignore
README.md
requirements.txt
```

## References

* [Scrapy](https://scrapy.org/)
* [Item Pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html)
* [Pillow + scrapy = sometimes cannot identify image file](https://stackoverflow.com/questions/30114305/pillow-scrapy-sometimes-cannot-identify-image-file)
* [GitHub - SkalskiP / make-sense](https://github.com/SkalskiP/make-sense)
* [Install TensorFlow with pip - Windows Native](https://www.tensorflow.org/install/pip#windows-native)
* [Pytorch - DCGAN Tutorial](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html)
* [Dst tensor is not initialized #38](https://github.com/aymericdamien/TensorFlow-Examples/issues/38)
* [Image Recognition Guide](https://www.fritz.ai/image-recognition/)
* [Dog and Cat Detection](https://www.kaggle.com/datasets/andrewmvd/dog-and-cat-detection?select=images)
* [Binary Classification](https://www.kaggle.com/code/ryanholbrook/binary-classification)
* [Unet CatDog detection](https://www.kaggle.com/code/lmanda/unet-catdog-detection/notebook)
* [PyTorch | CNN Binary Image Classification](https://www.kaggle.com/code/shtrausslearning/pytorch-cnn-binary-image-classification)
* [🐈🐕 Cat and Dog Classification](https://www.kaggle.com/code/gcdatkin/cat-and-dog-classification)
* [TF2 - Tutorials - Keras - Save and Restore Models](https://www.kaggle.com/code/vikramtiwari/tf2-tutorials-keras-save-and-restore-models)
* [Keras CNN Dog or Cat Classification](https://www.kaggle.com/code/uysimty/keras-cnn-dog-or-cat-classification)
* [3 Ways to Deploy Machine Learning Models in Production](https://towardsdatascience.com/3-ways-to-deploy-machine-learning-models-in-production-cdba15b00e)
* [How to Deploy Machine Learning Models](https://towardsdatascience.com/how-to-deploy-machine-learning-models-601f8c13ff45)
* [A faster way to build and share data apps](https://streamlit.io/)
* [Quickstart - Installing MLflow](https://mlflow.org/docs/latest/quickstart.html)
