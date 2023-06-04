

from base64 import b64encode, b64decode
text           = "Hello World"
text_as_bytes  = text.encode('utf-8')              # Encode text to bytes
print(text_as_bytes, 'text as bytes')
base64_bytes   = b64encode(text_as_bytes)          # Outputs b''
print(base64_bytes, 'base64 bytes')
base64_text    = base64_bytes.decode('utf-8')      # Transform to string "text"
print(base64_text, 'base64 text')
original_bytes = b64decode(base64_bytes)           # Convert back to bytes data - b''
print(original_bytes, 'original bytes')
original_text  = original_bytes.decode('utf-8')    # back to text
print(original_text, 'original text')