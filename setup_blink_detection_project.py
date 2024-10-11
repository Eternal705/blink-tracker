import os

# プロジェクトのルートディレクトリ
base_dir = 'blink-detection-system'

# 各ディレクトリの構成
directories = [
    os.path.join(base_dir, 'data'),                # データ関連のディレクトリ
    os.path.join(base_dir, 'dataset'),             # 新しく追加したデータセット用ディレクトリ
    os.path.join(base_dir, 'models'),              # モデル保存用ディレクトリ
    os.path.join(base_dir, 'scripts'),             # スクリプト用ディレクトリ
    os.path.join(base_dir, 'results'),             # 結果出力用ディレクトリ
    os.path.join(base_dir, 'notebooks'),           # Jupyter notebooks用ディレクトリ
    os.path.join(base_dir, 'tests'),               # テスト関連ディレクトリ
    os.path.join(base_dir, 'config'),              # 設定ファイル用ディレクトリ
    os.path.join(base_dir, 'docs')                 # ドキュメント用ディレクトリ
]

# 各ディレクトリを作成
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# ファイルの作成
files = [
    os.path.join(base_dir, 'README.md'),                # プロジェクトのREADME
    os.path.join(base_dir, 'requirements.txt'),         # 必要なパッケージリスト
    os.path.join(base_dir, 'scripts', 'main.py'),       # メインスクリプト
    os.path.join(base_dir, 'config', 'config.yaml'),    # 設定ファイル
    os.path.join(base_dir, 'tests', 'test_blink.py')    # テストファイル
]

# 空のファイルを作成
for file in files:
    with open(file, 'w') as f:
        if 'README.md' in file:
            f.write('# Blink Detection System\n\nプロジェクトの概要や目的をここに記述します。\n')
        elif 'requirements.txt' in file:
            f.write('# 必要なパッケージリスト\n')
        elif 'config.yaml' in file:
            f.write('# 設定ファイル\n\n# パラメータの設定を行います。\n')
        else:
            f.write('# TODO: Implement this file\n')

print("瞬き検知プロジェクトのディレクトリ構成が作成されました。")
