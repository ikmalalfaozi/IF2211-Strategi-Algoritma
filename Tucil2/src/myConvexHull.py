from asyncio.windows_events import NULL
import numpy as np

def convexHull(arrayOfPoint):
    # Mengurutkan point berdasarkan absis kemudian ordinat secara menaik
    arrayOfPoint = np.array(sorted(arrayOfPoint, key=lambda k: [k[0], k[1]]))

    # Mengambil P1 dan Pn
    p1 = arrayOfPoint[0]
    pn = arrayOfPoint[-1]

    # Divide: Membagi titik ke sebelah kiri (s1) dan kanan (s2) berdasarkan garis P1-Pn
    arrayOfPointLeft = np.array(left(arrayOfPoint,p1, pn))
    arrayOfPointRight = np.array(left(arrayOfPoint, pn, p1))
    
    # Divide and Conquer: Memproses titik-titik di s1 dan di s2
    leftVertices = np.array(process(arrayOfPointLeft,p1,pn))
    rightVertices = np.array(process(arrayOfPointRight,pn,p1))

    # Merge
    vertices = np.array([p1])
    if (len(leftVertices) != 0):
        vertices = np.concatenate((vertices, leftVertices), axis=0)
    vertices = np.append(vertices, [pn], axis=0)
    if (len(rightVertices) != 0):
        vertices = np.concatenate((vertices, rightVertices), axis=0)
    vertices = np.append(vertices, [p1], axis=0)

    return np.array(vertices)

def left(array,p1,p2):
    arrayOfPointLeft = []
    for i in range(len(array)):
        # x1y2 + x3y1 + x2y3 - x3y2- x2y1 - x1y3 = (y3-y1)(x2-x1) – (y2-y1)(x3-x1)
        if ((array[i][1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (array[i][0] - p1[0])) > 0:
            arrayOfPointLeft.append(array[i])
    return arrayOfPointLeft

def getFarthestPoint(array,p1,pn):
    # Mengambil titik dengan jarak terjauh
    if len(array) == 0:
        return NULL
    else:
        m = (pn[1]-p1[1])/(pn[0]-p1[0])
        # y - y1 = m(x-x1) <--> y - p1[1] = m*(x-p1[0]) <--> y - p1[1] = m*x - m*p1[0] <--> m*x - y + (p1[1] - m*p1[0]) = 0  
        # ax + by + c = 0
        arraydistance = []
        for p in array:
            arraydistance.append(abs(m*p[0] - p[1] + p1[1] - m*p1[0]))
        maxDistance = max(arraydistance)
        arrayIdxMaxDistance = [x for x, y in enumerate(arraydistance) if y == maxDistance]
        return array[arrayIdxMaxDistance[0]]

def process(array,p1,pn):
    vertices = []
    farthestPoint = getFarthestPoint(array,p1,pn)
    if (farthestPoint is not NULL):
        # print(farthestPoint)
        vertices.append(farthestPoint)
        array1 = np.array(left(array,p1,farthestPoint))
        array2 = np.array(left(array,farthestPoint,pn))
        # print(array1,array2)
        vertices1 = process(array1,p1,farthestPoint)
        vertices2 = process(array2,farthestPoint,pn)
        vertices = vertices1 + vertices + vertices2
    return vertices