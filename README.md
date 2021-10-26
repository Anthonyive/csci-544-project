# csci-544-project

CI/CD linters for Python are enabled, so please format your code and pass the checks before pull requests.

## First Steps

1. Clone this repo
2. Create your own branch named `name-dev`
3. Create a virtual environment using venv managers of your taste :) (preferably with something can generate `requirements.txt`)
   1. You may want to name your `requirements.txt` as `requirements-dev.txt` for distinction.
4. Make sure only pull requests when CI/CD passed

## What do all these files/directories mean??

```bash
$ tree -I "env" -L 3
.
├── LICENSE
├── Makefile # contains commands for linting/CICD
├── README.md
├── csci-544-project # actual package folder, you should add scripts under this folder
│   ├── __init__.py
│   ├── data # data folder
│   │   └── test-data.csv
│   └── tests # for testing scripts
│       └── test.py
├── notebooks # for experiments
│   └── notebook-test.ipynb
├── requirements.txt # pacakge requirements
├── scripts # not sure yet. prob for misc.
│   └── script-test.py
└── setup.cfg # linting configurations file
```

Note that files with name containing `test` are dummy files. You can remove them once you add something to that folder.

## When you see bugs or when you have something you want to achieve in foreseeable future...

Add an [issue](https://github.com/Anthonyive/csci-544-project/issues/new) in Issues tab!

## Data
- ArXiv
- PubMed

The follow data with description are sourced from: https://github.com/armancohan/long-summarization.git

### Get the datasets

ArXiv dataset: [Download](https://drive.google.com/file/d/1b3rmCSIoh6VhD4HKWjI4HOW-cSwcwbeC/view?usp=sharing) ([mirror](https://archive.org/download/armancohan-long-summarization-paper-code/arxiv-dataset.zip)) PubMed dataset: [Download](https://drive.google.com/file/d/1lvsqvsFi3W-pE1SqNZI0s8NR9rC1tsja/view?usp=sharing) ([mirror](https://archive.org/download/armancohan-long-summarization-paper-code/pubmed-dataset.zip))

The datasets are rather large. You need about 5G disk space to download and about 15G additional space when extracting the files. Each `tar` file consists of 4 files. `train.txt`, `val.txt`, `test.txt` respectively correspond to the training, validation, and test sets. The `vocab` file is a plaintext file for the vocabulary.

### Format of the data
The files are in jsonlines format where each line is a json object corresponding to one scientific paper from ArXiv or PubMed. The abstract, sections and body are all sentence tokenized. The json objects are in the following format:

```
{ 
  'article_id': str,
  'abstract_text': List[str],
  'article_text': List[str],
  'section_names': List[str],
  'sections': List[List[str]]
}
```
