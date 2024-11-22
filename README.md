# PaperNotes: A Semantic Search Tool for Research Notes

PaperNotes is a **Streamlit-based app** that uses **OpenAI's CLIP model** for semantic search of research notes written in Markdown. It lets users search notes by metadata, summary, or full text, view search results, and read notes rendered in Markdown.

---

## Key Features

- **Semantic Search**: 
  - High-accuracy keyword-based search using CLIP text encoding.
- **Markdown Rendering**:
  - Displays notes in an easy-to-read Markdown format.
- **Cached Search State**:
  - Keeps search results and queries for smooth navigation.
- **Interactive Interface**:
  - Switch between search results and detailed note views seamlessly.

---

## How It Works

1. **Index Creation**:
   - Scans the `notes/` directory for Markdown files.
   - Extracts metadata (title, authors, keywords, summary) and encodes the content with CLIP.

2. **Search**:
   - Input a query to find notes by similarity in the CLIP-encoded vector space.

3. **Results**:
   - Ranks notes by relevance.
   - Each result shows the title, summary, and similarity score.

4. **Detailed View**:
   - Click a result to read the full note in Markdown.
   - Navigate back to search results without losing query or state.

---

## Installation

### Prerequisites

- Python 3.8+
- Pip

### Steps

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser (e.g., `http://localhost:8501`).

---

## Usage

1. **Prepare Notes**:
   - Place your research notes in the `notes/` directory in Markdown format.

2. **Search**:
   - Click "インデックス作成" to create an index.
   - Enter a query to search notes.
   - View results with titles, summaries, and scores.

3. **Read Notes**:
   - Click "詳細を表示" to see the full note rendered in Markdown.

---

## Example Markdown Note

```markdown
# Tell Me More! Towards Implicit User Intention Understanding of Language Model Driven Agents
Metadata
Authors: [Cheng Qian, Bingxiang He, Zhong Zhuang, Jia Deng, Yujia Qin, Xin Cong, Zhong Zhang, Jie Zhou, Yankai Lin, Zhiyuan Liu, Maosong Sun]
Year: 2024
Category: Computation and Language
Topics: [LLM, agent]
Keyword: [IN3]
Summary
目的:

従来のエージェントモデルでは、ユーザーから曖昧なタスク指示に対応できない課題を解決するため、IN3データセットを構築し、Mistral-Interactモデルを開発しました。
```

---

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

Main libraries:

- **Streamlit**: Web interface.
- **Torch**: CLIP backend.
- **Transformers**: For loading CLIP models.
- **Pandas**: Data processing.
- **Scikit-learn**: Cosine similarity computation.

---

## Directory Structure

```plaintext
.
├── app.py               # Main application script
├── requirements.txt     # Python dependencies
├── notes/               # Directory containing Markdown notes
├── README.md            # Documentation
```

---

## Customization

- **Change Notes Directory**:
  Update the `NOTES_DIR` variable in `app.py` to point to a different folder.

- **Add Filters**:
  Extend the app to filter by metadata such as year, authors, or categories.

---

## Limitations

1. Notes must follow a predefined Markdown format for metadata extraction.
2. The index needs to be recreated manually if new notes are added.

---

## License

This project is licensed under the MIT License.