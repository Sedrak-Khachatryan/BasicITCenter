a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
gumar=0
artadryal=1
for i in a:
    if i/2==i/2-i%2:
        gumar=gumar+i
        artadryal=artadryal*i
print ("gumar="+str(gumar))
print ("artadryal="+str(artadryal))