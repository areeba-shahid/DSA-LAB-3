import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
# df = pd.read_csv('Train.csv')

# # print(df.head())

# symptom_columns = df.columns[:-1]  


# for symptom in symptom_columns:
#     plt.figure(figsize=(6, 4))
#     plt.scatter(df[symptom], df['TYPE'], alpha=0.5)
#     plt.title(f'Scatter plot of {symptom} vs Disease TYPE')
#     plt.xlabel(symptom)
#     plt.ylabel('Disease TYPE')
#     plt.xticks([0, 1]) 
#     plt.show()




# main_df = pd.read_csv('Train.csv')  
# test_df = pd.read_csv('Test.csv')    


# predicted_labels = []


# for _, test_row in test_df.iterrows():

#     # Calculate the distance to all main entries
#     distances = np.sqrt(((main_df.iloc[:, :-1] - test_row[:-1]) ** 2).sum(axis=1))
    
 
#     closest_index = distances.idxmin()
    
#     # Get the label of the closest entry
#     predicted_labels.append(main_df.loc[closest_index, 'TYPE'])

# # Add predicted labels to the test.csv
# test_df['Predicted Label'] = predicted_labels
# test_df.to_csv('Test.csv', index=False)
# # Show the result
# print(test_df)

# Total Time Complexity:

#                         O(m⋅n⋅k)
# Where:
# m = number of test entries
# n = number of entries in the main dataset
# k = number of symptoms (columns)


# main_df = pd.read_csv('Train.csv')

# # Split the data into Part1(with TYPE) and Part2 (without labels)
# part1 = main_df.copy()              
# part2 = part1.drop(columns=['TYPE']) 

# # Keep the original labels for  calculation
# original_labels = part1['TYPE'].values


# part1_values = part1.iloc[:, :-1].values
# part2_values = part2.values


# predicted_labels_part2 = []


# for test_row in part2_values:
#     distances = np.sqrt(((part1_values - test_row) ** 2).sum(axis=1))
#     closest_index = np.argmin(distances)
#     predicted_labels_part2.append(part1.iloc[closest_index]['TYPE'])

# # Calculate accuracy
# correct_predictions = sum(np.array(predicted_labels_part2) == original_labels)
# accuracy_percentage = (correct_predictions / len(original_labels)) * 100

# print(f'Accuracy: {accuracy_percentage:.2f}%')



#     Recursive algorithm 



import sys
sys.setrecursionlimit(50000)

def calculate_distance(test_row, train_data):
    return np.sqrt(((train_data - test_row) ** 2).sum(axis=1))

def knn_recursive(test_rows, train_data, train_labels, index=0, predictions=None):
    if predictions is None:
        predictions = []

    # Base case:
    if index >= len(test_rows):
        return predictions

   
    distances = calculate_distance(test_rows[index], train_data)

   
    closest_index = np.argmin(distances)
    predictions.append(train_labels[closest_index])

   
    return knn_recursive(test_rows, train_data, train_labels, index + 1, predictions)

# Load data
main_df = pd.read_csv('Train.csv')
part1 = main_df.copy()              
part2 = part1.drop(columns=['TYPE'])

# Keep the original labels for calculation
original_labels = part1['TYPE'].values
part1_values = part1.iloc[:, :-1].values
part2_values = part2.values


predicted_labels_part2 = knn_recursive(part2_values, part1_values, original_labels)

# Calculate accuracy
correct_predictions = sum(np.array(predicted_labels_part2) == original_labels)
accuracy_percentage = (correct_predictions / len(original_labels)) * 100

print(f'Accuracy: {accuracy_percentage:.2f}%')
