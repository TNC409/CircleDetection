import numpy as np
import cv2
import time
def robot_sag_ilerleme():
    print("")
    # burada arduino ile iletişimi kurmak için kullancağımız kanallar olacak sırayla içine yollarız
def robot_sola_ilerleme():
    print("")

def robot_yukarı_ilerleme():
    print("")
def robot_assagi_ilerleme():
    print("")
kamera = cv2.VideoCapture (0)
while True :
        ret, frame = kamera.read ()

        kopya = frame.copy () #görüntüyü burada kopyaladık üzerine işlem yaptığımızda orjinal görüntüyü korumak için

        gray = cv2.cvtColor (frame, cv2.COLOR_RGB2GRAY) #gri olarak algılayıp daha hızlı erişmek için
        gray = cv2.GaussianBlur (gray, (33,33),1) #gürültüleri silmek için görseli hafif bulanıklaştırır.


        kernel=np.ones((5,5),np.uint8) #önce bir kernel oluşturduk
        gary=cv2.erode(gray,kernel,iterations=1) # sonra kerneldeki gürültüleri sildik
        gray=cv2.dilate(gray,kernel,iterations=1) # burada ise gürültüler ile silinin asıl görüntüyü yeniden büyüttük
        circles = cv2.HoughCircles (gray, cv2.HOUGH_GRADIENT, 1, 200, param1 = 35, param2 = 50, minRadius = 0, maxRadius = 0)
        #ilki gri ton ,diğeri kullanılan method , bunu çözemedim şuanlık ,belirlenen merkezler arası minimum uzaklık ,  param1=kenar dedektörü için üst eşik,param2=merkez için eşik değeri ,son ikisi de  yarıçap için sınırlama


        if circles is not None: #eğer çember varsa bunları yap
            circles = np.round (circles[0,:]).astype("int") # değerleri int'e çevir
            for (x,y,r) in circles:

                cv2.circle(kopya,(x,y),r,(0,255,0),4)
                cv2.rectangle(kopya,(x-5,y-5),(x+5,y+5),(0,128,255),1)

                print("X Kordinati : ", x)
                print("Y Kordinati : ", y)
                print("Yarıçap Değeri : ", r)

                cv2.imshow('Çember Tespiti', kopya)
                if cv2.waitKey(1) & 0xFF == ord('w'):  # çıkmak için q ya bas
                    break


                #time.sleep(3)
                if(x==0 and y==0): #eğer hedef yoksa
                    print("Hedef algılanmadı")
                    # fonksiyon oluşturup içine değeri yollarız

                elif(x>390 and x<360 and y>240 and y<270): # hedef tam ortamızda ise
                    print("Düz gitmemiz gerek")
                    # fonksiyon oluşturup içine değeri yollarız
                   # print("X değerii" ,x ,"Y DEğeriii", y)

                elif(x>390): # yani hedef robotun sağ tarafında kalıyor
                    print("Sağa dön komutu gelir")
                 #   print("X değeriii: ", x )
                    # ama aynı zamanda çember robotun sağ altı ya da  sağ üstünde olabilir onu da kontrol etmemiz lazım
                    if(y<240):
                        print("Robotun havalanması lazım cisim sağ üstte kaldı ")
                       # print("Y DEğeriii: ", y)

                elif(y>270):
                    print("Robotun alçalması lazım cisim sağ  altta kaldı ")
                  #  print("Y değeriii ", y)

                elif(x<360): # cisim robotun solunda kalıyorsa
                    print("Sola dön komutu gelmesi gerekli ")
                    # print("X değerii" ,x ,"Y DEğeriii", y)


                    if(y<240):
                        print("Robotun havalanması lazım cisim  sol üstte kaldı ")
                       # print("Y DEğeriii: ", y)
                    elif(y>270):
                        print("Robotun alçalması lazım cisim sol altta kaldı ")
                     #   print("Y değeriii ", y)


kamera.release ()
cv2.destroyAllWindows ()