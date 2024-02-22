class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for _ in range(array_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def _probe_for_slot(self, key, value=None):
        count_collisions = 0
        while True:
            hash_code = self.hash(key, count_collisions)
            index = self.compressor(hash_code)
            current_array_value = self.array[index]

            if current_array_value is None:
                if value is not None:
                    return index
                return None

            if current_array_value[0] == key:
                return index

            count_collisions += 1

    def assign(self, key, value):
        slot_index = self._probe_for_slot(key, value)
        if slot_index is not None:
            self.array[slot_index] = [key, value]

    def retrieve(self, key):
        slot_index = self._probe_for_slot(key)
        if slot_index is not None:
            return self.array[slot_index][1]
        return None

# Test HashMap
hash_map = HashMap(array_size=15)

# Test assign
hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")

# Test retrieve
print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss")) 