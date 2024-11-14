"""
Visualizer

This module is responsible to visualize the dataset and prediction to user directly.

Author: Kai
Version: 1.0
Date: 2024-11-13
"""
from matplotlib import pyplot as plt
from KnnAlgorithmModule import KnnAlgorithmModule

# src/Visualizer.py

class Visualizer:
    """
        A class used to load data and visualize it.

        Methods:
            receive_training_data    : Loads the training data from DataProcessorModule.
            show_training_graph : Visualize the training data.
            input: input data.
            send_datapoint: send data inputted to KnnAlgorithmModule.
            receive_variety: receive data variety from KnnAlgorithmModule.
            show_variety: Visualize the variety of
        """
    def init(self):
        self.input_data = None
        self.training_data = None
        self.predicted_variety = None

    def receive_training_data(self, train_data):
        """Loads and processes the training data using DataProcessorModule."""
        self.training_data = train_data
        print("Training data successfully loaded.")

    def show_training_graph(self, file_path=None):
        """Visualizes the training data with a scatter plot."""
        if not self.training_data:
            print("Loaded training data fail.")
            return

        # get data from DataProcessorModule
        sepal_length = [data['SL'] for data in self.training_data]
        sepal_width = [data['SW'] for data in self.training_data]
        petal_length = [data['PL'] for data in self.training_data]
        petal_width = [data['PW'] for data in self.training_data]
        varietie = [data['variety'] for data in self.training_data]

        # Use different color to represent different varieties
        unique_varietie = list(set(varietie))
        colors = ['r', 'g', 'b']  # Adjust color for different varieties
        print("Red: Setosa, Green: Virginica, Blue: versicolor.")

        for i, variety in enumerate(unique_varietie):
            x = [sepal_length[j] for j in range(len(varietie)) if varietie[j] == variety]
            y = [sepal_width[j] for j in range(len(varietie)) if varietie[j] == variety]
            plt.scatter(x, y, c=colors[i], label=variety)

        plt.xlabel('Sepal Length')
        plt.ylabel('Sepal Width')
        plt.title("Iris Data Scatter Plot")
        plt.legend()
        plt.show()

        for i, variety in enumerate(unique_varietie):
            x = [petal_length[j] for j in range(len(varietie)) if varietie[j] == variety]
            y = [petal_width[j] for j in range(len(varietie)) if varietie[j] == variety]
            plt.scatter(x, y, c=colors[i], label=variety)

        plt.xlabel('Sepal Length')
        plt.ylabel('Sepal Width')
        plt.title("Iris Data Scatter Plot")
        plt.legend()
        plt.show()

        return


    def input(self):
        """ Let user input the parameters to predict the variety of iris """
        print("Please input parameters to predict the variety of iris.")
        try:
            sl = float(input("sepal.length: "))
            sw = float(input("sepal.width: "))
            pl = float(input("petal.length: "))
            pw = float(input("petal.width: "))
            self.input_data = {"sepal.length": sl, "sepal.width": sw, "petal.length": pl, "petal.width": pw}
        except ValueError:
            print("You can only input the numeric values.")
            return


    def send_datapoint(self):
        """ send input_data to KnnAlgorithmModule """
        return self.input_data


    def receive_variety(self):
        """ receive predicted variety from KnnAlgorithmModule """
        if self.input_data is None:
            print("You have not input anything yet. Please input some value first.")
            return

        self.predicted_variety = KnnAlgorithmModule.categorization(self.input_data)
        print("Predicted variety:", self.predicted_variety)
        return



    def  show_variety(self):
        """ Show the new point on the graph """
        formatted_data = {
            "SL": self.input_data["sepal.length"],
            "SW": self.input_data["sepal.width"],
            "PL": self.input_data["petal.length"],
            "PW": self.input_data["petal.width"],
            "variety": "newpoint"
        }

        self.training_data.append(formatted_data)

        # get data from DataProcessorModule
        sepal_length = [data['SL'] for data in self.training_data]
        sepal_width = [data['SW'] for data in self.training_data]
        petal_length = [data['PL'] for data in self.training_data]
        petal_width = [data['PW'] for data in self.training_data]
        varietie = [data['variety'] for data in self.training_data]

        # Use different color to represent different varieties
        unique_varietie = list(set(varietie))
        colors = ['r', 'g', 'b','y']  # Adjust color for different varieties
        print("Red: Setosa, Green: Virginica, Blue: versicolor, Yellow: newpoint")

        for i, variety in enumerate(unique_varietie):
            x = [sepal_length[j] for j in range(len(varietie)) if varietie[j] == variety]
            y = [sepal_width[j] for j in range(len(varietie)) if varietie[j] == variety]
            plt.scatter(x, y, c=colors[i], label=variety)

        plt.xlabel('Sepal Length')
        plt.ylabel('Sepal Width')
        plt.title("Iris Data Scatter Plot")
        plt.legend()
        plt.show()

        for i, variety in enumerate(unique_varietie):
            x = [petal_length[j] for j in range(len(varietie)) if varietie[j] == variety]
            y = [petal_width[j] for j in range(len(varietie)) if varietie[j] == variety]
            plt.scatter(x, y, c=colors[i], label=variety)

        plt.xlabel('Sepal Length')
        plt.ylabel('Sepal Width')
        plt.title("Iris Data Scatter Plot")
        plt.legend()
        plt.show()

        return




