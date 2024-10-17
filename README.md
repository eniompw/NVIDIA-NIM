# NVIDIA-NIM

Example code for using NVIDIA NIM APIs

## Setup

1. Create a `.env` file in the project root:
   ```
   NV_API_KEY=your-api-key-here
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

This repository contains two example scripts:

1. `rest.py`: A simple REST API implementation
2. `openai.py`: An example using the OpenAI-compatible API

Run either script to test the NVIDIA NIM API:

```bash
python rest.py
# or
python openai.py
```

## References

- [NVIDIA NIM APIs Documentation](https://build.nvidia.com/explore/discover)
- [Available Models](https://build.nvidia.com/models)

## License

[MIT License](LICENSE)
