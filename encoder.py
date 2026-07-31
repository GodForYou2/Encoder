# ဖိုင်အမည်: encoder.py
import base64
import hashlib

# Password ကို ကုဒ်ထဲတွင် အသေ (Hardcode) သတ်မှတ်ထားခြင်း
SECRET_PASSWORD = "unlimitedyg22"

def generate_encoded_hash(voucher: str) -> str:
    key = hashlib.sha256(SECRET_PASSWORD.encode('utf-8')).digest()
    key_len = len(key)
    
    cipher_bytes = bytearray()
    data_bytes = voucher.encode('utf-8')
    for i, byte in enumerate(data_bytes):
        cipher_bytes.append(byte ^ key[i % key_len])
        
    return base64.b64encode(cipher_bytes).decode('utf-8')

if __name__ == "__main__":
    print("--- Voucher Encoder (Fixed Password) ---")
    raw_voucher = input("Enter Real Voucher Code: ").strip()
    
    if raw_voucher:
        result_hash = generate_encoded_hash(raw_voucher)
        print("\n[+] Encoded Hash Output (Copy this for main tool):")
        print(f"\033[1;32m{result_hash}\033[0m\n")
    else:
        print("Voucher cannot be empty!")
