# 🧠 Aidnox SDK for Python

A lightweight and developer-friendly Python SDK for interacting with the **Aidnox AI Diagnostic Platform** — enabling easy integration of healthcare AI features like symptom-based diagnosis, image-based predictions, and health data reporting.

> ⚕️ Built for developers, hospitals, health researchers, and AI-enabled health tools.

---

## 🚀 Features

- 🔍 Text-based symptom diagnosis (LLM-powered)
- 🖼️ Image-based diagnosis (e.g., for skin conditions)
- 📡 Easy connection to Aidnox cloud API (REST)
- 📥 Offline support integration coming soon
- 🛠️ Lightweight and simple to extend

---

## 📦 Installation

Install via [PyPI](https://pypi.org):

```bash
pip install aidnox-sdk
````

Or install from source:

```bash
git clone https://github.com/Aidnox/aidnox-sdk-python.git
cd aidnox-sdk-python
pip install .
```

---

## 🧑‍💻 Quick Start

### 1. Import and initialize the client

```python
from aidnox_sdk import AidnoxClient

# Initialize the client with your API key (replace with your actual key)
client = AidnoxClient(api_key="your_api_key_here")
```

### 2. Run text-based diagnosis

```python
result = client.diagnose_symptoms("I have fever, rash, and joint pain")
print(result)
```

### 3. Run image-based diagnosis

```python
result = client.diagnose_image("path/to/image.jpg")
print(result)
```

---

## 📚 Example Response

```json
{
  "diagnosis": "Dengue Fever",
  "confidence": 0.92,
  "recommendation": "Consult a doctor and perform blood tests"
}
```

---

## 🧠 Use Cases

* Mobile & web healthcare apps
* Rural & offline health diagnostics
* Developer APIs for healthcare platforms
* AI-based triage systems

---

## 🛡️ Authentication

All requests require a valid `API Key` from Aidnox. You can obtain one by [contacting our team](https://aidnox-web.vercel.app).

---

## 🔧 Configuration

You can pass additional config options when initializing the client:

```python
client = AidnoxClient(
    api_key="your_api_key_here",
    base_url="https://api.aidnox.ai/v1",  # optional override
    timeout=10  # request timeout in seconds
)
```

---

## 📂 File Structure

```
aidnox-sdk-python/
├── aidnox_sdk/
│   ├── __init__.py
│   ├── client.py
│   └── utils.py
├── tests/
│   └── test_client.py
├── setup.py
├── README.md
└── LICENSE
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 🤝 Contributing

We welcome PRs! Feel free to open issues and contribute features or improvements.

### To contribute:

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/xyz`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push and create a pull request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 🌐 Links

* 🌍 [Aidnox Website](https://aidnox-web.vercel.app)
* 💡 [Aidnox GitHub Org](https://github.com/aidnox)
* 🧠 [Aidnox AI SDK](https://github.com/aidnox/aidnox-sdk-python)

---

## 💬 Questions or Support?

Open an issue or contact the Aidnox team at [support@aidnox.ai](mailto:hamza.00dev1@gmail.com)
