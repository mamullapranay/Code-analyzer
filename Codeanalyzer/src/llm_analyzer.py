import json
import os
from openai import OpenAI
from typing import Dict, Any

class LLMAnalyzer:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)

    def analyze_code(self, ast_data: Dict, question: str, question_num: int) -> Dict[str, Any]:
        """
        Analyze code using GPT-4 based on AST data and a specific question.
        """
        # Prepare context from AST data
        context = json.dumps(ast_data, indent=2)
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a code analysis assistant. Analyze the provided codebase information and answer questions about it."},
                {"role": "user", "content": f"Based on this codebase information:\n{context}\n\nQuestion: {question}"}
            ],
            temperature=0,
            seed=0
        )
        
        result = {
            "question": question,
            "answer": response.choices[0].message.content
        }
        
        # Save to JSON file
        output_file = os.path.join(self.output_dir, f"question_{question_num}.json")
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        
        return result

    def process_questions(self, ast_data: Dict) -> Dict[int, Dict[str, Any]]:
        """
        Process all predefined questions about the codebase.
        """
        questions = {
            1: "What functions does api.py have?",
            2: "What are different classes present in api.py?",
            3: "How many imports are present in app.py",
            4: "How many function are related in both app.py and api.py"
        }
        
        results = {}
        for q_num, question in questions.items():
            results[q_num] = self.analyze_code(ast_data, question, q_num)
        
        return results