import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///jobs.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or '52ea511f52d8e6125c8a73e30d8e1db2632cd681c2e70d8b'

    
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or '832ba57f1e968292bdd10ec1aaad50f08922367449e6b9bf'

    
    MONGO_URI = os.environ.get('DATABASE_URL') or 'mongodb+srv://amitanshusa2003:AB8GBHoAThFDkxlb@cluster0.ndmlqhp.mongodb.net/job_portal_db?retryWrites=true&w=majority'

   