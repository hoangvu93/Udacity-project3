import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="techconfdbsvr.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="techconfdbsvr@techconfdbsvr" #TODO: Update value
    POSTGRES_PW="admin@123456789"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'Os47f1tLxRXhdm_CDKf5772Pcm-XhVhHLSIvWiNkji0uAzFu8R-4nw=='
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://notificationqueue.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=3b/HgsJcWbM4rvQTLhT/vb6oQ1YbZO5cHuZF4+axXic=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'danhth90@gmail.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False