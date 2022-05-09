from Undirected_Graph import Vertex, Graph

if __name__ == '__main__':
    print("hola")
    g = Graph()
    for a in range(5):
        v = Vertex(str(a))
        g.addVertex(v)

    g.addEdge("1","2", 5)
    g.addEdge("3","4", 10)
    g.printGraph()