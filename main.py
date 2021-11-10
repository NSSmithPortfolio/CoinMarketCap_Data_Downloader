# Connects to CoinMarketCap API and downloads top 500 coins and outputs into excel named by date
# Use to watch for coins rising fast on CMC Rank (Market cap)


# Import Other Files
from CMCUtils import *
import pandas
import time
from os.path import exists


def main():
    already_ran = check_if_file_exists()
    already_ran = False  # uncomment this row for testing

    if already_ran is False:
        data_panda = create_starting_panda()
        data_panda = add_CMC_data(data_panda)
        data_panda = sort_panda_by_position(data_panda)
        print(data_panda)
        dump_to_excel(data_panda)  # has to occur after print to show warning the file is currently open
    else:
        print("File exists, exiting")


def check_if_file_exists():
    TodaysDate = time.strftime("%m-%d-%Y")
    excel_filename = "/CMCOutput - " + TodaysDate + ".xlsx"

    path_to_file = './outputs' + excel_filename

    file_exists = exists(path_to_file)

    return file_exists


def create_starting_panda():
    data = pandas.read_excel(r'.\CMCPandaTemplate.xlsx')
    data_panda = pandas.DataFrame(data,
                                  columns=['Coin', 'Name', 'CMC_Rank', 'CMC_Price',
                                           '90-Day', '60-Day',
                                           '30-Day', '7-Day', '24-Hour', 'URL'])

    return data_panda


def add_CMC_data(data_panda):
    cmc_data = pull_CMC_data()  # returns JSON object of data from CMC

    for k in cmc_data['data']:
        coin = k['symbol']
        coin_name = k['name']

        rank = k['cmc_rank']
        current_CMC_price = k['quote']['USD']['price']
        three_month_change = k['quote']['USD']['percent_change_90d']
        two_month_change = k['quote']['USD']['percent_change_60d']
        month_change = k['quote']['USD']['percent_change_30d']
        week_change = k['quote']['USD']['percent_change_7d']
        day_change = k['quote']['USD']['percent_change_24h']

        URL = "https://coinmarketcap.com/currencies/"
        formatted_coin_name = coin_name.replace(" ", "-")
        URL += formatted_coin_name
        URL += "/"

        new_row = {'CMC_Rank': rank, 'Coin': coin, 'Name': coin_name, 'CMC_Price': current_CMC_price,
                   '90-Day': three_month_change,
                   '60-Day': two_month_change, '30-Day': month_change,
                   '7-Day': week_change, '24-Hour': day_change,
                   'URL': URL}

        data_panda = data_panda.append(new_row, ignore_index=True)

        print(k)

    return data_panda


def dump_to_excel(data_panda):
    TodaysDate = time.strftime("%m-%d-%Y")
    excel_filename = "./outputs/CMCOutput - " + TodaysDate + ".xlsx"

    try:
        data_panda.to_excel(excel_filename, sheet_name='sheet1', index=False)
    except:
        excel_filename = "FileOpen" + TodaysDate + ".xlsx"
        data_panda.to_excel(excel_filename, sheet_name='sheet1', index=False)
        print("FILE OPEN, CLOSE AND RENAME")


def sort_panda_by_position(data_panda):
    sorted_panda = data_panda.sort_values(by=['CMC_Rank'], ascending=True)

    return sorted_panda


main()
