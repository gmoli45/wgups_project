# HashMap

class HashMap:
    def __init__(self, size=6):
        # constructor with optional size parameter
        # creates buckets each with value of None
        self.size = size
        self.map = [None] * self.size

    def _get_hash(self, key):
        # Polynomial hashing
        base = 31
        hash = 0
        for char in str(key):
            hash = (hash * base + ord(char)) % self.size
        return hash

        ## old hashing function
        # hash = 0
        # for char in str(key):
        #     hash += ord(char)
        # return hash % self.size

    def add(self, key, value):
        # handles both inserting and updating
        key_hash = self._get_hash(key)
        key_value = [key, value]

        # if nothing in bucket, insert key_value
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        # if key already exists in bucket, update value
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        # if bucket not empty, find and retrieve value by key
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def remove(self, key):
        key_hash = self._get_hash(key)
        # if key in bucket, find index and remove key_value pair
        if self.map[key_hash] is None:
            return False
        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print("--- HashMap contents ---")
        for item in self.map:
            if item is not None:
                print(str(item))
