try:
    from core.apis import principal
    from core import app
    print("Imports successful")
except ImportError as e:
    print(f"ImportError: {e}")