def create_features(df):
    df['price_per_area'] = df['price'] / df['area']
    return df