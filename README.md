# ☕ Coffee Pairing App (Supabase Edition)

コーヒーの「焙煎度」と「今の気分」を入力すると、Supabaseデータベースから最適な「ごはん（フード・スイーツ）」のペアリングを検索・提案してくれるWebアプリです。

## 🚀 デモ
（ここにStreamlit Cloudなどのデプロイ先URLがあれば貼る）
* https://your-app-url.streamlit.app/

## ✨ 機能
* **ペアリング検索:** 焙煎度（浅煎り・中煎り・深煎り）とカテゴリ（食事・スイーツ）を選択して検索。
* **データベース連携:** Supabase（PostgreSQL）に保存されたデータから、リアルタイムに情報を取得。
* **詳細表示:** 具体的なメニュー名と、その組み合わせが美味しい理由を表示。

## 🛠 使用技術
* **Frontend:** Python, Streamlit
* **Database:** Supabase (PostgreSQL)
* **Library:** `streamlit`, `supabase`

## ⚙️ セットアップ手順 (ローカル環境)

### 1. リポジトリのクローン
```bash
git clone [https://github.com/あなたのユーザー名/リポジトリ名.git](https://github.com/あなたのユーザー名/リポジトリ名.git)
cd リポジトリ名
