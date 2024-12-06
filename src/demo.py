import pandas as pd
import os

## get project root directory
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

## get paths to the JSON files
first_file_path = os.path.join(root_dir, "streaming_history_1.json")
second_file_path = os.path.join(root_dir, "streaming_history_2.json")
third_file_path = os.path.join(root_dir, "streaming_history_3.json")

## load json files
first_streaming_history = pd.read_json(first_file_path)
second_streaming_history = pd.read_json(second_file_path)
third_streaming_history= pd.read_json(third_file_path)

##  concat all streaming history
combined_streaming_history = pd.concat([first_streaming_history, second_streaming_history, third_streaming_history], ignore_index=True)
print(combined_streaming_history.head())