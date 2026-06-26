import requests
import json
import sys

# ご提示いただいた最新データ取得用APIアドレス
URL = "https://densho-bato.com/member/get_json_data_latest?term_id=1&pgn=miyagawa01"

def fetch_and_save():
    try:
        response = requests.get(URL, timeout=15)
        # ステータスコードが200(正常)かチェック
        if response.status_code == 200:
            raw_data = response.json()
            
            # 念のため、正しくデータが入っているか構造を簡易チェック
            if "term" in raw_data and len(raw_data["term"]) > 0:
                # 綺麗にインデント整形してファイルに上書き保存
                with open("data.json", "w", encoding="utf-8") as f:
                    json.dump(raw_data, f, ensure_ascii=False, indent=2)
                print("最新データの自動取得・保存に成功しました。")
            else:
                print("警告: 取得したデータの構造が想定と異なります。")
        else:
            print(f"エラー: サーバーからエラー応答が返されました (Status: {response.status_code})")
            sys.exit(1)
            
    except Exception as e:
        print(f"例外エラーが発生しました: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_and_save()
