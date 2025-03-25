# ヒューリスティック探索アルゴリズム

このリポジトリは書籍『[ヒューリスティック探索 合理的なAIをつくるためのアルゴリズム](https://www.amazon.co.jp/dp/4065392187)』の実装コードと練習問題の解答を収録しています。

## 目次
- [プロジェクト概要](#プロジェクト概要)
- [ディレクトリ構成](#ディレクトリ構成)
- [セットアップ方法](#セットアップ方法)
- [実装アルゴリズム一覧](#実装アルゴリズム一覧)
- [コードの実行方法](#コードの実行方法)
- [練習問題の解答](#練習問題の解答)
- [ライセンス](#ライセンス)
- [参考文献](#参考文献)

## プロジェクト概要
このリポジトリには以下の内容が含まれます：
- 教科書で紹介されている探索アルゴリズムのPython実装
- 各章の練習問題の解答
- サンプル問題とテストケース

## ディレクトリ構成
- `src/`: アルゴリズム実装ファイル
  - 探索アルゴリズム（A*、ダイクストラ法、ビームサーチなど）
  - データ構造（優先度付きキュー、ハッシュテーブル）
  - 問題領域（グリッド経路探索、スライディングタイルパズル、巡回セールスマン問題）
- `answers/`: 練習問題解答
  - 解説付きJupyterノートブック
  - 問題文のLaTeXソース

## セットアップ方法
1. リポジトリをクローン：
```bash
git clone https://github.com/yourusername/heuristic-search-answers.git
cd heuristic-search-answers
```

2. Python環境の準備（3.8以上推奨）：
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. 必要なパッケージをインストール：
```bash
pip install -r requirements.txt
```

## 実装アルゴリズム一覧
| アルゴリズム | ファイル名 |
|-------------|------------|
| A*探索 | `astar_search.py` |
| ダイクストラ法 | `dijkstra.py` |
| ビームサーチ | `beam_search.py` |
| 分枝限定法 | `branch_and_bound.py` |
| 幅優先探索 | `breadth_first_search.py` |
| 深さ優先探索 | `depth_first_search.py` |
| 反復深化A* | `iterative_deepening_astar.py` |
| 貪欲最良優先探索 | `greedy_best_first_search.py` |

## 状態空間問題一覧
| 問題 | ファイル名 |
|-------------|------------|
| グリッド経路探索問題 | `grid_pathfinding.py` |


## コードの実行方法
各アルゴリズムは独立したスクリプトとして実装されています。例：
```bash
python src/astar_search.py
```

特定の問題を解く場合：
```bash
python src/grid_pathfinding.py
```

## 練習問題の解答
`answers/`ディレクトリに各章の解答があります：
- `chapter2.ipynb`: 第2章の解答
- `chapter3.ipynb`: 第3章の解答

Jupyterノートブックを実行：
```bash
jupyter notebook answers/chapter2.ipynb
```

## ライセンス
このプロジェクトはMITライセンスで公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 参考文献
- [ヒューリスティック探索 合理的なAIをつくるためのアルゴリズム (KS情報科学専門書)](https://www.hanmoto.com/bd/isbn/9784065392188)
- 陣内 佑(著/文) 発行：講談社
