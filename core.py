# from PIL import Image as Im #Работа с графическими изображениями
import tkinter #Работа с GUI
import numpy as np #Работа с массивами
import matplotlib
import matplotlib.pyplot as plt #Вывод на экран
import clock as cl
import random


root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
#pic_size = min(int(width/2), int(height/2))
pic_size = 512

def show_image(image):
    # plt.imshow(image, cmap="gray")
    plt.imshow(image, cmap="gray", interpolation="none")
    plt.show()

def build_catmul_rom(vertexes, steps):
    pass

def build_kasteljo(mass_of_points, steps): #алгоритм кастольжо
    vertexes_result = []
    for four_points in mass_of_points:
        vertexes_result.append(middle_point_help(four_points,steps))
    img = prepare_image()
    #print(np.around(vertexes_result))
    img = vertexes_renderer(img, np.around(vertexes_result), [255,255,255])
    #show_image(img)

def get_digital(n):

    pass

def middle_point_help(vertex,steps):
    vertexes_result = []
    for dif in range(0,steps):
        #print("new step")
        m0 = middle_point(vertex[0], vertex[1], dif, steps)
        #print("m0 = ",m0)
        m1 = middle_point(vertex[1], vertex[2], dif, steps)
        #print("m1 = ", m1)
        m2 = middle_point(vertex[2], vertex[3], dif, steps)
        #print("m2 = ", m2)
        q0 = middle_point(m0, m1, dif, steps)
        q1 = middle_point(m1, m2, dif, steps)
        vertexes_result.append(middle_point(q0, q1, dif, steps))
    return vertexes_result

def middle_point(a, a1, b, steps): #нахождение определенной точки прямой
    res = [0,0]
    res[0] = a[0] + (a1[0] - a[0]) / steps * b
    res[1] = a[1] + (a1[1] - a[1]) / steps * b
    return res

def build_ermit_spline(image, vertexes, derivatives, steps):
    pass

def prepare_image():
    img = np.zeros(shape=(pic_size+1,pic_size+1, 3)).astype(np.uint8)
    return img

def vertexes_renderer(img, vertexes, color):
    for vertex in vertexes:
        for vert in vertex:
            img[int(vert[0]),int(vert[1])] = color
    return img

def draw_line_bad_float(img, x0, y0, x1, y1, color):
    steep = False
    #если ширина меньше высоты
    if (abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True
    #если первая координата больше второй
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    for x in range(x0, x1+1):
        if x1==x0:
            t = 0
        else:
            t = (x-x0) / (x1-x0)
        y = int(round(y0 * (1.-t) + y1 * t))
        #поменяли коорды, при отрисовке меняем обратно
        if (steep):
            img[x, y]=color
        else:
            img[y, x] = color

if __name__=="__main__":
    print(middle_point([10,10],[50,50],5,10))
