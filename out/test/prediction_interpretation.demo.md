# Prediction info
## Note: Please view with a color markdown viewer! The "@" signs are supposed to be colored according to the filter's identity class.

## Original input: 
``` a reality - @@UNK@@ @@UNK@@ . ``` 

## Marked input: 
<pre>a <span style="background-color: #6698FF">@</span>reality <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | filter class | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :-- | :--
w2.f0 | pos |   | `@@UNK@@ @@UNK@@` | 0.81 | ['1.98', '-0.79']
w2.f1 | pos |   | `a reality` | 0.91 | ['2.95', '-1.91']
w2.f2 | pos |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | neg |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f4 | pos |   | `a reality` | 1.81 | ['2.27', '-0.27']
w2.f5 | pos |   | `. @@PAD@@` | 0.37 | ['0.67', '0.00']
w2.f6 | pos |   | `a reality` | 1.10 | ['0.54', '0.66']
w2.f7 | neg |   | `reality -` | 0.47 | ['2.26', '-0.88']
w2.f8 | pos |   | `@@PAD@@ a` | 2.34 | ['0.00', '2.56']
w2.f9 | neg |   | `reality -` | 2.89 | ['2.44', '0.46']
w2.f10 | pos |   | `@@PAD@@ a` | 0.06 | ['0.00', '0.20']
w2.f11 | neg |   | `reality -` | 1.40 | ['2.70', '-1.02']
w2.f12 | neg |   | `reality -` | 1.05 | ['1.69', '-0.61']
w2.f13 | neg | x | `reality -` | 3.47 | ['2.43', '1.20']
w2.f14 | neg |   | `@@UNK@@ .` | 1.04 | ['0.69', '0.39']
w2.f15 | pos |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f16 | neg |   | `a reality` | 2.58 | ['-0.39', '3.73']
w2.f17 | neg |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f18 | pos |   | `a reality` | 0.94 | ['0.76', '0.30']
w2.f19 | pos |   | `a reality` | 2.94 | ['0.99', '2.25']
w3.f0 | neg | x | `@@PAD@@ a reality` | 4.60 | ['0.00', '3.29', '1.70']
w3.f1 | pos |   | `a reality -` | 0.06 | ['-1.76', '0.55', '1.66']
w3.f2 | neg |   | `a reality -` | 2.50 | ['1.87', '0.18', '0.54']
w3.f3 | pos |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.45']
w3.f4 | pos |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.65']
w3.f5 | pos |   | `@@PAD@@ @@PAD@@ a` | 0.74 | ['0.00', '0.00', '1.07']
w3.f6 | neg |   | `a reality -` | 3.16 | ['1.76', '2.16', '-0.54']
w3.f7 | pos |   | `reality - @@UNK@@` | 0.77 | ['2.40', '-1.06', '-0.07']
w3.f8 | pos |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.46']
w3.f9 | neg | x | `reality - @@UNK@@` | 3.84 | ['2.29', '-0.49', '2.13']
w3.f10 | neg |   | `@@UNK@@ . @@PAD@@` | 2.18 | ['0.33', '2.00', '0.00']
w3.f11 | neg |   | `@@PAD@@ @@PAD@@ a` | 2.59 | ['0.00', '0.00', '2.78']
w3.f12 | neg |   | `reality - @@UNK@@` | 3.81 | ['2.53', '2.81', '-1.41']
w3.f13 | pos |   | `@@UNK@@ @@UNK@@ .` | 0.42 | ['-0.04', '-1.74', '2.45']
w3.f14 | neg |   | `reality - @@UNK@@` | 0.18 | ['1.12', '0.52', '-1.37']
w3.f15 | neg |   | `@@PAD@@ a reality` | 1.29 | ['0.00', '-0.09', '1.55']
w3.f16 | pos |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-2.12']
w3.f17 | neg |   | `@@PAD@@ a reality` | 0.27 | ['0.00', '-1.45', '1.87']
w3.f18 | pos |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.37']
w3.f19 | pos |   | `a reality -` | 2.03 | ['3.70', '-0.05', '-1.51']

## Original input: 
``` it 's a glorious spectacle like those d . w . @@UNK@@ made in the early days of silent film . ``` 

