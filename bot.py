import os
import re
import json
import subprocess
from openrouter import OpenRouter
from IPython.display import display, Markdown
from dotenv import load_dotenv  # Add this import

class DevOpsBot:
    def __init__(self):
        # Load environment variables
        load_dotenv()  # Loads from .env file
        
        # Get API key from environment
        self.client = OpenRouter(
            api_key=os.getenv("OPENROUTER_API_KEY")
        )
        
    def _load_error_db(self):
        with open('error_db.json') as f:
            return json.load(f)['patterns']
        
    def resolve_error(self, error_msg):
        # Check local patterns first
        for entry in self.error_db:
            if re.search(entry['pattern'], error_msg, re.IGNORECASE):
                return entry['solution']
            
        # Query Qwen
        response = self.client.generate(
            model=self.model,
            prompt=f"Fix this error on Ubuntu 22.04:\n{error_msg}",
            max_tokens=500
        )
        return response.text.strip()
    
    def install_tool(self, tool_name):
        script_path = f"install_scripts/{tool_name}.sh"
        if not os.path.exists(script_path):
            return f"⚠️ No script for {tool_name}"
        
        try:
            result = subprocess.run(
                [script_path], 
                capture_output=True, 
                text=True,
                shell=True
            )
            return f"✅ Installed {tool_name}:\n{result.stdout}"
        except Exception as e:
            return f"❌ Failed: {str(e)}"
    
    def execute_command(self, command):
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )
            return f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        except Exception as e:
            return f"❌ Execution failed: {str(e)}"
    
    def update_repo(self):
        subprocess.run(["git", "pull", "origin", "main"])
        return "🔄 Updated! Please restart the runtime."
