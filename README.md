
# Data Quality Dashboard Application

## Overview
This application is designed to visualize data quality check logs and provide insights into the data health of a system. It is split into two main parts:

1. **Dashboard**: Visualizes the results from the check log CSV, providing a quick overview of the data quality checks performed.
2. **Log Details**: Allows users to view failed checks in a tabular format, enter remarks for any check, and persist these back to a CSV stored in a GCP bucket.

## Prerequisites
- **Docker**: This application is containerized with Docker. Ensure that you have Docker installed and running on your system.
- **GCP Account**: Deployment is done using Google Cloud Run, which requires a valid Google Cloud Platform (GCP) account.

## Local Development
To run the application locally, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the root of the project directory.
3. Build the Docker image:
   ```sh
   docker build -t data_quality_dashboard -f docker/Dockerfile .
   ```
4. Run the Docker container:
   ```sh
   docker run -p 8501:8501 data_quality_dashboard
   ```
5. Visit `http://localhost:8501` in your web browser to access the application.

## Deployment to Cloud Run
To deploy the application on Google Cloud Run, you must:

1. Have a valid GCP account and gcloud CLI installed.
2. Configure the gcloud CLI with your account and select the project.
3. Deploy the container to Cloud Run using the following command:
   ```sh
   gcloud run deploy --image gcr.io/YOUR_PROJECT_ID/data_quality_dashboard --platform managed
   ```
   Replace `YOUR_PROJECT_ID` with your actual GCP project ID.

## Contributing
Contributions to the project are welcome! Please follow the standard fork, branch, and pull request workflow.

## License
Specify your license or if the project is in the public domain.
