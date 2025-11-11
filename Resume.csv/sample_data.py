"""
Sample Data Generator for AI-Powered Resume Ranker
This script generates sample resumes and job descriptions for testing the system.
"""

import os
import random
from datetime import datetime, timedelta

def create_sample_resume(name, skills, experience_years, education, filename):
    """Create a sample resume in text format"""
    
    resume_content = f"""
{name.upper()}
{'=' * len(name)}

CONTACT INFORMATION
Email: {name.lower().replace(' ', '.')}@email.com
Phone: +1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}
LinkedIn: linkedin.com/in/{name.lower().replace(' ', '')}

PROFESSIONAL SUMMARY
Experienced {random.choice(['software engineer', 'data scientist', 'machine learning engineer', 'full-stack developer'])} with {experience_years} years of experience in {', '.join(random.sample(skills, min(3, len(skills))))}. Passionate about creating innovative solutions and driving business value through technology.

SKILLS
Technical Skills: {', '.join(skills)}
Programming Languages: {', '.join(random.sample(skills, min(5, len(skills))))}
Frameworks & Tools: {', '.join(random.sample(skills, min(4, len(skills))))}

EXPERIENCE

Senior {random.choice(['Software Engineer', 'Data Scientist', 'ML Engineer'])} | Tech Company Inc.
{datetime.now().year - experience_years} - Present
• Developed and maintained {random.choice(['web applications', 'machine learning models', 'data pipelines'])} using {random.choice(skills)}
• Collaborated with cross-functional teams to deliver high-quality software solutions
• Implemented {random.choice(['agile methodologies', 'CI/CD pipelines', 'automated testing'])} to improve development efficiency
• Mentored junior developers and conducted code reviews

{random.choice(['Software Engineer', 'Data Analyst', 'Developer'])} | Startup XYZ
{datetime.now().year - experience_years - 2} - {datetime.now().year - experience_years}
• Built {random.choice(['REST APIs', 'data visualization dashboards', 'automation scripts'])} using {random.choice(skills)}
• Analyzed large datasets and provided actionable insights
• Participated in {random.choice(['sprint planning', 'technical design', 'architecture discussions'])} meetings

EDUCATION
{education} | University of Technology
{datetime.now().year - experience_years - 4} - {datetime.now().year - experience_years - 1}
• GPA: {random.uniform(3.0, 4.0):.2f}
• Relevant Coursework: {', '.join(random.sample(skills, min(3, len(skills))))}

PROJECTS
• {random.choice(['E-commerce Platform', 'Machine Learning Model', 'Data Analysis Dashboard'])}: Built using {random.choice(skills)}
• {random.choice(['Mobile App', 'Web Application', 'API Service'])}: Developed with {random.choice(skills)}

CERTIFICATIONS
• {random.choice(['AWS Certified Developer', 'Google Cloud Professional', 'Microsoft Azure'])} Certification
• {random.choice(['Scrum Master', 'Product Owner', 'Agile Coach'])} Certification

LANGUAGES
English (Native), Spanish (Intermediate), French (Basic)

INTERESTS
{random.choice(['Open Source Contribution', 'Machine Learning Research', 'Web Development', 'Data Science'])}
"""
    
    # Create uploads directory if it doesn't exist
    os.makedirs('uploads', exist_ok=True)
    
    # Write resume to file
    with open(f'uploads/{filename}', 'w', encoding='utf-8') as f:
        f.write(resume_content)
    
    return f'uploads/{filename}'

