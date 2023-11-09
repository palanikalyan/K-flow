import networkx as nx
import matplotlib.pyplot as plt

def generate_flowchart(code):
    # Create a directed graph
    G = nx.DiGraph()

    # Split the code into lines
    lines = code.split('\n')

    # Add nodes and edges based on the code
    for i, line in enumerate(lines):
        G.add_node(i, label=line.strip())

        if i > 0:
            G.add_edge(i-1, i)

    # Draw the graph
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'))
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Show the plot
    plt.show()

# Example of a more complex Python code snippet
complex_code = """
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(f"The factorial of 5 is: {result}")
"""

generate_flowchart(complex_code)
