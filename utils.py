from google.oauth2 import service_account
from googleapiclient.discovery import build 

def chunk_array(array, n):
    for i in range(0, len(array), n): 
        yield array[i:i + n]

def insert_event(request_id, response, exception):
    if exception is not None:
      return exception
    else:
      return response

def indexing_api(urls):
  scopes = [ "https://www.googleapis.com/auth/indexing" ]

  JSON_KEY_FILE = "./client_secrets.json"
  credentials = service_account.Credentials.from_service_account_file(JSON_KEY_FILE, scopes=scopes)
  
  service = build('indexing', 'v3', credentials=credentials)

  batch = service.new_batch_http_request()

  for url in urls:
    batch.add(service.urlNotifications().publish(body={"url": url, "type": "URL_UPDATED"}))

  batch.execute()