## Marked input: 
<pre>it 's <span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>glorious <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>spectacle <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>like <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>those <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>d <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>w . <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>made <span style="background-color: #6698FF">@</span>in the early <span style="background-color: #FFFF00">@</span>days <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>silent <span style="background-color: #6698FF">@</span>film <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | filter class | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :-- | :--
w2.f0 | pos | x | `those d` | 6.44 | ['0.77', '6.05']
w2.f1 | pos | x | `a glorious` | 7.57 | ['2.95', '4.76']
w2.f2 | pos |   | `silent film` | 0.88 | ['1.10', '0.83']
w2.f3 | neg |   | `those d` | 1.98 | ['1.40', '1.13']
w2.f4 | pos |   | `a glorious` | 2.43 | ['2.27', '0.35']
w2.f5 | pos | x | `a glorious` | 4.87 | ['0.71', '4.47']
w2.f6 | pos |   | `in the` | 1.91 | ['1.77', '0.24']
w2.f7 | neg |   | `those d` | 1.28 | ['-0.49', '2.67']
w2.f8 | pos | x | `those d` | 5.53 | ['4.07', '1.68']
w2.f9 | neg |   | `made in` | 4.40 | ['2.52', '1.89']
w2.f10 | pos | x | `glorious spectacle` | 4.80 | ['3.18', '1.76']
w2.f11 | neg | x | `days of` | 3.36 | ['2.68', '0.95']
w2.f12 | neg |   | `silent film` | 1.65 | ['2.19', '-0.50']
w2.f13 | neg | x | `spectacle like` | 4.30 | ['1.42', '3.03']
w2.f14 | neg |   | `like those` | 2.57 | ['0.54', '2.06']
w2.f15 | pos | x | `early days` | 3.53 | ['2.34', '1.46']
w2.f16 | neg |   | `days of` | 2.54 | ['3.63', '-0.34']
w2.f17 | neg | x | `w .` | 3.81 | ['3.96', '0.47']
w2.f18 | pos |   | `silent film` | 2.33 | ['1.51', '0.95']
w2.f19 | pos |   | `silent film` | 2.39 | ['3.23', '-0.54']
w3.f0 | neg | x | `'s a glorious` | 4.44 | ['-1.14', '3.29', '2.68']
w3.f1 | pos |   | `early days of` | 1.52 | ['-1.21', '3.25', '-0.14']
w3.f2 | neg |   | `d . w` | 3.33 | ['3.29', '-1.42', '1.55']
w3.f3 | pos |   | `glorious spectacle like` | 1.32 | ['1.53', '-0.28', '0.68']
w3.f4 | pos | x | `glorious spectacle like` | 4.51 | ['2.49', '-0.85', '3.23']
w3.f5 | pos |   | `. w .` | 4.16 | ['-0.37', '0.54', '4.32']
w3.f6 | neg |   | `d . w` | 2.30 | ['3.69', '1.07', '-2.25']
w3.f7 | pos |   | `'s a glorious` | 4.11 | ['-0.31', '0.48', '4.43']
w3.f8 | pos |   | `a glorious spectacle` | 2.78 | ['0.66', '0.99', '1.42']
w3.f9 | neg | x | `w . @@UNK@@` | 7.34 | ['4.74', '0.58', '2.13']
w3.f10 | neg | x | `of silent film` | 4.83 | ['2.92', '-0.31', '2.36']
w3.f11 | neg | x | `it 's a` | 4.07 | ['1.01', '0.46', '2.78']
w3.f12 | neg |   | `the early days` | 3.16 | ['2.43', '0.82', '0.05']
w3.f13 | pos | x | `the early days` | 8.53 | ['4.70', '-0.15', '4.23']
w3.f14 | neg | x | `glorious spectacle like` | 4.42 | ['-1.17', '0.03', '5.65']
w3.f15 | neg | x | `early days of` | 5.25 | ['0.95', '2.46', '2.01']
w3.f16 | pos | x | `'s a glorious` | 7.35 | ['2.11', '0.35', '5.26']
w3.f17 | neg |   | `the early days` | 3.77 | ['-1.17', '2.86', '2.24']
w3.f18 | pos |   | `days of silent` | 2.48 | ['0.56', '2.10', '0.29']
w3.f19 | pos | x | `a glorious spectacle` | 5.16 | ['3.70', '1.96', '-0.38']

## Original input: 
``` it 's surprisingly decent , particularly for a @@UNK@@ installment in a series . ``` 

