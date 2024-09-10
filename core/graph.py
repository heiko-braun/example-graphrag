import networkx as nx
import re

def build_graph_from_summaries(summaries):
    G = nx.Graph()
    for index, summary in enumerate(summaries):
        print(f"Summary index {index} of {len(summaries)}:")
        
        # extract tuples
        pattern = r'\((.*?)\)'        
        lines = re.findall(pattern, summary)                
        
        entities_section = False
        relationships_section = False
        
        entities = []
        for line in lines:
            tuples = [item.strip().strip('"') for item in line.split(', ')]
            #print(tuples)
            if tuples[0] == ("entity"):
                entities_section = True
                relationships_section = False                
            elif tuples[0] == ("relationship"):
                entities_section = False
                relationships_section = True                
                
            if entities_section:
                #print("process entity line:", line)                
                entity = tuples[1]                
                entities.append(entity)
                G.add_node(entity)
                #print("Added entity", entity)
            elif relationships_section:
                #print("process relationship line:", line)                
                
                source = tuples[1]
                target = tuples[2]
                relation = tuples[3]
                #print("Added edge", source, target)
                G.add_edge(source, target, label=relation)
    return G