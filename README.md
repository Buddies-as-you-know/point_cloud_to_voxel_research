# 改善
もっと上手い人がいた場合、改善をお願いします。
## pullrequestの出し方
https://qiita.com/takamii228/items/80c0996a0b5fa39337bd
# 開発環境
計算機(実際にプログラムを動かすマシン)のOS：Ubuntu

コードエディタ：VS Code
# ssh接続
## github
https://qiita.com/shizuma/items/2b2f873a0034839e47ce
# python環境構築
## 採用技術
### Pyenv
pythonのマイナーバージョンのインストール及びプロジェクトごとに使用するpythonの切り替えを行います。
### venv
pythonの仮想環境の構築を行います。
### Poetry
使用する外部ライブラリの依存関係の管理を行います。
## インストール
### Pyenv

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
# pyenvでインストールできるpythonバージョンを更新するために必要
git clone https://github.com/pyenv/pyenv-update.git $(pyenv root)/plugins/pyenv-update
pyenv update
# pyenv-updateを入れなくても、以下のコマンドでできます。
cd ~/.pyenv && git fetch && git pull
```

### Poetry

```bash
#可能な限り最新のstableのpythonバージョンを指定(poetryの最新バージョンが入らないので3.6とかは使わない)
pyenv local <python-version>
#公式のインストーラーを使用してインストール
curl -sSL https://install.python-poetry.org | python3 -  
#pathを設定。$HOMEのところをは適宜書き換える。上記インストールのときの出力に実行コマンドが書かれている。例：Add `export PATH="/home/username/.local/bin:$PATH"` to your shell configuration file.
echo PATH="$HOME/.local/bin:$PATH" >> ~/.bashrc 
#poetryで作る仮想環境をプロジェクト直下に生成するようにする。その他の設定はpoetry config --listで見れる
poetry config virtualenvs.in-project true 
```
## それで結局どういう流れで使うんですか
例えば、最新版のpython3.11.0を使ったpython-demoというプロジェクトを作る場合は、以下のような操作をすることになります。
```bash
# ディレクトリ作成
mkdir python-demo
cd python-demo
# pythonバージョンのインストールとそのディレクトリで使用するpythonバージョンの指定
pyenv install 3.11.0
pyenv local 3.11.0
# 仮想環境の構築
python -m venv .venv
# poetryの初期設定
poetry init
# ライブラリの追加
poetry add <package> # プログラムの動作に必要なパッケージの追加
# poetry addで対応できないパッケージはpyproject.tomlに記述して以下のコマンドを打つ
poetry update
# sample.pyというプログラムを書いたら、以下のコマンドで実行
poetry run python sample.py
```

# 静的解析＆自動整形
読みにくいコードを避けるのとコードの書き方を統一する。
今後、コードを共有する機会が来たときに読みにくいものをなくすため
https://zenn.dev/zenizeni/books/a64578f98450c2/viewer/ac820f

上記のサイトの真似をする。
コードの書き方を出来る限り統一する。
型もできる限り書く（サボらない）

https://flake8.pycqa.org/en/latest/
https://mypy-lang.org/

# Makefile
コマンドひとつで自動化できるのがめちゃくちゃ便利。

```bash
make lint
```
規約に即しているかの確認

```bash
make format
```
コードの自動整形




# docker
dockerは再現性を保つために使用する。
環境に依存しなくなるためdockerがあれば再現可能になる。
しかし、起動が遅い。
open3dを動かすためにimageはubunutを使用

```Dockerfile
# This could also be another Ubuntu or Debian based distribution
# This could also be another Ubuntu or Debian based distribution
FROM ubuntu:22.04
# Install Open3D system dependencies 
ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    curl \
    gcc \
    libegl1 \
    libgl1 \
    libgomp1 \
    wget \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Size reduction by removing unnecessary things
RUN apt-get autoremove -y
# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
# Set the path for Poetry
ENV PATH /root/.local/bin:$PATH

# Prevent Poetry from creating a virtual environment
RUN poetry config virtualenvs.create false

# Create project directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

# Copy code for experimentation
COPY . .

```
## 実行時
src配下のmain.pyが実行されるようになっている。
```bash
make build
```

## open3d用
http://www.open3d.org/docs/release/docker.html

## GPGエラーを起こした場合
https://qiita.com/nissei777/items/9758b8f5140f2b8957a4
```
docker pull ubuntu
```
### 容量がいっぱいな場合
https://qiita.com/zembutsu/items/f577ea8dad6dc64d70b6
```bash
make delete
```

#　ディレクトリ構成
https://github.com/drivendata/cookiecutter-data-science

上記を参照して少し改造中、現状まだ足りてません。

```
.
├── Dockerfile
├── Makefile
├── README.md
├── Reports   論文を書くのに必要な図などを入れる。
│   └── Figuare
├── data　　　
│   ├── result
│   └── row
├── docker-compose.yml
├── docs　　　ここに生成されパラメータのoutputを入れる。
├── poetry.lock
├── pyproject.toml
└── src
    ├── __init__.py
    ├── config
    ├── features
    ├── main.py
    └── models

```
https://zenn.dev/hpp/articles/6307447e5a037d
階層をsrcより上に入れる場合は上記のサイト参照

# 実験設定の管理


# 参考文献

https://zenn.dev/zenizeni/books/a64578f98450c2/viewer/e5747f

https://speakerdeck.com/hpprc/zi-yuan-tositejian-rushi-yan-puroguramu

https://www.slideshare.net/cvpaperchallenge/tips-ver2-250474910




# やること
- [ ] ハードコーディング解消
- [ ] 点群をボクセル化してボクセル一つを大きくする。
- [ ] ボクセルの保存方法を模索
- [ ] unreal engineへの追加
