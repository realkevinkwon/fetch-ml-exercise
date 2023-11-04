import pandas as pd
import matplotlib.pyplot as plt
import datetime

def data_visualization(receipt_data):
    fig, ax = plt.subplots()

    plt.show()

def preprocess_data(receipt_df):
    date_col = receipt_df['# Date']
    new_df = {
        'year': [],
        'month': [],
        'day': [],
        'day_of_week': [],
        'count': receipt_df['Receipt_Count']
    }

    for row in date_col:
        year, month, day = row.split('-')
        new_df['year'].append(year)
        new_df['month'].append(month)
        new_df['day'].append(day)
        new_df['day_of_week'].append(
            datetime.date.weekday(
                datetime.date(int(year), int(month), int(day))
            )
        )

    return pd.DataFrame(data=new_df)

if __name__ == "__main__":
    receipt_df = preprocess_data(pd.read_csv('data_daily.csv'))
    print(receipt_df)
