"""
VisualizerModule

The Visualize data and make prediction after user input

Author: Kai
Version: 2.0
Date: 2024-11-19
"""
import tkinter as tk
from KnnAlgorithmModule import KnnAlgorithmModule

class VisualizerModule:
    """
       A class used to visualize the result of Knn algorithm, let user input iris data,
       predict the variety of iris then shows it on the GUI.

       Methods:
           __init__ : Draw the GUI.
           Draw_First_Graph : Draw the graph with training data.
           Draw_axes : Draw X-axis and Y-axis on the graph.
           Draw_point : Draw the point on the graph.
           Input_predict: Let user input new data of iris then shows the predicted variety on GUI and draw it on the graph.
       """

    # initial modules
    knn = KnnAlgorithmModule()

    def __init__(self, root, initial_data):
        """
        Draw the GUI.
        """
        # Initial tk.
        self.root = root
        self.root.title("Knn Algorithm Visualization")

        # Load data.
        self.data = initial_data
        self.user_points = []  # List to store user-added points

        # Use red to represent Setosa, green to represent Versicolor, blue to represent Virginica, orange to represent new data.
        self.colors = {'Setosa': 'red', 'Versicolor': 'green', 'Virginica': 'blue'}
        self.new_point = 'orange'

        # Add program description at the top
        self.description = tk.Label(
            self.root,
            text="KNN Algorithm Visualization\nVisualize Iris Data and Predict Varieties\nYou can input some iris data below to make a prediction, and the predicted variety will be shown on the graph.",
            font=("Arial", 16),
            justify="center"
        )
        self.description.pack(side=tk.TOP, pady=10)

        # Create the canvas frame
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        # Create canvases for graphs
        self.canvasSLSW_frame = tk.Frame(self.canvas_frame)
        self.canvasSLSW_frame.grid(row=0, column=0, padx=10, pady=10)

        self.canvasPLPW_frame = tk.Frame(self.canvas_frame)
        self.canvasPLPW_frame.grid(row=0, column=1, padx=10, pady=10)

        self.canvasSLSW = tk.Canvas(self.canvasSLSW_frame, width=550, height=550, bg="white")
        self.canvasSLSW.pack()

        self.canvasPLPW = tk.Canvas(self.canvasPLPW_frame, width=550, height=550, bg="white")
        self.canvasPLPW.pack()

        # Add labels below the graphs
        self.slsp_label = tk.Label(self.canvasSLSW_frame, text="Graph 1: Sepal Length vs Sepal Width", font=("Arial", 12))
        self.slsp_label.pack(pady=5)

        self.plpw_label = tk.Label(self.canvasPLPW_frame, text="Graph 2: Petal Length vs Petal Width", font=("Arial", 12))
        self.plpw_label.pack(pady=5)


        self.numeric_label = tk.Label(self.root, text="Your input should be numeric and between 0 and 10. ",font=("Arial", 12),justify="center")
        self.numeric_label.pack(pady=5)

        # Add input fields below the first graph
        self.sl_sw_frame = tk.Frame(self.canvasSLSW_frame)
        self.sl_sw_frame.pack(side=tk.BOTTOM, pady=10)

        tk.Label(self.sl_sw_frame, text="Sepal Length:").grid(row=0, column=0, sticky="e")
        self.sl_entry = tk.Entry(self.sl_sw_frame, width=10)
        self.sl_entry.grid(row=0, column=1)

        tk.Label(self.sl_sw_frame, text="Sepal Width:").grid(row=1, column=0, sticky="e")
        self.sw_entry = tk.Entry(self.sl_sw_frame, width=10)
        self.sw_entry.grid(row=1, column=1)

        # Add input fields below the second graph
        self.pl_pw_frame = tk.Frame(self.canvasPLPW_frame)
        self.pl_pw_frame.pack(side=tk.BOTTOM, pady=10)

        tk.Label(self.pl_pw_frame, text="Petal Length:").grid(row=0, column=0, sticky="e")
        self.pl_entry = tk.Entry(self.pl_pw_frame, width=10)
        self.pl_entry.grid(row=0, column=1)

        tk.Label(self.pl_pw_frame, text="Petal Width:").grid(row=1, column=0, sticky="e")
        self.pw_entry = tk.Entry(self.pl_pw_frame, width=10)
        self.pw_entry.grid(row=1, column=1)

        # Add the predict button below both graphs
        self.predict_button = tk.Button(self.root, text="Make Prediction", command=self.Input_predict)
        self.predict_button.pack(side=tk.BOTTOM, pady=10)

        self.result_label = tk.Label(self.root, text="Predicted Variety: ", font=("Arial", 14))
        self.result_label.pack(side=tk.BOTTOM, fill=tk.X)

        # Draw the first graph
        self.Draw_First_Graph()

    def Draw_First_Graph(self):
        """
        Draw the graph with training data.
        """
        # Draw axes
        self.Draw_axes(self.canvasSLSW, "Sepal Length (cm)", "Sepal Width (cm)")
        self.Draw_axes(self.canvasPLPW, "Petal Length (cm)", "Petal Width (cm)")

        # Draw points for initial data
        for point in self.data:
            self.Draw_point(self.canvasSLSW, point['SL'], point['SW'], self.colors[point['variety']])
            self.Draw_point(self.canvasPLPW, point['PL'], point['PW'], self.colors[point['variety']])

    def Draw_axes(self, canvas, xlabel, ylabel):
        """
        Draw X-axis and Y-axis on the graph.
        """
        # Draw coordinate axes
        canvas.create_line(50, 500, 500, 500, width=2)  # X-axis
        canvas.create_line(50, 500, 50, 50, width=2)  # Y-axis

        # Label scales
        for i in range(11):
            x = 50 + i * 45
            y = 500 - i * 45
            canvas.create_text(x, 510, text=f"{i}", font=("Arial", 10))  # X-axis
            canvas.create_text(40, y, text=f"{i}", font=("Arial", 10))  # Y-axis

        # Label axes
        canvas.create_text(275, 530, text=xlabel, font=("Arial", 12))
        canvas.create_text(20, 275, text=ylabel, font=("Arial", 12), angle=90)

        # Add legend to the top-right corner
        canvas.create_text(480, 50, text="Setosa", fill="black", font=("Arial", 10), anchor="ne")
        canvas.create_text(490, 50, text="●", fill="red", font=("Arial", 10), anchor="ne")
        canvas.create_text(480, 70, text="Versicolor", fill="black", font=("Arial", 10), anchor="ne")
        canvas.create_text(490, 70, text="●", fill="green", font=("Arial", 10), anchor="ne")
        canvas.create_text(480, 90, text="Virginica", fill="black", font=("Arial", 10), anchor="ne")
        canvas.create_text(490, 90, text="●", fill="blue", font=("Arial", 10), anchor="ne")
        canvas.create_text(480, 110, text="New Point", fill="black", font=("Arial", 10), anchor="ne")
        canvas.create_text(490, 110, text="●", fill="orange", font=("Arial", 10), anchor="ne")

    def Draw_point(self, canvas, x, y, color):
        """
        Draw the point on the graph
        """
        x_transform = 50 + x * 45
        y_transform = 500 - y * 45

        canvas.create_oval(
            x_transform - 5, y_transform - 5, x_transform + 5, y_transform + 5, fill=color, outline=color
        )

    def Input_predict(self):
        """
        Let user input new data of iris then shows the predicted variety on GUI and draw it on the graph.
        """
        try:
            sl = float(self.sl_entry.get())
            sw = float(self.sw_entry.get())
            pl = float(self.pl_entry.get())
            pw = float(self.pw_entry.get())

            if not (0 < sl <= 10 and 0 < sw <= 10 and 0 < pl <= 10 and 0 < pw <= 10):
                self.result_label.config(text="Invalid input! Please enter numbers between 0 and 10.")
                return

        except ValueError:
            self.result_label.config(text="Invalid input! Please enter numeric values.")
            return

        input_data = {'SL': sl, 'SW': sw, 'PL': pl, 'PW': pw}

        # Use KnnAlgorithm to predict the variety
        knn = KnnAlgorithmModule()
        knn.load_data(self.data)
        variety = knn.categorization(input_data)

        # Update previous points to their respective colors
        for point in self.user_points:
            self.Draw_point(self.canvasSLSW, point['SL'], point['SW'], self.colors[point['variety']])
            self.Draw_point(self.canvasPLPW, point['PL'], point['PW'], self.colors[point['variety']])

        # Add new point
        input_data['variety'] = variety
        self.user_points.append(input_data)
        self.Draw_point(self.canvasSLSW, sl, sw, self.new_point)
        self.Draw_point(self.canvasPLPW, pl, pw, self.new_point)

        # Show prediction
        self.result_label.config(text=f"Predicted Variety: {variety}")
