# autocomplete
An autocompletion API, as an exercise in end-to-end data science and ML engineering.


## Setup
Requirements: Python 3.7+

#### Basics:

1. Make and activate virtual environment with: `$ python3 -m venv venv && source venv/bin/activate`
2. Update pip and install requirements with: `$ pip3 install --upgrade pip && pip3 install -r requirements.txt`


#### Start working with notebooks:

Once you've created and activated your virtual environment and installed all requirements, start a notebook server with: `$ jupyter notebook`. This will also open a browser window showing the file tree, starting at the current working directory.

To create a new notebook: Navigate the file tree to the location you want to create the new notebook in, then click **New > Python 3**. This will create a new untitled notebook which you can then rename, work in, and save.

To open an existing notebook: Navigate to the location of the notebook in the file tree, and click on the notebook. This will open it in a new tab.


#### Running unit tests:

Once you've created and activated your virtual environment and installed all requirements, you can run unit tests with: `$ pytest --cov=src/. --cov-config=.coveragerc --disable-warnings`. By default this will suppress warnings, removing the `--disable-warnings` flag will include warnings in the report summary.
