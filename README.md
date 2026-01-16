# 🧠 Project MemToken: The Stateless AI Memory Bridge

MemToken is a privacy-focused architecture for Large Language Models (LLMs) that enables long-term memory without a central database. By using client-side JWT (JSON Web Tokens) to store conversation summaries, the user’s "context" stays in their own browser/device, not on your server.
🚀 Key Features

    Stateless Architecture: No SQL or NoSQL databases required.

    Privacy-First: Conversations are summarized and signed into a JWT stored in the user's browser/device.

    Context Preservation: Automatically restores past projects (like your "ABI Project") even after a browser refresh.

    Zero-Login Personalization: Users get a personalized AI experience without needing to create an account.

🛠️ Tech Stack

    AI Brain: Groq (Llama 3.1 8B)

    Framework: Streamlit (Python) — Flutter version in development

    Memory Logic: LangChain (SystemMessage injection)

    Security: PyJWT (HS256 Signing)

    Client Storage: extra-streamlit-components (Browser Cookies)

🏗️ How It Works (The Memory Loop)

    The Handshake: When the app loads, it retrieves the chat_memory cookie from the browser.

    The Verification: The backend decodes the JWT using a private key to ensure it hasn't been tampered with.

    The Jumpstart: The summary inside the JWT is injected into the AI's "System Prompt" as the foundational context.

    The Secretary: Every few messages, a secondary LLM call summarizes the current progress.

    The Update: This new summary overwrites the old JWT, updating the user's local "memory."

📥 Getting Started
1. Prerequisites

    Python 3.9+

    Groq API Key

2. Installation
Bash

# Clone the repository
git clone https://github.com/your-username/memtoken-ai.git
cd memtoken-ai

# Install dependencies
pip install streamlit langchain-groq pyjwt python-dotenv extra-streamlit-components

3. Configuration

Create a .env file in the root directory:
Code snippet

GROQ_API_KEY=your_gsk_key_here
JWT_SECRET=your_custom_secret_key

4. Run the App
Bash

streamlit run bot.py

📈 Roadmap (Startup Vision)

    [ ] Phase 1 (Current): Python/Streamlit MVP with Cookie-based JWT storage.

    [ ] Phase 2: Move to Flutter for cross-platform (iOS/Android) support using flutter_secure_storage.

    [ ] Phase 3: Implement Encrypted Payloads (JWE) so even the server can't read the summary without a client-side key.

    [ ] Phase 4: "Brain Export" — allow users to download their memory as a .brain file.

🤝 Contributing

This is an open-source project aimed at making AI more private. Feel free to fork the repo, create a branch, and submit a PR!
