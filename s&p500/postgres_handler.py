import psycopg2
import psycopg2.extras

from psycopg2 import sql
from create_cmp import Company
from config import consts

class PostgresHandler:
    def __init__(self, host, database, user, password):
        self.connection = None
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def convert_to_object(self, result):
        list_of_companies = []
        counter = 1
        for cmp in result:
            company = Company(counter, cmp[1], cmp[2], cmp[3], cmp[4], cmp[5], cmp[6], cmp[7], cmp[8], cmp[9], cmp[10],
                              cmp[11])
            list_of_companies.append(company)
            counter += 1
        return list_of_companies

    def search_by_name_symbol_sector(self, column, cmp):
        if self.connection == None or self.connection.closed:
            self.connect()

        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            search_cmp = sql.SQL(
                """
                    SELECT *
                    FROM {}
                    WHERE {} LIKE {}
                    ORDER BY name
                """
            ).format(
                sql.Identifier(consts.TABLE_NAME),
                sql.Identifier(column),
                sql.Literal(cmp)
            )
            cur.execute(search_cmp)
            result = cur.fetchall()
            converted_to_object = self.convert_to_object(result)

        self.connection.close()
        return converted_to_object

    def search_by_sector_price_marketCap(self, high, low, marketCap):
        if self.connection == None or self.connection.closed:
            self.connect()

        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            search_cmp = sql.SQL(
                """
                    SELECT *
                    FROM {}
                    WHERE {} > {} AND {} < {} AND {} > {}
                    ORDER BY sector, price DESC 

                """
            ).format(
                sql.Identifier(consts.TABLE_NAME),
                sql.Identifier(consts.COLUMN_PRICE),
                sql.Literal(low),
                sql.Identifier(consts.COLUMN_PRICE),
                sql.Literal(high),
                sql.Identifier(consts.MARKETCAP),
                sql.Literal(marketCap)
            )
            cur.execute(search_cmp)
            result = cur.fetchall()
            converted_to_object = self.convert_to_object(result)

        self.connection.close()
        return converted_to_object

    def search_by_financial_indicators(self, eps, pe, pb, ps):
        if self.connection == None or self.connection.closed:
            self.connect()

        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            search_cmp = sql.SQL(
                """
                    SELECT *
                    FROM {}
                    WHERE {} > {} AND {} > {} AND {} > {} AND {} > {}
                    ORDER BY sector, eps DESC 

                """
            ).format(
                sql.Identifier(consts.TABLE_NAME),
                sql.Identifier(consts.EPS),
                sql.Literal(eps),
                sql.Identifier(consts.PE),
                sql.Literal(pe),
                sql.Identifier(consts.PB),
                sql.Literal(pb),
                sql.Identifier(consts.PS),
                sql.Literal(ps)
            )
            cur.execute(search_cmp)
            result = cur.fetchall()
            converted_to_object = self.convert_to_object(result)

        self.connection.close()
        return converted_to_object

    # def insert_company_into_table(self, cmp):
    #     if self.connection == None or self.connection.closed:
    #         self.connect()
    #
    #     with self.connection, self.connection.cursor() as cur:
    #         insert_cmp = sql.SQL(
    #             """
    #                 INSERT INTO {} ({})
    #                 VALUES ({})
    #             """
    #         ).format(
    #             sql.Identifier(consts.TABLE_INVESTOR_NAME),
    #             sql.SQL(', ').join(map(sql.Identifier, consts.sql_columns)),
    #             sql.SQL(', ').join(map(sql.Literal, [cmp.name, cmp.symbol, cmp.sector, cmp.price, cmp.market_cap, cmp.pe, cmp.pb, cmp.ps, cmp.ebitda, cmp.eps, cmp.div_yield]))
    #         )
    #         cur.execute(insert_cmp)
    #
    #     self.connection.close()

