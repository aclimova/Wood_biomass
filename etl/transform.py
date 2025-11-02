import pandas as pd
import os

def load_and_write_data() -> pd.DataFrame:
    df = pd.read_csv("data/raw_ds/downloaded_dataset.csv")
    df = df.head(100)
    print("Колонки до трансформации:", df.columns.tolist())
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    if 'Unnamed: 0' in df.columns:
        df = df.rename(columns={'Unnamed: 0': 'Number'})

    numeric_cols = ['dbh', 'wood', 'bark', 'root', 'rootsk', 'branch']
    categorical_cols = ['species', 'fac26']

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype('category')
            df[col] = df[col].cat.add_categories(['Unknown'])
            df[col] = df[col].fillna('Unknown')
            if not isinstance(df[col].dtype, pd.CategoricalDtype):
                print(f"Внимание: колонка {col} не категориальная после преобразования")

    print("Данные преобразованы. Типы колонок:")
    print(df.dtypes)
    print("Колонки после переименования:", df.columns.tolist())

    return df

if __name__ == "__main__":
    df = load_and_write_data()
    df_transformed = transform(df)
    print("Трансформация завершена")

