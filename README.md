# Maithili Authorship Attribution & Influence Analysis

A Natural Language Processing (NLP) project focused on authorship attribution and stylistic analysis in Maithili, a low-resource Indo-Aryan language.

---

## Overview

This project implements a machine learning pipeline to analyze textual data and identify authorship based on writing style. It also explores stylistic patterns to study potential influence between authors.

---

## Features

* Authorship classification using stylometric features
* Text vectorization using Bag-of-Words / TF-IDF
* Machine learning model for prediction
* Interactive web interface using Streamlit
* Statistical evaluation using resampling techniques

---

## Project Structure

```
maithili-authorship/
│
├── Maithili_Authorship_Notebook.ipynb
├── app.py
├── README.md
└── .gitignore
```

---

## Installation

```bash
git clone https://github.com/kishlay-git/maithili-authorship.git
cd maithili-authorship
pip install -r requirements.txt
```

---

## Usage

Run the notebook:

```bash
jupyter notebook Maithili_Authorship_Notebook.ipynb
```

Run the web application:

```bash
streamlit run app.py
```

---

## Methodology

* Text preprocessing and normalization
* Feature extraction using vectorization techniques
* Model training using supervised learning algorithms
* Evaluation using accuracy metrics and resampling methods

---

## Notes

Model files (`.pkl`) are included for reproducibility. For production use, consider external model storage.

---

## Author

Kishlay Kashyap
GitHub: https://github.com/kishlay-git
