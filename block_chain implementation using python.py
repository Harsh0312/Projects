import hashlib
class harshcoin:
    def __init__(self,previous_hash,transaction):
        self.previous_hash=previous_hash
        self.transaction=transaction
        self.block_data="-".join(transaction)+"-"+self.previous_hash
        self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()
t1="Harsh send 4 to Neer"
t2="jude sends 4 to Darshan"
t3="Darshan sends 4 to jude"
t4="Neer sends 4 to Harsh"
t5="Harsh sends 4 to Neer"
t6="jude sends 4 to Darshan"

first_block=harshcoin('',[t1,t2])
print(first_block.block_data)
print(first_block.block_hash)

second_block=harshcoin(first_block.block_hash,[t3,t4])
print(second_block.block_data)
print(second_block.block_hash)


third_block=harshcoin(second_block.block_hash,[t5,t6])
print(third_block.block_data)
print(third_block.block_hash)

 
