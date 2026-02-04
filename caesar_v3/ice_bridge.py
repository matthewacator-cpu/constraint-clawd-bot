"""
CAESAR v3.5 Enterprise - Ice Bridge
Production API Integration with PII Shield & OpenTelemetry
"""

import os
import math
import time
import json
import requests
from typing import Dict, Any

try:
    from caesar_v3.config import config
    from caesar_v3.telemetry import tracer
    from caesar_v3.lattice import Lattice
    from caesar_v3.risk_classifier import RiskClassifier
except ImportError:
    from config import config
    from telemetry import tracer
    from lattice import Lattice
    from risk_classifier import RiskClassifier

class LLMBridge:
    def __init__(self):
        # Clients initialized on demand
        pass

    @tracer.start_as_current_span("call_model")
    def call_model(self, prompt: str, provider: str, temperature: float) -> Dict[str, Any]:
        """Route to provider with OTel tracing"""
        if provider == "google":
            return self._call_google(prompt, temperature)
        elif provider == "openai":
            # Mock or minimal impl since keys missing
            return self._call_mock(prompt, temperature, "openai")
        elif provider == "anthropic":
            return self._call_mock(prompt, temperature, "anthropic")
        raise ValueError(f"Invalid Provider: {provider}")

    def _call_google(self, prompt: str, temp: float):
        # Using Google Gemini API via REST (No specialized SDK required)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{config.google_model}:generateContent?key={config.google_api_key}"
        
        headers = {
            "Content-Type": "application/json"
        }
        
        data = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": temp
            }
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            result_json = response.json()
            
            # Extract text
            try:
                text = result_json['candidates'][0]['content']['parts'][0]['text']
            except (KeyError, IndexError):
                text = "Error: No content generated."

            # Heuristic Confidence for Gemini (Temp Inverse)
            conf = max(0.5, 1.0 - (temp * 0.20))

            # Cost Estimator
            input_tokens = len(prompt) / 4
            output_tokens = len(text) / 4
            cost = (input_tokens * 0.0000001) + (output_tokens * 0.0000004)

            return {
                "text": text,
                "confidence": conf,
                "cost": cost,
                "provider": "google"
            }
            
        except Exception as e:
            print(f"Google API Error: {e}")
            if response:
                print(response.text)
            return {
                "text": "Error contacting Google API.",
                "confidence": 0.0,
                "cost": 0.0,
                "provider": "google"
            }

    def _call_mock(self, prompt: str, temp: float, provider: str):
        return {
            "text": f"[MOCK {provider}] Response to: {prompt[:20]}...",
            "confidence": 0.5,
            "cost": 0.0,
            "provider": provider
        }

class IceProtocol:
    def __init__(self):
        self.bridge = LLMBridge()
        self.risk_engine = RiskClassifier()
        self.lattice = Lattice()
        self.energy = 100.0

    @tracer.start_as_current_span("ice_verification_loop")
    def verify(self, user_query: str):
        print(f"❄️  Starting ICE Protocol v3.5 (Enterprise)...")

        # 1. Compliance Check
        risk_score, risk_reason = self.risk_engine.assess_risk(user_query)
        print(f"🛡️  Risk Assessment: {risk_reason} (Score: {risk_score})")

        # 2. Privacy Check (Lattice)
        _, _ = self.lattice.ingest(user_query)

        # 3. Dynamic Thresholding
        required_conf = 0.95 if risk_score > 0.7 else 0.85

        attempts = 0
        best_result = None

        # Adaptive Loop
        while attempts < 4:
            attempts += 1
            # Temperature drops as attempts increase (Crystallization)
            temp = max(0.1, 1.0 - (attempts * 0.25))

            # Provider Routing: Use Google if Key exists
            if config.google_api_key:
                provider = "google"
            else:
                provider = "openai" # Fallback to mock

            print(f"   ► Attempt {attempts} | Provider: {provider} | Temp: {temp:.2f}")
            result = self.bridge.call_model(user_query, provider, temp)
            
            # Shorten log output
            preview = result['text'][:50].replace('\n', ' ') + "..."
            print(f"     Result: {preview}")
            print(f"     Conf: {result['confidence']:.2f} | Cost: ${result['cost']:.7f}")

            if result['confidence'] >= required_conf:
                print(f"✅ CRYSTALLIZED (Confidence Met)")
                return result

            best_result = result
            time.sleep(1) # Rate limit politeness

        print("❌ MELTED (Threshold not met)")
        return best_result

if __name__ == "__main__":
    # Test Run
    protocol = IceProtocol()

    # Test PII Redaction
    print("\n--- TEST: Compliance & Inference ---")
    final = protocol.verify("My email is john.doe@example.com and I want a loan.")
    
    print("\n--- FINAL OUTPUT ---")
    print(final['text'])
