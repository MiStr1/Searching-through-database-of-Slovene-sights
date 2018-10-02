import sqlite3

conn = sqlite3.connect('slovenia_db.db')
c = conn.cursor()

#objects
###########################################################################

#name:string
#kids:list of Trees
class Tree(object):
    def __init__(self):
        self.kids = []
        self.name = None
    
    #insert tag path into a tree
    def insert(self, data, depth = 0):
        if (depth == len(data)):
            return
        
        for i in self.kids:
            if i.name == data[depth]:
                i.insert(data, depth+1)
                return

        newNode = Tree()
        newNode.name = data[depth]
        self.kids.append(newNode)
        newNode.insert(data, depth+1)

    def prntTree(self, depth = 0):
        for i in range(depth):
            print(' ', end = '')
        print(self.name)
        for i in self.kids:
            i.prntTree(depth + 1)

    #recuresive building of tag path
    def buildTagConstraint(self):
        if (len(self.kids) == 0):
            return ""
     
        for i in range(len(self.kids)):
            print(str(i+1) + " " + self.kids[i].name)

        while (True):
            inp = input()

            if (inp == ""):
                return ""
            inp = int(inp)
            if (inp < 1 or inp > len(self.kids)):
                print ("wrong input")
                continue
        
            ret = self.kids[inp-1].buildTagConstraint()
            if (ret == ""):
                return self.kids[inp-1].name
            return self.kids[inp-1].name + "," + ret

    
        

#functions
############################################################################

#searches the database based on three constraints and prints name,tags,regionName for all hits
def query(nameConstraint, TagConstraint, regionConstraint):
    if (regionConstraint == ""):
        for row in c.execute("SELECT name,tags,regionName FROM attraction WHERE UPPER(name) LIKE '%" + nameConstraint + "%' AND tags LIKE '" + TagConstraint + "%'"):
            print (row)
        
    else:
        for row in c.execute("SELECT name,tags,regionName FROM attraction WHERE UPPER(name) LIKE '%" + nameConstraint + "%' AND tags LIKE '" + TagConstraint + "%' AND region_id IS "+str(regionConstraint)):
            print (row)




#data preprocessing
############################################################################
        
#root of tag tree
tags = Tree()


#transforming tag into tree structure
for row in c.execute('SELECT tags FROM attraction ORDER by tags'):
    
    row = row[0].split(',')
    tags.insert(row)

#root.prntTree()

regions = []
for row in c.execute('SELECT name FROM region'):
    regions.append(row[0])

#print (regions)


#user interaction
############################################################################

while (True):
    print("name must include:")
    nameConstraint = input()
    
    print("Type in the number before the tag that interests you. If you want all of them just press enter.")
    tagConstraint = tags.buildTagConstraint()

    print("Type in the number before the region that interests you. If you want all of them just press enter.")
    for i in range(len(regions)):
        print(str(i+1) + " " + regions[i])

    #loops until legal number is inputed
    while (True):
        regionConstraint = input()

        if (regionConstraint == ""):
            query(nameConstraint.upper(), tagConstraint, regionConstraint)
            break
        
        regionConstraint = int(regionConstraint)
        if (regionConstraint < 1 or regionConstraint > 12):
            print ("wrong input")
            continue
        
        query(nameConstraint.upper(), tagConstraint, regionConstraint)
        break
    
    print('\nFor another query type in 1 otherwise press enter')
    if (input() != "1"):
        break

