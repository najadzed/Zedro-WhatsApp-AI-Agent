# Zedro AI - WhatsApp Chatbot

A multilingual WhatsApp AI assistant built with FastAPI, LangChain, and OpenAI.

## Features

- 🤖 **Multilingual Support**: Responds in the same language as the user
- 🎤 **Voice Note Processing**: Transcribes and responds to voice messages using OpenAI Whisper
- 🔍 **RAG (Retrieval-Augmented Generation)**: Uses vector embeddings for context-aware responses
- 📱 **WhatsApp Integration**: Seamless integration with WhatsApp via Twilio
- 🚀 **FastAPI Backend**: Modern, fast, and scalable API framework
- 👨‍💻 **Developer Identity**: Automatically responds with "Najad" when asked about creator/developer
- 🎯 **Smart Voice Processing**: Voice messages are transcribed and processed through the RAG pipeline

## Prerequisites

- Python 3.8+
- OpenAI API Key
- Twilio Account (for WhatsApp integration)
- FFmpeg (for voice processing)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd zedro
   ```

2. **Create virtual environment**
   ```bash
   python -m venv zed_env
   ```

3. **Activate virtual environment**
   - Windows: `zed_env\Scripts\activate`
   - Linux/Mac: `source zed_env/bin/activate`

4. **Install dependencies (local/dev)**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TWILIO_ACCOUNT_SID=your_twilio_account_sid_here
   TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
   WHATSAPP_NUMBER=your_whatsapp_number_here
   ```

6. **Install FFmpeg** (for voice processing)
   - Windows: Download from https://ffmpeg.org/download.html
   - Linux: `sudo apt install ffmpeg`
   - Mac: `brew install ffmpeg`

## Usage

### Start the Chatbot

**Option 1: Using the startup script**
```bash
python start_chatbot.py
```

**Option 2: Manual start (local/dev)**
```bash
zed_env\Scripts\uvicorn.exe main:app --host 127.0.0.1 --port 8000 --reload
```

### Deploy to Render

1. Push your repo to GitHub
2. In Render, create a New Web Service and connect your repo
3. Render will detect `render.yaml` and auto-configure
4. Add environment variables in Render Dashboard:
   - `OPENAI_API_KEY`
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `WHATSAPP_NUMBER`
5. Deploy. Render will run: `uvicorn main:app --host 0.0.0.0 --port $PORT`

No `.env` file is needed on Render; use the dashboard env vars.

### API Endpoints

- **Root**: `http://127.0.0.1:8000/` - Health check
- **Docs**: `http://127.0.0.1:8000/docs` - Interactive API documentation
- **WhatsApp Webhook**: `http://127.0.0.1:8000/whatsapp` - Twilio webhook endpoint

### Testing

Test the chatbot by sending a POST request to the WhatsApp webhook:

```bash
curl -X POST "http://127.0.0.1:8000/whatsapp" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "Body=Hello&MessageType=text"
```

### Voice Message Testing

Test voice message processing:

```bash
curl -X POST "http://127.0.0.1:8000/whatsapp" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "MessageType=voice&MediaUrl0=https://example.com/audio.mp3"
```

### Developer Identity Testing

Test developer identity responses:

```bash
curl -X POST "http://127.0.0.1:8000/whatsapp" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "Body=Who created you?&MessageType=text"
```

## Project Structure

```
zedro/
├── agents/           # AI agents and handlers
│   ├── rag_agent.py     # RAG pipeline for text responses
│   ├── voice_handler.py # Voice note processing
│   └── translator.py    # Translation utilities
├── retriever/        # Vector store and embeddings
│   └── vectorstore.py   # ChromaDB vector store
├── routes/           # API routes
│   └── whatsapp.py     # WhatsApp webhook endpoint
├── utils/            # Utility functions
├── data/             # Data storage
│   └── embeddings/      # Vector embeddings database
├── main.py           # FastAPI application
├── config.py         # Configuration settings
├── requirements.txt  # Python dependencies
└── start_chatbot.py  # Startup script
```

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `TWILIO_ACCOUNT_SID`: Twilio account SID (required)
- `TWILIO_AUTH_TOKEN`: Twilio auth token (required)
- `WHATSAPP_NUMBER`: Your WhatsApp number (required)

### RAG Configuration

The chatbot uses ChromaDB for vector storage and OpenAI embeddings. The vector store is automatically created and populated when the application starts.

## Troubleshooting

### Common Issues

1. **FFmpeg not found**
   - Install FFmpeg and ensure it's in your PATH
   - Voice processing will not work without FFmpeg

2. **OpenAI API Key not set**
   - Ensure your `.env` file contains a valid `OPENAI_API_KEY`
   - Check that the `.env` file is in the root directory

3. **Import errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Activate the virtual environment before running

4. **Vector store errors**
   - The embeddings database will be created automatically
   - Ensure the `data/embeddings/` directory exists and is writable

### Logs

The application logs important events and errors to the console. Check the terminal output for debugging information.

## Development

### Adding New Features

1. **New AI Agents**: Add to the `agents/` directory
2. **New Routes**: Add to the `routes/` directory
3. **New Utilities**: Add to the `utils/` directory

### Testing

Run the application in development mode with auto-reload:
```bash
zed_env\Scripts\uvicorn.exe main:app --reload
```

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please create an issue in the repository or contact the development team.
