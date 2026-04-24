# learn-celery
learn celery from scratch

# Step 1: install dependencies
pip install -r requirements.txt

# step 2: run fast api app
bash: uvicorn main:app --reload

# step 3: run celery
bash: celery -A celery_worker.celery_app worker --loglevel=info


