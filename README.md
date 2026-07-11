# 🤖 AI Text Analyzer

A powerful Natural Language Processing (NLP) application that performs **Sentiment Analysis**, **Named Entity Recognition (NER)**, and **Zero-Shot Topic Classification** on any given text. Available in both a **Command Line Interface (CLI)** and an interactive **Web Interface** built with Streamlit.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Models Used](#-models-used)
- [Supported Topics](#-supported-topics)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## 📌 Overview

AI Text Analyzer leverages pre-trained transformer models from [Hugging Face](https://huggingface.co/) to provide three core NLP capabilities:

1. **Sentiment Analysis** — Determines whether the tone of the input text is **Positive** or **Negative** along with a confidence score.
2. **Named Entity Recognition (NER)** — Identifies and classifies named entities such as persons, organizations, and locations within the text.
3. **Zero-Shot Topic Classification** — Predicts the most relevant topic for the given text from a predefined set of categories, without requiring any task-specific training.

---

## ✨ Features

- ✅ Sentiment detection with confidence percentage
- ✅ Named entity extraction with entity type and score
- ✅ Zero-shot topic classification across **8 categories**
- ✅ Visual progress bars for topic scores *(CLI)*
- ✅ Interactive and user-friendly **Streamlit** web interface
- ✅ Locally saved models for **faster and offline inference**
- ✅ Dual interface support: **CLI** and **Web Application**

---

## 📂 Project Structure

```
ai-text-analyzer/
│
├── Saved_Model/
│   ├── sentiment/         # Saved sentiment analysis model
│   ├── ner/               # Saved NER model
│   └── zero_shot/         # Saved zero-shot classification model
│
├── save_models.py         # Script to download and save models locally
├── main.py                # Command Line Interface application
├── app.py                 # Streamlit Web Interface application
├── requirements.txt       # Required Python dependencies
├── LICENSE                # MIT License
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

---

## ⚙️ Requirements

| Requirement | Details                                |
|-------------|----------------------------------------|
| Python      | 3.8 or higher                          |
| pip         | Python package manager                 |
| Internet    | Only required for first-time download  |

---

## 🔧 Installation

Follow the steps below to set up the project on your local machine.

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ai-text-analyzer.git
cd ai-text-analyzer
```

### Step 2: Create a Virtual Environment *(Recommended)*

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **macOS / Linux:**

  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download and Save Models Locally

Run the following script **once** to download all required models and save them to your local machine:

```bash
python save_models.ipynb
```

> ⚠️ **Note:** This step requires an active internet connection. Once completed, all models will be saved in the `Saved_Model/` directory and no internet connection will be needed afterward.

---

## 🚀 Usage

### Option 1: 🌐 Web Interface (Streamlit)

Launch the interactive web application:

```bash
streamlit run app.py
```

Then open your browser and navigate to:

```
http://localhost:8501
```

### Option 2: 💻 Command Line Interface (CLI)

Run the terminal-based application:

```bash
python main.py
```

Follow the on-screen prompts to enter text and view the analysis results.

---

## 🤗 Models Used

| Task                       | Model Name                                         |
|----------------------------|----------------------------------------------------|
| Sentiment Analysis         | `distilbert-base-uncased-finetuned-sst-2-english`  |
| Named Entity Recognition   | `dslim/bert-base-NER`                              |
| Zero-Shot Classification   | `facebook/bart-large-mnli`                         |

All models are sourced from the [Hugging Face Model Hub](https://huggingface.co/models).

---

## 🏷️ Supported Topics

The following topic categories are supported for **Zero-Shot Classification**:

| # | Topic         |
|---|---------------|
| 1 | 💻 Technology |
| 2 | 💼 Business   |
| 3 | 📚 Education  |
| 4 | 🏥 Health     |
| 5 | ⚽ Sports     |
| 6 | 🏛️ Politics  |
| 7 | 🎬 Entertainment |
| 8 | 🔬 Science    |

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for full details.

---

## 🙏 Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Streamlit](https://streamlit.io/)
- [PyTorch](https://pytorch.org/)

---

# 👨‍💻 Author

**Mahadi ur Rehman**

**GitHub:** https://github.com/mahadiurrehman-pixel

**LinkedIn:** [www.linkedin.com/in/mahadi-ur-rehman-siddiqui-139b93386](http://www.linkedin.com/in/mahadi-ur-rehman-siddiqui-139b93386)

---