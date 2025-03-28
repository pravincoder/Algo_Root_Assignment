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

## Notes
- The calculator function is Windows-specific and needs modification for other operating systems
- Shell command execution should be used with caution in production environments
- Session history is stored in memory and will be cleared on server restart

## Security Considerations
- Function execution is limited to predefined system operations.
- Shell command execution should be properly sanitized in production.
- Consider implementing authentication for the API endpoint.