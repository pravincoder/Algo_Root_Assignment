# code_generator.py
def generate_code(function_name):
    code = f"""
from function_registry import {function_name}

def main():
    try:
        {function_name}()
        print("{function_name} executed successfully.")
    except Exception as e:
        print(f"Error executing {function_name}: {{e}}")

if __name__ == "__main__":
    main()
    """
    return code