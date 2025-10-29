import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = ['dbh', 'wood', 'bark', 'root', 'rootsk', 'branch']
    categorical_cols = ['species', 'fac26']
    
    # Преобразование числовых столбцов
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    # Преобразование категориальных столбцов
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype('category')  # Явное преобразование
            df[col] = df[col].cat.add_categories(['Unknown'])
            df[col] = df[col].fillna('Unknown')
            if not isinstance(df[col].dtype, pd.CategoricalDtype):
                print(f"Внимание: колонка {col} не категориальная после преобразования")
    
    print("Данные преобразованы. Типы колонок:")
    print(df.dtypes)
    
    return df

def load_and_write_data():
    df = pd.read_csv("data/raw_ds/downloaded_dataset.csv")
    df = df.head(100)
    
    if df.columns[0].startswith("Unnamed"):
        new_columns = df.columns.tolist()
        new_columns[0] = "Number"
        df.columns = new_columns
    
    return df

if __name__ == "__main__":
    df = load_and_write_data()
    df_transformed = transform(df)
    print("Трансформация завершена")


