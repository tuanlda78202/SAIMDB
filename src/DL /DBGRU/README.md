# DBLSTM - Deep Bi-directional LSTM 
| ![Architecture](http://www.gabormelli.com/RKB/images/a/ad/1801.02143_Fig5.png) | 
|:--:| 
| Deep Bidirectional Long Short Term Memmory|

Bidirectional RNNs is based on the idea that the output at each time may not only depend on the previous elements in the sequence, but also depend on the next elements in the sequence. For instance, to predict a missing word in a sequence, we may need to look at both the left and the right context. 

A Bidirectional LSTM, or biLSTM, is a sequence processing model that consists of two LSTMs: one taking the input in a forward direction, and the other in a backwards direction, which are stacked on the top of each other. The one that processes the input in its original order and the one that processes the reversed input sequence. The output is then computed based on the hidden state of both LSTMs. biLSTMs effectively increase the amount of information available to the network, improving the context available to the algorithm (e.g. knowing what words immediately follow and precede a word in a sentence).

Deep bidirectional LSTM is similar to bidirectional LSTM. The only difference is that it has multiple layers per time step, which provides higher learning capacity but needs a lot of training data.
