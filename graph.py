import matplotlib.pyplot as plt
import argparse
import numpy as np

def calculate_percentage_change(start_value, end_value):
    if np.isnan(start_value) or np.isnan(end_value):
        return None
    return (end_value - start_value) / start_value * 100

def plot_graph(data):
    quarters = ['Q1']
    if len(data) > 1:
        quarters += ['Q2']
    if len(data) > 2:
        quarters += ['Q3']
    if len(data) > 3:
        quarters += ['Q4']

    quarter_sprints = 6  # Number of sprints per quarter
    
    # Plotting the graph and calculating average per quarter
    quarter_averages = []
    for i, quarter_data in enumerate(data):
        sprint_numbers = range(1, quarter_sprints + 1)
        quarter_data = np.array([np.nan if x is None else x for x in quarter_data])
        quarter_average = np.nanmean(quarter_data)
        quarter_averages.append(quarter_average)
        plt.plot(sprint_numbers, quarter_data, label=quarters[i])
    
    # Adding legend and title
    percentage_difference = calculate_percentage_change(quarter_averages[0], quarter_averages[-1])
    legend_text = [f'{quarters[i]} (Avg: {quarter_averages[i]:.2f})' + (f', Difference: {percentage_difference:.2f}%' if i == len(quarters) - 1 and percentage_difference != 0 else '') for i in range(len(quarters))]
    plt.legend(legend_text)
    plt.title('Average Sprint Speeds')
    plt.xlabel('Sprint Number')
    plt.ylabel('Speed (m/s)')
    plt.show()

def main():
    # Parse the arguments
    parser = argparse.ArgumentParser(description='Generate a graph of quarterly data.')
    parser.add_argument('data', metavar='D', type=str, nargs='*', help='quarterly data')
    args = parser.parse_args()

    # Parse the provided data
    data = []
    for d in args.data:
        quarter_data = [float(x) if x != 'None' else None for x in d.split(',')]
        data.append(quarter_data)

    # Plot the graph
    plot_graph(data)

if __name__ == '__main__':
    main()