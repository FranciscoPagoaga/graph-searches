from Undirected_Graph import Vertex, Graph
import json

def getJson(nameArch):
    with open(str(nameArch)) as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    return jsonObject

def createGraph(graph, nameArch):
    jsonObject = getJson(nameArch)

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
    nameArch = input("Ingrese el nombre del archivo: ")
    createGraph(graph, nameArch)
    graph.printGraph()
    iniSucursal = input("Ingrese la sucursal inicial: ")
    listaEntregas = input("Ingrese la nombres de las ubicaciones de entrega: ")
    CostoMax = input("Ingrese el costo maximo que puede tener: ")