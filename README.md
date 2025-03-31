# Drug-Drug Interaction Using XGBoost
Drug-drug interactions 
This project aims to create a machine learning model that can classify the interactions of two drugs, given their `SMILES` input

## Pre-requisites
- Jupyter Notebook


## Installation/Steps to run project locally
- Clone the repository `https://github.com/valentina-buoro/outreachy-contributions.git`
- Open Jupyter notebook and `cd` into the `/notebook` folder
- Open the `drug_drug_interactions.ipynb` file
- uncomment the first cell in the notebook and run using `shift + enter`. This runs a python script that installs the required packages.
  N.B. if along the line, you experience an error that says `ModuleNotFoundError: No module named 'module_name'`, just run `pip install module_name`
- The notebook is divided into four(4) parts, namely `Installation, Loading Dataset From TDC package, Exploratory Data Analysis, Featurisation`
- run the cells in the notebook sequentially


## Development Workflow:
- Pre-requisites for development were sucessfully installed
- I explored the TDC dataset catalogue and selected a dataset for classification modelling
- I wrote a python script that downloads the dataset and saves to the `/data` folder
- The data was split into `train, valid and test` for training the machine learning model, carrying out cross validation of the model, and finally testing the model on new data.
- I carried out basic Exploratory Data Analysis to have a better understanding of my dataset
      - The Dataset has 4 columns `Drug1_ID Drug1 Drug2_ID Drug2 Y `
      - Drug1_ID column contains the ID for the first drug in each observation(row), Drug1 column contains the SMILES representation of the first drug in each observation(row), Drug2_ID column  contains the ID for the second drug in each observation(row) and Drug2 column contains the the SMILES representation for the second drug in each observation(row)
      - Y column contains the type of interaction between Drug1 and Drug2. In the dataset these interactions are represented by intergers numbering 1 to 86. The TDC package contains a function to map each interger to the type of interaction observed.
     
- I featurised the model using the *Morgan Fingerprints in binary form* `eos4wt0` from Ersilia Hub
  ` Morgan fingerprints are a popular type molecular fingerprint used in cheminformatics. It represent the substructures within a molecule, capturing information about the connectivity and nature of atoms within a specified radius. The Ersilia model hub provides an implementation that provides a binary output, and I chose to use it because its output is suitable for the nature of model (XGBoost) that I plan on implementing. Although featurisation of my data would increase the size of the dataset, I confirmed that I had enough computational capacity to contain the featurised dataset.`
- To reproduce the featurisation process, I wrote a script that featurises the original dataset and returns only the featurised dataset into the `/data` folder at the end of the process.
  
  
## Issues faced
The featurised datasets could not be uploaded to github because of size constraints
I implemented the use of git large file storage, but found difficulty pushing the changes to github as I am working on a fork.
Upon further research, I discovered that git large file storage does not support the implemetation of forks as mentioned [here](https://github.com/homuler/MediaPipeUnityPlugin/issues/475) because it counts towards the original repo owner's quota.-~(Neleac)~

## Solution
Featurisation of the data is reproducible, with `%run '../scripts/featuriser.py'`, I refrained from uploading the featurised dataset to github

  


