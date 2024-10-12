# Sales Data ETL Pipeline with Data.gov API

This project demonstrates an ETL pipeline that extracts sales data from the [Data.gov API](https://api.data.gov/), transforms it, and loads it into a SQL database for further analysis.

## Features
- **API Integration**: Fetches dynamic retail sales data from Data.gov.
- **Data Transformation**: Cleans and aggregates the data for better insights.
- **Database Loading**: Stores the processed data in a relational database using SQL.
- **Automation**: Script can be scheduled using cron jobs for automatic daily updates.

## Setup Instructions

### Prerequisites
- Python 3.8 or above
- PostgreSQL or MySQL (or any preferred SQL database)
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
    1. **Extract data** from the API:
       ```bash
       python extract_data.py
       ```
    2. **Transform** the extracted data:
       ```bash
       python transform.py
       ```
    3. **Load** the data into the database:
       ```bash
       python load.py
       ```

### Automating the Pipeline
You can schedule the pipeline to run at regular intervals using cron jobs.

```bash
# Open the cron editor
crontab -e

# Add this line to schedule the ETL pipeline to run daily at 2 AM
0 2 * * * /usr/bin/python3 /path/to/your/repo/extract_data.py
