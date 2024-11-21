"""
DataProcessorModule

This module is responsible for loading and splitting a dataset. It includes functions to load a CSV file,
process the data, and split it into training and testing sets.

Author: Erdun E
Version: 1.0
Date: 2024-11-07
"""

import os
import csv
import random

class DataProcessorModule:
    """
    A class used to load, process, and split a dataset for machine learning purposes.

    Methods:
        load_dataset    : Loads the dataset from a CSV file.
        data_processing : Processes the raw data into a usable format.
        train_test_split: Splits the data into training and testing sets.
    """
    def load_dataset(self, file_path=None):
        """
        Loads the raw dataset from a CSV file and returns it as a list of dictionaries.

        Returns:
            list: A list of dictionaries representing the raw data loaded from the CSV file.
        """
        if file_path is None:
            # Use relative path to locate the file in the parent directory
            file_path = os.path.join(os.path.dirname(__file__), "../iris.csv")

        raw_data = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                raw_data.append(row)
        return raw_data

    def data_processing(self, raw_data):
        """
        Processes the raw dataset to extract relevant fields and convert them to the usable format.
        
        Returns:
            list: A list of processed dictionaries, where each dictionary contains:
                - "SL"      : Sepal length.
                - "SW"      : Sepal width.
                - "PL"      : Petal length.
                - "PW"      : Petal width.
                - "variety" : The species variety.
        """
        processed_data = []
        for row in raw_data:
            processed_data.append({
                "SL": float(row["sepal.length"]),
                "SW": float(row["sepal.width"]),
                "PL": float(row["petal.length"]),
                "PW": float(row["petal.width"]),
                "variety": row["variety"]
            })
        return processed_data

    def train_test_split(self, processed_data, test_size=0.2):
        """
        Splits the processed dataset into training and testing sets.
        By default, 80% of the data is used for training, and 20% is used for testing.
        
        Returns:
            tuple: A tuple containing two lists:
                - train_data: The training set, a list of dictionaries with the same format as the input data.
                - test_data : The testing set, a list of dictionaries with the same format as the input data.
        """
        # Shuffle data randomly
        random.shuffle(processed_data)
        split_index = int(len(processed_data) * (1 - test_size))
        train_data = processed_data[:split_index]
        test_data = processed_data[split_index:]
        return train_data, test_data


# Local Unit Test
if __name__ == "__main__":
    processor = DataProcessorModule()

    # Load raw data
    raw_data = processor.load_dataset()
    print(f"Loaded {len(raw_data)} raw records")
    print("Sample raw record:", raw_data[0])

    # Process data
    processed_data = processor.data_processing(raw_data)
    print("Processed data sample:", processed_data[0])

    # Split dataset into training and testing sets
    train_data, test_data = processor.train_test_split(processed_data)
    print(f"Train set size: {len(train_data)}, Test set size: {len(test_data)}")
    print("Sample train data:", train_data[0])
    print("Sample test data:", test_data[0])