def clean_data(df):
    df = df.drop_duplicates()
    df.fillna(df.mean(numeric_only=True), inplace=True)
    return df