## Marked input: 
<pre>it 's <span style="background-color: #FFFF00">@</span>surprisingly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>decent <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>particularly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>for <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>installment <span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>series <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | filter class | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :-- | :--
w2.f0 | pos |   | `@@UNK@@ installment` | 2.15 | ['1.98', '0.54']
w2.f1 | pos |   | `it 's` | 1.94 | ['0.50', '1.57']
w2.f2 | pos |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | neg |   | `particularly for` | 0.01 | ['1.92', '-1.35']
w2.f4 | pos |   | `a series` | 2.60 | ['2.27', '0.52']
w2.f5 | pos |   | `surprisingly decent` | 2.69 | ['4.16', '-1.17']
w2.f6 | pos | x | `decent ,` | 5.02 | ['1.19', '3.93']
w2.f7 | neg |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 | pos |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 | neg |   | `@@UNK@@ installment` | 4.07 | ['2.38', '1.70']
w2.f10 | pos | x | `'s surprisingly` | 3.02 | ['2.75', '0.40']
w2.f11 | neg |   | `installment in` | 1.66 | ['3.40', '-1.47']
w2.f12 | neg | x | `@@UNK@@ installment` | 3.56 | ['-0.28', '3.87']
w2.f13 | neg | x | `particularly for` | 4.15 | ['1.51', '2.78']
w2.f14 | neg |   | `@@UNK@@ installment` | 2.61 | ['0.69', '1.96']
w2.f15 | pos |   | `, particularly` | 3.20 | ['2.19', '1.28']
w2.f16 | neg |   | `series .` | 0.90 | ['3.19', '-1.53']
w2.f17 | neg |   | `surprisingly decent` | 1.26 | ['1.66', '0.21']
w2.f18 | pos | x | `surprisingly decent` | 3.32 | ['2.98', '0.47']
w2.f19 | pos |   | `particularly for` | 1.09 | ['0.69', '0.69']
w3.f0 | neg | x | `in a series` | 4.41 | ['-0.14', '3.29', '1.65']
w3.f1 | pos |   | `series . @@PAD@@` | 1.06 | ['1.79', '-0.35', '0.00']
w3.f2 | neg | x | `surprisingly decent ,` | 4.09 | ['4.01', '-1.16', '1.32']
w3.f3 | pos |   | `in a series` | 0.27 | ['1.23', '-1.71', '1.35']
w3.f4 | pos | x | `it 's surprisingly` | 3.60 | ['-0.70', '2.08', '2.58']
w3.f5 | pos | x | `a series .` | 8.17 | ['1.79', '2.39', '4.32']
w3.f6 | neg | x | `'s surprisingly decent` | 4.25 | ['3.62', '2.60', '-1.76']
w3.f7 | pos |   | `a series .` | 2.68 | ['-0.02', '3.02', '0.18']
w3.f8 | pos | x | `it 's surprisingly` | 5.76 | ['2.11', '0.26', '3.68']
w3.f9 | neg | x | `in a series` | 3.90 | ['1.57', '-0.16', '2.60']
w3.f10 | neg |   | `decent , particularly` | 2.12 | ['-0.77', '-0.41', '3.44']
w3.f11 | neg | x | `particularly for a` | 4.81 | ['5.72', '-3.50', '2.78']
w3.f12 | neg |   | `'s surprisingly decent` | 3.20 | ['-0.70', '0.68', '3.35']
w3.f13 | pos |   | `decent , particularly` | 4.58 | ['-0.04', '1.92', '2.95']
w3.f14 | neg |   | `it 's surprisingly` | 0.45 | ['0.08', '1.15', '-0.69']
w3.f15 | neg |   | `@@PAD@@ it 's` | 2.22 | ['0.00', '2.22', '0.17']
w3.f16 | pos |   | `particularly for a` | 2.62 | ['1.31', '3.80', '-2.12']
w3.f17 | neg | x | `particularly for a` | 6.52 | ['3.49', '5.11', '-1.92']
w3.f18 | pos |   | `surprisingly decent ,` | 1.76 | ['1.12', '0.32', '0.79']
w3.f19 | pos |   | `installment in a` | 3.13 | ['2.65', '1.23', '-0.64']

## Original input: 
``` bad beyond @@UNK@@ and ridiculous beyond @@UNK@@ . ``` 

