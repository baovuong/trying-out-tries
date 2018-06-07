
class StupidTextSearch:

    def __init__(self):
        self.words = []

    def insert(self, text):
        self.words.append(text)
    
    def search(self, query):
        # this would probably be around O(n^2)
        return [w for w in self.words if query in w]  
    
    def __iter__(self):
        return iter(self.words)
    
    def __next__(self):
        return next(self.words)

class TrieNode:
    def __init__(self, value=0):
        self.children = {}
        self.parent = None 
        self.value = value

class TrieTextSearch:
    
    def __init__(self):
        self.root = TrieNode()
    
    def search(self, query):
        resultingnode = self._findnode(query)

        if resultingnode == None:
            return None 
        
        

        return None 
    
    def insert(self, value):
        pass
    
    def __iter__(self):
        # TODO work on this
        return iter([])
    
    def __next__(self):
        # TODO work on this 
        return next([])


    

    def _findnode(self, value):
        characters = [ord(c) for c in value]

        current = self.root 

        for c in characters:
            if c not in current.children:
                return None 
            current = current.children[c]
        return current


if __name__ == '__main__':
    searcher = StupidTextSearch()
    searcher.insert('hello')
    searcher.insert('what')

    for word in searcher:
        print(word)


