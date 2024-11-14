"""
KnnAlgorithmModule

This module includes the functionalities list below:
Calculate the distance between data points based on the SL, SW, PL, and PW attributes;
Find the k nearest neighbors of a training point;
Categorize the the variety of a data point.

Author: Hailee Wang
Version: 1.0
Date: 2024-11-12
"""

import math
from collections import Counter

class KnnAlgorithmModule:
    def __init__(self, k=3):
        self.k = k
        self.data = []

    def load_data(self, data):
        """
        Load preprocessed data into this model.
        The data is a list of dictionaries:
        {'SL': 5.1, 'SW': 3.5, 'PL': 1.4, 'PW': 0.2, 'variety': 'Setosa'}
        """
        self.data = data

    def calculate_distance(self, point1, point2):
        """
        Calculate the Euclidean distance between two data points.
        Each data point is a dictionary includes 'SL', 'SW', 'PL', 'PW'.
        """
        return math.sqrt(
            (point1['SL'] - point2['SL']) ** 2 +
            (point1['SW'] - point2['SW']) ** 2 +
            (point1['PL'] - point2['PL']) ** 2 +
            (point1['PW'] - point2['PW']) ** 2
        )

    def k_nearest_neighbor(self, data_point):
        """
        Find the k nearest neighbors of the given data point.
        """
        distances = []
        for train_data in self.data:
            distance = self.calculate_distance(data_point, train_data)
            distances.append((distance, train_data['variety']))

        # Sort the data points by distance and find the k nearest data points
        distances.sort(key=lambda x: x[0])
        nearest_neighbors = distances[:self.k]

        return nearest_neighbors

    def categorization(self, data_point):
        """
        Predict the variety category of this given data point
        by learning from its k nearest neighbors.
        """
        nearest_neighbors = self.k_nearest_neighbor(data_point)
        
        # Get the varieties from its k nearest neighbors
        varieties = [neighbor[1] for neighbor in nearest_neighbors]

        # Find the most common variety among the neighbors
        predicted_variety = Counter(varieties).most_common(1)[0][0]
        
        return predicted_variety

    def calculate_accuracy(self, test_data):
        """
        Check the accuracy of this Knn algorithm model using some test data.
        """
        correct = 0
        for data_point in test_data:
            accurate_variety = data_point['variety']
            predicted_variety = self.categorization(data_point)
            if predicted_variety == accurate_variety:
                correct += 1

        accuracy = correct / len(test_data) * 100  # Accuracy as a percentage
        return accuracy