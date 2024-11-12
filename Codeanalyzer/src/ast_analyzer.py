import os
from tree_sitter import Language, Parser
from typing import Dict, List, Set

class ASTAnalyzer:
    def __init__(self):
        # Determine the dynamic path for the Tree-sitter language library
        base_dir = os.path.dirname(os.path.dirname(__file__))
        tree_sitter_path = os.path.join(base_dir, 'tree-sitter-python')

        # Build the Tree-sitter language library
        Language.build_library(
        'build/my-languages.so',
        [
            tree_sitter_path
        ])

        self.PY_LANGUAGE = Language('build/my-languages.so', 'python')
        self.parser = Parser()
        self.parser.set_language(self.PY_LANGUAGE)

    def parse_file(self, file_path: str) -> dict:
        """Parse a Python file and extract relevant information."""
        with open(file_path, 'rb') as file:
            content = file.read()
        
        tree = self.parser.parse(content)
        
        return {
            'functions': self._extract_functions(tree.root_node),
            'classes': self._extract_classes(tree.root_node),
            'imports': self._extract_imports(tree.root_node)
        }

    def _extract_functions(self, node) -> List[str]:
        """Extract function definitions from the AST."""
        functions = []
        for child in node.children:
            if child.type == 'function_definition':
                for sub_child in child.children:
                    if sub_child.type == 'identifier':
                        functions.append(sub_child.text.decode('utf-8'))
            functions.extend(self._extract_functions(child))
        return functions

    def _extract_classes(self, node) -> List[str]:
        """Extract class definitions from the AST."""
        classes = []
        for child in node.children:
            if child.type == 'class_definition':
                for sub_child in child.children:
                    if sub_child.type == 'identifier':
                        classes.append(sub_child.text.decode('utf-8'))
            classes.extend(self._extract_classes(child))
        return classes

    def _extract_imports(self, node) -> List[str]:
        """Extract import statements from the AST."""
        imports = []
        for child in node.children:
            if child.type in ['import_statement', 'import_from_statement']:
                imports.append(child.text.decode('utf-8'))
        return imports

    def analyze_codebase(self, directory: str) -> Dict:
        """Analyze all Python files in the given directory."""
        results = {}
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    results[file] = self.parse_file(file_path)
        return results