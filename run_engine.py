import sys
from engine.parser import YAMLParser
from engine.engine import IntegrationEngine

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_engine.py <path_to_yaml_file>")
        sys.exit(1)

    yaml_file = sys.argv[1]

    try:
        # Parse YAML configuration
        config = YAMLParser.load_yaml(yaml_file)
        # Initialize and run the engine
        engine = IntegrationEngine(config)
        engine.run()
        print("Integration executed successfully!")
    except Exception as e:
        print(f"Error: {e}")
