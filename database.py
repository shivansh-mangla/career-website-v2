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


def load_job_from_db(id):
  data = supabase.table('jobs').select('*').eq('id', id).execute().data
  if len(data) == 0:
    return None
  return data[0]


def add_application_to_db(job_id, data):
  supabase.table('applications').insert([{
      'job_id':
      job_id,
      'full_name':
      data['full_name'],
      'email':
      data['email'],
      'linkedin_url':
      data['linkedin_url'],
      'education':
      data['education'],
      'work_experience':
      data['work_experience'],
      'resume_url':
      data['resume_url']
  }]).execute()
