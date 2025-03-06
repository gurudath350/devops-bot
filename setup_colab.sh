#!/bin/bash
# Install dependencies
pip install -q -r requirements.txt

# Make install scripts executable
chmod +x install_scripts/*.sh

# Setup environment
if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env file. Add your API key!"
fi
