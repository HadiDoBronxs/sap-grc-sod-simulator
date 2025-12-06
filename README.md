# 🛡️ Automated Risk Analyzer: Python Compliance Engine

Ein performantes Python-Tool zur **automatisierten Risiko-Analyse** in großen Datensätzen. Es implementiert logische Prüfverfahren (basierend auf Segregation of Duties), um Konflikte in Berechtigungsstrukturen algorithmisch zu erkennen.

### 🎯 Engineering Goal
Entwicklung einer leichtgewichtigen, CLI-basierten Engine, die komplexe Compliance-Logik in effizienten Code abbildet, ohne auf schwere Enterprise-Software angewiesen zu sein.

![Ergebnis Screenshot](execution_result.png)

### 🚀 Key Features
* **Algorithmic Risk Detection:** Effiziente Erkennung von Konflikten mittels Mengenlehre (Set Operations) statt verschachtelter Schleifen.
* **Automated Reporting:** Generierung von Audit-Logs und Management-Summaries für Entscheidungsträger.
* **CI/CD Integration:** Das Projekt demonstriert **DevSecOps**-Prinzipien durch eine integrierte Security-Pipeline (GitHub Actions).

### 🛠 Tech Stack & Performance
* **Language:** Python 3.x
* **Data Processing:** Stream-basierte CSV-Verarbeitung für Speichereffizienz.
* **Algorithm:** Nutzung von Hash-Sets für **O(1) Lookup-Performance** beim Abgleich von Millionen potentieller Berechtigungskombinationen.

### 🛡️ DevSecOps & Quality Assurance
Dieses Projekt setzt auf **Security by Design**. Eine GitHub Actions Pipeline prüft jeden Commit automatisch:
* **Tool:** [Bandit](https://github.com/PyCQA/bandit) (SAST - Static Application Security Testing)
* **Trigger:** Push/Pull-Request auf Main-Branch.
* **Ziel:** Automatisierte Einhaltung von Code-Security-Standards.

### 📂 Projektstruktur
* `sod_checker.py`: Die Hauptlogik (Engine).
* `users.csv`: Simulierte Export-Daten (Ist-Zustand).
* `sod_matrix.csv`: Konfigurierbare Matrix für Compliance-Regeln (Soll-Zustand).

### 🚀 Installation & Usage

**1. Repository klonen**
```bash
git clone [https://github.com/HadiDoBronxs/automated-risk-analyzer.git](https://github.com/DEIN_GITHUB_NAME/automated-risk-analyzer.git)
cd automated-risk-analyzer
```
**2. Engine starten**
```bash
python3 sod_checker.py
```
