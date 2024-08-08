# HashMap

class HashMap:
    def __init__(self, size=30):
        # constructor with optional size parameter
        # creates buckets each with value of None
        self.size = size
        self.map = [None] * self.size
        self.num_items = 0

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

        # check for resize condition
        if self.num_items / self.size >= 1.5:
            self._resize(2 * self.size)  # double the size

        # if nothing in bucket, insert key_value
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            self.num_items += 1
            return True
        # if key already exists in bucket, update value
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            self.num_items += 1
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
                self.num_items -= 1
                return True

    def _resize(self, new_size):
        # create new map with new size
        new_map = [None] * new_size
        self.size = new_size

        # re-hash all existing key_value pairs
        for bucket in self.map:
            if bucket is not None:
                for key_value in bucket:
                    new_hash = self._get_hash(key_value[0])  # re-hash the key
                    if new_map[new_hash] is None:
                        new_map[new_hash] = list([key_value])
                    else:
                        new_map[new_hash].append(key_value)

    def print(self):
        print("--- HashMap contents ---")
        for item in self.map:
            if item is not None:
                print(str(item))
