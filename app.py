import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def generate_bar_chart(data_file, reference_file):
    # Read the data from the Excel files into DataFrames
    data_df = pd.read_excel(data_file)
    reference_df = pd.read_excel(reference_file)

    # Merge the data DataFrame with the reference DataFrame on the "Table_Name" column
    merged_df = pd.merge(data_df, reference_df, on='Table_Name', how='left')

    # Group by table group and calculate total row count for each group
    table_group_summary = merged_df.groupby('Table_Group')['Row_Count'].sum()

    # Plot bar chart for each table group
    plt.figure(figsize=(10, 6))
    table_group_summary.plot(kind='bar')
    plt.title('Total Row Count by Table Group')
    plt.xlabel('Table Group')
    plt.ylabel('Total Row Count')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot()

# Streamlit app title
st.title('Table Group Bar Chart')

# Sidebar file upload
data_file = st.sidebar.file_uploader("Upload Data File", type=["xlsx"])
reference_file = st.sidebar.file_uploader("Upload Reference File", type=["xlsx"])

# Display the bar chart if files are uploaded
if data_file and reference_file:
    generate_bar_chart(data_file, reference_file)
else:
    st.write("Please upload both data and reference files.")
