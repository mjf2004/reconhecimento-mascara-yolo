import os

#o que o codigo abaixo faz: adiciona o nome  e caminho num arquivo txt chamado test.txt
imagens = []
os.chdir(os.path.join("data","test"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        imagens.append("data/test/" + filename)
os.chdir("..")

with open("test.txt","w") as outfile:
    for img in imagens:
        outfile.write(img)
        outfile.write("\n")
    outfile.close()
os.chdir("..")