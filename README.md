# Multi-AI Agent Tech News Generator 🤖

An innovative AI-powered system that automatically generates comprehensive tech news articles using collaborative AI agents. The project leverages CrewAI to orchestrate multiple AI agents that work together to research and write engaging tech content.

## 🌟 Features

- **Dual AI Agent System**
  - Senior Researcher Agent: Conducts in-depth research on tech topics
  - Writer Agent: Transforms research into engaging articles
- **Flexible LLM Integration**
  - Supports both local (Ollama) and cloud-based (OpenAI) language models
  - Easy configuration through environment variables
- **Web Interface**
  - Built with Streamlit for easy interaction
  - Real-time article generation
  - PDF export functionality
- **Automated Research Pipeline**
  - Internet search capabilities using SerperDev API
  - Comprehensive topic analysis
  - Trend identification

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Ollama (for local LLM)
- OpenAI API key (optional)
- SerperDev API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Hetpat02/Multi-AI-Agent_Tech-News-Generator.git
cd Multi-AI-Agent_Tech-News-Generator
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Streamlit web interface:
```bash
streamlit run webapp.py
```
2. Open your browser and navigate to the provided local URL (typically http://localhost:8501)

3. Enter a technology topic and click "Generate Report"

## 🛠️ Project Structure

- `agents.py`: Defines AI agent configurations and roles
- `tasks.py`: Contains task definitions for research and writing
- `tools.py`: Implements research tools and API integrations
- `webapp.py`: Streamlit web interface implementation

## 💡 Usage Example

1. Enter a technology topic (e.g., "Quantum Computing")
2. Click "Generate Report"
3. Wait for the agents to:
   - Research the latest trends
   - Analyze the information
   - Generate a comprehensive article
4. Download the result as a PDF or view it directly in the interface

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the multi-agent framework
- Streamlit for the web interface framework
- OpenAI and Ollama for LLM support

## 📧 Contact

Your Name - [pathakhet2@gmail.com / https://www.linkedin.com/in/het-pathak-1b2361213/]

Project Link: [https://github.com/Hetpat02/Multi-AI-Agent_Tech-News-Generator](https://github.com/Hetpat02/Multi-AI-Agent_Tech-News-Generator)
