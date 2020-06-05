from resources.read_data import ReadData

use_cols = ['Activity Period', 'Operating Airline', 'GEO Summary', 'GEO Region', 'Price Category Code', 'Passenger Count', 'Year', 'Month']
d1 = ReadData("Air_Traffic_Passenger_Statistics.csv").read_from_csv(use_cols)
ReadData.visualize_data(d1)
