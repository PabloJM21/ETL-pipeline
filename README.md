# ETL Pipeline for Manufacturers’ Shipments, Inventories, and Orders

This project is an ETL pipeline that processes data from the U.S. Census Bureau related to manufacturers’ shipments, inventories, and orders. The pipeline extracts data from a public API, transforms it into a usable format, and loads it into a structured set of CSV files.

## Data Description

The data corresponds to Manufacturers’ Shipments, Inventories, and Orders from the U.S. Census Bureau. Each CSV file within the `processed` data folder contains the monthly percentual change in a specific data type for several manufacturing categories (which can be found [here](INSERT_LINK_HERE)). 

The specific data types included in this project are:

- **Value of Shipments (MPCVS)**
- **New Orders (MPCNO)**
- **Unfilled Orders (MPCUO)**
- **Total Inventories (MPCTI)**

## Structure

sales-data-etl/
│
├── data/
│   ├── raw_data.json                  # Raw data extracted from the API
│   └── processed/                     # Processed CSV files
│       ├── MPCVS_data.csv             # CSV file for Value of Shipments
│       ├── MPCNO_data.csv             # CSV file for New Orders
│       ├── MPCUO_data.csv             # CSV file for Unfilled Orders
│       └── MPCTI_data.csv             # CSV file for Total Inventories
│
├── extract_data.py                    # Script to extract the raw data
├── run_etl.py                         # Script for the etl pipeline


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
