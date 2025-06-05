# 🤖 AI Agent Chatbot with Visual Voice Feedback

An interactive AI chatbot built using LangChain's agent architecture with a Tkinter UI and real-time animated voice frequency visualization. This assistant is designed to answer any user queries using large language models (LLMs) and can be further upgraded with powerful tools for enhanced capabilites.

## 🚀 Features

- 🧠 **Scholarly Responses** powered by GPT-4o via OpenAI API
- 🔊 **Text-to-Speech Capability** via `pyttsx3`
- 🌊 **Dynamic Audio Waveform Animation** in real-time
- 🛠️ **Built, Tool-Ready LangChain Agent** 
- 🖥️ **Simplistic, User-Friendly GUI** via Tkinter

---

## 🛠 Tech Stack

| Layer         | Tools / Libraries                  |
|---------------|------------------------------------|
| LLM Backend   | `OpenAI GPT-4o`                    |
| Tools Agent   | `LangChain ToolCallingAgent`       |
| Parsing       | `PydanticOutputParser`             |
| GUI           | `Tkinter`                          |
| TTS           | `pyttsx3`                          |

---

## 🧩 File Structure

```
├── main.py            # Sets up LLM agent with LangChain
├── ui.py              # Tkinter GUI with audial visualization
├── .env               # Your OpenAI API key goes here
├── tools.py           # (Optional) Built-in Tools to enhance the capabilites of the agent
├── README.md          # documentation
```

## 🧪 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-agent-chatbot.git
cd ai-agent-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your environment variables
Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=api key for claude or other llm
```

### 4. Run the Application
```bash
python ui.py
```

## 🧠 How It Works

1. **User Query Submission** in the GUI
2. **LangChain Processing** processes query using `GPT-4o`
3. **Output Parsing** into structured format (topic, summary)
4. **Visual waveform** during text-to-speech response
5. **Vocal Response from Agent** to the user

## 🛠 Adding Additional Tools to Agent (Optional)

To expand agent capabilities, edit `main.py`:
```python
tools = [your_custom_tool]
```
Define tools in `tools.py` using LangChain's `Tool` class.

## 🙋‍♂️ Author

**Thomas Medina**  
🔗 [LinkedIn](https://www.linkedin.com/in/thomas-medina-herrera/)  
📧 tamedin02@gmail.com

---

## 📄 Credentials

This project was implemented using official LangChain Documentation via their official website, 
https://python.langchain.com/docs/how_to/, for Python Tutorials and Tips https://www.youtube.com/TechWithTim, and GPT-4o.

