# 🏥 Obesity Prediction System

A Streamlit-based web application that predicts obesity categories using a trained Random Forest machine learning model with a sleek black-themed user interface.

## 📋 Overview

This application takes user health metrics as input, scales them using a MinMax scaler, and predicts obesity categories with the following classifications:
- 🟢 **Normal weight**
- 🔴 **Obese**
- 🟡 **Overweight**
- 🔵 **Underweight**

## 🎯 Features

- **Black Background UI** - Dark-themed interface with neon accents for comfortable viewing
- **User Input Form** - Easy-to-use interface for entering health metrics
- **Automatic Data Scaling** - Scales Height and Weight using MinMax normalization
- **Random Forest Prediction** - Uses trained Random Forest model for classification
- **Balloon Animation** - Celebratory balloon effect on prediction completion
- **Real-time Processing** - Fast prediction results

## 📊 Input Parameters

The application accepts the following health metrics:

| Parameter | Range |
|-----------|-------|
| **Age** | 1-120 years |
| **Gender** | Male / Female |
| **Height** | 50-250 cm |
| **Weight** | 20-200 kg |
| **BMI** | 10-60 |
| **Physical Activity Level** | 1-5 (scale) |

## 🗂️ Project Structure

```
.
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── objects/
│   ├── rf.pkl                     # Trained Random Forest model
│   └── scaler.pkl                 # MinMax Scaler (not used in app)
├── data/
│   ├── raw_data/
│   │   └── obesity_data.csv       # Original dataset
│   └── processed_data/
│       ├── x_train.csv            # Training features
│       ├── x_test.csv             # Testing features
│       ├── y_train.csv            # Training labels
│       └── y_test.csv             # Testing labels
└── src/
    └── data_preprocessing.ipynb    # Data preprocessing notebook
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone or Download the project**
   ```bash
   cd path/to/project
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Running the Application

Start the Streamlit app with:

```bash
streamlit run app.py
```

The application will launch in your default browser at:
- **Local URL:** `http://localhost:8501`
- **Network URL:** `http://your-ip:8501`

## 📝 How to Use

1. Enter your health metrics in the input form
2. Adjust sliders and dropdowns for your details
3. Click the **"🔮 Predict Obesity Category"** button
4. View the prediction result with balloon animation 🎈

## 🤖 Model Information

- **Algorithm:** Random Forest Classifier
- **Training Set:** ~1000 obesity dataset samples
- **Input Features:** 6 health metrics
- **Output Classes:** 4 obesity categories
- **Scaling Method:** MinMax Normalization (for Height and Weight)

## 📦 Dependencies

All required packages are listed in `requirements.txt`:

- `streamlit` - Web app framework
- `scikit-learn` - Machine learning models and preprocessing
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing

See `requirements.txt` for exact versions.

## ⚠️ Notes

- The scaler is fitted on training data during app startup
- Models are cached in memory for performance
- Ensure data files are in the correct paths before running
- Version compatibility warnings from scikit-learn may appear (normal)

## 🛠️ Development

To modify the model or preprocessing:

1. Edit `src/data_preprocessing.ipynb` 
2. Regenerate `rf.pkl` file by running the notebook
3. Restart the Streamlit app

## 📧 Support

For issues or questions:
- Check the file paths are correct
- Ensure all dependencies are installed
- Verify Python version compatibility

## 📄 License

This project is for educational purposes.

---

**Created:** March 2026  
**Framework:** Streamlit  
**ML Library:** scikit-learn
