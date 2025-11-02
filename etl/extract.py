import pandas as pd
import os
import gdown

def extract_data(file_id: str, output_dir: str = 'data/raw_ds') -> pd.DataFrame:
    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, 'downloaded_dataset.csv')
    url = f'https://drive.google.com/uc?id={file_id}'
  
    gdown.download(url, save_path, quiet=False)
 
    df = pd.read_csv(save_path)
    
    if df.empty:
        raise ValueError('CSV с данными пустой')
    
    print(f'Сырые данные сохранены в {save_path}')
    return df

if __name__ == "__main__":
    FILE_ID = "1U3DpetAYEV6RiAhVdqMXeu1nmz0C45ec"
    extract_data(FILE_ID)


