#!/usr/bin/env python3
"""
Setup Script for AI-Powered Resume Ranker
This script automates the installation and setup process.
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error during {description}: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"✗ Python 3.8 or higher is required. Current version: {version.major}.{version.minor}")
        return False
    print(f"✓ Python version {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("\nInstalling Python dependencies...")
    
    # Check if pip is available
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("✗ pip is not available. Please install pip first.")
        return False
    
    # Install requirements
    if not run_command(f"{sys.executable} -m pip install -r requirements.txt", "Installing requirements"):
        return False
    
    return True

def download_spacy_model():
    """Download spaCy language model"""
    print("\nSetting up spaCy...")
    
    # Check if spaCy is installed
    try:
        import spacy
        print("✓ spaCy is installed")
    except ImportError:
        print("✗ spaCy is not installed. Please run the installation again.")
        return False
    
    # Try to load the model
    try:
        nlp = spacy.load("en_core_web_sm")
        print("✓ spaCy model 'en_core_web_sm' is already downloaded")
        return True
    except OSError:
        print("Downloading spaCy model 'en_core_web_sm'...")
        if run_command(f"{sys.executable} -m spacy download en_core_web_sm", "Downloading spaCy model"):
            return True
        else:
            return False

def create_directories():
    """Create necessary directories"""
    print("\nCreating directories...")
    
    directories = ['uploads', 'templates']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✓ Created directory: {directory}")
        else:
            print(f"✓ Directory already exists: {directory}")
    
    return True

def generate_sample_data():
    """Generate sample data for testing"""
    print("\nGenerating sample data...")
    
    try:
        from sample_data import generate_sample_data
        generate_sample_data()
        print("✓ Sample data generated successfully")
        return True
    except ImportError as e:
        print(f"✗ Error importing sample_data: {e}")
        return False
    except Exception as e:
        print(f"✗ Error generating sample data: {e}")
        return False

def test_installation():
    """Test if the application can start"""
    print("\nTesting installation...")
    
    try:
        # Test imports
        import flask
        import spacy
        import sklearn
        import pandas
        import numpy
        import PyPDF2
        from docx import Document
        print("✓ All required packages imported successfully")
        
        # Test spaCy model
        nlp = spacy.load("en_core_web_sm")
        doc = nlp("This is a test sentence.")
        print("✓ spaCy model working correctly")
        
        return True
    except Exception as e:
        print(f"✗ Installation test failed: {e}")
        return False

def print_success_message():
    """Print success message with next steps"""
    print("\n" + "="*60)
    print("🎉 AI-Powered Resume Ranker Setup Complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Start the application:")
    print("   python app.py")
    print("\n2. Open your web browser and go to:")
    print("   http://localhost:5000")
    print("\n3. Upload sample resumes from the 'uploads' folder")
    print("\n4. Use job descriptions from 'sample_job_descriptions.txt'")
    print("\n5. Click 'Rank Resumes' to see the AI in action!")
    print("\nFor help, check the README.md file")
    print("="*60)

def print_troubleshooting():
    """Print troubleshooting information"""
    print("\n" + "="*60)
    print("🔧 Troubleshooting")
    print("="*60)
    print("\nIf you encounter issues:")
    print("\n1. Python version issues:")
    print("   - Ensure Python 3.8+ is installed")
    print("   - Use 'python --version' to check")
    print("\n2. Package installation issues:")
    print("   - Try: pip install --upgrade pip")
    print("   - Then: pip install -r requirements.txt")
    print("\n3. spaCy model issues:")
    print("   - Run: python -m spacy download en_core_web_sm")
    print("\n4. Port already in use:")
    print("   - Change port in app.py line: app.run(port=5001)")
    print("\n5. File permission issues:")
    print("   - Run as administrator (Windows)")
    print("   - Use sudo (Linux/Mac)")
    print("="*60)

def main():
    """Main setup function"""
    print("🚀 AI-Powered Resume Ranker Setup")
    print("="*40)
    
    # Check Python version
    if not check_python_version():
        print("\nPlease upgrade Python to version 3.8 or higher.")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("\nFailed to install dependencies. Please check the error messages above.")
        sys.exit(1)
    
    # Download spaCy model
    if not download_spacy_model():
        print("\nFailed to download spaCy model. Please check the error messages above.")
        sys.exit(1)
    
    # Create directories
    if not create_directories():
        print("\nFailed to create directories. Please check the error messages above.")
        sys.exit(1)
    
    # Generate sample data
    if not generate_sample_data():
        print("\nWarning: Failed to generate sample data. You can still use the application.")
    
    # Test installation
    if not test_installation():
        print("\nInstallation test failed. Please check the error messages above.")
        print_troubleshooting()
        sys.exit(1)
    
    # Success
    print_success_message()

if __name__ == "__main__":
    main() 