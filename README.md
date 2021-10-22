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
