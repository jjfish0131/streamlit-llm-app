# 🧠 AI専門家コンサルタント

LangChainとOpenAI GPTを使用した専門家AI相談アプリケーションです。

## 📋 概要

このアプリケーションでは、以下の専門分野から選択して、その分野の専門家として振る舞うAIに相談することができます：

- 💻 **プログラミング専門家**: ソフトウェア開発、コーディング、技術的問題解決
- 📊 **データサイエンティスト**: データ分析、機械学習、統計処理
- 📈 **ビジネスコンサルタント**: 経営戦略、マーケティング、ビジネス課題解決
- 🏥 **健康・医療アドバイザー**: 健康管理、栄養学、予防医学
- 📚 **教育コンサルタント**: 学習方法、教育技術、スキル開発

## 🚀 使用方法

1. 専門分野をラジオボタンから選択
2. 質問や相談内容をテキストエリアに入力
3. 「回答を取得」ボタンをクリック
4. 選択した専門家からの詳細な回答を確認

## 🛠️ 技術スタック

- **Frontend**: Streamlit
- **LLM Framework**: LangChain
- **AI Model**: OpenAI GPT-3.5 Turbo
- **Python Version**: 3.11

## 📦 依存関係

```
streamlit>=1.28.0
python-dotenv>=1.0.0
openai>=1.0.0
langchain>=0.1.0
langchain-openai>=0.1.0
```

## ⚙️ セットアップ

### ローカル環境

1. リポジトリをクローン
```bash
git clone https://github.com/jjfish0131/streamlit-llm-app.git
cd streamlit-llm-app
```

2. 仮想環境を作成・アクティベート
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. 依存関係をインストール
```bash
pip install -r requirements.txt
```

4. 環境変数を設定
`.env`ファイルを作成し、OpenAI APIキーを設定：
```
OPENAI_API_KEY=your_openai_api_key_here
```

5. アプリケーションを実行
```bash
streamlit run app.py
```

### Streamlit Community Cloud

1. [Streamlit Community Cloud](https://share.streamlit.io/)にアクセス
2. GitHubリポジトリを連携
3. デプロイ設定で以下を指定：
   - **Python version**: 3.11 (`.python-version`ファイルで指定済み)
   - **Main file path**: `app.py`
4. Secretsに`OPENAI_API_KEY`を設定
5. デプロイを実行

## 🔐 セキュリティ

- OpenAI APIキーは環境変数として安全に管理
- `.env`ファイルは`.gitignore`に含まれており、リポジトリにはコミットされません
- 本番環境では適切なシークレット管理を実装

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🤝 貢献

プルリクエストや Issue の報告を歓迎します！

## 📞 サポート

質問や問題がある場合は、GitHub Issues でお知らせください。
