import csv
import pandas as pd
from sqlalchemy import create_engine, types

#engine
engine = create_engine('mysql://ryan:Abc123def!@#ghi@localhost/mydatabase') 

#csv transformation
df = pd.read_csv("Clients.csv",sep=',',quotechar='\'',encoding='utf8') 

#append table
df.to_sql('Clients',con=engine,index=False,if_exists='append')