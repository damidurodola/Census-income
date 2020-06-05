import pandas as pd
import matplotlib.pyplot as plt

class ReadData:

  def __init__(self, data):
    self.data = data

  def read_from_csv(self, use_cols):
    extract_data = pd.read_csv(self.data, usecols=use_cols)
    return extract_data


  def visualize_data(self, formated_columns):
    fig, ax = plt.subplots()
    x_column = formated_columns['Operating Airline']
    y_column = formated_columns['Passenger Count']
    ax.bar(x_column, y_column)
    ax.set_title('Passenger count for Airlines')
    ax.set_xlabel('Airlines')
    ax.set_ylabel('Passenger Count')
    plt.show()

