import array as arr
import numpy as np 

#a1 = arr.array('i', [1, 0])

a2 = np.array([[1, 0], [0, 1]])
b1 = 1
b2 = 0 
w = [1, 2]

sınır = -1
katsayı =  0.5
cıkıs = 1

#formul1 = float(w[0]) * float(a2[0]) 
#formul2 = float(w[1]) * float(a2[1]) 


def fonksiyon():
    while True:



        formul1 = int(w[0]) * int(a2[1,0]) + int(w[1]) * int(a2[1,1])
 
        i = 0

        if formul1 > sınır:
            
            if formul1  == b1:
                print("f1 = b1")
                
                print (w[0], end =" ")
                print (w[1], end =" ")

                break

            else:

                w[0] = w[0] - katsayı * int(a2[1,0])
                w[1] = w[1] - katsayı * int(a2[1,1])
                print(1)
                i += i 
                print("iterasyon {i}")

                if  formul1  == b2:
                    print("f1 = b2")
                    
                    print (w[0], end =" ")
                    print (w[1], end =" ")
                    break

                else: 
                    print("f1 eşit değil")
                    
                    w[0] = w[0] - katsayı * int(a2[1,0])
                    w[1] = w[1] - katsayı * int(a2[1,1])
                    i += i 
                    print("iterasyon {i}")

                    print("w11")
                    print (w[0], end =" ")
                    print("\nw12")
                    print (w[1], end =" ")


                    print("\ntoplam")
                    print(formul1)

                    print("net")
                    print(formul1)

                    if formul1 > 200:
                        print("değer çok büyük")
                        break

                    if formul1 < -200:
                        print("değer çok düşük")
                        break

        else:
            print("Formul net sınırdan küçük.")


    
# w0 hatalı çıkıyor 3. iterasyonda kapatıyor

fonksiyon()
