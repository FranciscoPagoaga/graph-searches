from Undirected_Graph import Vertex, Graph
import json

def getJson():
    with open("SimplifiedMap.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    return jsonObject

def createGraph(graph):
    jsonObject = getJson()

    for name in jsonObject['cities']:
        v= Vertex(name.get('name'))
        graph.addVertex(v)

    for edge in jsonObject['connections']:
        firstCity = edge.get('cityA')
        secondCity = edge.get('cityB')
        weight = edge.get('weight')
        graph.addEdge(firstCity, secondCity, weight)

if __name__ == '__main__':
    graph = Graph()
    createGraph(graph)
    graph.printGraph()