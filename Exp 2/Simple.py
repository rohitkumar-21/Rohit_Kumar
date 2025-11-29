import hashlib 

M="Hello"
Digest=hashlib.sha256(M.encode()).hexdigest()
print (M)
print(Digest)
M="Hell"
Digest=hashlib.sha256(M.encode()).hexdigest()
print(Digest)
