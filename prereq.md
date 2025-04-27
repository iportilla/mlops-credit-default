# Prerequisites for Credit Default Predictor MLOps Lab

Welcome to the setup guide for the Credit Default MLOps Lab!
Follow these steps to prepare your environment before starting the exercises.

---

## 1. Install System Packages

```bash
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev git
```

---

## 2. Install pyenv (Python Version Manager)

```bash
curl https://pyenv.run | bash
```

---

## 3. Configure Your Shell

For bash:

```bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
```

For zsh:

```bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
source ~/.zshrc
```

---

## 4. Verify pyenv Installation

```bash
pyenv --version
```

---

## 5. Install Python 3.11.4

```bash
pyenv install 3.11.4
pyenv global 3.11.4
```

---

## 6. Install Project Requirements

```bash
pip install -r requirements.txt
```

---

# Ready to start the lab!