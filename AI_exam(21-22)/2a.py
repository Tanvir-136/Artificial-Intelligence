import math 
import numpy as np
import pandas as pd
import pprint

# Step 1: Create dataset manually
data = {
    "Outlook": [
        "sunny", "sunny", "overcast", "rainy", "rainy", "rainy", "overcast",
        "sunny", "sunny", "rainy", "sunny", "overcast", "overcast", "rainy",
    ],
    "Temperature": [
        "hot", "hot", "hot", "mild", "cool", "cool", "cool",
        "mild", "cool", "mild", "mild", "mild", "hot", "mild",
    ],
    "Humidity": [
        "high", "high", "high", "high", "normal", "normal", "normal",
        "high", "normal", "normal", "normal", "high", "normal", "high",
    ],
    "Windy": [
        "false", "true", "false", "false", "false", "true", "true",
        "false", "false", "false", "true", "true", "false", "true",
    ],
    "Play": [
        "no", "no", "yes", "yes", "yes", "no", "yes",
        "no", "yes", "yes", "yes", "yes", "yes", "no",
    ],
}
df = pd.DataFrame(data)

# Step 2: Entropy function
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy = 0
    for i in range(len(elements)):
        p = counts[i] / np.sum(counts)
        entropy += -p * math.log2(p)
    return entropy

# print(entropy)
#step 3 : Information gain
def info_gain(data, split_attribute_name,target_name = "Play"):
    total_entropy = entropy(data[target_name])
    vals, counts = np.unique(data[split_attribute_name], return_counts=True)

    weighted_entropy = 0
    for i in range(len(vals)):
        subset = data[data[split_attribute_name] == vals[i]]
        weighted_entropy += (counts[i] / np.sum(counts)) * entropy(subset[target_name])

    information_gain = total_entropy - weighted_entropy
    return information_gain

# Step 4: Recursive ID3 function
def id3(data, originaldata, features, target_attribute_name="Play", parent_node_class=None):
    unique_classes = np.unique(data[target_attribute_name])
    if len(unique_classes) == 1:
        return unique_classes[0]
    elif len(data) == 0:
        majority_class = np.unique(originaldata[target_attribute_name])[
            np.argmax(np.unique(originaldata[target_attribute_name], return_counts=True)[1])
        ]
        return majority_class
    elif len(features) == 0:
        return parent_node_class
    else:
        parent_node_class = np.unique(data[target_attribute_name])[
            np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])
        ]
        item_values = [info_gain(data, feature, target_attribute_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]

        tree = {best_feature: {}}
        features = [i for i in features if i != best_feature]

        for value in np.unique(data[best_feature]):
            sub_data = data[data[best_feature] == value]
            subtree = id3(sub_data, data, features, target_attribute_name, parent_node_class)
            tree[best_feature][value] = subtree

        return tree
    
# Step 5: Build and display tree
features = df.columns[:-1]
tree = id3(df, df, features)

print("\nDecision Tree (built manually):\n")
pprint.pprint(tree)

# Step 6: Final decision
majority_class = np.unique(df["Play"])[
    np.argmax(np.unique(df["Play"], return_counts=True)[1])
]
print("\nFinal Decision:", majority_class)