import json
import psycopg2

from psycopg2 import sql
from config import consts

conn=psycopg2.connect(
    host=consts.POSTGRES_HOST,
    database=consts.POSTGRES_DATABASE,
    user=consts.POSTGRES_USER,
    password=consts.POSTGRES_PASSWORD
)

with open("dataset/s&p500.json", "r") as f:
    sp = json.load(f)

f.close()


def required_data(cmp):
    return [cmp['Name'], cmp['Symbol'], cmp['Sector'], cmp['Price'], cmp['Market Cap'], cmp['Price/Earnings'],
            cmp['Price/Book'], cmp['Price/Sales'], cmp['EBITDA'], cmp['Earnings/Share'], cmp['Dividend Yield']]


def insert_data():
    with conn, conn.cursor() as cur:
        for company_id in range(0, len(sp)):
            insert_company=sql.SQL(
                """
                    INSERT INTO {} ({})
                    VALUES ({})
                """
            ).format(
                sql.Identifier(consts.TABLE_NAME),
                sql.SQL(', ').join(map(sql.Identifier, consts.sql_columns)),
                sql.SQL(', ').join(map(sql.Literal, required_data(sp[company_id])))
            )
            cur.execute(insert_company)

    conn.close()


insert_data()
