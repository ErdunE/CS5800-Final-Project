"""
Controller

This module is responsible for connect Visualizer, KnnAlgorithmModule and DaraProcessorModule.

Author: Kai
Version: 1.0
Date: 2024-11-18
"""
import tkinter as tk
from DataProcessorModule import DataProcessorModule
from KnnAlgorithmModule import KnnAlgorithmModule
from VisualizerModule import VisualizerModule


class Controller:
    """
    A class used to control other classes. It processes the raw data and use it to train Knn algorithm and visualize all data.

    Methods:
        __init__  : Processes data and train the Knn algorithm.
        run : start the Visualizer Module.
    """
    def __init__(self):
        """
        Process data and train the Knn algorithm.
        """
        # initial modules
        self.processor = DataProcessorModule()
        self.knn = KnnAlgorithmModule(k=3)

        # load data from processor
        self.data = self.processor.load_dataset()

        # process and split data
        self.processed_data = self.processor.data_processing(self.data)
        self.train_data, self.test_data = self.processor.train_test_split(self.processed_data)

        # train KnnAlgorithm
        self.knn.load_data(self.train_data)

    def run(self):
        """
        Run the whole program, draw two graphs to visualize the iris_data_set and let user
        input new iris data to predict the variety.
        """
        #create tkinter GUI
        root = tk.Tk()

        #draw the GUI
        VisualizerModule(root, initial_data=self.train_data)

        #keep running the algorithm
        root.mainloop()
