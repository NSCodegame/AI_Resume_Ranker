# AI-Powered Resume Ranker

An intelligent Flask web application that ranks resumes based on job descriptions using NLP techniques and machine learning algorithms.

## Features

- **Multi-format Support**: Upload PDF, DOCX, and TXT resume files
- **NLP Processing**: Uses spaCy for advanced text preprocessing and analysis
- **TF-IDF Vectorization**: Converts text to numerical vectors for similarity comparison
- **Intelligent Scoring**: Combines cosine similarity and keyword matching for accurate rankings
- **Modern Web UI**: Beautiful, responsive interface built with Bootstrap
- **Excel Reports**: Download comprehensive ranking reports
- **Real-time Processing**: Instant ranking results with progress indicators

## Technology Stack

- **Backend**: Flask (Python web framework)
- **NLP**: spaCy (Natural Language Processing)
- **ML**: scikit-learn (Machine Learning algorithms)
- **Text Processing**: PyPDF2, python-docx
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Data Export**: pandas, openpyxl

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step-by-Step Setup

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download spaCy language model**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://localhost:5000`

## Usage Guide

### Step 1: Upload Resumes
- Click "Choose Files" to select resume files (PDF, DOCX, or TXT)
- Supported formats: PDF, DOCX, TXT
- You can upload multiple files at once
- Click "Upload Resumes" to process the files

### Step 2: Set Job Description
- Enter the job description in the text area
- Optionally add keywords with weights (format: `keyword:weight`)
- Example keywords: `Python:2, Machine Learning:1.5, 5 years:1`
- Click "Set Job Description" to save

### Step 3: Rank Resumes
- Click "Rank Resumes" to start the ranking process
- The system will analyze all uploaded resumes
- Results are displayed with scores and rankings

### Step 4: Download Report
- After ranking, click "Download Report (Excel)"
- The report includes rankings and summary statistics

## How It Works

### Text Extraction
- **PDF**: Uses PyPDF2 to extract text from PDF files
- **DOCX**: Uses python-docx to extract text from Word documents
- **TXT**: Direct text file reading

### Text Preprocessing
1. **Tokenization**: Breaks text into individual words
2. **Stop Word Removal**: Removes common words (the, and, is, etc.)
3. **Lemmatization**: Converts words to their base form
4. **Punctuation Removal**: Cleans up text formatting

### Scoring Algorithm
The ranking system uses a combination of two scoring methods:

1. **Cosine Similarity (70% weight)**:
   - Converts job description and resumes to TF-IDF vectors
   - Calculates cosine similarity between vectors
   - Measures overall content similarity

2. **Keyword Matching (30% weight)**:
   - Identifies important keywords from job description
   - Counts keyword occurrences in resumes
   - Applies custom weights for different keywords

### Final Score Calculation
```
Final Score = (Cosine Similarity × 0.7) + (Keyword Score × 0.3)
```

## File Structure

```
AI-Resume-Ranker/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Web interface
├── uploads/              # Temporary file storage
└── Resume.csv           # Sample data file
```

## API Endpoints

- `GET /` - Main application page
- `POST /upload` - Upload resume files
- `POST /set-job-description` - Set job description and keywords
- `POST /rank` - Rank uploaded resumes
- `POST /download-report` - Download Excel report
- `POST /reset` - Reset the system

## Configuration

### Supported File Formats
- PDF (.pdf)
- Microsoft Word (.docx)
- Plain Text (.txt)

### File Size Limits
- Maximum file size: 10MB per file
- Recommended: Keep files under 5MB for optimal performance

### Performance Tips
- Limit uploads to 20-30 resumes at once for best performance
- Use clear, well-formatted job descriptions
- Include relevant keywords in job descriptions

## Troubleshooting

### Common Issues

1. **spaCy model not found**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

2. **Port already in use**:
   Change the port in `app.py`:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

3. **File upload errors**:
   - Check file format (PDF, DOCX, TXT only)
   - Ensure file size is under 10MB
   - Verify file is not corrupted

4. **Memory issues with large files**:
   - Reduce number of simultaneous uploads
   - Process files in smaller batches
   - Restart the application

## Sample Output

The system generates rankings like this:

| Rank | Filename | Score | Similarity |
|------|----------|-------|------------|
| 1 | John_Doe_Resume.pdf | 85.2% | 87.1% |
| 2 | Jane_Smith_CV.docx | 78.9% | 82.3% |
| 3 | Bob_Johnson_Resume.txt | 72.1% | 75.6% |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the documentation
3. Create an issue in the repository

---

**Note**: This application is designed for educational and demonstration purposes. For production use, consider adding authentication, input validation, and security measures. "# Resume.csv" 
