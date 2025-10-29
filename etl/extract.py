import pandas as pd
import os

def extract_data(file_id: str, output_dir: str = 'data/raw_ds') -> pd.DataFrame:
    file_url = f'https://drive.google.com/uc?id={file_id}&export=download'
    try:
        df = pd.read_csv(file_url)
    except Exception as e:
        raise RuntimeError(f"Ошибка загрузки данных: {e}")

    if df.empty:
        raise ValueError('CSV с данными пустой')

    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, 'downloaded_dataset.csv')
    df.to_csv(save_path, index=False)
    print(f'Сырые данные сохранены в {save_path}')
    return df

if __name__ == "__main__":
    FILE_ID = "1U3DpetAYEV6RiAhVdqMXeu1nmz0C45ec"
    extract_data(FILE_ID)
