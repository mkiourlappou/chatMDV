# Installation and running instructions for MDVAPI

## Introduction
Multi Dimensional Viewer (MDV) is web based application for analyzing, annotating and sharing multi-dimensional data from different modalities. If you have large amounts of data or projects you may wish to install MDV locally. MDV is written JavaScript designed to be embedded in a web page (https://mdv.molbiol.ox.ac.uk/). However, one can deploy it locally using python scripts. The python scripts format data to a specific file structure and compiled JavaScript that can display that format. Likewise the MDVAPI which is written in python can be run and allow the user to create certain types of graphs as per the user's will.  the local deployment of the project

## Prerequisites
The MDV-dev version of the MDV repository which contains the python scripts required.

### System Requirements

* A modern browser
* python (3.6 or above)
* only 4GB of ram is required even for large datasets (~10 000 000 items) as data is lazily loaded as raw bytes
* Packages:
  * pandas
  * os
  * json

## Installation

### Step1: Download and unzip the repository

https://github.com/Taylor-CCB-Group/MDV.git

or clone it
```
git clone https://github.com/Taylor-CCB-Group/MDV.git
```

Then cd to the python directory
```
cd path/to/mdv/python
```
### Step2: Set up a virtual environment (optional but recommended)
```
python -m venv /path/to/myenv
source /path/to/myenv/bin/activate
```

### Step3: Install dependencies and MDV
```
pip install -r requirements.txt
```

Install `mdv` (using `editable` flag for development):

```
cd MDV/python
pip install -e .
```
### Step4: Deploy an MDV project locally
Open a python shell
```
python
```

Create an MDV project display it in a browser:

```python
from mdvtools.mdvproject import MDVProject
p = MDVProject("/path/to/example/data")
p.serve()
```

This will open a browser window at http://localhost:5000/

## Running the MDV API

base_plot.py: The foundational class for all chart objects.

box_plot.py, dot_plot.py, heatmap_plot.py, scatter_plot.py, row_chart.py, ring_plot.py, stacked_row_plot.py: The files to create the class for each chart object as described by their name.

box_plot_example.py, dot_plot_example.py, heatmap_plot_example.py: The files to create each type of graph and deploy a local MDV project. 

One requirement is to have a .csv file containing the data. In each of the _example.py files the user should change the `params` variable to correspond to column names from the data file. 