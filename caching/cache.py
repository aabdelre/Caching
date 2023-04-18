from memory import Memory
import utilities
import random

# This class simply adds a variable that will keep track of cache
# hits. This should be incremented in a subclass whenever the cache is
# hit.
class AbstractCache(Memory):
    def name(self):
        return "Cache"

    # Takes two parameters. Data is the data that forms the
    # "memory". Size is a non-negative integer that indicates the size
    # of the cache.
    def __init__(self, data, size=5):
        super().__init__(data)
        self.cache_hit_count = 0

    # Returns information on the number of cache hit counts
    def get_cache_hit_count(self):
        # TODO: Edit this code to correctly return the count of cache hits.
        return self.cache_hit_count
    
class CyclicCache(AbstractCache):
    def name(self):
        return "Cyclic"

    # TODO: Edit the code below to provide an implementation of a cache that
    # uses a cyclic caching strategy with the given cache size. You
    # can use additional methods and variables as you see fit as long
    # as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)
        self.cache = []
        self.locations = []
        self.cache_size = size

    def lookup(self, address):
        #print("Using This One!")
        if address in self.locations:
            #print(address, self.locations) 
            self.cache_hit_count += 1
            return self.cache[self.locations.index(address)]

        self.locations.append(address)
        self.cache.append(self.memory[address])
        if len(self.cache) > self.cache_size: 
            self.cache.pop(0)
            self.locations.pop(0)
        self.memory_hit_count += 1
        ### Is there a way to try multiple try/excpetion statements?
        try:
            return self.memory[address]
        except IndexError as error:
            print("Error: Unknown memory location")
            return None

class LRUCache(AbstractCache):
    def name(self):
        return "LRU"

    # TODO: Edit the code below to provide an implementation of a cache that
    # uses a least recently used caching strategy with the given cache size.
    # You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)

class RandomCache(AbstractCache):
    def name(self):
        return "Random"

    # TODO: Edit the code below to provide an implementation of a cache that
    # uses a random eviction strategy with the given cache size.
    # You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.
    # Make sure that you increment cache_hit_count when appropriate!
    
    def __init__(self, data, size=5):
        super().__init__(data)
        self.cache = []
        self.locations = []
        self.cache_size = size

    def lookup(self, address):
        #print("Using Ranodm!")
        if address in self.locations:
            #print(address, self.locations) 
            self.cache_hit_count += 1
            return self.cache[self.locations.index(address)]
        
        self.locations.append(address)
        self.cache.append(self.memory[address])

        if len(self.cache) > self.cache_size: 
            index = random.randint(0, self.cache_size - 1)
            self.cache = self.cache[:index] + self.cache[index + 1:]
            self.locations = self.locations[:index] + self.locations[index + 1:]
        self.memory_hit_count += 1
        ### Is there a way to try multiple try/excpetion statements?
        try:
            return self.memory[address]
        except IndexError as error:
            print("Error: Unknown memory location")
            return None