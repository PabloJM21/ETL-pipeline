# Sales Data ETL Pipeline with Data.gov API

This project demonstrates an ETL pipeline that extracts sales data from the [Data.gov API](https://api.data.gov/), transforms it, and loads it into a SQL database for further analysis.

## Features
- **API Integration**: Fetches dynamic retail sales data from Data.gov from 2020 to 2024.
- **Data Extraction, Transformation and Loading**: Extracts only seasonally adjusted data that corresponds to the monthly percentual changes in the sales for each data type in each category. 
- **Data Transformation**: Aggregates the data
- **Database Loading**: Stores the processed data in a relational database using SQL.

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
