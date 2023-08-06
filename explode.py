import pandas as pd

#import df

# Assuming df is your DataFrame and 'tags' is the column with the list of tags
df['tags'] = df['tags'].apply(lambda x: x if isinstance(x, list) else [x])  # Ensure all rows have a list, even if it's a list with a single element

# if tags is comma seperated string
#df['tags'] = df['tags'].apply(lambda x: x.split(","))  # Ensure all rows have a list, even if it's a list with a single element
exploded_df = df.explode('tags')  # Explode the DataFrame on the 'tags' column

dummies_df = pd.get_dummies(exploded_df, columns=['tags'])  # Get dummies for the 'tags' column

# Then, if you want to remove duplicates (i.e., if a single row had the same tag multiple times and you just want to indicate whether the tag was present or not), you can do the following:
final_df = dummies_df.groupby(dummies_df.columns.difference(['tags']).tolist()).max().reset_index()

#final_df
# id is_spaghetti is_sugar
# 1   0             1
# 2   1             0