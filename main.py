import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from google.cloud import bigquery
import settings

def set_environment():
    """Set up the environment variable for Google Cloud authentication."""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GOOGLE_APPLICATION_CREDENTIALS

def init_webdriver():
    """Initialize and return a Chrome WebDriver."""
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)

def scrape_job_postings(driver):
    """Scrape job postings from a fake job board and return them as a list of dictionaries."""
    driver.get(settings.JOB_BOARD_URL)
    time.sleep(settings.PAGE_LOAD_DELAY)  # Ensure the page has loaded completely
    
    jobs = []
    job_cards = driver.find_elements(By.CLASS_NAME, "card-content")
    
    for card in job_cards:
        title = card.find_element(By.CLASS_NAME, "title").text
        company = card.find_element(By.CLASS_NAME, "company").text
        content = card.find_element(By.CLASS_NAME, "content").text
        location_date_list = content.rsplit('\n', 1)
        location = location_date_list[0].strip()
        date_posted = location_date_list[1]
        
        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "date_posted": date_posted
        })
    
    return jobs

def upload_df_to_bigquery(dataframe, project_id, dataset_id, table_name):
    """Upload a pandas DataFrame to a BigQuery table."""
    client = bigquery.Client()
    dataset_id = f"{project_id}.{dataset_id}"
    
    # Construct a full Dataset object to send to the API.
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = settings.BIGQUERY_LOCATION
    try:
       dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
       print("Created dataset {}.{}".format(client.project, dataset.dataset_id))
    except:
        print("Dataset already exists")
        
    table_id = f"{dataset_id}.{table_name}"
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        write_disposition='WRITE_TRUNCATE',
        create_disposition='CREATE_IF_NEEDED'
    )
    
    try:
        job = client.load_table_from_dataframe(dataframe, table_id, job_config=job_config)
        job.result()  # Wait for the job to complete
        print(f"Data uploaded successfully to {table_id}")
    except Exception as e:
        print(f"Failed to upload data: {e}")
        raise

def main():
    """Main function to orchestrate the scraping and uploading processes."""
    set_environment()
    driver = init_webdriver()
    
    try:
        jobs = scrape_job_postings(driver)
        jobs_df = pd.DataFrame(jobs)
        jobs_df['date_posted'] = pd.to_datetime(jobs_df['date_posted'], errors='coerce', format='%Y-%m-%d')
        upload_df_to_bigquery(jobs_df, settings.BIGQUERY_PROJECT_ID, settings.BIGQUERY_DATASET_ID, settings.BIGQUERY_TABLE_NAME)
    finally:
        driver.quit()
        print("WebDriver session has been closed.")

if __name__ == "__main__":
    main()