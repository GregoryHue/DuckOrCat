# DOCDatasetManager

Python/Scrapy project that helps with DOC - Duck Or Cat.

## Project setup

Get into the project folder:
```bash
cd DOCDatasetManager
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

This will download pictures, depending which website you have put in `app/downloader/spiders/ducks.py` in `allowed_domains` and `start_urls`. You can try with `https://unsplash.com/s/photos/duck`. The pictures will be available in `app/images/`.

Some scripts are available in `app/tools/`:

* ``delete_duplicate.py``: delete every picture duplicates in a folder.
* ``rename.py``: rename every pictures of a folder following a pattern.
* ``resize.py``: to save on storage and RAM, resize every pictures to be maximum 1024 pixels of width and height.

To use any of them :

```bash
cd app/tools/ && python3 [script_name]
```

To label pictures, I recommend using `make-sense` (see references):

```bash
cd app/tools/ && git clone https://github.com/SkalskiP/make-sense.git && cd make-sense && npm install && npm start
```

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
* [GitHub - SkalskiP / make-sense](https://github.com/SkalskiP/make-sense)
