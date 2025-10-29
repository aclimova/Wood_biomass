from extract import extract_data
from validate import validate
from transform import transform
from load import get_engine, load_and_write_data

def main():
    FILE_ID = "1U3DpetAYEV6RiAhVdqMXeu1nmz0C45ec"
    df_raw = extract_data(FILE_ID)

    if not validate(df_raw):
        print("Валидация не пройдена. Завершение работы.")
        return

    df_transformed = transform(df_raw)
    engine = get_engine()
    load_and_write_data(engine, table_name="klimova")

if __name__ == "__main__":
    main()

