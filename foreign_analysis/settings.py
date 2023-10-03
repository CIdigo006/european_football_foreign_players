from dotenv import load_dotenv
import os
import sys
load_dotenv()

api_key = os.environ.get("api_key")
api_host = os.environ.get("api_host")
api_domain = os.environ.get("api_domain")
s3_path = os.environ.get("S3_PATH")
glue_db = os.environ.get("GLUE_DB")