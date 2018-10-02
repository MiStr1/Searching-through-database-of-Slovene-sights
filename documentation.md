# Documentation

1. Objects

	* Tree
		Values:
		
			* kids is a list of Trees.
			* name is a string.
		
		Functions
		
			* insert(self, data, depth)
				Data is a list of path of tags and depth is 
				current depth of recursion. Inserts a path of
				tags into a tree with recursion.
			
			* prntTree(self, depth = 0)
				Used to print out the whole tag tree recursively in the order
				of printing the name and cheking all the kids afterwards.
				Depth of each element is shown by the amount of space before the tag.
				
			* buildTagConstraint(self):
				Builds a string wich is later used as a tag constraint in the query.
				User gets an option to choose a tag at each level of recursion wich 
				adds the tag to the string. It returns an empty string if it gets an empty 
				input or if it reaches the bottom of the tree.

2. Functions

	* query(nameConstraint, TagConstraint, regionConstraint)
		Searches the table attraction with three constraints and then prints out name, tags and regionName for each hit.

3. Data preprocessing
	
	* Tag tree preprocessing
		Iterates through all tags of table attraction sorted alphabetically by tags. Decomposes a tag into a path of tags and runs
		insert function to put the path into the tag tree.
	
	* Regions list
		Iterates through all the names of table region and stores them into list.

4. User interaction

	Consists of prints, inputs and loops wich ensure that the input numbers are ok.
	
		
		
		
		
		
		
		
		
		
		
		
		
		
