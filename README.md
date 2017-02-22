# sprintdeeplearning

collected codes from 

https://github.com/IanLewis/tensorflow-examples

https://github.com/leriomaggio/deep-learning-keras-tensorflow

https://github.com/rouseguy/scipyUS2016_dl-image

http://speech.ee.ntu.edu.tw/~tlkagk/courses_MLSD15_2.html

https://github.com/mikekestemont/ghentDL

http://brohrer.github.io/how_convolutional_neural_networks_work.html

https://ronxin.github.io/wevi/


# Homework Protein-DNA binding prediction (CTCF)

* CHIP-seq data
https://www.encodeproject.org/experiments/ENCSR000AQU/

* Reference: http://www.nature.com/nbt/journal/v33/n8/full/nbt.3300.html
* Supplementary Notes: http://www.nature.com/nbt/journal/v33/n8/extref/nbt.3300-S2.pdf

train.data: Train sample size 77531

|        | name | sequence | label |
|--------|----------|-----------|-----------|
| train.data  |     name    |     101 length     |     0 negative, 1 positive     |


test.data: Test sample szie 19383 (positive 9709 , negative 9674)

encodingSeq.py - sequence encoding
```
# change the first line #!/home/fish/anaconda3/bin/python to your python directory
# encodingSeq.py train.data flanking_length
# for example
encodingSeq.py train.data 10
```

繳交作業
* Programs (.txt, .py)
* Training data and validation data accuracy. (Trend Chart)
* Prediction for 19383 test.data. (19383 row, 0 negative, 1 positive)
* Description(1~2 pages) for what paramters do you try in this homework.

繳交日期
* 2/22 中午前.

繳交方式
* 寄給ifishlin324@gmail.com

分組
* 2/15上課分組.

|  組別      | 成員 | accuracy |
|--------|----------|----------|
| 1 | winiel559 |----------|
| 2 | chou.yuta |----------|
| 3 | wtwang, jason |----------|
| 4 | rouanshen, ilunteng |----------|
| 5 | bomson, andrewkuo | 0.8845|
| 6 | yichun1492 |0.5299|
| 7 | alicetuan |0.5050|
| 8 | jill |0.6538|
| 9 | fish |0.8260| 

 

|  Fish's 參數  | value |
|--------|----------|
| convolution | 2  (32 filter, size 11 * 4) |
| NN |32 hidden |
| GE | SGE, batch_size 1000, 30000 run|
| Learning rate | 0.05 |
| relu | unused |
| pooling | unused |
| k-fold | unused |
| strides | 2 |
| padding | VALID (no padding)|

可以調的參數
* CNN(width, depth, filter size, filter number, max_pool/avg_pool ,full-connected network (hidden number), learning rate, stochastic GD, dropout ... etc

參考範本
* https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/4_convolutions.ipynb
