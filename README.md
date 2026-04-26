# ETL Pipeline for Manufacturers’ Shipments, Inventories, and Orders

This project is an ETL pipeline that extracts data from a public API and transforms it for better analysis.

The data extracted from the API corresponds to Manufacturers’ Shipments, Inventories, and Orders from the U.S. Census Bureau. 

A more accurate description of the dataset can be found here: https://api.census.gov/data/timeseries/eits/advm3.html.

The ETL pipeline is divided into two main stages:

1. **Data Extraction**:  
   Raw data is extracted from the U.S. Census Bureau API, covering the last five years of Manufacturers’ Shipments, Inventories, and Orders data. This data is stored in a JSON file for the next stage.

2. **Data Transformation and Organization**:  
   The extracted data is filtered to retain only seasonally adjusted records that represent monthly percentual changes. The data is then reorganized such that the cell values are separated by time and manufacturing category. Finally, the data is saved into four separate CSV files, each corresponding to one of the following data types:  
   - Value of Shipments (MPCVS)  
   - New Orders (MPCNO)  
   - Unfilled Orders (MPCUO)  
   - Total Inventories (MPCTI)  

   This structure allows for easy comparison of the evolution of monthly percentual changes across different manufacturing categories for each data type.

# Data variables

The data extracted contains the following variables:

- `data_type_code`: The code corresponding to the data types, starting with "MPC" for the montlhy percentual change.
- `seasonally_adj`: Denotes whether the outcome has been seasonally adjusted. 
- `category_code`: Indicates the manufacture category.
- `cell_value`: The outcome of the corresponding data type.
- `time`: Indicates the year and month. 






## Project Directory Structure

```plaintext
sales-data-etl/
├── data/
│   ├── raw_data.json                  # Raw data extracted from the API
│   └── processed/                     # Processed CSV files
│       ├── MPCVS_data.csv             # CSV file for Value of Shipments
│       ├── MPCNO_data.csv             # CSV file for New Orders
│       ├── MPCUO_data.csv             # CSV file for Unfilled Orders
│       └── MPCTI_data.csv             # CSV file for Total Inventories
│
├── extract_data.py                    # Script to extract the raw data from the API corresponding to the last 5 years
├── run_etl.py                         # Script for the etl pipeline. Filters, transforms and loads data into four csv files.

```

## Setup Instructions

### Prerequisites
- Python 3.8 or above
- MySQL 
- API Key from Data.gov (sign up [here](https://api.data.gov/signup/))

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/PabloJM21/sales-data-etl.git
    cd sales-data-etl
    ```

2. Install required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:
    Create a `.env` file in the root directory and add your Data.gov API key:
    ```bash
    DATAGOV_API_KEY=your_api_key_here
    ```

4. Run the ETL pipeline:
    1. **Retrieve data** from the API:
       ```bash
       python extract_data.py
       ```
    2. **Extract, Transform and Load** the raw data:
       ```bash
       run_etl.py
       ```





| train \ test | flsim | arcgis | real |
|---|---|---|---|
| flsim | prec0.25(pixel): 0.891<br>**rec0.25(pixel): 0.873**<br>ap50: 0.790<br>ap50_90: 0.527<br>**throughput: 39.480** | prec0.25(pixel): 0.805<br>rec0.25(pixel): 0.782<br>ap50: 0.518<br>ap50_90: 0.280<br>throughput: 39.480 | **prec0.25(pixel): 0.931**<br>rec0.25(pixel): 0.868<br>**ap50: 0.898**<br>**ap50_90: 0.567**<br>throughput: 14.630 |
| arcgis | prec0.25(pixel): 0.841<br>rec0.25(pixel): 0.791<br>ap50: 0.544<br>ap50_90: 0.313<br>throughput: 42.990 | prec0.25(pixel): 0.847<br>**rec0.25(pixel): 0.863**<br>ap50: 0.741<br>ap50_90: 0.494<br>**throughput: 55.290** | **prec0.25(pixel): 0.925**<br>rec0.25(pixel): 0.820<br>**ap50: 0.863**<br>**ap50_90: 0.601**<br>throughput: 16.030 |
| all | prec0.25(pixel): 0.869<br>**rec0.25(pixel): 0.885**<br>ap50: 0.769<br>ap50_90: 0.495<br>throughput: 49.110 | prec0.25(pixel): 0.854<br>rec0.25(pixel): 0.861<br>ap50: 0.736<br>ap50_90: 0.487<br>**throughput: 54.660** | **prec0.25(pixel): 0.932**<br>rec0.25(pixel): 0.885<br>**ap50: 0.939**<br>**ap50_90: 0.675**<br>throughput: 18.100 |








| train \ test | flsim | arcgis | real |
|---|---|---|---|
| flsim | **prec0.25(pixel): 0.949**<br>**rec0.25(pixel): 0.941**<br>ap50: 0.989<br>**ap50_90: 0.898**<br>**throughput: 37.370** | prec0.25(pixel): 0.888<br>rec0.25(pixel): 0.935<br>**ap50: 0.994**<br>ap50_90: 0.755<br>throughput: 34.450 | prec0.25(pixel): 0.944<br>rec0.25(pixel): 0.903<br>ap50: 0.973<br>ap50_90: 0.859<br>throughput: 17.620 |
| arcgis | prec0.25(pixel): 0.873<br>rec0.25(pixel): 0.913<br>ap50: 0.978<br>ap50_90: 0.695<br>**throughput: 56.960** | prec0.25(pixel): 0.913<br>**rec0.25(pixel): 0.942**<br>**ap50: 0.994**<br>**ap50_90: 0.832**<br>throughput: 42.570 | **prec0.25(pixel): 0.931**<br>rec0.25(pixel): 0.873<br>ap50: 0.954<br>ap50_90: 0.813<br>throughput: 20.940 |
| all | prec0.25(pixel): 0.930<br>**rec0.25(pixel): 0.955**<br>ap50: 0.989<br>ap50_90: 0.875<br>throughput: 54.440 | prec0.25(pixel): 0.924<br>rec0.25(pixel): 0.934<br>**ap50: 1.000**<br>ap50_90: 0.820<br>**throughput: 61.860** | **prec0.25(pixel): 0.940**<br>rec0.25(pixel): 0.921<br>ap50: 1.000<br>**ap50_90: 0.877**<br>throughput: 22.710 |
