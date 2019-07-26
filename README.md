# Understanding Convolutional Neural Networks for Text Classification
## PyTorch implementation

# Paper
Link: https://aclweb.org/anthology/papers/W/W18/W18-5408/

Arxiv: https://arxiv.org/abs/1809.08037

Please cite:
```
@inproceedings{jacovi-etal-2018-understanding,
    title = "Understanding Convolutional Neural Networks for Text Classification",
    author = "Jacovi, Alon  and
      Sar Shalom, Oren  and
      Goldberg, Yoav",
    booktitle = "Proceedings of the 2018 {EMNLP} Workshop {B}lackbox{NLP}: Analyzing and Interpreting Neural Networks for {NLP}",
    month = nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W18-5408",
    doi = "10.18653/v1/W18-5408",
    pages = "56--65",
    abstract = "We present an analysis into the inner workings of Convolutional Neural Networks (CNNs) for processing text. CNNs used for computer vision can be interpreted by projecting filters into image space, but for discrete sequence inputs CNNs remain a mystery. We aim to understand the method by which the networks process and classify text. We examine common hypotheses to this problem: that filters, accompanied by global max-pooling, serve as ngram detectors. We show that filters may capture several different semantic classes of ngrams by using different activation patterns, and that global max-pooling induces behavior which separates important ngrams from the rest. Finally, we show practical use cases derived from our findings in the form of model interpretability (explaining a trained model by deriving a concrete identity for each filter, bridging the gap between visualization tools in vision tasks and NLP) and prediction interpretability (explaining predictions).",
}
```
