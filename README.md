# DuckPicturesDownloader

A Scrapy project to massively download pictures of ducks that will be later used to train a machine learning model.

## Project setup

Get into the project folder:
```bash
cd DuckPicturesDownloader
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
cd app && scrapy crawl ducks
```

This will download pictures, depending which website you have put in `app/app/spiders/ducks.py` in `allowed_domains` and `start_urls`. You can try with `https://unsplash.com/s/photos/duck`. The pictures will be available in `app/images/`.

## Versions

* Python 3.10.6
* Ubuntu 20.04.5

## Structure

```
app/
env/
.gitignore
README.md
requirements.txt
```

## References

* [Scrapy](https://scrapy.org/)
* [Item Pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html)
* [Pillow + scrapy = sometimes cannot identify image file](https://stackoverflow.com/questions/30114305/pillow-scrapy-sometimes-cannot-identify-image-file)