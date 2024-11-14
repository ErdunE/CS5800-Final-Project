"""
Controller

This module is responsible to controll all program, connect other classes.

Author: Kai
Version: 1.0
Date: 2024-11-13
"""
from DataProcessorModule import DataProcessorModule
from KnnAlgorithmModule import KnnAlgorithmModule
from Visualizer import Visualizer


# src/Controller.py

class Controller:

    def __init__(self):

    def run(self):
        processor = DataProcessorModule
        KnnAlgo = KnnAlgorithmModule
        visual = Visualizer
        visual.init()
        raw_data = processor.load_dataset(self.file_path)
        processed_data = processor.data_processing(raw_data)
        self.train_data, self.test_data = processor.train_test_split(processed_data)
        visual.receive_training_data(self.train_data)
        visual.show_training_graph()
        KnnAlgo.Calculate_distance(self.train_data)
        KnnAlgo.K_nearest_neighbor(self.train_data)
        KnnAlgo.Calculate_distance(self.test_data)
        KnnAlgo.K_nearest_neighbor(self.test_data)
        KnnAlgo.calculate_accuracy()
        i = "1"
        while( i!="0"):
            visual.input()
            inputdata = visual.send_datapoint()
            KnnAlgo.categorization(inputdata)
            visual.receive_variety()
            visual.show_variety()
            i = input("Enter number 0 to quit")

        return


