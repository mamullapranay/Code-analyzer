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
