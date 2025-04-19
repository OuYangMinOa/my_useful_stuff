# UV 簡易教學 (UV Simple Tutorial)

## 什麼是 UV (What is UV)

UV 是一個高效能的 Python 套件管理工具，由 Astral 團隊開發。它比傳統的 pip 更快，支援虛擬環境管理，並提供了更好的依賴解析能力。

UV is a high-performance Python package management tool developed by the Astral team. It's faster than traditional pip, supports virtual environment management, and provides better dependency resolution capabilities.

## 安裝 UV (Installing UV)

```bash
# 使用 pip 安裝 UV
# Install UV using pip
pip install uv

# 或使用 curl (Linux/macOS)
# Or use curl (Linux/macOS)
curl -sSf https://astral.sh/uv/install.sh | sh

# 或使用 PowerShell (Windows)
# Or use PowerShell (Windows)
irm https://astral.sh/uv/install.ps1 | iex
```

## 基本使用方法 (Basic Usage)

### 建立虛擬環境 (Create a Virtual Environment)

```bash
# 建立虛擬環境
# Create a virtual environment
uv venv

# 指定 Python 版本建立虛擬環境
# Create a virtual environment with a specific Python version
uv venv --python=3.10
```

### 安裝套件 (Install Packages)

```bash
# 安裝單一套件
# Install a single package
uv pip install pandas

# Install a package and add in pyproject.toml
uv add pandas

# 從 requirements.txt 安裝
# Install from requirements.txt
uv pip add -r requirements.txt

# 安裝開發依賴
# Install development dependencies
uv pip install -e ".[dev]"
```
## 比較 `uv add` v.s `uv pip install`

- #### `uv add <dependency>`

    1. 此命令用於將依賴添加到專案的 pyproject.toml 文件中。這意味著依賴會被記錄在專案的配置中，並且在未來的環境同步中會自動處理。

    2. 使用 uv add 時，您可以直接將依賴添加到專案中，並且它會更新鎖定文件（如果存在）。

    3. 這種方法適合於需要持續管理專案依賴的情況。

- #### `uv pip install <dependency>`

    1. 此命令則是直接使用 pip 來安裝依賴，這意味著依賴會被安裝到當前的虛擬環境中，但不會自動更新 pyproject.toml 文件。

    2. 使用 uv pip install 時，您需要手動管理依賴的版本和更新，這可能會導致未來的環境不一致。

    3. 這種方法適合於臨時安裝或測試依賴的情況。

### 使用 UV 加速依賴管理 (Speed Up Dependency Management with UV)

```bash
# 直接從 pyproject.toml 安裝依賴
# Install dependencies directly from pyproject.toml
uv pip sync pyproject.toml

# 產生 requirements.txt 檔案
# Generate requirements.txt file
uv pip compile pyproject.toml -o requirements.txt
```

### 可重現的環境 (Reproducible Environments)

```bash
# 凍結當前環境
# Freeze current environment
uv pip freeze > requirements.txt

# 同步環境 (pyproject.toml)
# Sync environment
uv pip sync requirements.txt
```

## 參考資源 (References)

- [UV 官方文件 (UV Official Documentation)](https://github.com/astral-sh/uv)
- [Astral 官方網站 (Astral Official Website)](https://astral.sh/)