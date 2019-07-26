# Understanding Convolutional Neural Networks for Text Classification - PyTorch Implementation

Alon Jacovi, Oren Sar Shalom, Yoav Goldberg

Link: https://aclweb.org/anthology/papers/W/W18/W18-5408/

Contact: Alon Jacovi (alonjacovi@gmail.com)

### Getting started

This code requires PyTorch and Scikit-learn. A Markdown viewer is also recommended.

1. Clone the repository
2. Run `train_model.py -c config.json`
3. Run `interpret_model.py -c interpretation_config.json`

Step (2) trains a CNN model on the MR dataset (already in the repo) according to the parameters in the `config.json` file. Step (3) interprets the model according to parameters in the `interpretation_config.json` file.

### General usage

#### `config.json` 
Contains the paths to the data files and other training parameters. Use as a template for your own configuration.

`rare_word_threshold` - any token that occurs less than this number will be converted to UNK when creating the token indexer, ONLY if a token indexer is not already provided.

#### `train_model.py -c <path_to_config>`
Loads the given data (via `data.py`) and trains a model (via `model.py`), then saves the model, a copy of the config, a copy of the token indexer, and the training metrics (loss+accuracy over every epoch). The best performing model on the validation set throughout training is saved.

#### `interpretation_config.json` 
Contains the paths to the trained model and data to do prediction interpretation as well as other interpretation parameters. Any parameters in this config that also exist in the training config will override the training config's parameters during interpretation. Use as a template for your own configuration.

`minimum_purity` refers to the lowest purity level we require of each threshold.

`top_k_in_logs` refers to the top-k level of biggest/smallest ngrams to be printed to the Markdown files.

#### `interpret_model.py -c <path_to_config>`
Interpret a model according to the paper in multiple stages:

1. Get all of the inference data for interpretation:
    a. The filter activations for every ngram in the input
    b. The chosen ngrams during max-pooling
    b. The max-pooled activations for the chosen ngrams
    c. The final prediction
2. Token-level interpretation: the biggest and smallest tokens (words) per slot of every filter. The information is saved to a Markdown file in top-k format (see the "interpretation output" section of this README).
3. Ngram-level interpretation: the biggest and smallest ngrams per filter, as well as threshold calculation according to the paper's "purity" heuristic. The information is saved as a Markdown file and is also present as an organized python dict in the code.
4. Clustering of the slot activation vectors. The information is saved as a Markdown file and clustering scatter plots.
5. Prediction interpretation of a separate data file (specified in the interpretation config). This is saved both as a json dict and as a Markdown file.

This file is quite complicated and hard to read. I've done my best to add documentation via comments, but please contact me for any questions.

#### Output
For a pre-specified output path in the training config, after both training and interpretation, it will contain:

1. `config.json` - a copy of the config file (the training config overriden with the interpretation config)
2. `metrics.json` - the training metrics, which include the loss and accuracy per epoch as well as the best accuracy on the validation set.
3. `model` - the PyTorch model (can be replaced with any model of your choosing, as long as it conforms to the interface of the model in `model.py`)
4. `w2i.json` - the token indexer
5. `model_interpretation/w@.f@` - a folder for each filter

    a. `w@` indicates the window/ngram size of the filter (ex. w3 = 3 tokens)
    
    b. `f@` indicates the index of the filter in the CNN weight matrix
    
    c. `filter_info.md` - Token-level interpretation of the filter
    
    d. `filter_info_2.md` - Ngram-level interpretation of the filter
    
    d. `cluster_info.md` - a Markdown description of the filter's semantic clusters (hopefully - but beware, clustering is not an exact science)
    
    e. `clusters.pdf` - a visualization of the clustering, only for `w2` and `w3` where such a thing is possible (2D and 3D plots).

#### Limitations

1. This code doesn't (yet) support pre-trained embeddings, but it's easy to add! If you wish to use them, you need to do two things:

    a. Prepare a mapping dictionary from token strings to embedding indices, and pass it to the `load_data()` function in `train_model.py`.

    b. Prepare an embeddings matrix and just plug it into the model using the `set_pretrained_embeddings()` function of the model class, also in `train_model.py`.
    
2. The model interpretation currently just saves Markdown files that have the top-k scoring tokens/ngrams per slot/filter. If you wish to get better access to the interpretation info, you'll have to look into the code of the `model_interpretation_?()` functions and extract whatever info you want.

3. I haven't extensively tested the code for data that has more than two classes (binary classification). If your data has more than 2 classes, it should still work, but let me know if something breaks or seems wrong.

### Paper

Arxiv: https://arxiv.org/abs/1809.08037

Abstract: We present an analysis into the inner workings of Convolutional Neural Networks (CNNs) for processing text. CNNs used for computer vision can be interpreted by projecting filters into image space, but for discrete sequence inputs CNNs remain a mystery. We aim to understand the method by which the networks process and classify text. We examine common hypotheses to this problem: that filters, accompanied by global max-pooling, serve as ngram detectors. We show that filters may capture several different semantic classes of ngrams by using different activation patterns, and that global max-pooling induces behavior which separates important ngrams from the rest. Finally, we show practical use cases derived from our findings in the form of model interpretability (explaining a trained model by deriving a concrete identity for each filter, bridging the gap between visualization tools in vision tasks and NLP) and prediction interpretability (explaining predictions).

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
