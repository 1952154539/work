import hashlib
import time

nickname = "haha"
nonce = 0

for target_zeros in [4, 5]:
    target_prefix = "0" * target_zeros
    nonce = 0
    start = time.time()

    while True:
        content = f"{nickname}{nonce}"
        h = hashlib.sha256(content.encode()).hexdigest()
        if h.startswith(target_prefix):
            elapsed = time.time() - start
            print(f"[{target_zeros} zeros]")
            print(f"  Time : {elapsed:.4f}s")
            print(f"  Hash : {content}")
            print(f"  SHA256: {h}")
            print()
            break
        nonce += 1
