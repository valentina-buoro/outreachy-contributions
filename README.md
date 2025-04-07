



https://github.com/user-attachments/assets/cc2523d0-c2a6-4e54-86ef-8ab562432584



# Drug-Drug Interaction Using XGBoost
Drug-drug interactions are interactions that occur when two or more drugs are taken together. In these interaction, one drug alters the effect of another, and these may potentially lead to decreased effectiveness, increased side effects, or unexpected reactions. 

Acording to [TDC](https://tdcommons.ai/multi_pred_tasks/ddi) analyis of patient records showed that drug-drug interactions were the cause of admission for prolonged hospital stays in 7% of the cases. Estimating drug drug interaction during the early phase of drug development essentially helps the screening process by the rejection of drugs that have the risk of potential drug–drug interaction. 

This project aims to create a machine learning model that can classify the interactions of two drugs, given their `SMILES` input

## Pre-requisites
- Jupyter Notebook
- Python


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
- Although this dataset was fairly large, I choose it because I wanted to prevent overfitting the data by providing sufficient amount of training data to learn with
- I wrote a python script that downloads the dataset and saves to the `/data` folder
- The data was split into `train, valid and test` for training the machine learning model, carrying out cross validation of the model, and finally testing the model on new data.
- I carried out basic Exploratory Data Analysis to have a better understanding of my dataset
      - The Dataset has 5 columns `Drug1_ID Drug1 Drug2_ID Drug2 Y `
      - Drug1_ID column contains the ID for the first drug in each observation(row), Drug1 column contains the SMILES representation of the first drug in each observation(row), Drug2_ID column  contains the ID for the second drug in each observation(row) and Drug2 column contains the the SMILES representation for the second drug in each observation(row)
      - Y column contains the type of interaction between Drug1 and Drug2. In the dataset these interactions are represented by intergers numbering 1 to 86. The TDC package contains a function to map each interger to the type of interaction observed.
     
- I featurised the model using the *Morgan Fingerprints in binary form* `eos4wt0` from Ersilia Hub
  ` Morgan fingerprints are a popular type molecular fingerprint used in cheminformatics. It represent the substructures within a molecule, capturing information about the connectivity and nature of atoms within a specified radius. The Ersilia model hub provides an implementation that provides a binary output, and I chose to use it because its output is suitable for the nature of model (XGBoost) that I plan on implementing. Although featurisation of my data would increase the size of the dataset, I confirmed that I had enough computational capacity to contain the featurised dataset.`
- To reproduce the featurisation process, I wrote a script that featurises the original dataset and returns only the featurised dataset into the `/data` folder at the end of the process.
- I proceeded to create the model using XGBoost classifier
- After model creation, I trained my model with the featurised test dataset, then I proceeded to make predictions using the featurised validation dataset, and the featurised test dataset and carried out performance evaluation for all the three(3) datasets.
- I proceeded to save my model for use in a web application.


## Model Selection
The model of choice for this project is the XGBoost algorithm. The choice of this model depended on many factors. XGBoost works efficiently with large datasets, such as was used for this project  
  
## Issues faced
1) The featurised datasets could not be uploaded to github because of size constraints
I implemented the use of git large file storage, but found difficulty pushing the changes to github as I am working on a fork.
Upon further research, I discovered that git large file storage does not support the implemetation of forks as mentioned [here](https://github.com/homuler/MediaPipeUnityPlugin/issues/475) because it counts towards the original repo owner's quota.-~(Neleac)~

2) XGBoost expects class labels to start from 0 and be contiguous. Therefore I adjusted the y_train to start from 0. 
This will not affect the model's eventual output
3) Backend server issues on render.


## Solution to issues
1) Featurisation of the data is reproducible, with `%run '../scripts/featuriser.py'`, I refrained from uploading the featurised dataset to github
2) I adjusted the y_train to start from 0 using the min value of the target `Y`
3) The webapp is currently served and accessible locally. I recorded a demo of the web application in action and updated steps to run the code locally


## Web application
The primary objective of any machine learning project is not solely to develop a performant model, but to ensure its utility in real-world applications. It is estimated that approximately 87% of data science models never make it into production environments. To address this gap, I developed a web application for my model that enables users to input two drug molecules in SMILES format and obtain a prediction of their potential interaction type.

The predictive model is based on an XGBoost classifier trained using binary Morgan fingerprints generated via the Ersilia platform. The app serves as a user-friendly interface to demonstrate how cheminformatics and machine learning can be integrated into accessible tools for drug interaction screening. This work illustrates a practical approach toward the translational deployment of AI in drug discovery and research.

- The backend for the website was built using the Python flask framework, and hosted on Render. Code for the backend api can be viewed [here](https://github.com/valentina-buoro/Drug-Interaction-Backend)
- The frontend was built using React framework, and hosted on netlify. [Live link to the website](https://drug-drug-interaction.netlify.app/) .The frontend code can be viewed [here](https://github.com/valentina-buoro/Drug-Interaction-Frontend)