## Marked input: 
<pre>bad <span style="background-color: #6698FF">@</span>beyond <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>ridiculous <span style="background-color: #6698FF">@</span>beyond <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | filter class | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :-- | :--
w2.f0 | pos |   | `@@UNK@@ and` | 0.12 | ['1.98', '-1.48']
w2.f1 | pos |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f2 | pos |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | neg | x | `bad beyond` | 2.19 | ['3.46', '-0.71']
w2.f4 | pos |   | `@@PAD@@ bad` | 1.40 | ['0.00', '1.59']
w2.f5 | pos |   | `beyond @@UNK@@` | 1.57 | ['2.59', '-0.71']
w2.f6 | pos |   | `@@PAD@@ bad` | 2.27 | ['0.00', '2.37']
w2.f7 | neg |   | `bad beyond` | 0.18 | ['0.37', '0.72']
w2.f8 | pos |   | `@@UNK@@ and` | 0.34 | ['0.21', '0.34']
w2.f9 | neg |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 | pos |   | `@@UNK@@ and` | 1.28 | ['-0.06', '1.48']
w2.f11 | neg |   | `ridiculous beyond` | 1.91 | ['2.74', '-0.56']
w2.f12 | neg | x | `ridiculous beyond` | 3.99 | ['-1.25', '5.28']
w2.f13 | neg | x | `@@PAD@@ bad` | 3.47 | ['0.00', '3.62']
w2.f14 | neg | x | `and ridiculous` | 8.82 | ['0.13', '8.72']
w2.f15 | pos |   | `bad beyond` | 2.15 | ['2.76', '-0.34']
w2.f16 | neg | x | `bad beyond` | 4.69 | ['1.40', '4.05']
w2.f17 | neg |   | `bad beyond` | 1.90 | ['1.16', '1.35']
w2.f18 | pos |   | `and ridiculous` | 2.32 | ['3.52', '-1.08']
w2.f19 | pos |   | `ridiculous beyond` | 2.05 | ['0.85', '1.50']
w3.f0 | neg | x | `@@PAD@@ bad beyond` | 4.18 | ['0.00', '5.19', '-0.62']
w3.f1 | pos |   | `beyond @@UNK@@ and` | 1.51 | ['2.79', '-0.73', '-0.17']
w3.f2 | neg | x | `@@PAD@@ bad beyond` | 11.88 | ['0.00', '5.83', '6.15']
w3.f3 | pos |   | `@@PAD@@ @@PAD@@ bad` | 0.00 | ['0.00', '0.00', '-1.86']
w3.f4 | pos |   | `@@PAD@@ @@PAD@@ bad` | 0.00 | ['0.00', '0.00', '-2.64']
w3.f5 | pos |   | `beyond @@UNK@@ and` | 2.29 | ['0.80', '-4.00', '5.81']
w3.f6 | neg |   | `and ridiculous beyond` | 3.60 | ['-0.42', '4.63', '-0.40']
w3.f7 | pos |   | `beyond @@UNK@@ and` | 1.32 | ['1.79', '-1.81', '1.83']
w3.f8 | pos |   | `and ridiculous beyond` | 1.06 | ['2.47', '-1.38', '0.26']
w3.f9 | neg | x | `@@PAD@@ bad beyond` | 5.25 | ['0.00', '6.27', '-0.91']
w3.f10 | neg | x | `ridiculous beyond @@UNK@@` | 4.23 | ['3.29', '0.23', '0.86']
w3.f11 | neg | x | `bad beyond @@UNK@@` | 4.32 | ['5.12', '0.14', '-0.75']
w3.f12 | neg | x | `@@PAD@@ bad beyond` | 4.27 | ['0.00', '2.46', '1.93']
w3.f13 | pos |   | `@@UNK@@ and ridiculous` | 0.60 | ['-0.04', '0.60', '0.29']
w3.f14 | neg |   | `@@PAD@@ bad beyond` | 1.87 | ['0.00', '1.89', '0.07']
w3.f15 | neg | x | `@@PAD@@ bad beyond` | 4.40 | ['0.00', '2.39', '2.18']
w3.f16 | pos |   | `bad beyond @@UNK@@` | 0.34 | ['-0.15', '4.39', '-3.52']
w3.f17 | neg | x | `beyond @@UNK@@ .` | 4.99 | ['2.78', '1.39', '0.98']
w3.f18 | pos |   | `@@PAD@@ @@PAD@@ bad` | 0.00 | ['0.00', '0.00', '-1.44']
w3.f19 | pos |   | `ridiculous beyond @@UNK@@` | 1.27 | ['2.72', '0.68', '-2.02']

## Original input: 
``` it 's possible that something hip and @@UNK@@ was being @@UNK@@ here that @@UNK@@ @@UNK@@ to gel , but the result is more puzzling than unsettling . ``` 

