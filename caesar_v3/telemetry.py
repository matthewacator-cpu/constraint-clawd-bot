try:
    from caesar_v3.config import config
except ImportError:
    from config import config
from contextlib import contextmanager

class NoOpTracer:
    def start_as_current_span(self, name):
        # This needs to handle both @decorator and 'with' usage
        # But in the code it's used as a decorator @tracer...
        # If used as decorator, this function is called with 'name'
        # and returns the actual decorator.
        
        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
            
        class ContextManager:
            def __enter__(self): return self
            def __exit__(self, exc_type, exc_val, exc_tb): pass
            def __call__(self, func): return decorator(func)
            
        return ContextManager()

tracer = NoOpTracer()
