"""
Visualizer

This module is responsible for visualize the result of Knn algorithm, let user input iris
data, predict the variety of iris then shows it on the GUI.

Author: Kai
Version: 1.0
Date: 2024-11-18
"""
# src/VisualizerModule.py
import tkinter as tk

from DataProcessorModule import DataProcessorModule
from KnnAlgorithmModule import KnnAlgorithmModule

class VisualizerModule:
    """
       A class used to visualize the result of Knn algorithm, let user input iris data,
       predict the variety of iris then shows it on the GUI.

       Methods:
           __init__ : Draw the GUI.
           Draw_First_Graph : Draw the graph with training data.
           Draw_axes : Draw X-axis and Y-axis on the graph.
           Draw_point : Draw the point on the graph
           Input_predict: Let user input new data of iris then shows the predicted variety on GUI and draw it on the graph.
       """

    # initial modules
    knn = KnnAlgorithmModule()
    data = DataProcessorModule()

    def __init__(self, root, initial_data):
        """
        Draw the GUI.
        """
        # Initial tk.
        self.root = root
        self.root.title("Knn Algorithm")

        # Load data.
        self.data = initial_data

        # Use red to represent Setosa, green to represent Versicolor, bluew to represent Virginica, yellow to represent new data.
        self.colors = {'Setosa': 'red', 'Versicolor': 'green', 'Virginica': 'blue'}
        self.new_point = 'yellow'

        # Create the canvas.
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.canvasSLSW = tk.Canvas(self.canvas_frame, width=550, height=550, bg="white")
        self.canvasSLSW.pack(side=tk.LEFT, padx=10, pady=10)

        self.canvasPLPW = tk.Canvas(self.canvas_frame, width=550, height=550, bg="white")
        self.canvasPLPW.pack(side=tk.LEFT, padx=10, pady=10)

        # Create input button
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(side=tk.BOTTOM, fill=tk.X)

        tk.Label(self.input_frame, text="SL:").grid(row=0, column=0)
        self.sl_entry = tk.Entry(self.input_frame)
        self.sl_entry.grid(row=0, column=1)

        tk.Label(self.input_frame, text="SW:").grid(row=0, column=2)
        self.sw_entry = tk.Entry(self.input_frame)
        self.sw_entry.grid(row=0, column=3)

        tk.Label(self.input_frame, text="PL:").grid(row=0, column=4)
        self.pl_entry = tk.Entry(self.input_frame)
        self.pl_entry.grid(row=0, column=5)

        tk.Label(self.input_frame, text="PW:").grid(row=0, column=6)
        self.pw_entry = tk.Entry(self.input_frame)
        self.pw_entry.grid(row=0, column=7)

        self.predict_button = tk.Button(self.input_frame, text="Predict", command=self.Input_predict)
        self.predict_button.grid(row=0, column=8)

        self.result_label = tk.Label(self.root, text="Predicted Variety: (Setosa: red Versicolor: green Virginica: blue)", font=("Arial", 14))
        self.result_label.pack(side=tk.BOTTOM, fill=tk.X)

        # Draw the first graph
        self.Draw_First_Graph()

    def Draw_First_Graph(self):
        """
        Draw the graph with training data.
        """

        #Draw axes.
        self.Draw_axes(self.canvasSLSW, "SL", "SW")
        self.Draw_axes(self.canvasPLPW, "PL", "PW")

        #Draw point from iris data_set and use different color to mark different varieties.
        for point in self.data:
            self.Draw_point(self.canvasSLSW, point['SL'], point['SW'], self.colors[point['variety']])
            self.Draw_point(self.canvasPLPW, point['PL'], point['PW'], self.colors[point['variety']])

    def Draw_axes(self, canvas, xlabel, ylabel):
        """
        Draw X-axis and Y-axis on the graph
        """

        # Draw coordinate axes.
        # Draw X-axis
        canvas.create_line(50, 500, 500, 500, width=2)

        # Draw Y-axis
        canvas.create_line(50, 500, 50, 50, width=2)

        # Label the Scales
        # split into 10 scales
        for i in range(11):
            x = 50 + i * 45
            y = 500 - i * 45

            # X-axis
            canvas.create_text(x, 510, text=f"{i}", font=("Arial", 10))

            # Y-axis
            canvas.create_text(40, y, text=f"{i}", font=("Arial", 10))

        # Label X-axis and Y-axis
        canvas.create_text(275, 530, text=xlabel, font=("Arial", 12))
        canvas.create_text(20, 275, text=ylabel, font=("Arial", 12), angle=90)

    def Draw_point(self, canvas, x, y, color):
        """
        Draw the point on the graph
        """

        # Transform the values of x and y to better distinguish them in the graph.
        x_transform = 50 + x * 45
        y_transform = 500 - y * 45

        # Draw the points.
        canvas.create_oval(
            x_transform - 5, y_transform - 5, x_transform + 5, y_transform + 5, fill=color, outline=color
        )

    def Input_predict(self):
        """
        Let user input new data of iris then shows the predicted variety on GUI and draw it on the graph.
        """
        try:
            # input
            sl = float(self.sl_entry.get())
            sw = float(self.sw_entry.get())
            pl = float(self.pl_entry.get())
            pw = float(self.pw_entry.get())

            #Strict the input.
            if sl > 10 or sl <= 0 or sw > 10 or sw <= 0 or pl > 10 or pl <= 0 or pw > 10 or pw <=0:
                self.result_label.config(text="Invalid input! Please enter number between 0-10.")
                return

        except ValueError:
            self.result_label.config(text="Invalid input! Please enter numeric values.")
            return

        #Form the data inputted.
        input_data = {'SL': sl, 'SW': sw, 'PL': pl, 'PW': pw}

        # Use KnnAlgorithm to predict the variety
        knn = KnnAlgorithmModule()
        knn.load_data(self.data)
        variety = knn.categorization(input_data)

        # Add new data to previous data.
        self.data.append({**input_data, 'variety': variety})

        # Draw the graph with new data.
        self.Draw_point(self.canvasSLSW, sl, sw, self.new_point)
        self.Draw_point(self.canvasPLPW, pl, pw, self.new_point)

        # Shows prediction to user.
        self.result_label.config(text=f"Predicted Variety is(Setosa: red Versicolor: green Virginica: blue newpoint: yellow): {variety}")






