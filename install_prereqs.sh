#!/bin/bash

# Install system packages
echo "✅ Installing system dependencies..."
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev git

# Install pyenv
echo "✅ Installing pyenv..."
curl https://pyenv.run | bash

# Add pyenv to bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc

# Install Python 3.11.4
echo "✅ Installing Python 3.11.4 with pyenv..."
pyenv install 3.11.4
pyenv global 3.11.4

# Install pip packages
echo "✅ Installing pip packages..."
pip install -r requirements.txt
pip install virtualenv

# Create mlruns folder
echo "✅ Creating mlruns folder..."
mkdir -p ~/mlruns

echo "🎯 Setup complete! You can now start MLflow server."