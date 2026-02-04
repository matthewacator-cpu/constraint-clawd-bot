import os

class CaesarConfig:
    def __init__(self):
        # Load from .env manually since python-dotenv might be missing
        self._load_env()

        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY", "")
        self.google_api_key = os.getenv("GOOGLE_API_KEY", "")

        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.anthropic_model = os.getenv("ANTHROPIC_MODEL", "claude-3-5-haiku-20241022")
        self.google_model = os.getenv("GOOGLE_MODEL", "gemini-2.0-flash")

        self.enable_pii_redaction = os.getenv("ENABLE_PII_REDACTION", "false").lower() == "true"
        self.enable_otel_tracing = os.getenv("ENABLE_OTEL_TRACING", "false").lower() == "true"
        self.otel_endpoint = os.getenv("OTEL_ENDPOINT", "http://localhost:4317")

    def _load_env(self):
        try:
            with open(".env", "r") as f:
                for line in f:
                    if "=" in line and not line.startswith("#"):
                        key, val = line.strip().split("=", 1)
                        os.environ[key] = val
        except FileNotFoundError:
            pass

config = CaesarConfig()
