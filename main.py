import sys

VOCAB_SIZE = 128

class TrieNode:
    """
    Class for indicates Trie tree one node

    Attributes
    ---
    item : str
        pronaunciation for registrated word
        except case word terminal, it None

    children : list
        list for destination
    """

    def __init__(self, item = None):
        self.item = item
        self.children = [ -1 for i in range(VOCAB_SIZE)]

    def __str__(self):
        ret = ""
        ret = ret + "item = {}\n".format(self.item)
        ret = ret + "children = \n{}".format(self.children)
        return ret

class Trie:
    """
    Class for Trie tree

    Attributes 
    -----
    nodes : TrieNode
        List of Node

    """
    def __init__(self):
        root = TrieNode()
        self.nodes = [root]

    
    def __add_node(self, node):
        """
        add node to nodes variable
        return index to added node

        Parameters
        -----
        node : Trienode
            Node will be added
        
        Returns
        -----
        index: int
            index number of added node

        """
        self.nodes.append(node)
        return len(self.nodes) - 1


    def __get_char_num(self,c):
        """
        return id of char 
        for example, a = 1, b = 2 ..., z = 26 (order of alphabet)


        Parameters
        -----
        c : char 
            char that wanna get id
        
        Returns
        -----
        id : int
            id of char
            
        """
        return ord(c) - ord('a')
    
    def insert(self, word, item, char_index=0, node_index=0):
        """
        Register a new word to Trie

        Parameteres
        -----
        word : str
            word to register
        
        item :str
            pronaunciation for the word
        
        char_index : int
            pos for current char
        
        node_index : int
            current node position
        """

        char_num = self.__get_char_num(word[char_index])
        next_node_index = self.nodes[node_index].children[char_num]
        if next_node_index == -1:
            # case there is nothing moving to curent node on word[char_index]
            new_node = TrieNode()
            next_node_index = self.__add_node(new_node)
            self.nodes[node_index].children[char_num] = next_node_index
        
        if char_index == len(word) - 1:
            # case last char
            self.nodes[next_node_index].item = item
        else:
            self.insert(word, item, char_index+1,next_node_index)

    def query(self, word):
        """
        Search created Trie

        Parameters
        -----
        word : str
            a word wanna search

        Returns
        item : str or Node
            result of search
            case not found, it is None
        """

        node_index = 0

        for c in word:
            char_num = self.__get_char_num(c)
            tmp_node = self.nodes[node_index]


            node_index = tmp_node.children[char_num]
            if node_index == -1:
                return None
        
        return self.nodes[node_index].item
        



trie = Trie()
trie.insert("b","ビー")
trie.insert("bc","ビーシー")
trie.insert("bcd","ビーシーディー")
trie.insert("c","シー")
trie.insert("cd","シーディー")
trie.insert("cde","シーディーいー")

print(trie.query("c"))
print(trie.query("cde"))
print(trie.query("cdef"))
