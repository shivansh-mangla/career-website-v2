from supabase import create_client
import os

API_URL = os.environ['DATABASE_API_URL']
API_KEY = os.environ['DATABASE_API_KEY']
supabase = create_client(API_URL, API_KEY)


def load_jobs_from_db():
  data = supabase.table('jobs').select('*').execute().data
  JOBS = []
  for row in data:
    JOBS.append(row)
  return JOBS
