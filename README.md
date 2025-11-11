# AI_Resume_Ranker

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is an AI-powered resume ranking system built with Flask that uses NLP techniques to match resumes against job descriptions. The system implements a custom TF-IDF vectorization and cosine similarity algorithm without using spaCy or scikit-learn's built-in vectorizers.

## Development Commands

### Setup
```powershell
# Install dependencies
pip install -r requirements_basic.txt

# Run automated setup (creates directories, generates sample data)
python run_setup.py
```

### Running the Application
```powershell
# Start the Flask development server (runs on http://localhost:5000)
python app_basic.py
```

### Testing with Sample Data
```powershell
# Generate sample resumes and job descriptions
python sample_data.py
```

## Architecture

### Core Components

**BasicResumeRanker Class** (`app_basic.py`): The main ranking engine implementing:
- Custom text preprocessing with stop word removal
- Manual TF-IDF calculation from scratch
- Cosine similarity computation between document vectors
- Hybrid scoring: 70% cosine similarity + 30% weighted keyword matching

**Text Processing Pipeline**:
1. Extract text from PDF (PyPDF2), DOCX (python-docx), or TXT files
2. Lowercase conversion and special character removal
3. Stop word filtering (custom set)
4. TF-IDF vectorization (manual implementation using Counter and math.log)
5. Similarity calculation between job description and resume vectors

**Scoring Algorithm**:
- TF-IDF vectors calculated for all documents (job description + resumes)
- Cosine similarity computed using dot product / (norm1 × norm2)
- Keyword matching with configurable weights (default: auto-extracted from job description)
- Final score combines both methods: `score = (cosine_sim × 0.7) + (keyword_score × 0.3)`

### Flask API Endpoints

- `POST /upload`: Upload resume files, stores in `uploads/` directory
- `POST /set-job-description`: Set job description and optional weighted keywords
- `POST /rank`: Triggers ranking calculation, returns sorted results
- `POST /download-report`: Generates Excel report with pandas/openpyxl
- `POST /reset`: Clears uploaded files and resets ranker state

### File Structure

```
app_basic.py              # Main Flask application with BasicResumeRanker class
requirements_basic.txt    # Python dependencies (Flask, pandas, PyPDF2, python-docx, etc.)
run_setup.py             # Automated setup script
sample_data.py           # Generates 8 sample resumes and 3 job descriptions
templates/index.html     # Frontend UI (Bootstrap 5)
uploads/                 # Temporary storage for uploaded resumes
```

## Important Implementation Details

- **No spaCy/scikit-learn for vectorization**: This codebase implements TF-IDF and cosine similarity from scratch using Python's Counter and math libraries
- **Stateful ranker**: The `BasicResumeRanker` instance persists between requests; use `/reset` endpoint to clear state
- **File formats**: Supports PDF, DOCX, and TXT; text extraction methods differ per format
- **Keyword format**: When setting keywords via API, use format `{"keyword": weight}` where weight is a float (e.g., `{"Python": 2.0, "Machine Learning": 1.5}`)
- **Auto-keyword extraction**: If no keywords provided, top 20 most frequent words (length > 3) from job description are used with weight 1.0

## Configuration

- Upload folder: `uploads/` (auto-created)
- Allowed file extensions: `.pdf`, `.docx`, `.txt`
- Default port: 5000
- CORS: Enabled for all origins
- File size limits: Not explicitly enforced (relies on Werkzeug defaults)

