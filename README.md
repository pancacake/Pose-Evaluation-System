# Pose-Estimation System

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15%2B-41CD52.svg)](https://pypi.org/project/PyQt5/)
[![QFluentWidgets](https://img.shields.io/badge/QFluentWidgets-1.5%2B-00B4D8.svg)](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)

> An intelligent desktop application for pose evaluation and visualization. The UI is built on the refined PyQt5 component library QFluentWidgets, delivering a modern Fluent design experience. Local LLM assistance (via Ollama) transforms numeric scores into actionable guidance.

## 🌟 Overview

Pose-Estimation System provides an end-to-end workflow for ingesting videos, analyzing movements, visualizing per-limb metrics, and generating tailored improvement suggestions with the help of a local LLM. 
It is engineered with PyQt5 and QFluentWidgets to achieve a clean, responsive, and consistent desktop UX.


## ✨ Key Features

### 📥 Video Ingestion
- Load both standard reference videos and user videos for analysis
- Built-in demo assets for quick exploration

### 📊 Pose Evaluation & Visualization (Vis)
- Overall and per-limb scoring (e.g., standardness/accuracy and amplitude)
- Visualization pages to inspect results at a glance

### 🎞️ Video Results (VID)
- Play aligned/processed comparison videos for qualitative inspection

### 🤖 AI Assistant
- Local LLM (Ollama) turns computed metrics into human-friendly recommendations
- Default model: `qwen2.5:3b` (configurable)

### ⚙️ Settings & 🔎 Help
- Theme, language, and download directory management
- Help and support links surfaced within the app

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Windows 10/11 recommended (cross-platform PyQt is supported)

### Installation
```bash
git clone <your-repo-url>
cd Pose-Estimation System
pip install -r requirements.txt
```

### (Optional) Local LLM with Ollama
```bash
# Install and start Ollama (see official docs)
ollama pull qwen2.5:3b
# If running remotely, set OLLAMA_HOST accordingly
```

### Launch
```bash
python main.py
```
On first launch, the application reads `app/common/config.py` and `app/config/config.json` for theme, language, and folder settings.

## 📖 Usage Guide

1. Home: read quick guidance; Help: access support links
2. Demo/Upload: import a standard reference video and a user video
3. Vis: review overall and per-limb scores with visualizations
4. VID: play the aligned result video
5. AI: ask domain questions and receive tailored improvement suggestions

## 🏗️ Architecture

### Frontend (Desktop UI)
- PyQt5 + PyQtWebEngine: core UI and embedded web content
- QFluentWidgets: modern Fluent design components and UX patterns

### Views & Navigation
- `MainWindow` organizes pages: Home, Upload, Vis, VID, AI, Help, Settings
- Reusable components located under `app/components/*`

### Common Utilities & Resources
- `app/common/*` for config, styling, signals, i18n, resource loading
- `app/resource/*` for images, icons, QSS themes, and translations managed by `resource.qrc`

### Optional Local LLM
- `app/view/llm_worker.py` integrates Ollama for on-device inference
- `qwen2.5-7b/*` shows a Transformers/LangChain-based local LLM class for experimentation

## 🔧 Configuration

- Runtime configuration is stored in `app/config/config.json` and described in `app/common/config.py`
- Key options: theme mode, DPI scaling, language, download folder
- Update URLs for Help/Home in `app/common/config.py` as needed

## 📁 Project Structure

```
root
│  main.py                 # Application entry point
│  run_server.py           # Placeholder for server-side extensions
│  requirements.txt        # Python dependencies (replaces PESUI_ENV.yml)
│
├─app
│  ├─common                # Config, style, signals, i18n, resources
│  ├─components            # Reusable UI components
│  ├─resource              # Images / QSS themes / translations / qrc
│  ├─UI                    # QtDesigner generated and adjusted UI
│  └─view                  # Page views and navigation
│
└─qwen2.5-7b              # Optional: local LLM examples (Qwen)
       llm.py
       api-chat.py
       download_model.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m "Add AmazingFeature"`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## 📄 License

Specify the license that applies to this project and add a `LICENSE` file. Third-party dependencies are subject to their respective licenses.
