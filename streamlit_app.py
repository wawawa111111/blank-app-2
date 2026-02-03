import streamlit as st
from supabase import create_client, Client

# --- 1. Supabase接続設定 ---
try:
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
except FileNotFoundError:
    st.error("設定ファイル (.streamlit/secrets.toml) が見つかりません。")
    st.stop()

# リソースをキャッシュして再接続を防ぐ
@st.cache_resource
def init_connection():
    return create_client(url, key)

supabase: Client = init_connection()

# --- 2. データベースからデータを取得する関数 ---
def get_pairing(roast, category):
    # coffee_pairings テーブルから、条件に合うものを検索
    response = supabase.table("coffee_pairings")\
        .select("*")\
        .eq("roast_level", roast)\
        .eq("food_category", category)\
        .execute()
    return response.data

# --- 3. アプリのUI構築 ---
st.set_page_config(page_title="Coffee Pairing DB", page_icon="☕")

st.title("☕ Supabase Coffee Pairing")
st.caption("Supabaseデータベースから最適な組み合わせを検索します")

st.divider()

# 入力フォーム
col1, col2 = st.columns(2)

with col1:
    st.subheader("焙煎度")
    # 選択肢はDBに合わせて設定
    roast_options = ["浅煎り", "中煎り", "深煎り"]
    selected_roast = st.selectbox("コーヒーのタイプは？", roast_options)

with col2:
    st.subheader("食べたいもの")
    category_options = ["食事", "スイーツ"]
    selected_category = st.selectbox("今の気分は？", category_options)

st.write("") # 余白

# 検索ボタン
if st.button("検索する 🔍", type="primary", use_container_width=True):
    
    # Supabaseに問い合わせ
    with st.spinner("データベースを検索中..."):
        results = get_pairing(selected_roast, selected_category)

    st.divider()

    # 結果表示
    if results:
        # データが見つかった場合（リストの最初の要素を取得）
        data = results[0]
        
        st.subheader("🎉 おすすめのペアリング")
        
        # カード風の表示
        st.markdown(
            f"""
            <div style="padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9;">
                <h2 style="color: #4a148c; margin-top: 0;">{data['menu_name']}</h2>
                <p><b>コーヒー:</b> {data['roast_level']} × <b>ジャンル:</b> {data['food_category']}</p>
                <hr>
                <p style="font-size: 16px;"><b>💡 理由:</b><br>{data['reason']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        # データが見つからなかった場合
        st.warning("該当するデータがデータベースに見つかりませんでした。")

# --- デバッグ用：全データ表示（開発時のみ便利） ---
with st.expander("データベースの中身を全て見る"):
    all_data = supabase.table("coffee_pairings").select("*").execute()
    st.dataframe(all_data.data)
