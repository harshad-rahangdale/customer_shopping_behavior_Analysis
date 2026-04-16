import pandas as pd

# Load Excel file
# df = pd.read_excel("customer_shopping_behavior.csv")   # replace with your actual file name
# import pandas as pd

df = pd.read_csv(r"D:\New folder (2)\customer_shopping_behavior.csv")
print(df.head())
# Show first 5 rows
print(df.head())
df=pd.read_csv('customer_shopping_behavior.csv')
print(df.head())          # top 5 valuse 

print(df.info())          # datatypes 

print(df.describe())      # numerical colums 

print(df.describe(include="all"))  # catogoricall data 

print(df.isnull().sum())  # find some null values 

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df['Review Rating']) 

print(df.isnull().sum())

df.columns = df.columns.str.lower()
df.columns =  df.columns.str.replace(' ','_')

print(df.columns)

df = df.rename(columns={'purchase_amount_(usd)' : 'purchase_amount'})
print(df)

# create a column age_group

labels =[ 'Young Adult','Adult' ,'middlle-aged','Senior']

df['age_group'] =pd.qcut(df['age'],q=4,labels=labels)

print(df[['age','age_group']].head(10))

# create column purchase_frequency_days

frequency_mapping= {
    'Fortnightly':14,
    'weekly':7,
    'monthly':30,
    'Quarterly':90,
    'Bi-Weekly' :14,
    'Annually' :365,
    'Every 3 Months': 90
}

df['purchase_frequwncy_days'] =df['frequency_of_purchases'].map(frequency_mapping)

print(df[['purchase_frequwncy_days','frequency_of_purchases']].head(10))

print(df[['discount_applied','promo_code_used']].head(10))

print((df['discount_applied']==df['promo_code_used']).all())

df=df.drop('promo_code_used',axis=1)
print(df.columns)




import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

database = "Customer_behavior"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harshad@1234",
    database=database,
    port=3306
)

print("Connected to MySQL")

# engine = create_engine(f"mysql+pymysql://root:Harshad@1234@localhost:3306/{database}")
engine = create_engine(
    "mysql+pymysql://root:Harshad%401234@localhost:3306/Customer_behavior"
)

# Write DataFrame to MySQL
table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)

# Read back sample
print(pd.read_sql("SELECT * FROM customer LIMIT 5;", engine))