# UMLFiT - Universal Language Model Fine-tuning

| ![Architecture](https://production-media.paperswithcode.com/methods/Screen_Shot_2020-05-26_at_5.11.04_PM.png) | 
|:--:| 
| Howard et al. in [Universal Language Model Fine-tuning for Text Classification](https://paperswithcode.com/paper/universal-language-model-fine-tuning-for-text) |

## Architecture 
**Universal Language Model Fine-tuning**, or **ULMFiT**, is an architecture and transfer learning method that can be applied to NLP tasks. It involves a 3-layer [AWD-LSTM](https://paperswithcode.com/method/awd-lstm) architecture for its representations. The training consists of three steps: 
1. General language model pre-training on a Wikipedia-based text
2. Fine-tuning the language model on a target task
3. Fine-tuning the classifier on the target task.

As different layers capture different types of information, they are fine-tuned to different extents using [discriminative fine-tuning](https://paperswithcode.com/method/discriminative-fine-tuning). Training is performed using [Slanted triangular learning rates](https://paperswithcode.com/method/slanted-triangular-learning-rates) (STLR), a learning rate scheduling strategy that first linearly increases the learning rate and then linearly decays it.

Fine-tuning the target classifier is achieved in ULMFiT using gradual unfreezing. Rather than fine-tuning all layers at once, which risks catastrophic forgetting, ULMFiT gradually unfreezes the model starting from the last layer (i.e., closest to the output) as this contains the least general knowledge. First the last layer is unfrozen and all unfrozen layers are fine-tuned for one epoch. Then the next group of frozen layers is unfrozen and fine-tuned and repeat, until all layers are fine-tuned until convergence at the last iteration.

## Pre-trained Weight 
[@tuanlda78202](https://github.com/tuanlda78202) finetuned model AWD-LSTM pre-trained with Wiki-103M mix IMDb. I used Google Colab Pro with GPU P100, training approximate 22 hours and collected accuracy 94.4%

You can load pre-trained model finetuned in [here](https://husteduvn-my.sharepoint.com/:u:/g/personal/tuan_lda204929_sis_hust_edu_vn/EeY-5xv_iT9Jl6DsOwsNsUEB59da4IbHKQb4GrqTlroI7w?e=nFYHLE) for training classifier.
