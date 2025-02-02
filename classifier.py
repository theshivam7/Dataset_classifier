import pandas as pd
import os

def classify_question(question):
    """Enhanced classification with better keyword handling"""
    if not isinstance(question, str):
        return 'Unknown'
    
    q = question.lower().strip()
    
    # Boolean check first
    if q.startswith(('is', 'are', 'was', 'were', 'do', 'does', 'did', 'can', 
                    'could', 'will', 'would', 'should', 'has', 'have', 'had')):
        return 'Boolean'
    
    # Factor detection (reasons/causes)
    if any(kw in q for kw in ['why', 'reason', 'cause', 'because']):
        return 'Factor'
    
    # Reasoning detection (analysis/explanation)
    if any(kw in q for kw in ['how', 'what', 'explain', 'describe', 'determine', 'who']):
        return 'Reasoning'
    
    return 'Unknown'

def process_file(input_path, output_path):
    """Process CSV with proper path handling"""
    # Create output directory if not exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df = pd.read_csv(input_path)
    df['Category'] = df['Questions'].apply(classify_question)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    process_file('Class6th.csv', 'Output/Classified_Questions.csv')
