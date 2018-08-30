from app import create_app
from app.database import Database

import os
import sys
sys.path.append(os.getcwd())

config_name = "development"
app = create_app(config_name)

if __name__ =='__main__':
    db = Database()
    db.create_tables()   
    app.run()