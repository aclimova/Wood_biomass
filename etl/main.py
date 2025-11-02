import argparse
from extract import extract_data
from validate import validate
from transform import transform
from load import get_engine, load_and_write_data

def main():
    parser = argparse.ArgumentParser(description="ETL pipeline")
    parser.add_argument(
        "--file_id",
        type=str,
        required=True,
        help="Google Drive file ID для загрузки данных"
    )
    parser.add_argument(
        "--table_name",
        type=str,
        default="klimova",
        help="Имя таблицы в базе данных"
    )

    args = parser.parse_args()

    df_raw = extract_data(args.file_id)

    if not validate(df_raw):
        print("Валидация не пройдена. Завершение работы.")
        return

    df_transformed = transform(df_raw)
    engine = get_engine()
    load_and_write_data(engine, table_name=args.table_name)

if __name__ == "__main__":
    main()
