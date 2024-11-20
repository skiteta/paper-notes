import os
import re
import streamlit as st
import torch
from transformers import CLIPProcessor, CLIPModel
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# CLIPモデルのロード
@st.cache_resource
def load_clip_model():
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    return model, processor


model, processor = load_clip_model()

# 論文ファイルのディレクトリ
NOTES_DIR = "../notes"


# メタデータとSummary抽出関数
def extract_metadata(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    metadata = {}
    metadata["file"] = file_path
    metadata["title"] = re.search(r"(.*?)\n", content).group(1) if re.search(r"(.*?)\n", content) else "N/A"
    metadata["authors"] = re.search(r"Authors: \[(.*?)\]", content).group(1) if re.search(r"Authors: \[(.*?)\]",
                                                                                          content) else "N/A"
    metadata["year"] = re.search(r"Year: (\d{4})", content).group(1) if re.search(r"Year: (\d{4})", content) else "N/A"
    metadata["category"] = re.search(r"Category: (.*?)\n", content).group(1) if re.search(r"Category: (.*?)\n",
                                                                                          content) else "N/A"
    metadata["topics"] = re.search(r"Topics: \[(.*?)\]", content).group(1) if re.search(r"Topics: \[(.*?)\]",
                                                                                        content) else "N/A"
    metadata["keywords"] = re.search(r"Keyword: \[(.*?)\]", content).group(1) if re.search(r"Keyword: \[(.*?)\]",
                                                                                           content) else "N/A"
    metadata["summary"] = re.search(r"Summary\n(.*?)\n(?:目的|手法|成果|$)", content, re.S).group(
        1).strip() if re.search(r"Summary\n(.*?)\n(?:目的|手法|成果|$)", content, re.S) else "N/A"
    metadata["content"] = content
    return metadata


# ディレクトリから論文をロードしてメタデータとSummaryを抽出
def load_papers(directory):
    papers = []
    for file_name in os.listdir(directory):
        if file_name.endswith(".md"):
            file_path = os.path.join(directory, file_name)
            metadata = extract_metadata(file_path)
            papers.append(metadata)
    return papers


# テキストのCLIPベクトルを生成
def encode_text(texts, model, processor):
    inputs = processor(text=texts, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        text_features = model.get_text_features(**inputs)
    return text_features.cpu().numpy()


# ページ遷移の管理
def switch_page(page_name):
    st.session_state["current_page"] = page_name


# 初期状態を設定
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "search"
if "query" not in st.session_state:
    st.session_state["query"] = ""
if "results" not in st.session_state:
    st.session_state["results"] = []

# 検索ページ
if st.session_state["current_page"] == "search":
    st.title("CLIPベース論文検索アプリ (詳細ビュー対応)")
    st.header("論文データをロード")
    if st.button("インデックス作成"):
        papers = load_papers(NOTES_DIR)
        st.session_state["papers"] = papers

        # Summaryとメタデータの結合テキストをベクトル化
        combined_texts = [
            f"{paper['title']} {paper['authors']} {paper['keywords']} {paper['summary']}" for paper in papers
        ]
        text_features = encode_text(combined_texts, model, processor)
        st.session_state["features"] = text_features
        st.success("インデックス作成が完了しました！")

    # 検索処理
    if "papers" in st.session_state and "features" in st.session_state:
        st.header("検索")
        query = st.text_input("検索キーワードを入力してください", value=st.session_state["query"])
        if query:
            st.session_state["query"] = query
            # 検索クエリをベクトル化
            query_feature = encode_text([query], model, processor)

            # コサイン類似度計算
            similarities = cosine_similarity(query_feature, st.session_state["features"]).flatten()

            # 類似度でソート
            papers = st.session_state["papers"]
            results = sorted(
                zip(papers, similarities), key=lambda x: x[1], reverse=True
            )
            st.session_state["results"] = results

        # 結果を表示
        if st.session_state["results"]:
            st.subheader("検索結果")
            result_df = pd.DataFrame(
                [(res[0]["file"], res[0]["title"], res[0]["summary"], res[1]) for res in st.session_state["results"]],
                columns=["ファイル名", "タイトル", "Summary", "スコア"]
            ).query("スコア > 0")
            if result_df.empty:
                st.write("該当する論文がありませんでした。")
            else:
                for _, row in result_df.iterrows():
                    if st.button(f"詳細を表示: {row['タイトル']}", key=row['ファイル名']):
                        st.session_state["selected_file"] = row["ファイル名"]
                        switch_page("details")

# 詳細ページ
elif st.session_state["current_page"] == "details":
    selected_file = st.session_state.get("selected_file", None)
    if selected_file:
        with open(selected_file, "r", encoding="utf-8") as file:
            content = file.read()
        st.title("論文詳細ビュー")
        st.markdown(content)  # マークダウンで表示
    else:
        st.write("選択されたファイルがありません。")

    # 戻るボタン
    if st.button("検索画面に戻る"):
        switch_page("search")
