import os
import argparse
from dotenv import load_dotenv
from ast_analyzer import ASTAnalyzer
from llm_analyzer import LLMAnalyzer
from mermaid_generator import MermaidGenerator

def main():
    # Load environment variables
    load_dotenv()
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Analyze Python codebase using Tree-sitter and GPT-4')
    default_codebase_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Code analyzer', 'codebase')
    parser.add_argument('--codebase_path', default=default_codebase_path, help='Path to the Python codebase to analyze')
    args = parser.parse_args()
    
    # Initialize analyzers
    ast_analyzer = ASTAnalyzer()
    llm_analyzer = LLMAnalyzer(os.getenv('OPENAI_API_KEY'))
    mermaid_generator = MermaidGenerator()
    
    # Analyze codebase
    print("Analyzing codebase structure...")
    ast_data = ast_analyzer.analyze_codebase(args.codebase_path)
    
    # Process questions using LLM
    print("Processing questions with GPT-4...")
    results = llm_analyzer.process_questions(ast_data)
    
    # Generate Mermaid diagram
    print("Generating Mermaid diagram...")
    mermaid_generator.generate_class_diagram(ast_data)
    
    print("Analysis complete! Results have been saved to the output directory.")

if __name__ == "__main__":
    main()