## Marked input: 
<pre>it 's possible <span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>something <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hip <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and @@UNK@@ was <span style="background-color: #6698FF">@</span>being <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>here <span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>gel <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span>but <span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>result <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>more <span style="background-color: #6698FF">@</span>puzzling <span style="background-color: #6698FF">@</span>than <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>unsettling <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | filter class | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :-- | :--
w2.f0 | pos |   | `was being` | 1.75 | ['-0.59', '2.72']
w2.f1 | pos |   | `puzzling than` | 2.91 | ['2.66', '0.39']
w2.f2 | pos |   | `than unsettling` | 0.00 | ['0.22', '0.83']
w2.f3 | neg |   | `is more` | 1.90 | ['0.28', '2.17']
w2.f4 | pos |   | `that something` | 1.29 | ['1.54', '-0.07']
w2.f5 | pos |   | `the result` | 2.63 | ['1.16', '1.77']
w2.f6 | pos |   | `possible that` | 3.10 | ['2.15', '1.05']
w2.f7 | neg |   | `the result` | 0.50 | ['-1.19', '2.60']
w2.f8 | pos |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 | neg | x | `@@UNK@@ to` | 7.04 | ['2.38', '4.67']
w2.f10 | pos | x | `'s possible` | 6.06 | ['2.75', '3.44']
w2.f11 | neg | x | `more puzzling` | 3.36 | ['2.11', '1.52']
w2.f12 | neg | x | `that something` | 7.33 | ['1.55', '5.82']
w2.f13 | neg | x | `unsettling .` | 4.51 | ['4.65', '0.01']
w2.f14 | neg | x | `@@UNK@@ was` | 5.80 | ['0.69', '5.14']
w2.f15 | pos |   | `'s possible` | 1.45 | ['1.82', '-0.09']
w2.f16 | neg | x | `was being` | 4.90 | ['3.28', '2.38']
w2.f17 | neg |   | `something hip` | 2.96 | ['0.56', '3.02']
w2.f18 | pos |   | `unsettling .` | 2.82 | ['2.72', '0.22']
w2.f19 | pos |   | `something hip` | 3.10 | ['2.41', '0.99']
w3.f0 | neg | x | `is more puzzling` | 5.26 | ['-1.82', '4.04', '3.44']
w3.f1 | pos | x | `possible that something` | 5.03 | ['3.90', '0.66', '0.85']
w3.f2 | neg | x | `but the result` | 4.89 | ['1.07', '0.94', '2.98']
w3.f3 | pos |   | `that @@UNK@@ @@UNK@@` | 1.59 | ['2.19', '-0.06', '0.07']
w3.f4 | pos |   | `it 's possible` | 3.04 | ['-0.70', '2.08', '2.03']
w3.f5 | pos |   | `something hip and` | 2.79 | ['-3.75', '1.06', '5.81']
w3.f6 | neg |   | `the result is` | 3.42 | ['-0.32', '2.30', '1.64']
w3.f7 | pos | x | `to gel ,` | 4.61 | ['3.76', '0.16', '1.18']
w3.f8 | pos | x | `puzzling than unsettling` | 9.61 | ['1.55', '1.81', '6.53']
w3.f9 | neg | x | `possible that something` | 5.31 | ['2.31', '1.05', '2.05']
w3.f10 | neg | x | `here that @@UNK@@` | 4.37 | ['4.29', '-0.63', '0.86']
w3.f11 | neg |   | `@@PAD@@ it 's` | 1.99 | ['0.00', '0.91', '1.27']
w3.f12 | neg | x | `@@UNK@@ was being` | 5.65 | ['-0.75', '2.90', '3.63']
w3.f13 | pos |   | `result is more` | 4.64 | ['0.35', '2.81', '1.72']
w3.f14 | neg | x | `is more puzzling` | 6.79 | ['-0.45', '4.60', '2.74']
w3.f15 | neg |   | `@@PAD@@ it 's` | 2.22 | ['0.00', '2.22', '0.17']
w3.f16 | pos |   | `is more puzzling` | 3.56 | ['1.27', '1.96', '0.72']
w3.f17 | neg | x | `than unsettling .` | 5.07 | ['2.28', '1.96', '0.98']
w3.f18 | pos | x | `was being @@UNK@@` | 3.44 | ['0.41', '3.72', '-0.23']
w3.f19 | pos |   | `result is more` | 3.66 | ['0.51', '3.62', '-0.36']

## Original input: 
``` a bit too eager to please . ``` 

