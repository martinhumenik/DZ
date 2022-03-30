from postgres_handler import PostgresHandler
from psycopg2 import sql
from config import consts

pg_handler=PostgresHandler(
    host=consts.POSTGRES_HOST,
    database=consts.POSTGRES_DATABASE,
    user=consts.POSTGRES_USER,
    password=consts.POSTGRES_PASSWORD
)


def create_sp_table(pg_handler):
    if pg_handler.connection == None or pg_handler.connection.closed:
        pg_handler.connect()

    with pg_handler.connection, pg_handler.connection.cursor() as cur:
        create_table_query=sql.SQL(
            """
                DROP TABLE IF EXISTS {};
                CREATE TABLE {}(
                    company_id SERIAL PRIMARY KEY,
                    name VARCHAR (128),
                    symbol VARCHAR (128),
                    sector VARCHAR (128),
                    price FLOAT ,
                    market_cap FLOAT ,
                    PE FLOAT ,
                    PB FLOAT ,
                    PS FLOAT ,
                    EBITDA FLOAT ,
                    EPS FLOAT ,
                    div_yield FLOAT
                );
            """
        ).format(
            sql.Identifier(consts.TABLE_NAME),
            sql.Identifier(consts.TABLE_NAME)
        )
        cur.execute(create_table_query)
    pg_handler.connection.close()


def create_investor_table(pg_handler):
    if pg_handler.connection == None or pg_handler.connection.closed:
        pg_handler.connect()

    with pg_handler.connection, pg_handler.connection.cursor() as cur:
        create_table_query=sql.SQL(
            """
                DROP TABLE IF EXISTS {};
                CREATE TABLE {}(
                    company_id SERIAL PRIMARY KEY,
                    name VARCHAR (128),
                    symbol VARCHAR (128),
                    sector VARCHAR (128),
                    price FLOAT ,
                    market_cap FLOAT ,
                    PE FLOAT ,
                    PB FLOAT ,
                    PS FLOAT ,
                    EBITDA FLOAT ,
                    EPS FLOAT ,
                    div_yield FLOAT
                );
            """
        ).format(
            sql.Identifier(consts.TABLE_INVESTOR_NAME),
            sql.Identifier(consts.TABLE_INVESTOR_NAME)
        )
        cur.execute(create_table_query)
    pg_handler.connection.close()


create_sp_table(pg_handler)
create_investor_table(pg_handler)
