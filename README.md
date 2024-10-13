# ETL Pipeline for Manufacturers’ Shipments, Inventories, and Orders

This project is an ETL pipeline that extracts data from a public API and transforms it for better analysis.

The data extracted from the API corresponds to Manufacturers’ Shipments, Inventories, and Orders from the U.S. Census Bureau. 

A more accurate description of the dataset can be found [here]([(https://api.census.gov/data/timeseries/eits/advm3.html)]).

# Data variables

The data extracted contains the following variables:

- `data_type_code`: The code corresponding to the monthly outcome and its percentual change of each data type. These data types, along with their codes are: Value of Shipments (VS, MPCVS), New Orders (NO, MPCNO), Unfilled Orders (UO, MPCUO) and Total Inventories (TI, MPCTI).  
- `seasonally_adj`: Denotes wheather the outcome has been seasonally adjusted. 
- `category_code`: Indicates the manufacture category.
- `cell_value`: The outcome of the corresponding data type.
- `time`: Indicates the year and month. 

# Pipeline structure

The pipeline is divided in two stages. In the first one, raw data is extracted from the API corresponding to the last 5 years.
In the second one, the data is filtered to retain only the monthly percentual change that has been seasonally adjusted. Then, it is organized such that the cell values are split across time and category. They are stored in different csv files according to the four data types.
This allows to compare the evolution of the monthly percentual changes between all categories. 


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
├── run_etl.py                         # Script for the etl pipeline. Filters seasonally adjusted data for the monthly percentage change and t

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
