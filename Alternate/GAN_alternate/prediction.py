# Import necessary libraries
import pandas as pd
from Bio import SeqIO
import numpy as np
import joblib

import numpy as np
import pandas as pd
import os, re, math, platform
from pathlib import Path
import matplotlib.pyplot as plts
import json
import joblib
from scipy.stats import randint as sp_randint
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import RandomizedSearchCV
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import matthews_corrcoef, confusion_matrix
from sklearn.metrics import precision_recall_curve, roc_curve, auc, fbeta_score
from imblearn.metrics import geometric_mean_score
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier 
from xgboost import plot_importance
from sklearn.ensemble import GradientBoostingClassifier,RandomForestClassifier,ExtraTreesClassifier,AdaBoostClassifier
from sklearn.linear_model import SGDClassifier
#from sklearn.linear_model import ElasticNet
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from lightgbm import LGBMClassifier
from sklearn.svm import SVC
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis as PA
from modlamp.descriptors import PeptideDescriptor, GlobalDescriptor
from matplotlib import pyplot
from sklearn.metrics import matthews_corrcoef, confusion_matrix,precision_recall_curve, roc_curve, auc, fbeta_score,roc_auc_score
from fea_extract import read_fasta,insert_AAC,insert_DPC,insert_CKSAAGP,insert_CTD,insert_PAAC,insert_AAI,insert_GTPC,insert_QSO,insert_AAE,insert_PSAAC,insert_word2int,insert_ASDC
import warnings 
from collections import Counter
from tools import cv,evaluate
import matplotlib.pyplot as plt
import seaborn as sns

# or pickle, depending on the model's serialization method

# Define the feature encoding function
def pro_data(seq):
    # Define functions for feature extraction (insert_XXXX)
    # Replace these with your actual feature extraction functions
    df_n = insert_PAAC(seq)
    df_n = insert_AAC(df_n)
    df_n = insert_CKSAAGP(df_n)
    df_n = insert_CTD(df_n)
    df_n = insert_DPC(df_n)
    df_n = insert_GTPC(df_n)
    df_n = insert_QSO(df_n)
    df_n = insert_AAE(df_n)
    df_n = insert_ASDC(df_n)
    return df_n

# Load the trained model
def load_model(model_path):
    # Load the model using joblib or pickle
    model = joblib.load(model_path)  # Adjust the serialization method accordingly
    return model

# Predict ACPs from FASTA file
def predict_acps(fasta_file, model):
    predictions = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence = str(record.seq)
        # Encode features for the sequence
        features = pro_data(sequence)
        # Make predictions using the loaded model
        prediction = model.predict(features.reshape(1, -1))  # Assuming a single sample prediction
        predictions.append((record.id, sequence, prediction))
    return predictions

# Main function
def main():
    # Define paths to FASTA file and trained model
    fasta_file = './ACPs10.fasta'
    model_path = './model_weights/Two_eclf_weights.pkl'  # Adjust the model path

    # Load the model
    model = load_model(model_path)

    # Predict ACPs
    predictions = predict_acps(fasta_file, model)

    # Display predictions
    for result in predictions:
        print(f"ID: {result[0]}\nSequence: {result[1]}\nPrediction: {result[2]}")

# Entry point of the script
if __name__ == "__main__":
    main()