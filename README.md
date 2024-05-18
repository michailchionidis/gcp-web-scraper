# Automated Web Scraper for Python Job Listings on Google Cloud Platform

## Project Overview
This repository showcases an automated web scraper developed to extract Python job listings, demonstrating the setup of a complete data pipeline on Google Cloud Platform (GCP).

## Project Architecture
![Project Architecture](<img width="865" alt="Screenshot 2024-05-05 at 3 43 24 PM" src="https://github.com/michailchionidis/gcp-web-scraper/assets/104796421/25aeae3b-5631-4605-b8c9-c170b7ca1b97">
)

## Skills Demonstrated
- **Web Scraping**: Uses Selenium for automated extraction of job listing data.
- **Cloud Automation**: Implements Cloud Run and Cloud Scheduler for deploying and scheduling the scraper.
- **Data Management**: Utilizes BigQuery for efficient data storage and management.
- **Data Visualization**: Employs Looker Studio for creating insightful visual dashboards.

## Technologies Used
- Python, Selenium
- Google Cloud Platform: Cloud Run, Cloud Scheduler, BigQuery, Looker Studio

## Project Files
- `main.py`: Main script for scraping job listings.
- `app.py`: Flask application for deploying the scraper as a web service.
- `settings.py`: Configuration settings for API keys and database connections.
- `requirements.txt`: Lists all Python dependencies.
- `Dockerfile`: Docker configuration for building the application.

## Setup and Installation
### Prerequisites
- A Google Cloud Platform account. [Start your free trial here](https://cloud.google.com/free).
- Basic knowledge of Python and Selenium for web scraping.

### Configuration and Deployment
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/python-job-scraper.git
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Test the main.py locally to ensure the scraper functions correctly.**
   -  Run app.py using Flask locally to validate the web service.
   -  Deploy on Google Cloud Run

4. **Deploy on Google Cloud.**
   - Deploy the containerized Flask application on Cloud Run.
   - Set up Cloud Scheduler to automate the scraping process.

### Running the Project
   - Ensure all settings in settings.py are correctly configured, deploy the scraper to Google Cloud Run, and manage the scraping schedule with Cloud Scheduler.

Contributions to this project are welcome! Please fork this repository and submit a pull request with your proposed changes.

## Acknowledgments
This project is provided by [DataProjects.io](https://dataprojects.io), a platform that helps data professionals build a portfolio of real-world, end-to-end projects on the cloud.

## License
This project is licensed under the Mozilla Public License 2.0 - see the [LICENSE](LICENSE) file for details.
