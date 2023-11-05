import pandas as pd
import matplotlib.pyplot as plt
import datetime

def data_visualization(receipt_df):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'b', 'w']
    for i in range(52):
        plt.plot(receipt_df['day_of_week'][i*7+3:i*7+10], receipt_df['count'][i*7+3:i*7+10], color=colors[i%8])

    plt.show()

def preprocess_data(receipt_df):
    date_col = receipt_df['# Date']
    new_df = {
        'year': [],
        'month': [],
        'day': [],
        'week': [],
        'day_of_week': [],
        'count': receipt_df['Receipt_Count']
    }

    for row in date_col:
        year, month, day = row.split('-')
        date = datetime.date(int(year), int(month), int(day))
        new_df['year'].append(year)
        new_df['month'].append(month)
        new_df['day'].append(day)
        new_df['week'].append(date.isocalendar()[1])
        new_df['day_of_week'].append(date.isoweekday())

    return pd.DataFrame(data=new_df)

if __name__ == "__main__":
    receipt_df = preprocess_data(pd.read_csv('data_daily.csv'))
    print(receipt_df)
