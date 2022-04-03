from postgres_handler import PostgresHandler
from graphical_performance import Graph
from config import consts

pg_handler=PostgresHandler(
    host=consts.POSTGRES_HOST,
    database=consts.POSTGRES_DATABASE,
    user=consts.POSTGRES_USER,
    password=consts.POSTGRES_PASSWORD
)


def print_menu():
    print("\n[1]-----Search company by name, symbol or sector")
    print("[2]-----Search company by price or market capitalization")
    print("[3]-----Search company by financial indicators")
    print("[4]-----Pick company from list")
    print("[5]-----Remove company from a list")
    print("[8]-----Compare my companies")
    print("[9]-----Show my list of companies")
    print("[0]-----Quit searching\n")
    print("halaballa")

def print_cmp(list_of_cmp):
    for cmp in list_of_cmp:
        print("-------------------------------------------------")
        print("Company's ID:  "+ str(cmp.company_id))
        print("Name : "+ cmp.name + '     ' + "Symbol : "+ cmp.symbol)
        print("Sector : " + cmp.sector + '     ' + "Price : " + str(cmp.price))
        print("Market Cap : " + str(cmp.market_cap) + '     ' + "PE : " + str(cmp.pe))
        print("PB : " + str(cmp.pb) + '     ' + "PS : " + str(cmp.ps))
        print("EBITDA : " + str(cmp.ebitda) + '     ' + "EPS : " + str(cmp.eps))
        print("Div. Yield : " + str(cmp.div_yield) + '\n')


def print_search_by_name_symbol_sector():
    try:
        column = input("By what do you want to search, choose 1 of these - name, symbol, sector:  ")
        cmp = input("Enter name or symbol or sector of searched company:  ")
        cmp_sql = cmp.upper() + '%' if column == 'symbol' else cmp.title() + '%'
        result = pg_handler.search_by_name_symbol_sector(column, cmp_sql)
        print_cmp(result)
        return result

    except Exception as e:
        print("\nError with inserted data!")


def print_search_by_stock_price_or_marketcap():
    try:
        high_str = input("Enter upper stock price border or continue:  ")
        low_str = input("Enter lower stock price border or continue:  ")
        marketcap_str = input("Enter market cap of company or continue:  ")
        if not high_str.isnumeric():
            high = 9999999999999999
        else:
            high = int(high_str)

        if not low_str.isnumeric():
            low = 0
        else:
            low = int(low_str)

        if not marketcap_str.isnumeric():
            marketcap = 0
        else:
            marketcap = int(marketcap_str)
        result = pg_handler.search_by_sector_price_marketCap(high, low, marketcap)
        print_cmp(result)
        return result

    except Exception as e:
        print("\nError with inserted data!")


def print_search_by_financial_indicators():
    try:
        eps_str = input("Enter lower price border of EPS or continue:  ")
        pe_str = input("Enter price border of PE or continue:  ")
        pb_str = input("Enter price border of PB or continue:  ")
        ps_str = input("Enter price border of PS or continue:  ")
        if not eps_str.isnumeric():
            eps = -10000
        else:
            eps = int(eps_str)
        if not pe_str.isnumeric():
            pe = -10000
        else:
            pe = int(pe_str)
        if not pb_str.isnumeric():
            pb = -10000
        else:
            pb = int(pb_str)
        if not ps_str.isnumeric():
            ps = -10000
        else:
            ps = int(ps_str)

        result = pg_handler.search_by_financial_indicators(eps, pe, pb, ps)
        print_cmp(result)
        return result

    except Exception as e:
        print("Error with inserted data!")


def pick_company_from_list(budget, my_cmp):
    pick_cmp = input("Pick companies from a list, if you pick more than 1, please use ',':  ")
    for rank in pick_cmp.split(','):
        stop = False
        for cmp in my_cmp:
            if cmp.name != budget[int(rank) - 1].name:
                continue
            else:
                stop = True
                print("\nCompany is already in list!!!")
                break
        if not stop:
            # pg_handler.insert_company_into_table(budget[int(rank) - 1])
            my_cmp.append(budget[int(rank) - 1])
            print("\nSuccessfully added!")


def print_graphs(my_cmp, temp):
    if my_cmp == []:
        print("\nEmpty list")
        return
    choosen_graph = int(input("Graphs:\n"
                              "[1]-----Market capitalization\n"
                              "[2]-----PE\n"
                              "[3]-----PB\n"
                              "[4]-----PS\n"
                              "[5]-----EPS\n"
                              "[6]-----Dividend yield\n"
                              "Your choice:  "))
    if choosen_graph == 1:
        temp.market_cap_graph()
    elif choosen_graph == 2:
        temp.pe_graph()
    elif choosen_graph == 3:
        temp.pb_graph()
    elif choosen_graph == 4:
        temp.ps_graph()
    elif choosen_graph == 5:
        temp.eps_graph()
    elif choosen_graph == 6:
        temp.div_yield_graph()


def remove_company_from_list(my_cmp):
    if my_cmp == []:
        print("\nEmpty list")
        return

    idx = input("Enter company's ID:  ")
    my_cmp.remove(my_cmp[int(idx) - 1])
    print("\nSuccessfully removed")


def print_my_companies(my_cmp):
    if my_cmp == []:
        print("\nEmpty list")
        return

    counter = 1
    try:
        for cmp in my_cmp:
            cmp.company_id = counter
            counter += 1
        print_cmp(my_cmp)
    except ValueError as e:
        print("\nPlease continue")
        return


if __name__ == "__main__":
    my_cmp = []
    budget = []
    while True:
        temp = Graph(my_cmp)
        print_menu()

        choice_str = input("Select from menu:  ")

        if not choice_str.isnumeric():
            print("\nWrong input!!!\n")
            continue
        else:
            choice = int(choice_str)

        if choice == 0:
            break

        elif choice == 1:
            budget = print_search_by_name_symbol_sector()

        elif choice == 2:
            budget = print_search_by_stock_price_or_marketcap()

        elif choice == 3:
            budget = print_search_by_financial_indicators()

        elif choice == 4:
            pick_company_from_list(budget, my_cmp)

        elif choice == 5:
            remove_company_from_list(my_cmp)

        elif choice == 8:
            print_graphs(my_cmp, temp)

        elif choice == 9:
            print_my_companies(my_cmp)
