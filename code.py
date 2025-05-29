import pandas as pd
import os
# Sample data
data={"Name":["sandeep","KV"],"Age":[22,22]}
# Creating a data frame
df=pd.DataFrame(data)
# Creating a data directory
data_dir="data"
os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,"sample_data.csv")
df.to_csv(file_path,index=False)
print("File has been saved")