## Marked input: 
<pre>a bit <span style="background-color: #FFFF00">@</span>too <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>eager <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>please <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | filter class | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :-- | :--
w2.f0 | pos |   | `bit too` | 3.01 | ['0.28', '3.11']
w2.f1 | pos |   | `a bit` | 2.22 | ['2.95', '-0.60']
w2.f2 | pos |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | neg | x | `too eager` | 2.81 | ['1.12', '2.25']
w2.f4 | pos | x | `a bit` | 3.73 | ['2.27', '1.65']
w2.f5 | pos |   | `eager to` | 2.34 | ['0.25', '2.39']
w2.f6 | pos |   | `eager to` | 2.89 | ['2.66', '0.33']
w2.f7 | neg | x | `too eager` | 3.75 | ['0.79', '3.87']
w2.f8 | pos |   | `@@PAD@@ a` | 2.34 | ['0.00', '2.56']
w2.f9 | neg | x | `eager to` | 9.78 | ['5.13', '4.67']
w2.f10 | pos |   | `a bit` | 1.03 | ['1.97', '-0.80']
w2.f11 | neg | x | `too eager` | 4.51 | ['3.88', '0.90']
w2.f12 | neg | x | `too eager` | 4.41 | ['1.83', '2.63']
w2.f13 | neg |   | `please .` | 2.32 | ['2.46', '0.01']
w2.f14 | neg |   | `to please` | 2.88 | ['-2.35', '5.26']
w2.f15 | pos |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f16 | neg | x | `too eager` | 3.82 | ['2.26', '2.32']
w2.f17 | neg | x | `too eager` | 5.55 | ['1.23', '4.93']
w2.f18 | pos |   | `eager to` | 2.78 | ['0.41', '2.50']
w2.f19 | pos |   | `a bit` | 0.34 | ['0.99', '-0.35']
w3.f0 | neg | x | `eager to please` | 6.63 | ['3.34', '-1.42', '5.11']
w3.f1 | pos | x | `bit too eager` | 5.09 | ['2.18', '1.10', '2.19']
w3.f2 | neg |   | `to please .` | 3.05 | ['0.63', '1.67', '0.84']
w3.f3 | pos |   | `bit too eager` | 0.70 | ['1.29', '-0.10', '0.12']
w3.f4 | pos |   | `too eager to` | 1.66 | ['3.10', '-0.31', '-0.77']
w3.f5 | pos | x | `a bit too` | 5.81 | ['1.79', '3.51', '0.85']
w3.f6 | neg |   | `bit too eager` | 1.37 | ['-1.29', '4.25', '-1.38']
w3.f7 | pos | x | `to please .` | 4.46 | ['3.76', '1.02', '0.18']
w3.f8 | pos |   | `bit too eager` | 0.56 | ['0.63', '0.25', '-0.03']
w3.f9 | neg | x | `please . @@PAD@@` | 6.13 | ['5.66', '0.58', '0.00']
w3.f10 | neg |   | `eager to please` | 2.94 | ['2.90', '1.69', '-1.50']
w3.f11 | neg | x | `too eager to` | 7.90 | ['3.15', '2.88', '2.06']
w3.f12 | neg |   | `bit too eager` | 3.02 | ['-1.15', '3.22', '1.08']
w3.f13 | pos |   | `to please .` | 4.08 | ['1.07', '0.81', '2.45']
w3.f14 | neg | x | `bit too eager` | 8.05 | ['1.15', '3.69', '3.30']
w3.f15 | neg |   | `bit too eager` | 1.71 | ['0.32', '3.12', '-1.57']
w3.f16 | pos |   | `bit too eager` | 3.36 | ['0.98', '-0.92', '3.68']
w3.f17 | neg | x | `eager to please` | 7.09 | ['-0.89', '1.66', '6.48']
w3.f18 | pos |   | `@@PAD@@ a bit` | 0.45 | ['0.00', '-0.07', '0.98']
w3.f19 | pos |   | `too eager to` | 0.58 | ['1.09', '0.65', '-1.05']

## Original input: 
``` hey arnold ! is now stretched to barely feature length , with a little more attention paid to the animation . still , the @@UNK@@ @@UNK@@ sensibility of writer @@UNK@@ @@UNK@@ 's story is appealing . ``` 

