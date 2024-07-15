import hashlib
import time
class Block:
    def __init__(self, index, previous_hash, timestamp, patient_id, record_id, doctor_id, diagnosis, treatment, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.patient_id = patient_id
        self.record_id = record_id
        self.doctor_id = doctor_id
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.hash = hash
        self.nonce = nonce

class MedicalRecordBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(0, "0", int(time.time()), "GenesisPatient", "GenesisRecord", "GenesisDoctor", "None", "None", self.calculate_hash(0, "0", int(time.time()), "GenesisPatient", "GenesisRecord", "GenesisDoctor", "None", "None", 0), 0)
        self.chain.append(genesis_block)

    def add_medical_record(self, patient_id, record_id, doctor_id, diagnosis, treatment):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        previous_hash = previous_block.hash
        nonce = self.proof_of_work(index, previous_hash, timestamp, patient_id, record_id, doctor_id, diagnosis, treatment)
        new_hash = self.calculate_hash(index, previous_hash, timestamp, patient_id, record_id, doctor_id, diagnosis, treatment, nonce)
        new_block = Block(index, previous_hash, timestamp, patient_id, record_id, doctor_id, diagnosis, treatment, new_hash, nonce)
        self.chain.append(new_block)

    def proof_of_work(self, index, previous_hash, timestamp, patient_id, record_id, doctor_id, diagnosis, treatment):
        nonce = 0
        while True:
            new_hash = self.calculate_hash(index, previous_hash, timestamp, patient_id, record_id, doctor_id, diagnosis, treatment, nonce)
            if new_hash[:4] == "0000":
                return nonce
            nonce += 1

    def calculate_hash(self, index, previous_hash, timestamp, patient_id, record_id, doctor_id, diagnosis, treatment, nonce):
        value = str(index) + str(previous_hash) + str(timestamp) + str(patient_id) + str(record_id) + str(doctor_id) + str(diagnosis) + str(treatment) + str(nonce)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def print_chain(self):
        for block in self.chain:
            print(vars(block))

if __name__ == '__main__':
    medical_record_blockchain = MedicalRecordBlockchain()
    medical_record_blockchain.add_medical_record("Patient_1", "Record_1", "Doctor_A", "Flu", "Rest and hydration")
    medical_record_blockchain.add_medical_record("Patient_2", "Record_2", "Doctor_B", "Fracture", "Cast and rest")
    medical_record_blockchain.add_medical_record("Patient_3", "Record_3", "Doctor_C", "Diabetes", "Insulin therapy")
    medical_record_blockchain.print_chain()