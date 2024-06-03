# NYC Airbnb Rental Price Prediction

This project is a comprehensive machine learning pipeline designed to predict short-term rental prices in New York City (NYC) using Airbnb data. The pipeline encompasses all essential stages from data preprocessing to model evaluation.

## Reqiured Submission Links
1. [**Github**](https://github.com/DrUkachi/build-ml-pipeline-for-short-term-rental-prices)

2. [**W & B**](https://wandb.ai/drukachi/nyc_airbnb)


## Project Overview

The project structure is organized as follows:

- **components/**: Contains the reusable componets for validation.

   - **get_data/**: Used for dowlading the data
   - **test_regression_model/**: Used for testing the regression model
   - **train_val_test_split/**: Used for data segregation

- **src/**: Source code directory.
  - **eda/**: Exploratory data analysis notebooks.
  - **basic_cleaning/**: Scripts for basic data cleaning.
  - **data_check/**: Module for data integrity checks.
  - **train_random_forest/**: Random Forest model training scripts.
  - **main.py**: Main script orchestrating the pipeline.
- **.gitignore**: Gitignore file.
- **README.md**: Project readme file.

## Setup

To set up the project:

1. Clone the repository: `git clone <repository_url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Weights & Biases (W&B) for experiment tracking and visualization.

## Weights & Biases (W&B) Set-Up

To utilize W&B:

1. Create a W&B account at [wandb.ai](https://wandb.ai).
2. Install the W&B Python library: `pip install wandb`
3. Log in to your W&B account: `wandb login`
4. Initialize W&B in your project: `wandb init`
5. Make your W&B project "nyc_airbnb" public for reviewer access.
6. For this project you can view my Weights and Biases Project here: https://wandb.ai/drukachi/nyc_airbnb



## Exploratory Data Analysis (EDA)

I explored the Airbnb dataset using the EDA notebook. I fetched the sample data from W&B by running the EDA notebook and grabbing the `sample.csv` artifact.

## Data Cleaning

I executed the data cleaning step using the `basic_cleaning.py` script in the `basic_cleaning` module. I ensured I provided the necessary parameters like `input_artifact`, `output_name`, `output_type`, `output_description`, `min_price`, and `max_price`.

## Data Testing

I ran data integrity tests using the `test_data.py` module within the `data_check` directory. I verified that the tests for dataset size and price range passed successfully.

## Data Splitting

I split the dataset into training, validation, and test sets using the `train_val_test_split` component.

## Train the Random Forest

I trained a Random Forest model using the preprocessed data. I used the `run.py` script within the `train_random_forest` module to facilitate this process.

## Optimize Hyperparameters

I utilized the Hydra system for hyperparameter optimization. I logged the results of each training job to W&B for performance evaluation.

You can see the results of all the runs here:

## Select the Best Model

I identified the best-performing model and tagged it as "prod" in W&B for production readiness. The best model was produced by this [**run**](https://wandb.ai/drukachi/nyc_airbnb/runs/8yirec5y?nw=nwuserdrukachi)

## Test Set Verification

I tested the selected model on a separate test set to ensure performance consistency. I implemented the `test_regression_model` function in `main.py` for this purpose.

## Visualize the Pipeline

I visualized the pipeline structure and data flow using the W&B artifact section's "Graph view".

## Release the Pipeline

I created a new release on GitHub with a suitable version number (1.0.0) to mark a stable version of the pipeline. 

Release Title: **ML Pipeline for the Short-Term Rental Prices Project**

## Train the Model on a New Data Sample

I tested the data on a new data sample and obtained a [succesful failure](https://wandb.ai/drukachi/nyc_airbnb/runs/laafrfc6/overview?nw=nwuserdrukachi)

I made the fix for the geolocation verification and created a new release with version number 1.0.1 see link [here](https://github.com/DrUkachi/build-ml-pipeline-for-short-term-rental-prices/releases/tag/1.0.1)
