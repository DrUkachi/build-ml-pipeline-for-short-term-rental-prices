#!/usr/bin/env python
"""
[An example of a step using MLflow and Weights & Biases]: Performs basic cleaning on the data and save the results in Weights & Biases
"""
import os
import argparse
import logging

import wandb
import pandas as pd



logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################

    logger.info("Downloading artifact")

    artifact_local_path = run.use_artifact(args.input_artifact).file()

    df = pd.read_csv(artifact_local_path)

    min_price = args.min_price
    max_price = args.max_price

    idx = df['price'].between(min_price, max_price)
    df = df[idx].copy()

    # Convert the last_review column to datetime

    df['last_review'] = pd.to_datetime(df['last_review'])

    filename = "clean_sample.csv"

    df.to_csv(filename, index=False)

    artifact = wandb.Artifact(
        name=args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file(filename)

    logger.info("Logging artifact")
    run.log_artifact(artifact)

    os.remove(filename)




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This step cleans the data")


    parser.add_argument(
        "--input_artifact", 
        type=str, ## INSERT TYPE HERE: str, float or int,
        help= "This is the file name of the input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="This is the file name of the output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="This is the type for the output artifact created",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="This is the description of the output artifact that will be created and stored",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="This is the minimum price of the house in our model",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="This is the maximum price of the house in our model",
        required=True
    )


    args = parser.parse_args()

    go(args)
