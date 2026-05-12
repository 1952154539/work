import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# 1. 生成 RSA 公私钥对 (2048-bit)
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

print("=== RSA Key Pair Generated ===")
print(f"Private key size: {len(private_key.export_key())} bytes")
print(f"Public key size:  {len(public_key.export_key())} bytes")
print(f"N bit length:     {private_key.n.bit_length()}")
print()

# 2. 找到符合 POW 4 个 0 开头的哈希值的 "昵称 + nonce"
nickname = "haha"
nonce = 0
target_prefix = "0000"

while True:
    content = f"{nickname}{nonce}"
    h = hashlib.sha256(content.encode()).hexdigest()
    if h.startswith(target_prefix):
        print("=== Proof of Work Found ===")
        print(f"  Content: {content}")
        print(f"  SHA256:  {h}")
        print()
        break
    nonce += 1

# 3. 用私钥对 content 进行签名
h_obj = SHA256.new(content.encode())
signature = pkcs1_15.new(private_key).sign(h_obj)

print("=== Signature Created ===")
print(f"  Signature (hex): {signature.hex()}")
print(f"  Signature length: {len(signature)} bytes")
print()

# 4. 用公钥验证签名
h_obj_verify = SHA256.new(content.encode())
try:
    pkcs1_15.new(public_key).verify(h_obj_verify, signature)
    print("=== Signature Verification ===")
    print("  Result: VALID - Signature matches!")
    print(f"  Nickname: {nickname}")
    print(f"  Nonce:    {nonce}")
    print(f"  Message:  {content}")
except (ValueError, TypeError):
    print("  Result: INVALID - Signature does NOT match!")
