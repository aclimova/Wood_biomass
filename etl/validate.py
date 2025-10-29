import pandas as pd

def validate(df: pd.DataFrame) -> bool:
    if df.empty:
        print("Ошибка: DataFrame пустой.")
        return False

    required_columns = [
        'dbh', 'wood', 'bark', 'root', 'rootsk', 'branch', 
        'species', 'fac26'
    ]
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        print(f"Ошибка: отсутствуют колонки {missing_cols}")
        return False

    duplicates_count = df.duplicated().sum()
    if duplicates_count > 0:
        print(f"Обнаружено дубликатов строк: {duplicates_count}. Рекомендуется их удалить.")

    numeric_cols = ['dbh', 'wood', 'bark', 'root', 'rootsk', 'branch']
    categorical_cols = ['species', 'fac26']

    is_valid = True
    for col in numeric_cols:
        if col in df.columns:
            if not pd.api.types.is_numeric_dtype(df[col]):
                print(f"Ошибка: колонка {col} не числовая")
                is_valid = False

    for col in categorical_cols:
        if col in df.columns:
            if not isinstance(df[col].dtype, pd.CategoricalDtype):
                print(f"Внимание: колонка {col} не категориальная")

    if is_valid:
        print("Валидация пройдена успешно.")
    else:
        print("Валидация завершена с ошибками.")
    return is_valid


if __name__ == "__main__":
    df = pd.read_csv("data/raw_ds/downloaded_dataset.csv")  # Используй свой путь
    validate(df)

