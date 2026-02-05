# NVIDIA-NIM

Example code for using NVIDIA NIM (NVIDIA Inference Microservices) APIs.

## Project Structure

```text
.
├── openai.py         # Example using OpenAI-compatible API
├── rest.py           # Example using standard REST API
├── requirements.txt  # Python dependencies
├── .env              # API Key configuration (not committed)
└── README.md
```

## Prerequisites

- Python 3.9+ recommended
- An [NVIDIA NIM API key](https://build.nvidia.com/explore/discover)

## Setup

1. Create a `.env` file in the project root containing your API key:
   ```env
   NV_API_KEY=nvapi-your-key-here
   ```

2. Create and activate a virtual environment (optional but recommended):

   **Linux/macOS**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   **Windows**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

This repository contains two example scripts demonstrating different ways to interact with the API.

### 1. REST API (`rest.py`)
Uses the standard `requests` library to make a direct HTTP POST call.
- **Model**: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- **Behavior**: Loads `NV_API_KEY` directly from your `.env` file.

### 2. OpenAI SDK (`openai.py`)
Uses the `openai` Python client, pointing it to NVIDIA's base URL.
- **Model**: `meta/llama3-70b-instruct`
- **Behavior**: Expects `NV_API_KEY` to be set in your active environment.

### Running the examples

To run the REST example:
```bash
python rest.py
```

To run the OpenAI SDK example (ensure your environment variable is set, or export it):
```bash
# Example of exporting the key if not using a tool that auto-loads .env
export NV_API_KEY=$(grep NV_API_KEY .env | cut -d '=' -f2)

python openai.py
```

### Example Output

*Output from `openai.py` (text streaming):*

```text
In the land of the silicon chip,
A GPU took a computing trip.
With cuda cores bright,
It processed with might,
And rendered the graphics with zip!
```

## Configuration

- **API Key**: The scripts reference `NV_API_KEY`.
- **Models**: To change the model, update the `model` identifier string inside `rest.py` or `openai.py`.

## Troubleshooting

- `401 Unauthorized`: Your API key is missing or invalid.
- `429 Too Many Requests`: Rate limit exceeded. Retry after a short delay.
- `ConnectionError`: Ensure you are connected to the internet and can reach `integrate.api.nvidia.com`.

## References

- [NVIDIA NIM APIs Documentation](https://build.nvidia.com/explore/discover)
- [Available Models](https://build.nvidia.com/models)

## License

[MIT License](LICENSE)
