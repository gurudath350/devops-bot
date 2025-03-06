#!/bin/bash
# Install dependencies
pip install -q -r requirements.txt

# Setup environment
if [ ! -f .env ]; then
  cp .env.example .env
  echo "⚠️ Add your OpenRouter API key to .env file!"
fi

# Make scripts executable
chmod +x install_scripts/*.sh
