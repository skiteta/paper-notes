PaperNotes

This application is a Streamlit-based research note search tool that uses OpenAI's CLIP model for semantic search. It enables users to search for research notes written in Markdown format based on their metadata, summary, or full text. Users can view search results and explore the detailed contents of each note in a markdown-rendered format. The search results and state are cached for a smooth user experience.

Features

Semantic Search:
Powered by CLIP's text encoding for high-accuracy search.
Allows keyword-based queries to find relevant research notes based on metadata and summary.
Markdown Rendering:
Displays research notes in markdown format for clear readability.
Cached Search State:
Retains search results and query inputs for seamless navigation between search results and note details.
Interactive User Interface:
Streamlit-based interface with easy navigation between search results and note details.
How It Works

Index Creation:
The application scans a specified directory (notes) containing Markdown files.
Extracts metadata (e.g., title, authors, keywords, summary) and processes the content with CLIP for vectorization.
Search:
Users input a query.
The app computes the similarity between the query and indexed notes using cosine similarity in the CLIP-encoded vector space.
Results:
Displays a ranked list of relevant research notes based on similarity scores.
Each result includes the title, summary, and score.
Detailed View:
Clicking on a result shows the full content of the note in markdown format.
Users can navigate back to the search results.
Installation

Prerequisites
Python 3.8+
Pip
Clone the Repository
git clone <repository_url>
cd <repository_directory>
Install Dependencies
pip install -r requirements.txt
Usage

Place your research notes in the notes directory in Markdown format.
Run the application:
streamlit run app.py
Open the local Streamlit server URL (e.g., http://localhost:8501) in your web browser.
Perform the following actions:
Create an index by clicking "インデックス作成".
Enter search queries in the text box.
Click "詳細を表示" to view the full content of a selected note.
Directory Structure

.
├── app.py               # Main application script
├── requirements.txt     # Python dependencies
├── notes/               # Directory containing research notes in Markdown format
├── README.md            # Documentation
Example Markdown Note Format

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
Requirements

Streamlit: Web interface
Torch: CLIP model backend
Transformers: Hugging Face CLIP model loader
Pandas: Data manipulation
Scikit-learn: Cosine similarity computation
Install via requirements.txt
pip install -r requirements.txt
Key Libraries

Streamlit: For creating the user interface.
Transformers: For loading CLIP models.
Torch: Backend for CLIP operations.
Customization

Change Notes Directory: Modify the NOTES_DIR variable in the code to point to a different directory containing Markdown files.
Add Filters: Extend the app to allow filtering by metadata such as year, authors, or categories.
Known Limitations

Markdown Format Dependence: Notes must follow the defined format for metadata extraction.
No Real-time Index Update: The index must be recreated manually if new notes are added.
Future Enhancements

Real-time Index Update: Automatically detect and index new notes.
Highlight Matching Text: Highlight query matches in the results and detailed view.
Export Results: Add an option to export search results to a CSV or JSON file.
License

This project is licensed under the MIT License. See the LICENSE file for details.