def generate_sample_data():
    """Generate sample resumes and job descriptions"""
    
    # Sample skills pool
    all_skills = [
        'Python', 'JavaScript', 'Java', 'C++', 'C#', 'Ruby', 'PHP', 'Go', 'Rust',
        'React', 'Angular', 'Vue.js', 'Node.js', 'Django', 'Flask', 'Spring Boot',
        'Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch', 'Scikit-learn',
        'Data Analysis', 'SQL', 'MongoDB', 'PostgreSQL', 'Redis', 'Docker', 'Kubernetes',
        'AWS', 'Azure', 'Google Cloud', 'Git', 'Jenkins', 'CI/CD', 'Agile', 'Scrum',
        'REST APIs', 'GraphQL', 'Microservices', 'Big Data', 'Hadoop', 'Spark',
        'Natural Language Processing', 'Computer Vision', 'Data Visualization',
        'Tableau', 'Power BI', 'Excel', 'Pandas', 'NumPy', 'Matplotlib', 'Seaborn'
    ]
    
    # Sample candidates
    candidates = [
        {
            'name': 'John Smith',
            'skills': ['Python', 'Machine Learning', 'TensorFlow', 'Data Analysis', 'SQL', 'Pandas'],
            'experience': 5,
            'education': 'Master of Science in Computer Science',
            'filename': 'John_Smith_Resume.txt'
        },
        {
            'name': 'Sarah Johnson',
            'skills': ['JavaScript', 'React', 'Node.js', 'MongoDB', 'AWS', 'Docker'],
            'experience': 3,
            'education': 'Bachelor of Science in Software Engineering',
            'filename': 'Sarah_Johnson_Resume.txt'
        },
        {
            'name': 'Michael Chen',
            'skills': ['Java', 'Spring Boot', 'Microservices', 'Kubernetes', 'PostgreSQL', 'Git'],
            'experience': 7,
            'education': 'Master of Engineering in Computer Science',
            'filename': 'Michael_Chen_Resume.txt'
        },
        {
            'name': 'Emily Davis',
            'skills': ['Python', 'Deep Learning', 'PyTorch', 'Computer Vision', 'OpenCV', 'NumPy'],
            'experience': 4,
            'education': 'PhD in Artificial Intelligence',
            'filename': 'Emily_Davis_Resume.txt'
        },
        {
            'name': 'David Wilson',
            'skills': ['C++', 'Data Structures', 'Algorithms', 'System Design', 'Linux', 'Git'],
            'experience': 6,
            'education': 'Bachelor of Science in Computer Science',
            'filename': 'David_Wilson_Resume.txt'
        },
        {
            'name': 'Lisa Brown',
            'skills': ['Python', 'Data Science', 'Scikit-learn', 'SQL', 'Tableau', 'Excel'],
            'experience': 2,
            'education': 'Master of Science in Data Science',
            'filename': 'Lisa_Brown_Resume.txt'
        },
        {
            'name': 'Robert Taylor',
            'skills': ['JavaScript', 'Angular', 'TypeScript', 'REST APIs', 'MongoDB', 'AWS'],
            'experience': 4,
            'education': 'Bachelor of Science in Information Technology',
            'filename': 'Robert_Taylor_Resume.txt'
        },
        {
            'name': 'Jennifer Lee',
            'skills': ['Python', 'Natural Language Processing', 'SpaCy', 'BERT', 'Hugging Face', 'SQL'],
            'experience': 3,
            'education': 'Master of Science in Computational Linguistics',
            'filename': 'Jennifer_Lee_Resume.txt'
        }
    ]
    
    # Generate resumes
    created_files = []
    for candidate in candidates:
        file_path = create_sample_resume(
            candidate['name'],
            candidate['skills'],
            candidate['experience'],
            candidate['education'],
            candidate['filename']
        )
        created_files.append(file_path)
        print(f"Created resume: {candidate['filename']}")
    
    # Sample job descriptions
    job_descriptions = {
        'Senior Python Developer': {
            'description': """
We are seeking a Senior Python Developer to join our dynamic team. The ideal candidate will have strong experience in Python development, web frameworks, and database management.

Key Responsibilities:
• Develop and maintain scalable web applications using Python
• Work with frameworks like Django or Flask
• Design and implement RESTful APIs
• Collaborate with cross-functional teams
• Mentor junior developers
• Participate in code reviews and technical discussions

Required Skills:
• 5+ years of experience in Python development
• Strong knowledge of web frameworks (Django/Flask)
• Experience with SQL databases (PostgreSQL, MySQL)
• Familiarity with version control systems (Git)
• Understanding of RESTful API design
• Experience with cloud platforms (AWS, Azure, GCP)
• Knowledge of containerization (Docker)

Preferred Skills:
• Experience with microservices architecture
• Knowledge of CI/CD pipelines
• Familiarity with Agile methodologies
• Experience with NoSQL databases
• Understanding of DevOps practices
            """,
            'keywords': {
                'Python': 2.0,
                'Django': 1.5,
                'Flask': 1.5,
                'REST APIs': 1.5,
                'SQL': 1.5,
                'Git': 1.0,
                'AWS': 1.0,
                'Docker': 1.0,
                '5 years': 1.5
            }
        },
        'Machine Learning Engineer': {
            'description': """
We are looking for a talented Machine Learning Engineer to join our AI team. The successful candidate will develop and deploy machine learning models to solve complex business problems.

Key Responsibilities:
• Develop and implement machine learning models
• Preprocess and analyze large datasets
• Deploy models to production environments
• Collaborate with data scientists and engineers
• Optimize model performance and accuracy
• Stay updated with latest ML technologies

Required Skills:
• 3+ years of experience in machine learning
• Proficiency in Python and ML libraries (TensorFlow, PyTorch, Scikit-learn)
• Experience with data preprocessing and feature engineering
• Knowledge of statistical analysis and modeling
• Familiarity with cloud platforms for ML deployment
• Understanding of model evaluation metrics

Preferred Skills:
• Experience with deep learning frameworks
• Knowledge of MLOps and model deployment
• Familiarity with big data technologies (Spark, Hadoop)
• Experience with computer vision or NLP
• Understanding of model interpretability techniques
            """,
            'keywords': {
                'Machine Learning': 2.0,
                'Python': 1.5,
                'TensorFlow': 1.5,
                'PyTorch': 1.5,
                'Scikit-learn': 1.5,
                'Deep Learning': 1.0,
                'Data Analysis': 1.0,
                '3 years': 1.0
            }
        },
        'Full Stack Developer': {
            'description': """
We are seeking a Full Stack Developer to build and maintain web applications. The ideal candidate will have experience with both frontend and backend technologies.

Key Responsibilities:
• Develop responsive web applications
• Build and maintain RESTful APIs
• Work with modern JavaScript frameworks
• Design and implement database schemas
• Collaborate with UI/UX designers
• Ensure code quality and performance

Required Skills:
• 4+ years of full stack development experience
• Proficiency in JavaScript/TypeScript
• Experience with React, Angular, or Vue.js
• Knowledge of Node.js and backend frameworks
• Familiarity with SQL and NoSQL databases
• Understanding of web security best practices

Preferred Skills:
• Experience with cloud platforms (AWS, Azure)
• Knowledge of containerization (Docker, Kubernetes)
• Familiarity with CI/CD pipelines
• Experience with GraphQL
• Understanding of microservices architecture
            """,
            'keywords': {
                'JavaScript': 2.0,
                'React': 1.5,
                'Angular': 1.5,
                'Node.js': 1.5,
                'Full Stack': 1.5,
                'REST APIs': 1.0,
                'SQL': 1.0,
                '4 years': 1.0
            }
        }
    }
    
    # Save job descriptions to file
    with open('sample_job_descriptions.txt', 'w', encoding='utf-8') as f:
        f.write("SAMPLE JOB DESCRIPTIONS\n")
        f.write("=" * 50 + "\n\n")
        
        for title, details in job_descriptions.items():
            f.write(f"JOB TITLE: {title}\n")
            f.write("-" * 30 + "\n")
            f.write("DESCRIPTION:\n")
            f.write(details['description'])
            f.write("\nKEYWORDS:\n")
            for keyword, weight in details['keywords'].items():
                f.write(f"  {keyword}: {weight}\n")
            f.write("\n" + "=" * 50 + "\n\n")
    
    print(f"\nGenerated {len(created_files)} sample resumes in the 'uploads' folder")
    print("Created 'sample_job_descriptions.txt' with sample job descriptions")
    print("\nTo use these samples:")
    print("1. Start the Flask application: python app.py")
    print("2. Upload the generated resume files")
    print("3. Copy and paste job descriptions from sample_job_descriptions.txt")
    print("4. Add keywords as specified in the file")
    print("5. Click 'Rank Resumes' to see the results")

if __name__ == "__main__":
    generate_sample_data() 