## Marked input: 
<pre>hey arnold <span style="background-color: #6698FF">@</span>! <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>now <span style="background-color: #FFFF00">@</span>stretched <span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>barely <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>feature <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>length <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>little <span style="background-color: #6698FF">@</span>more <span style="background-color: #6698FF">@</span>attention <span style="background-color: #6698FF">@</span>paid <span style="background-color: #6698FF">@</span>to the animation . still , <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ @@UNK@@ sensibility <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>writer <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>'s <span style="background-color: #FFFF00">@</span>story <span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>appealing <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | filter class | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :-- | :--
w2.f0 | pos | x | `@@UNK@@ sensibility` | 6.88 | ['1.98', '5.27']
w2.f1 | pos |   | `arnold !` | 3.54 | ['0.79', '2.88']
w2.f2 | pos |   | `barely feature` | 0.47 | ['0.51', '1.01']
w2.f3 | neg | x | `of writer` | 2.43 | ['-0.30', '3.29']
w2.f4 | pos | x | `still ,` | 10.39 | ['8.07', '2.50']
w2.f5 | pos |   | `sensibility of` | 2.84 | ['1.38', '1.76']
w2.f6 | pos | x | `still ,` | 6.90 | ['3.07', '3.93']
w2.f7 | neg |   | `barely feature` | 1.65 | ['1.53', '1.03']
w2.f8 | pos | x | `@@UNK@@ 's` | 3.81 | ['0.21', '3.82']
w2.f9 | neg | x | `stretched to` | 9.51 | ['4.85', '4.67']
w2.f10 | pos | x | `'s story` | 3.45 | ['2.75', '0.83']
w2.f11 | neg | x | `feature length` | 4.84 | ['2.08', '3.03']
w2.f12 | neg |   | `to the` | 2.81 | ['1.53', '1.32']
w2.f13 | neg | x | `length ,` | 3.93 | ['1.90', '2.18']
w2.f14 | neg | x | `length ,` | 4.05 | ['3.19', '0.89']
w2.f15 | pos | x | `arnold !` | 4.98 | ['2.22', '3.03']
w2.f16 | neg | x | `of writer` | 3.38 | ['0.18', '3.95']
w2.f17 | neg | x | `hey arnold` | 7.01 | ['2.55', '5.08']
w2.f18 | pos |   | `length ,` | 2.66 | ['1.89', '0.89']
w2.f19 | pos |   | `@@UNK@@ sensibility` | 2.55 | ['0.39', '2.46']
w3.f0 | neg | x | `stretched to barely` | 6.47 | ['1.59', '-1.42', '6.69']
w3.f1 | pos | x | `stretched to barely` | 4.02 | ['0.81', '0.48', '3.11']
w3.f2 | neg | x | `a little more` | 9.11 | ['1.87', '2.64', '4.68']
w3.f3 | pos |   | `little more attention` | 0.17 | ['-0.42', '-1.00', '2.19']
w3.f4 | pos | x | `@@UNK@@ 's story` | 3.52 | ['0.36', '2.08', '1.45']
w3.f5 | pos | x | `is appealing .` | 7.03 | ['0.80', '2.24', '4.32']
w3.f6 | neg |   | `more attention paid` | 2.73 | ['0.39', '1.02', '1.52']
w3.f7 | pos |   | `is now stretched` | 4.01 | ['-0.51', '3.09', '1.93']
w3.f8 | pos | x | `@@UNK@@ sensibility of` | 5.68 | ['0.50', '5.52', '-0.05']
w3.f9 | neg | x | `of writer @@UNK@@` | 3.97 | ['-1.50', '3.44', '2.13']
w3.f10 | neg | x | `of writer @@UNK@@` | 4.33 | ['2.92', '0.70', '0.86']
w3.f11 | neg |   | `little more attention` | 3.15 | ['0.04', '0.13', '3.18']
w3.f12 | neg | x | `length , with` | 6.00 | ['3.61', '-0.15', '2.68']
w3.f13 | pos | x | `is appealing .` | 7.87 | ['1.15', '4.53', '2.45']
w3.f14 | neg | x | `little more attention` | 4.82 | ['0.42', '4.60', '-0.10']
w3.f15 | neg | x | `, with a` | 4.03 | ['1.52', '3.85', '-1.17']
w3.f16 | pos | x | `barely feature length` | 6.36 | ['0.34', '3.02', '3.38']
w3.f17 | neg | x | `barely feature length` | 7.76 | ['3.51', '2.32', '2.09']
w3.f18 | pos |   | `still , the` | 3.20 | ['4.25', '-3.16', '2.57']
w3.f19 | pos | x | `! is now` | 5.77 | ['1.75', '3.62', '0.51']

## Original input: 
``` as @@UNK@@ its title , this @@UNK@@ piffle is ultimately as @@UNK@@ as the @@UNK@@ fabric @@UNK@@ bear . ``` 

