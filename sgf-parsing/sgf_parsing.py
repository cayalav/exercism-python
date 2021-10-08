import re, string

class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def group_paren(string):
    trans = {'(':1,')':-1}
    index, cnt = 0, 0
    while(True):
        cnt += trans.get(string[index], 0)
        index+=1
        if cnt == 0:
            return string[:index], string[index:]



def sanitize(string):
    groups = []
    while(len(string) != 0):
        if(string[0] == ';'): 
            if(string.count(';') == 1):
                groups.append(string)
                return groups
            end = re.search(r'^;.*?[;(]', string).end() - 1 
            groups.append(string[:end])
            string = string[end:] 
        else:
            child, string = group_paren(string)
            groups.append(child)
    return groups

def create_node(string):

    split_properties = re.findall(r'([A-Z]+\[.*?(?<!\\)\](?!\[))', string, re.S)
    if not split_properties: 
        raise ValueError("Nonconforming input.")
    property_dict = {}
    for prop in split_properties:
        p = re.findall(r'^([A-Z]+)\[', prop)[0] 
        a = [s.replace(r'\]', ']') for s in re.findall(r'\[(.*?)(?<!\\)\]', prop, re.S)] 
        property_dict[p] = a
    return SgfTree(property_dict) 


def parse(input_string):
    #return value error in obvious cases
    if len(input_string) < 3 or not re.findall(r'^\(;.*\)$', input_string, re.S):
        raise ValueError("Nonconforming input.")
    if input_string == '(;)': 
        return SgfTree()
    
    node_list = sanitize(input_string[1:-1].expandtabs(1))
    parent_node = create_node(node_list[0])
    for node in node_list[1:]:
        if node[0] == ';':
            parent_node.children.append(create_node(node))
        else:
            parent_node.children.append(parse(node)) 
    return parent_node
