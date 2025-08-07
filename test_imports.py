import sys
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

try:
    import openai
    print("✅ OpenAI module imported successfully")
    print(f"OpenAI version: {openai.__version__}")
except ImportError as e:
    print(f"❌ Failed to import OpenAI: {e}")

try:
    import streamlit
    print("✅ Streamlit module imported successfully")
    print(f"Streamlit version: {streamlit.__version__}")
except ImportError as e:
    print(f"❌ Failed to import Streamlit: {e}")

try:
    import dotenv
    print("✅ python-dotenv module imported successfully")
except ImportError as e:
    print(f"❌ Failed to import python-dotenv: {e}")
