# Naive-Bayes-Classifier-App

**Offline Desktop-Based Classifier App** using Naive Bayes algorithm for Yes/No predictions.

This repository contains a desktop-based Python application that allows users to perform predictions based on different datasets. The app features a user-friendly interface with multiple tabs for different datasets. It is designed for learning and demonstrating Naive Bayes classification in a simple and interactive way.

---

## 📂 Repository Structure



pythonProject/
│
├── .venv/ # Python virtual environment
├── data/ # CSV datasets for predictions
│ ├── animal.csv
│ ├── email.csv
│ ├── loan.csv
│ └── weather.csv
├── web/ # UI files (HTML/CSS) for desktop interface
│ ├── background.jpg
│ ├── dataset.html
│ ├── index.html
│ └── style.css
├── .gitignore
├── app.py # Main Python script for Naive Bayes predictions
└── README.md


---

## 🛠 Features

- **Offline Desktop Application** — No internet required.
- **Naive Bayes Predictions** — Classifies input data as **Yes/No**.
- **Multiple Tabs/Datasets:**  
  - **Animal Tab** — Predicts animal-related categories.  
  - **Email Tab** — Predicts email spam or not.  
  - **Loan Tab** — Predicts loan approval (Yes/No).  
  - **Weather Tab** — Predicts weather conditions (Yes/No).  
- **User Input via Dataset Variables** — Users can select values from the dataset variables to make predictions.  
- **Simple HTML/CSS Interface** — Desktop-like web interface for easy interaction.

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Ayesha1143/Naive-Bayes-Classifier-App.git


Navigate to the project folder:

cd Naive-Bayes-Classifier-App/pythonProject


Create and activate Python virtual environment (if not already):

python -m venv .venv
# Activate
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


Install dependencies (if any) — for basic Naive Bayes using sklearn:

pip install pandas scikit-learn


Run the app:

python app.py


Open the interface in your browser or desktop window (depending on implementation) and start making predictions using different tabs.

💡 How It Works

The user selects a dataset tab (Animal, Email, Loan, Weather).

Values are selected according to available dataset variables.

The Naive Bayes model predicts the outcome (Yes/No) based on the selected inputs.

Results are displayed instantly in the interface.

📌 Technologies Used

Python

Pandas

Scikit-Learn (Naive Bayes)

HTML / CSS (for desktop interface)

📝 Notes

All datasets are included in the data/ folder.

The app works offline — no internet connection required.

This app is primarily for learning, experimentation, and demonstration of Naive Bayes classification.

📧 Contact

GitHub: https://github.com/Ayesha1143