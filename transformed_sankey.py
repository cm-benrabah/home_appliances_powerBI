import pandas as pd

# Read both CSV files
df1 = pd.read_csv("vente.csv")  # Contains Source → Target1
df2 = pd.read_csv("movements.csv")  # Contains Target1 → Target2



df_selected1 = df1[["Region", "Wholesaler Name","Quantity Sold"]]

df_selected2 = df2[["Wholesaler Name", "Vendor Name","Quantity Sold to Vendor"]]



df_selected1.columns = ["Source", "Target","Quantity Sold"] # Wholesaler Name,Region
df_selected2.columns = ["Source", "Target","Quantity Sold"]



df_union = pd.concat([df_selected1, 
                      df_selected2], ignore_index=True)

# Display the result
print(df_union)

# Save the DataFrame to a CSV file
df_union.to_csv('transformed_sankey.csv', index=False)
