from typing import Dict

class MermaidGenerator:
    def __init__(self):
        self.output_file = "output/codebase_diagram.mmd"

    def generate_class_diagram(self, ast_data: Dict) -> str:
        """Generate a Mermaid class diagram from the AST data."""
        mermaid_code = ["classDiagram"]
        
        for file_name, file_data in ast_data.items():
            # Add classes
            for class_name in file_data.get('classes', []):
                mermaid_code.append(f"    class {class_name}")
                
            # Add relationships between classes and their functions
            for func_name in file_data.get('functions', []):
                if any(func_name.startswith(f"{class_name}_") for class_name in file_data.get('classes', [])):
                    class_name = next(c for c in file_data.get('classes', []) if func_name.startswith(f"{class_name}_"))
                    mermaid_code.append(f"    {class_name} : +{func_name}")
        
        diagram = "\n".join(mermaid_code)
        
        # Save the diagram
        with open(self.output_file, 'w') as f:
            f.write(diagram)
        
        return diagram