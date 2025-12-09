import sys
import pandas as pd
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, pyqtSlot, QObject, pyqtSignal
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from PyQt5.QtWebChannel import QWebChannel
import json


# --------------------- Backend Functions ---------------------
def load_dataset(path):
    df = pd.read_csv(path)
    # Last column = target
    target_col = df.columns[-1]
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y, target_col


def train_naive_bayes(X, y):
    enc = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
    X_enc = enc.fit_transform(X.astype(str))
    model = CategoricalNB()
    model.fit(X_enc, y.astype(str))
    return model, enc


# --------------------- Bridge (Frontend ↔ Backend) ---------------------
class Bridge(QObject):
    sendData = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.datasets = {
            "animal": "data/animal.csv",
            "email": "data/email.csv",
            "loan": "data/loan.csv",
            "weather": "data/weather.csv"
        }

    @pyqtSlot(str)
    def loadDataset(self, name):
        path = self.datasets.get(name)
        if not path or not os.path.exists(path):
            self.sendData.emit(json.dumps({"error": f"{name} dataset not found"}))
            return

        X, y, target = load_dataset(path)
        dropdowns = {col: ["None"] + sorted(X[col].astype(str).unique().tolist()) for col in X.columns}
        # 🔹 Added "None" option in every dropdown
        data = {"columns": list(X.columns), "dropdowns": dropdowns, "target": target}
        self.sendData.emit(json.dumps(data))

    @pyqtSlot(str, str)
    def predict(self, name, input_json):
        path = self.datasets.get(name)
        if not path or not os.path.exists(path):
            self.sendData.emit(json.dumps({"error": f"{name} dataset not found"}))
            return

        X, y, target = load_dataset(path)
        model, enc = train_naive_bayes(X, y)

        input_data = json.loads(input_json)

        # 🔹 Ignore "None" features: remove them from input
        input_data = {k: v for k, v in input_data.items() if v != "None"}

        # 🔹 Make sure we only use columns that are selected (not None)
        used_columns = [col for col in X.columns if col in input_data]

        if not used_columns:
            self.sendData.emit(json.dumps({"error": "Please select at least one feature (not None)."}))
            return

        # 🔹 Filter training data & encoder for selected columns only
        X = X[used_columns]
        enc = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
        X_enc = enc.fit_transform(X.astype(str))
        model = CategoricalNB()
        model.fit(X_enc, y.astype(str))

        # 🔹 Predict only with selected columns
        input_df = pd.DataFrame([input_data], columns=used_columns)
        input_enc = enc.transform(input_df.astype(str))
        pred = model.predict(input_enc)[0]
        self.sendData.emit(json.dumps({"result": str(pred)}))


# --------------------- Main Window ---------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Naive Bayes Offline App")
        self.setGeometry(100, 100, 900, 650)

        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)

        url = QUrl.fromLocalFile(os.path.abspath("web/index.html"))
        self.view.load(url)

        self.bridge = Bridge()
        self.channel = QWebChannel()
        self.channel.registerObject("bridge", self.bridge)
        self.view.page().setWebChannel(self.channel)

        self.bridge.sendData.connect(self.handleData)

    def handleData(self, data_str):
        self.view.page().runJavaScript(f"window.receiveFromPython({data_str});")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
