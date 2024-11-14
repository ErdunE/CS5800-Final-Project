
"""
Unit test for KnnAlgorithmModule

Unit tests for the calculate_distance, k_nearest_neighbor, categorization, and calculate_accuracy function.

Author: Hailee Wang
Version: 1.0
Date: 2024-11-12
"""
import unittest
from collections import Counter
from KnnAlgorithmModule import KnnAlgorithmModule

class TestKNearestNeighbor(unittest.TestCase):
    def setUp(self):
        # Sample training data
        self.train_data = [
            {'SL': 5.1, 'SW': 3.5, 'PL': 1.4, 'PW': 0.2, 'variety': 'Setosa'},
            {'SL': 4.9, 'SW': 3.0, 'PL': 1.4, 'PW': 0.2, 'variety': 'Setosa'},
            {'SL': 7.0, 'SW': 3.2, 'PL': 4.7, 'PW': 1.4, 'variety': 'Versicolor'},
            {'SL': 6.4, 'SW': 3.2, 'PL': 4.5, 'PW': 1.5, 'variety': 'Versicolor'},
            {'SL': 6.3, 'SW': 3.3, 'PL': 6.0, 'PW': 2.5, 'variety': 'Virginica'},
            {'SL': 5.8, 'SW': 2.7, 'PL': 5.1, 'PW': 1.9, 'variety': 'Virginica'}
        ]
        
        self.knn = KnnAlgorithmModule(k=3)
        self.knn.load_data(self.train_data)

    def test_calculate_distance(self):
        point1 = {'SL': 5.1, 'SW': 3.5, 'PL': 1.4, 'PW': 0.2}
        point2 = {'SL': 4.9, 'SW': 3.0, 'PL': 1.4, 'PW': 0.2}
        
        distance = self.knn.calculate_distance(point1, point2)
        expected_distance = ((5.1 - 4.9) ** 2 + (3.5 - 3.0) ** 2) ** 0.5
        self.assertAlmostEqual(distance, expected_distance, places=2)
        print("point1 = ", point1)
        print("point2 = ", point2)
        print("Distance between point1 and point2: ", distance)
        print("Expected distance: ", expected_distance)

    def test_k_nearest_neighbor(self):
        test_point = {'SL': 5.0, 'SW': 3.4, 'PL': 1.5, 'PW': 0.2}
        
        neighbors = self.knn.k_nearest_neighbor(test_point)
        nearest_varieties = [neighbor[1] for neighbor in neighbors]
        print("Test data point: ", test_point)
        print("Neighbors: ", neighbors)
        print("The varieties of nearest neighbors: ", nearest_varieties)
        print("Expected variety: Setosa")
        
        # Expecting the neighbors have the variety 'Setosa'
        self.assertIn('Setosa', nearest_varieties)
        # Should return exactly k neighbors
        self.assertEqual(len(neighbors), 3)  
        print("Number of neighbors: ", len(neighbors))
        print("Expected number of neighbors: 3")

    def test_categorization(self):
        test_point = {'SL': 5.0, 'SW': 3.4, 'PL': 1.5, 'PW': 0.2}
        
        predicted_variety = self.knn.categorization(test_point)
        self.assertEqual(predicted_variety, 'Setosa')
        print("Test data point: ", test_point)
        print("Predicted variety: ", predicted_variety)
        print("Expected variety: Setosa")

    def test_calculate_accuracy(self):
        # Test data with known varieties
        test_data = [
            {'SL': 5.1, 'SW': 3.5, 'PL': 1.4, 'PW': 0.2, 'variety': 'Setosa'},
            {'SL': 6.4, 'SW': 3.2, 'PL': 4.5, 'PW': 1.5, 'variety': 'Versicolor'},
            {'SL': 6.3, 'SW': 3.3, 'PL': 6.0, 'PW': 2.5, 'variety': 'Virginica'}
        ]
        
        accuracy = self.knn.calculate_accuracy(test_data)
        # Expecting a high accuracy rate
        self.assertGreaterEqual(accuracy, 90.0)  
        print("Accuracy: ", accuracy)
        print("Expected least accuracy: 90.0")

if __name__ == '__main__':
    unittest.main()