## Marked input: 
<pre>as @@UNK@@ its title <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>this <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>piffle <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>ultimately <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>as <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>as the @@UNK@@ fabric <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>bear <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | filter class | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :-- | :--
w2.f0 | pos | x | `@@UNK@@ fabric` | 7.47 | ['1.98', '5.87']
w2.f1 | pos |   | `bear .` | 0.88 | ['3.38', '-2.37']
w2.f2 | pos |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | neg | x | `title ,` | 4.27 | ['4.39', '0.44']
w2.f4 | pos | x | `title ,` | 3.90 | ['1.59', '2.50']
w2.f5 | pos |   | `this @@UNK@@` | 1.82 | ['2.84', '-0.71']
w2.f6 | pos | x | `its title` | 4.23 | ['0.58', '3.75']
w2.f7 | neg |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 | pos |   | `title ,` | 2.17 | ['3.17', '-0.79']
w2.f9 | neg | x | `@@UNK@@ piffle` | 6.78 | ['2.38', '4.42']
w2.f10 | pos |   | `@@UNK@@ piffle` | 0.18 | ['-0.06', '0.37']
w2.f11 | neg | x | `@@UNK@@ bear` | 4.35 | ['-0.97', '5.59']
w2.f12 | neg |   | `its title` | 2.20 | ['-0.82', '3.07']
w2.f13 | neg | x | `title ,` | 4.92 | ['2.88', '2.18']
w2.f14 | neg |   | `@@UNK@@ its` | 2.35 | ['0.69', '1.69']
w2.f15 | pos |   | `title ,` | 1.52 | ['2.10', '-0.31']
w2.f16 | neg |   | `@@UNK@@ bear` | 1.41 | ['-0.75', '2.92']
w2.f17 | neg |   | `title ,` | 1.74 | ['2.74', '-0.38']
w2.f18 | pos |   | `its title` | 1.86 | ['0.68', '1.30']
w2.f19 | pos |   | `as the` | 1.74 | ['1.84', '0.20']
w3.f0 | neg | x | `fabric @@UNK@@ bear` | 8.41 | ['1.10', '0.35', '7.35']
w3.f1 | pos |   | `title , this` | 2.87 | ['3.45', '0.90', '-1.11']
w3.f2 | neg | x | `fabric @@UNK@@ bear` | 6.20 | ['2.96', '-0.65', '3.98']
w3.f3 | pos |   | `@@PAD@@ @@PAD@@ as` | 0.00 | ['0.00', '0.00', '-2.59']
w3.f4 | pos |   | `@@UNK@@ piffle is` | 1.94 | ['0.36', '-0.51', '2.46']
w3.f5 | pos |   | `@@UNK@@ bear .` | 1.69 | ['0.08', '-2.39', '4.32']
w3.f6 | neg |   | `@@UNK@@ piffle is` | 2.27 | ['-0.28', '1.11', '1.64']
w3.f7 | pos |   | `as @@UNK@@ its` | 3.92 | ['1.64', '-1.81', '4.59']
w3.f8 | pos |   | `fabric @@UNK@@ bear` | 2.69 | ['1.41', '-0.27', '1.84']
w3.f9 | neg | x | `piffle is ultimately` | 4.49 | ['2.29', '0.12', '2.18']
w3.f10 | neg | x | `piffle is ultimately` | 4.08 | ['3.18', '0.69', '0.36']
w3.f11 | neg |   | `piffle is ultimately` | 2.29 | ['-0.74', '-0.19', '3.42']
w3.f12 | neg | x | `@@UNK@@ piffle is` | 5.39 | ['-0.75', '4.45', '1.82']
w3.f13 | pos | x | `is ultimately as` | 5.69 | ['1.15', '3.90', '0.88']
w3.f14 | neg | x | `@@UNK@@ piffle is` | 5.67 | ['-0.34', '3.47', '2.63']
w3.f15 | neg |   | `this @@UNK@@ piffle` | 2.60 | ['2.58', '-1.69', '1.87']
w3.f16 | pos |   | `title , this` | 2.78 | ['-1.31', '3.78', '0.68']
w3.f17 | neg | x | `this @@UNK@@ piffle` | 8.06 | ['1.37', '1.39', '5.46']
w3.f18 | pos |   | `@@UNK@@ as the` | 1.45 | ['-2.55', '1.90', '2.57']
w3.f19 | pos | x | `is ultimately as` | 4.91 | ['0.33', '2.83', '1.86']