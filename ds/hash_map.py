def _check_null(key):
    if key is None:
        raise KeyError("Accessing an entry w/o providing a key")


class HashMap:
    class MapEntry:
        def __init__(self, key: int, data):
            self.key = key
            self.data = data

        def __repr__(self):
            return str(self.data)

    def __init__(self, buckets_count=10):
        self._buckets_count = buckets_count
        self.buckets = [[] for _ in range(self._buckets_count)]

    def __getitem__(self, key: int):
        # Time complexity: O(1) average, O(n) worst case
        return self.get(key)

    def __setitem__(self, key: int, value):
        # Time complexity: O(1) average, O(n) worst case
        self.upsert(key, value)

    def upsert(self, key: int, data):
        # Time complexity: O(1) average, O(n) worst case
        entry = HashMap.MapEntry(key, data)
        bucket, item, index = self._find_item(key)
        if item:
            bucket[index] = entry
        else:
            bucket.append(entry)

    def get(self, key):
        # Time complexity: O(1) average, O(n) worst case
        bucket, item, _ = self._find_item(key)
        if item:
            return item.data

    def values(self):
        # Time complexity: O(n)
        return [entry.data for bucket in self.buckets for entry in bucket]

    def remove(self, key):
        # Time complexity: O(1) average, O(n) worst case
        bucket, item, index = self._find_item(key)
        if item:
            return bucket.remove(item)

    def _find_item(self, key):
        _check_null(key)
        bucket = self._get_bucket(key)
        for index, item in enumerate(bucket):
            if item.key == key:
                return bucket, item, index
        return bucket, None, None

    def _hash(self, value):
        return value % self._buckets_count

    def _get_bucket(self, key):
        index = self._hash(key)
        return self.buckets[index]
