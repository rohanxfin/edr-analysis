gcloud auth login

gcloud artifacts repositories create edr-analysis-repo --repository-format=docker --location=us-west1 --project=ai-projects-453411 --description="Docker repository for edr app"

docker build -t us-west1-docker.pkg.dev/ai-projects-453411/edr-analysis-repo/edr-analysis-app .

docker push us-west1-docker.pkg.dev/ai-projects-453411/edr-analysis-repo/edr-analysis-app


gcloud run deploy edr-analysis-app --image us-west1-docker.pkg.dev/ai-projects-453411/edr-analysis-repo/edr-analysis-app --platform managed --region us-west1 --allow-unauthenticated --memory 8Gi --cpu 2 --timeout 300 --execution-environment=gen2 --max-instances=2
