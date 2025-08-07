import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# 環境変数を読み込み
load_dotenv()

def get_expert_response(input_text: str, expert_type: str) -> str:
    """
    入力テキストと専門家タイプを受け取り、LLMからの回答を返す関数
    
    Args:
        input_text (str): ユーザーからの入力テキスト
        expert_type (str): 選択された専門家のタイプ
    
    Returns:
        str: LLMからの回答
    """
    # 専門家タイプに応じたシステムメッセージを定義
    expert_prompts = {
        "プログラミング専門家": """
あなたは経験豊富なソフトウェアエンジニアです。
プログラミング言語、アルゴリズム、ソフトウェア設計、デバッグなどの技術的な質問に対して、
実践的で分かりやすい解答を提供してください。
コード例がある場合は、コメントを含めて説明してください。
        """,
        "データサイエンティスト": """
あなたは経験豊富なデータサイエンティストです。
統計学、機械学習、データ分析、データの可視化などに関する質問に対して、
実用的で詳細な解答を提供してください。
必要に応じて、具体的な手法やツールの使用方法も説明してください。
        """,
        "ビジネスコンサルタント": """
あなたは経験豊富なビジネスコンサルタントです。
経営戦略、マーケティング、組織運営、プロジェクト管理などのビジネス課題に対して、
戦略的で実行可能な解決策を提案してください。
具体的な事例や手順も含めて説明してください。
        """,
        "健康・医療アドバイザー": """
あなたは健康と医療に関する知識を持つアドバイザーです。
一般的な健康管理、予防医学、栄養学、運動療法などに関する質問に対して、
科学的根拠に基づいた情報を提供してください。
ただし、具体的な診断や治療については医師に相談するよう促してください。
        """,
        "教育コンサルタント": """
あなたは教育分野の専門家です。
学習方法、教育技術、カリキュラム設計、スキル開発などの教育に関する質問に対して、
効果的で実践的なアドバイスを提供してください。
年齢や学習レベルに応じた具体的な方法も提案してください。
        """
    }
    
    # OpenAI APIキーの確認
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "エラー: OpenAI APIキーが設定されていません。"
    
    try:
        # LangChainのChatOpenAIを初期化
        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            openai_api_key=api_key
        )
        
        # メッセージを構成
        system_message = SystemMessage(content=expert_prompts.get(expert_type, expert_prompts["プログラミング専門家"]))
        human_message = HumanMessage(content=input_text)
        
        # LLMに質問を送信
        response = llm([system_message, human_message])
        
        return response.content
        
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

def main():
    # ページ設定
    st.set_page_config(
        page_title="AI専門家コンサルタント",
        page_icon="🧠",
        layout="wide"
    )
    
    # アプリのタイトル
    st.title("🧠 AI専門家コンサルタント")
    st.markdown("---")
    
    # アプリの概要説明
    st.markdown("""
    ## 📋 アプリケーション概要
    
    このアプリケーションは、様々な分野の専門家AIとして振る舞うチャットボットです。
    専門分野を選択し、質問や相談を入力すると、その分野の専門家として詳細な回答を提供します。
    
    ### 🔧 操作方法
    1. **専門家を選択**: 下のラジオボタンから相談したい分野の専門家を選択してください
    2. **質問を入力**: テキストエリアに質問や相談内容を入力してください
    3. **回答を取得**: 「回答を取得」ボタンをクリックして専門家の回答を表示します
    
    ### 🎯 利用可能な専門分野
    - **プログラミング専門家**: ソフトウェア開発、アルゴリズム、技術的課題
    - **データサイエンティスト**: データ分析、機械学習、統計
    - **ビジネスコンサルタント**: 経営戦略、マーケティング、組織運営
    - **健康・医療アドバイザー**: 健康管理、栄養、予防医学
    - **教育コンサルタント**: 学習方法、スキル開発、教育技術
    """)
    
    st.markdown("---")
    
    # メイン機能のレイアウト
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🎯 専門家選択")
        
        # 専門家選択のラジオボタン
        expert_type = st.radio(
            "相談したい専門分野を選択してください:",
            [
                "プログラミング専門家",
                "データサイエンティスト", 
                "ビジネスコンサルタント",
                "健康・医療アドバイザー",
                "教育コンサルタント"
            ],
            help="選択した分野の専門家として回答します"
        )
        
        # 選択された専門家の説明を表示
        expert_descriptions = {
            "プログラミング専門家": "💻 ソフトウェア開発、コーディング、技術的問題解決の専門家",
            "データサイエンティスト": "📊 データ分析、機械学習、統計処理の専門家",
            "ビジネスコンサルタント": "📈 経営戦略、マーケティング、ビジネス課題解決の専門家",
            "健康・医療アドバイザー": "🏥 健康管理、栄養学、予防医学の専門家",
            "教育コンサルタント": "📚 学習方法、教育技術、スキル開発の専門家"
        }
        
        st.info(expert_descriptions[expert_type])
    
    with col2:
        st.subheader("💭 質問・相談内容")
        
        # テキスト入力フォーム
        user_input = st.text_area(
            "質問や相談内容を入力してください:",
            height=200,
            placeholder="例: Pythonでデータを効率的に処理する方法を教えてください。",
            help="詳細な質問ほど、より具体的な回答が得られます"
        )
        
        # 回答取得ボタン
        if st.button("🚀 回答を取得", type="primary", use_container_width=True):
            if user_input.strip():
                with st.spinner(f"{expert_type}が回答を作成中..."):
                    # 専門家からの回答を取得
                    response = get_expert_response(user_input, expert_type)
                    
                    # 回答を表示
                    st.subheader("📝 専門家の回答")
                    st.markdown(f"**{expert_type}からの回答:**")
                    st.markdown(response)
                    
                    # 追加の情報
                    st.markdown("---")
                    st.info("💡 **ヒント**: さらに詳しい情報が必要な場合は、より具体的な質問をしてみてください。")
            else:
                st.warning("⚠️ 質問内容を入力してください。")
    
    # フッター
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🤖 Powered by OpenAI GPT-3.5 & LangChain | 作成者: AI専門家コンサルタント</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()