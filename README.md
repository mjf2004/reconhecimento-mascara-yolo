# reconhecimento-mascara-yolo
Projeto de dissertação iniciado 2020. 
Neste projeto foi usado os três modelos pré-treinados: YOLOv2, YOLOv3 e o até então estado da arte YOLOv4. O novo estado da arte YOLOv7 foi lançado somente em julho /2022, reconhecido pelo autor original da arquitetura YOLO.
 
E foi usado seis modelos pré-treinados da Tensorflow API Object Detection: três Faster R-CNN e três SSD.
Os resultados mostraram o SSD Mobilenet V2 FPNLite como um detector de máscara competitivo com o YOLOv4 e nas condições do projeto foi o escolhido como o detector mais eficiente.

A visualização dos resultados com API Object Detection podem ser visto no repositório https://github.com/mjf2004/reconhecimento-mascara-tensorflow

# Resultados YOLO

As inferências foram realizadas em cinco imagens. Três fora do dataset de teste e duas do dataset de test. Cada imagem teve um critério analisado. Em cada modelo foi retirado os VP (verdadeiro positivo), FP (falso positivo) e FN (falso negativo). As imagens de exemplo pode ser visto abaixo e em seguida os resultados.

![image](https://user-images.githubusercontent.com/71648038/210083312-4e477059-017b-4054-bf55-de47049830f6.png)

resultados base 70-30

![image](https://user-images.githubusercontent.com/71648038/210083354-ffd89583-5dcf-4068-89ff-27aced17d83e.png)

resultados base 80-20

![image](https://user-images.githubusercontent.com/71648038/210083380-200472cf-4fe1-43f6-b759-0c28a001d9e5.png)

resultados base 90-10

![image](https://user-images.githubusercontent.com/71648038/210083455-c5d60335-c837-4fed-8be3-a55e61359219.png)

Exemplo de inferência com o YOLOv4. Caixa de cor roxo "com_mascara" e verde "sem_mascara".
![image](https://user-images.githubusercontent.com/71648038/210083667-99c818d2-c552-41bd-90fd-ea2acbb43b5a.png)

# Tempo de treinamento de cada modelo.
![image](https://user-images.githubusercontent.com/71648038/210083723-57319f02-4fd9-4264-ad99-7387bb0917cd.png)

# Outros resultados. FPS e tamanho do arquivo da rede neural com os pesos.
![image](https://user-images.githubusercontent.com/71648038/210083804-2e273728-10f2-4595-919d-2fcb42c29c33.png)
