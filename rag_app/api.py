# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from function_registry import open_chrome, open_calculator, get_cpu_usage, run_shell_command
from rag import RAGSystem
from session_manager import SessionManager
from code_generator import generate_code

app = FastAPI()
functions = [open_chrome, open_calculator, get_cpu_usage, run_shell_command]
rag_system = RAGSystem(functions)
session_manager = SessionManager()

class RequestBody(BaseModel):
    prompt: str
    session_id: str

@app.post("/execute")
def execute_function(request: RequestBody):
    try:
        # Get session history and build context
        history = session_manager.get_history(request.session_id)
        query = " ".join(history + [request.prompt])
        # Retrieve function and generate code
        function_name = rag_system.retrieve_function(query)
        code = generate_code(function_name)
        # Update session history
        session_manager.add_to_history(request.session_id, request.prompt)
        return {"function": function_name, "code": code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)