# RAG-based Function Execution System

A FastAPI-based application that uses Retrieval-Augmented Generation (RAG) to intelligently match user prompts with predefined system functions and generate executable code.

## Overview

This system provides an API endpoint that:
1. Matches natural language prompts to appropriate system functions using RAG
2. Maintains conversation history for context-aware responses
3. Generates executable Python code for the matched functions
4. Supports various system operations like opening applications and checking system metrics

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Required Dependencies

- fastapi - Web framework for building APIs
- uvicorn - ASGI server implementation
- sentence-transformers - For text embeddings
- faiss-cpu - For efficient similarity search
- psutil - For system monitoring utilities

## Project Structure

- `api.py` - Main FastAPI application and endpoint definitions
- `rag.py` - RAG system implementation for function matching
- `session_manager.py` - Manages conversation history
- `code_generator.py` - Generates executable Python code
- `function_registry.py` - Contains available system functions

## Available Functions

The system currently supports the following operations:
- Opening Google Chrome (`open_chrome`)
- Opening system calculator (`open_calculator`)
- Getting CPU usage (`get_cpu_usage`)
- Running shell commands (`run_shell_command`)

## API Usage

The system exposes a single endpoint at `/execute`:

```python
POST /execute
{
    "prompt": "string",
    "session_id": "string"
}
```

### Response Format
```python
{
    "function": "function_name",
    "code": "generated_python_code"
}
```

## Key Features

### RAG System
- Uses the 'all-MiniLM-L6-v2' model for text embeddings
- Matches user prompts with function docstrings
- Returns the most relevant function based on semantic similarity

### Session Management
- Maintains conversation history per session
- Stores up to 5 most recent prompts
- Provides context for more accurate function matching

### Code Generation
- Automatically generates executable Python code
- Includes proper error handling
- Creates standalone scripts that can be executed independently

## Running the Application

Start the server using:
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

## Testing with Postman

### Testing the `/execute` Endpoint

1. Open Postman and create a new request
2. Set the request method to `POST`
3. Enter the URL: `http://localhost:8000/execute`
4. Go to the "Headers" tab and add:
   - Key: `Content-Type`
   - Value: `application/json`

5. Go to the "Body" tab:
   - Select "raw"
   - Choose "JSON" format
   - Use the following example payloads:

#### Example 1: Opening Chrome
```json
{
    "prompt": "I want to open chrome browser",
    "session_id": "user123"
}
```

#### Example 2: Checking CPU Usage
```json
{
    "prompt": "What's my current CPU usage?",
    "session_id": "user123"
}
```

#### Example 3: Opening Calculator
```json
{
    "prompt": "Can you open the calculator app",
    "session_id": "user123"
}
```

### Expected Responses

For Chrome:
```json
{
    "function": "open_chrome",
    "code": "\nfrom function_registry import open_chrome\n\ndef main():\n    try:\n        open_chrome()\n        print(\"open_chrome executed successfully.\")\n    except Exception as e:\n        print(f\"Error executing open_chrome: {e}\")\n\nif __name__ == \"__main__\":\n    main()\n    "
}
```

For CPU Usage:
```json
{
    "function": "get_cpu_usage",
    "code": "\nfrom function_registry import get_cpu_usage\n\ndef main():\n    try:\n        get_cpu_usage()\n        print(\"get_cpu_usage executed successfully.\")\n    except Exception as e:\n        print(f\"Error executing get_cpu_usage: {e}\")\n\nif __name__ == \"__main__\":\n    main()\n    "
}
```

### Testing Session History

To test how the system uses conversation history, you can send multiple requests with the same `session_id`. The system will maintain context for up to 5 previous prompts.

### Error Responses

If something goes wrong, you'll receive a response with a 500 status code and an error message:

```json
{
    "detail": "Error message description"
}
```
### Example ScreenShots 

![Postman1](https://github.com/user-attachments/assets/51f6c034-58af-4953-bde0-b4fb268bab9a)

![Postman2](https://github.com/user-attachments/assets/6378e143-0ac0-4b2f-b929-fb684a1c2fea)

### Tips for Testing
- Use different `session_id` values to test session isolation
- Try similar prompts to test the RAG system's matching capabilities
- Test with invalid inputs to verify error handling
- Monitor the server console for additional debugging information