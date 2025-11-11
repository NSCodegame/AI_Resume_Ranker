import os
import json
import pandas as pd
from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import PyPDF2
from docx import Document
import re
import io
import math
from datetime import datetime
from collections import Counter

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class BasicResumeRanker:
    def __init__(self):
        self.job_keywords = {}
        self.resume_texts = []
        self.resume_names = []
        self.job_description = ""
        
    def extract_text_from_pdf(self, pdf_path):
        """Extract text from PDF file"""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return ""
    
    def extract_text_from_docx(self, docx_path):
        """Extract text from DOCX file"""
        try:
            doc = Document(docx_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        except Exception as e:
            print(f"Error extracting text from DOCX: {e}")
            return ""
    
    def preprocess_text(self, text):
        """Basic text preprocessing"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and extra whitespace
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        
        # Remove common stop words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those',
            'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
        }
        
        words = text.split()
        filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
        
        return " ".join(filtered_words)
    
    def calculate_tf_idf_scores(self, documents):
        """Calculate TF-IDF scores for documents"""
        # Calculate term frequency for each document
        tf_scores = []
        all_terms = set()
        
        for doc in documents:
            words = doc.split()
            tf = Counter(words)
            tf_scores.append(tf)
            all_terms.update(words)
        
        # Calculate inverse document frequency
        idf_scores = {}
        num_docs = len(documents)
        
        for term in all_terms:
            doc_count = sum(1 for tf in tf_scores if term in tf)
            idf_scores[term] = math.log(num_docs / (1 + doc_count))
        
        # Calculate TF-IDF vectors
        tfidf_vectors = []
        for tf in tf_scores:
            vector = {}
            for term in all_terms:
                tf_score = tf.get(term, 0)
                idf_score = idf_scores[term]
                vector[term] = tf_score * idf_score
            tfidf_vectors.append(vector)
        
        return tfidf_vectors, all_terms
    
    def cosine_similarity(self, vec1, vec2, all_terms):
        """Calculate cosine similarity between two vectors"""
        dot_product = 0
        norm1 = 0
        norm2 = 0
        
        for term in all_terms:
            val1 = vec1.get(term, 0)
            val2 = vec2.get(term, 0)
            dot_product += val1 * val2
            norm1 += val1 * val1
            norm2 += val2 * val2
        
        if norm1 == 0 or norm2 == 0:
            return 0
        
        return dot_product / (math.sqrt(norm1) * math.sqrt(norm2))
    
    def set_job_description(self, job_description, keywords=None):
        """Set job description and keywords for ranking"""
        self.job_description = job_description
        if keywords:
            self.job_keywords = {keyword.lower(): weight for keyword, weight in keywords.items()}
        else:
            # Extract common keywords from job description
            processed_desc = self.preprocess_text(job_description)
            words = processed_desc.split()
            # Count word frequencies
            word_freq = Counter(words)
            
            # Take top 20 most frequent words as keywords
            most_common = word_freq.most_common(20)
            self.job_keywords = {word: 1.0 for word, _ in most_common if len(word) > 3}
    
    def add_resume(self, file_path, filename):
        """Add a resume to the ranking system"""
        # Extract text based on file type
        if file_path.endswith('.pdf'):
            text = self.extract_text_from_pdf(file_path)
        elif file_path.endswith('.docx'):
            text = self.extract_text_from_docx(file_path)
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        
        # Preprocess text
        processed_text = self.preprocess_text(text)
        
        self.resume_texts.append(processed_text)
        self.resume_names.append(filename)
    
    def calculate_scores(self):
        """Calculate similarity scores for all resumes"""
        if not self.resume_texts:
            return []
        
        # Combine job description with resume texts for vectorization
        all_documents = [self.job_description] + self.resume_texts
        
        # Calculate TF-IDF vectors
        tfidf_vectors, all_terms = self.calculate_tf_idf_scores(all_documents)
        
        # Calculate cosine similarity between job description and each resume
        job_vector = tfidf_vectors[0]
        resume_vectors = tfidf_vectors[1:]
        
        similarities = []
        for resume_vector in resume_vectors:
            similarity = self.cosine_similarity(job_vector, resume_vector, all_terms)
            similarities.append(similarity)
        
        # Calculate keyword-based scores
        keyword_scores = []
        for resume_text in self.resume_texts:
            score = 0
            for keyword, weight in self.job_keywords.items():
                if keyword in resume_text:
                    score += weight
            keyword_scores.append(score)
        
        # Normalize keyword scores
        if keyword_scores:
            max_keyword_score = max(keyword_scores)
            if max_keyword_score > 0:
                keyword_scores = [score / max_keyword_score for score in keyword_scores]
        
        # Combine similarity and keyword scores
        final_scores = []
        for i in range(len(similarities)):
            combined_score = (similarities[i] * 0.7) + (keyword_scores[i] * 0.3)
            final_scores.append(combined_score)
        
        return final_scores
    
    def rank_resumes(self):
        """Rank resumes and return results"""
        scores = self.calculate_scores()
        
        # Create results with ranking
        results = []
        for i, (name, score) in enumerate(zip(self.resume_names, scores)):
            results.append({
                'rank': i + 1,
                'filename': name,
                'score': round(score * 100, 2),
                'similarity_percentage': round(score * 100, 2)
            })
        
        # Sort by score (descending)
        results.sort(key=lambda x: x['score'], reverse=True)
        
        # Update ranks after sorting
        for i, result in enumerate(results):
            result['rank'] = i + 1
        
        return results

# Initialize the ranker
ranker = BasicResumeRanker()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resumes():
    if 'resumes' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400
    
    files = request.files.getlist('resumes')
    uploaded_files = []
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Add to ranker
            ranker.add_resume(filepath, filename)
            uploaded_files.append(filename)
    
    return jsonify({
        'message': f'Successfully uploaded {len(uploaded_files)} files',
        'files': uploaded_files
    })

@app.route('/set-job-description', methods=['POST'])
def set_job_description():
    data = request.get_json()
    job_description = data.get('job_description', '')
    keywords = data.get('keywords', {})
    
    ranker.set_job_description(job_description, keywords)
    
    return jsonify({'message': 'Job description set successfully'})

@app.route('/rank', methods=['POST'])
def rank_resumes():
    if not ranker.resume_texts:
        return jsonify({'error': 'No resumes uploaded'}), 400
    
    if not hasattr(ranker, 'job_description') or not ranker.job_description:
        return jsonify({'error': 'No job description set'}), 400
    
    results = ranker.rank_resumes()
    
    return jsonify({
        'results': results,
        'total_resumes': len(results)
    })

@app.route('/download-report', methods=['POST'])
def download_report():
    data = request.get_json()
    results = data.get('results', [])
    
    # Create Excel report
    df = pd.DataFrame(results)
    
    # Create Excel file in memory
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Resume Rankings', index=False)
        
        # Add summary sheet
        summary_data = {
            'Metric': ['Total Resumes', 'Average Score', 'Highest Score', 'Lowest Score'],
            'Value': [
                len(results),
                round(df['score'].mean(), 2) if len(results) > 0 else 0,
                round(df['score'].max(), 2) if len(results) > 0 else 0,
                round(df['score'].min(), 2) if len(results) > 0 else 0
            ]
        }
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
    
    output.seek(0)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"resume_rankings_{timestamp}.xlsx"
    
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=filename
    )

@app.route('/reset', methods=['POST'])
def reset():
    global ranker
    ranker = BasicResumeRanker()
    
    # Clear uploaded files
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    
    return jsonify({'message': 'System reset successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
