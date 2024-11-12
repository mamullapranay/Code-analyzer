# Tunable Labs Code Analysis Project

## Project Structure
```
tunable-labs-analysis/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── ast_analyzer.py
│   ├── llm_analyzer.py
│   ├── mermaid_generator.py
│   └── config.py
├── output/
│   ├── question_1.json
│   ├── question_2.json
│   ├── question_3.json
│   ├── question_4.json
│   └── codebase_diagram.mmd
├── tests/
│   ├── __init__.py
│   └── test_analyzers.py
└── build/
    └── my-languages.so

```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/your-username/tunable-labs-analysis.git
cd tunable-labs-analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Clone Tree-sitter Python grammar:
```bash
git clone https://github.com/tree-sitter/tree-sitter-python.git
```

## Configuration

1. Create a `.env` file in the project root with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the analysis:
```bash
python src/main.py --codebase_path /path/to/your/codebase
```

## Dependencies

See `requirements.txt` for complete list. Main dependencies:
- tree-sitter
- openai
- python-dotenv
- pytest (for testing)

## Output

The analysis results will be saved in the `output` folder:
- JSON files containing LLM responses to each question
- Mermaid diagram of the codebase structure

## Testing

Run tests:
```bash
pytest tests/
```
