class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child (self, data):
        #If the value already exist
        if data == self.data:
            return 

        #If data is less than the value of current node --Add to left subtree
        if data < self.data:
            if self.left:
                self.left.add_child(data) 
            else:
                self.left = BinarySearchTreeNode(data)

        #If data is greater than the value of current node --Add to right subtree
        else:
            if self.right:
                self.right.add_child(data) 
            else:
                self.right = BinarySearchTreeNode(data)
                
    def search (self, val):
        if self.data == val:
            return True

        if val < self.data:
            #value should be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False #means the value does not exist in the elements

        if val > self.data:
            #value should be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False #means the value does not exist in the elements
        
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def delete (self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
                
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree (numbers)
    numbers_tree.delete(20)
    print("After deleting 20", numbers_tree.in_order_traversal())