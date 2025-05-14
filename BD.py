import pymysql
import pandas as pd

connexion = pymysql.connect(
    host="charlydb.cb4cow8oeq2r.us-west-1.rds.amazonaws.com",
    user="admin",
    password="K31n3ng3l#",
    database="CharlyDB",
    port=3306
)