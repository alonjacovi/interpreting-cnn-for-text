# Prediction info
## Note: Please view with a color markdown viewer! The "@" signs are supposed to be colored according to the filter's identity class.

## Original input: 
``` a reality - @@UNK@@ @@UNK@@ . ``` 

## Marked input: 
<pre>a <span style="background-color: #6698FF">@</span>reality <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ @@UNK@@` | 0.81 | ['1.98', '-0.79']
w2.f1 |   | `a reality` | 0.91 | ['2.95', '-1.91']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f4 |   | `a reality` | 1.81 | ['2.27', '-0.27']
w2.f5 |   | `. @@PAD@@` | 0.37 | ['0.67', '0.00']
w2.f6 |   | `a reality` | 1.10 | ['0.54', '0.66']
w2.f7 |   | `reality -` | 0.47 | ['2.26', '-0.88']
w2.f8 |   | `@@PAD@@ a` | 2.34 | ['0.00', '2.56']
w2.f9 |   | `reality -` | 2.89 | ['2.44', '0.46']
w2.f10 |   | `@@PAD@@ a` | 0.06 | ['0.00', '0.20']
w2.f11 |   | `reality -` | 1.40 | ['2.70', '-1.02']
w2.f12 |   | `reality -` | 1.05 | ['1.69', '-0.61']
w2.f13 | x | `reality -` | 3.47 | ['2.43', '1.20']
w2.f14 |   | `@@UNK@@ .` | 1.04 | ['0.69', '0.39']
w2.f15 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f16 |   | `a reality` | 2.58 | ['-0.39', '3.73']
w2.f17 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f18 |   | `a reality` | 0.94 | ['0.76', '0.30']
w2.f19 |   | `a reality` | 2.94 | ['0.99', '2.25']
w3.f0 | x | `@@PAD@@ a reality` | 4.60 | ['0.00', '3.29', '1.70']
w3.f1 |   | `a reality -` | 0.06 | ['-1.76', '0.55', '1.66']
w3.f2 |   | `a reality -` | 2.50 | ['1.87', '0.18', '0.54']
w3.f3 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.45']
w3.f4 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.65']
w3.f5 |   | `@@PAD@@ @@PAD@@ a` | 0.74 | ['0.00', '0.00', '1.07']
w3.f6 |   | `a reality -` | 3.16 | ['1.76', '2.16', '-0.54']
w3.f7 |   | `reality - @@UNK@@` | 0.77 | ['2.40', '-1.06', '-0.07']
w3.f8 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.46']
w3.f9 | x | `reality - @@UNK@@` | 3.84 | ['2.29', '-0.49', '2.13']
w3.f10 |   | `@@UNK@@ . @@PAD@@` | 2.18 | ['0.33', '2.00', '0.00']
w3.f11 |   | `@@PAD@@ @@PAD@@ a` | 2.59 | ['0.00', '0.00', '2.78']
w3.f12 |   | `reality - @@UNK@@` | 3.81 | ['2.53', '2.81', '-1.41']
w3.f13 |   | `@@UNK@@ @@UNK@@ .` | 0.42 | ['-0.04', '-1.74', '2.45']
w3.f14 |   | `reality - @@UNK@@` | 0.18 | ['1.12', '0.52', '-1.37']
w3.f15 |   | `@@PAD@@ a reality` | 1.29 | ['0.00', '-0.09', '1.55']
w3.f16 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-2.12']
w3.f17 |   | `@@PAD@@ a reality` | 0.27 | ['0.00', '-1.45', '1.87']
w3.f18 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.37']
w3.f19 |   | `a reality -` | 2.03 | ['3.70', '-0.05', '-1.51']

## Original input: 
``` it 's a glorious spectacle like those d . w . @@UNK@@ made in the early days of silent film . ``` 

## Marked input: 
<pre>it 's <span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>glorious <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>spectacle <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>like <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>those <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>d <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>w . <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>made <span style="background-color: #6698FF">@</span>in the early <span style="background-color: #FFFF00">@</span>days <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>silent <span style="background-color: #6698FF">@</span>film <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `those d` | 6.44 | ['0.77', '6.05']
w2.f1 | x | `a glorious` | 7.57 | ['2.95', '4.76']
w2.f2 |   | `silent film` | 0.88 | ['1.10', '0.83']
w2.f3 |   | `those d` | 1.98 | ['1.40', '1.13']
w2.f4 |   | `a glorious` | 2.43 | ['2.27', '0.35']
w2.f5 | x | `a glorious` | 4.87 | ['0.71', '4.47']
w2.f6 |   | `in the` | 1.91 | ['1.77', '0.24']
w2.f7 |   | `those d` | 1.28 | ['-0.49', '2.67']
w2.f8 | x | `those d` | 5.53 | ['4.07', '1.68']
w2.f9 |   | `made in` | 4.40 | ['2.52', '1.89']
w2.f10 | x | `glorious spectacle` | 4.80 | ['3.18', '1.76']
w2.f11 | x | `days of` | 3.36 | ['2.68', '0.95']
w2.f12 |   | `silent film` | 1.65 | ['2.19', '-0.50']
w2.f13 | x | `spectacle like` | 4.30 | ['1.42', '3.03']
w2.f14 |   | `like those` | 2.57 | ['0.54', '2.06']
w2.f15 | x | `early days` | 3.53 | ['2.34', '1.46']
w2.f16 |   | `days of` | 2.54 | ['3.63', '-0.34']
w2.f17 | x | `w .` | 3.81 | ['3.96', '0.47']
w2.f18 |   | `silent film` | 2.33 | ['1.51', '0.95']
w2.f19 |   | `silent film` | 2.39 | ['3.23', '-0.54']
w3.f0 | x | `'s a glorious` | 4.44 | ['-1.14', '3.29', '2.68']
w3.f1 |   | `early days of` | 1.52 | ['-1.21', '3.25', '-0.14']
w3.f2 |   | `d . w` | 3.33 | ['3.29', '-1.42', '1.55']
w3.f3 |   | `glorious spectacle like` | 1.32 | ['1.53', '-0.28', '0.68']
w3.f4 | x | `glorious spectacle like` | 4.51 | ['2.49', '-0.85', '3.23']
w3.f5 |   | `. w .` | 4.16 | ['-0.37', '0.54', '4.32']
w3.f6 |   | `d . w` | 2.30 | ['3.69', '1.07', '-2.25']
w3.f7 |   | `'s a glorious` | 4.11 | ['-0.31', '0.48', '4.43']
w3.f8 |   | `a glorious spectacle` | 2.78 | ['0.66', '0.99', '1.42']
w3.f9 | x | `w . @@UNK@@` | 7.34 | ['4.74', '0.58', '2.13']
w3.f10 | x | `of silent film` | 4.83 | ['2.92', '-0.31', '2.36']
w3.f11 | x | `it 's a` | 4.07 | ['1.01', '0.46', '2.78']
w3.f12 |   | `the early days` | 3.16 | ['2.43', '0.82', '0.05']
w3.f13 | x | `the early days` | 8.53 | ['4.70', '-0.15', '4.23']
w3.f14 | x | `glorious spectacle like` | 4.42 | ['-1.17', '0.03', '5.65']
w3.f15 | x | `early days of` | 5.25 | ['0.95', '2.46', '2.01']
w3.f16 | x | `'s a glorious` | 7.35 | ['2.11', '0.35', '5.26']
w3.f17 |   | `the early days` | 3.77 | ['-1.17', '2.86', '2.24']
w3.f18 |   | `days of silent` | 2.48 | ['0.56', '2.10', '0.29']
w3.f19 | x | `a glorious spectacle` | 5.16 | ['3.70', '1.96', '-0.38']

## Original input: 
``` it 's surprisingly decent , particularly for a @@UNK@@ installment in a series . ``` 

## Marked input: 
<pre>it 's <span style="background-color: #FFFF00">@</span>surprisingly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>decent <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>particularly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>for <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>installment <span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>series <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ installment` | 2.15 | ['1.98', '0.54']
w2.f1 |   | `it 's` | 1.94 | ['0.50', '1.57']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `particularly for` | 0.01 | ['1.92', '-1.35']
w2.f4 |   | `a series` | 2.60 | ['2.27', '0.52']
w2.f5 |   | `surprisingly decent` | 2.69 | ['4.16', '-1.17']
w2.f6 | x | `decent ,` | 5.02 | ['1.19', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 |   | `@@UNK@@ installment` | 4.07 | ['2.38', '1.70']
w2.f10 | x | `'s surprisingly` | 3.02 | ['2.75', '0.40']
w2.f11 |   | `installment in` | 1.66 | ['3.40', '-1.47']
w2.f12 | x | `@@UNK@@ installment` | 3.56 | ['-0.28', '3.87']
w2.f13 | x | `particularly for` | 4.15 | ['1.51', '2.78']
w2.f14 |   | `@@UNK@@ installment` | 2.61 | ['0.69', '1.96']
w2.f15 |   | `, particularly` | 3.20 | ['2.19', '1.28']
w2.f16 |   | `series .` | 0.90 | ['3.19', '-1.53']
w2.f17 |   | `surprisingly decent` | 1.26 | ['1.66', '0.21']
w2.f18 | x | `surprisingly decent` | 3.32 | ['2.98', '0.47']
w2.f19 |   | `particularly for` | 1.09 | ['0.69', '0.69']
w3.f0 | x | `in a series` | 4.41 | ['-0.14', '3.29', '1.65']
w3.f1 |   | `series . @@PAD@@` | 1.06 | ['1.79', '-0.35', '0.00']
w3.f2 | x | `surprisingly decent ,` | 4.09 | ['4.01', '-1.16', '1.32']
w3.f3 |   | `in a series` | 0.27 | ['1.23', '-1.71', '1.35']
w3.f4 | x | `it 's surprisingly` | 3.60 | ['-0.70', '2.08', '2.58']
w3.f5 | x | `a series .` | 8.17 | ['1.79', '2.39', '4.32']
w3.f6 | x | `'s surprisingly decent` | 4.25 | ['3.62', '2.60', '-1.76']
w3.f7 |   | `a series .` | 2.68 | ['-0.02', '3.02', '0.18']
w3.f8 | x | `it 's surprisingly` | 5.76 | ['2.11', '0.26', '3.68']
w3.f9 | x | `in a series` | 3.90 | ['1.57', '-0.16', '2.60']
w3.f10 |   | `decent , particularly` | 2.12 | ['-0.77', '-0.41', '3.44']
w3.f11 | x | `particularly for a` | 4.81 | ['5.72', '-3.50', '2.78']
w3.f12 |   | `'s surprisingly decent` | 3.20 | ['-0.70', '0.68', '3.35']
w3.f13 |   | `decent , particularly` | 4.58 | ['-0.04', '1.92', '2.95']
w3.f14 |   | `it 's surprisingly` | 0.45 | ['0.08', '1.15', '-0.69']
w3.f15 |   | `@@PAD@@ it 's` | 2.22 | ['0.00', '2.22', '0.17']
w3.f16 |   | `particularly for a` | 2.62 | ['1.31', '3.80', '-2.12']
w3.f17 | x | `particularly for a` | 6.52 | ['3.49', '5.11', '-1.92']
w3.f18 |   | `surprisingly decent ,` | 1.76 | ['1.12', '0.32', '0.79']
w3.f19 |   | `installment in a` | 3.13 | ['2.65', '1.23', '-0.64']

## Original input: 
``` bad beyond @@UNK@@ and ridiculous beyond @@UNK@@ . ``` 

## Marked input: 
<pre>bad <span style="background-color: #6698FF">@</span>beyond <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>ridiculous <span style="background-color: #6698FF">@</span>beyond <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ and` | 0.12 | ['1.98', '-1.48']
w2.f1 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `bad beyond` | 2.19 | ['3.46', '-0.71']
w2.f4 |   | `@@PAD@@ bad` | 1.40 | ['0.00', '1.59']
w2.f5 |   | `beyond @@UNK@@` | 1.57 | ['2.59', '-0.71']
w2.f6 |   | `@@PAD@@ bad` | 2.27 | ['0.00', '2.37']
w2.f7 |   | `bad beyond` | 0.18 | ['0.37', '0.72']
w2.f8 |   | `@@UNK@@ and` | 0.34 | ['0.21', '0.34']
w2.f9 |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 |   | `@@UNK@@ and` | 1.28 | ['-0.06', '1.48']
w2.f11 |   | `ridiculous beyond` | 1.91 | ['2.74', '-0.56']
w2.f12 | x | `ridiculous beyond` | 3.99 | ['-1.25', '5.28']
w2.f13 | x | `@@PAD@@ bad` | 3.47 | ['0.00', '3.62']
w2.f14 | x | `and ridiculous` | 8.82 | ['0.13', '8.72']
w2.f15 |   | `bad beyond` | 2.15 | ['2.76', '-0.34']
w2.f16 | x | `bad beyond` | 4.69 | ['1.40', '4.05']
w2.f17 |   | `bad beyond` | 1.90 | ['1.16', '1.35']
w2.f18 |   | `and ridiculous` | 2.32 | ['3.52', '-1.08']
w2.f19 |   | `ridiculous beyond` | 2.05 | ['0.85', '1.50']
w3.f0 | x | `@@PAD@@ bad beyond` | 4.18 | ['0.00', '5.19', '-0.62']
w3.f1 |   | `beyond @@UNK@@ and` | 1.51 | ['2.79', '-0.73', '-0.17']
w3.f2 | x | `@@PAD@@ bad beyond` | 11.88 | ['0.00', '5.83', '6.15']
w3.f3 |   | `@@PAD@@ @@PAD@@ bad` | 0.00 | ['0.00', '0.00', '-1.86']
w3.f4 |   | `@@PAD@@ @@PAD@@ bad` | 0.00 | ['0.00', '0.00', '-2.64']
w3.f5 |   | `beyond @@UNK@@ and` | 2.29 | ['0.80', '-4.00', '5.81']
w3.f6 |   | `and ridiculous beyond` | 3.60 | ['-0.42', '4.63', '-0.40']
w3.f7 |   | `beyond @@UNK@@ and` | 1.32 | ['1.79', '-1.81', '1.83']
w3.f8 |   | `and ridiculous beyond` | 1.06 | ['2.47', '-1.38', '0.26']
w3.f9 | x | `@@PAD@@ bad beyond` | 5.25 | ['0.00', '6.27', '-0.91']
w3.f10 | x | `ridiculous beyond @@UNK@@` | 4.23 | ['3.29', '0.23', '0.86']
w3.f11 | x | `bad beyond @@UNK@@` | 4.32 | ['5.12', '0.14', '-0.75']
w3.f12 | x | `@@PAD@@ bad beyond` | 4.27 | ['0.00', '2.46', '1.93']
w3.f13 |   | `@@UNK@@ and ridiculous` | 0.60 | ['-0.04', '0.60', '0.29']
w3.f14 |   | `@@PAD@@ bad beyond` | 1.87 | ['0.00', '1.89', '0.07']
w3.f15 | x | `@@PAD@@ bad beyond` | 4.40 | ['0.00', '2.39', '2.18']
w3.f16 |   | `bad beyond @@UNK@@` | 0.34 | ['-0.15', '4.39', '-3.52']
w3.f17 | x | `beyond @@UNK@@ .` | 4.99 | ['2.78', '1.39', '0.98']
w3.f18 |   | `@@PAD@@ @@PAD@@ bad` | 0.00 | ['0.00', '0.00', '-1.44']
w3.f19 |   | `ridiculous beyond @@UNK@@` | 1.27 | ['2.72', '0.68', '-2.02']

## Original input: 
``` it 's possible that something hip and @@UNK@@ was being @@UNK@@ here that @@UNK@@ @@UNK@@ to gel , but the result is more puzzling than unsettling . ``` 

## Marked input: 
<pre>it 's possible <span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>something <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hip <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and @@UNK@@ was <span style="background-color: #6698FF">@</span>being <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>here <span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>gel <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span>but <span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>result <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>more <span style="background-color: #6698FF">@</span>puzzling <span style="background-color: #6698FF">@</span>than <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>unsettling <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `was being` | 1.75 | ['-0.59', '2.72']
w2.f1 |   | `puzzling than` | 2.91 | ['2.66', '0.39']
w2.f2 |   | `than unsettling` | 0.00 | ['0.22', '0.83']
w2.f3 |   | `is more` | 1.90 | ['0.28', '2.17']
w2.f4 |   | `that something` | 1.29 | ['1.54', '-0.07']
w2.f5 |   | `the result` | 2.63 | ['1.16', '1.77']
w2.f6 |   | `possible that` | 3.10 | ['2.15', '1.05']
w2.f7 |   | `the result` | 0.50 | ['-1.19', '2.60']
w2.f8 |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 | x | `@@UNK@@ to` | 7.04 | ['2.38', '4.67']
w2.f10 | x | `'s possible` | 6.06 | ['2.75', '3.44']
w2.f11 | x | `more puzzling` | 3.36 | ['2.11', '1.52']
w2.f12 | x | `that something` | 7.33 | ['1.55', '5.82']
w2.f13 | x | `unsettling .` | 4.51 | ['4.65', '0.01']
w2.f14 | x | `@@UNK@@ was` | 5.80 | ['0.69', '5.14']
w2.f15 |   | `'s possible` | 1.45 | ['1.82', '-0.09']
w2.f16 | x | `was being` | 4.90 | ['3.28', '2.38']
w2.f17 |   | `something hip` | 2.96 | ['0.56', '3.02']
w2.f18 |   | `unsettling .` | 2.82 | ['2.72', '0.22']
w2.f19 |   | `something hip` | 3.10 | ['2.41', '0.99']
w3.f0 | x | `is more puzzling` | 5.26 | ['-1.82', '4.04', '3.44']
w3.f1 | x | `possible that something` | 5.03 | ['3.90', '0.66', '0.85']
w3.f2 | x | `but the result` | 4.89 | ['1.07', '0.94', '2.98']
w3.f3 |   | `that @@UNK@@ @@UNK@@` | 1.59 | ['2.19', '-0.06', '0.07']
w3.f4 |   | `it 's possible` | 3.04 | ['-0.70', '2.08', '2.03']
w3.f5 |   | `something hip and` | 2.79 | ['-3.75', '1.06', '5.81']
w3.f6 |   | `the result is` | 3.42 | ['-0.32', '2.30', '1.64']
w3.f7 | x | `to gel ,` | 4.61 | ['3.76', '0.16', '1.18']
w3.f8 | x | `puzzling than unsettling` | 9.61 | ['1.55', '1.81', '6.53']
w3.f9 | x | `possible that something` | 5.31 | ['2.31', '1.05', '2.05']
w3.f10 | x | `here that @@UNK@@` | 4.37 | ['4.29', '-0.63', '0.86']
w3.f11 |   | `@@PAD@@ it 's` | 1.99 | ['0.00', '0.91', '1.27']
w3.f12 | x | `@@UNK@@ was being` | 5.65 | ['-0.75', '2.90', '3.63']
w3.f13 |   | `result is more` | 4.64 | ['0.35', '2.81', '1.72']
w3.f14 | x | `is more puzzling` | 6.79 | ['-0.45', '4.60', '2.74']
w3.f15 |   | `@@PAD@@ it 's` | 2.22 | ['0.00', '2.22', '0.17']
w3.f16 |   | `is more puzzling` | 3.56 | ['1.27', '1.96', '0.72']
w3.f17 | x | `than unsettling .` | 5.07 | ['2.28', '1.96', '0.98']
w3.f18 | x | `was being @@UNK@@` | 3.44 | ['0.41', '3.72', '-0.23']
w3.f19 |   | `result is more` | 3.66 | ['0.51', '3.62', '-0.36']

## Original input: 
``` a bit too eager to please . ``` 

## Marked input: 
<pre>a bit <span style="background-color: #FFFF00">@</span>too <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>eager <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>please <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `bit too` | 3.01 | ['0.28', '3.11']
w2.f1 |   | `a bit` | 2.22 | ['2.95', '-0.60']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `too eager` | 2.81 | ['1.12', '2.25']
w2.f4 | x | `a bit` | 3.73 | ['2.27', '1.65']
w2.f5 |   | `eager to` | 2.34 | ['0.25', '2.39']
w2.f6 |   | `eager to` | 2.89 | ['2.66', '0.33']
w2.f7 | x | `too eager` | 3.75 | ['0.79', '3.87']
w2.f8 |   | `@@PAD@@ a` | 2.34 | ['0.00', '2.56']
w2.f9 | x | `eager to` | 9.78 | ['5.13', '4.67']
w2.f10 |   | `a bit` | 1.03 | ['1.97', '-0.80']
w2.f11 | x | `too eager` | 4.51 | ['3.88', '0.90']
w2.f12 | x | `too eager` | 4.41 | ['1.83', '2.63']
w2.f13 |   | `please .` | 2.32 | ['2.46', '0.01']
w2.f14 |   | `to please` | 2.88 | ['-2.35', '5.26']
w2.f15 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f16 | x | `too eager` | 3.82 | ['2.26', '2.32']
w2.f17 | x | `too eager` | 5.55 | ['1.23', '4.93']
w2.f18 |   | `eager to` | 2.78 | ['0.41', '2.50']
w2.f19 |   | `a bit` | 0.34 | ['0.99', '-0.35']
w3.f0 | x | `eager to please` | 6.63 | ['3.34', '-1.42', '5.11']
w3.f1 | x | `bit too eager` | 5.09 | ['2.18', '1.10', '2.19']
w3.f2 |   | `to please .` | 3.05 | ['0.63', '1.67', '0.84']
w3.f3 |   | `bit too eager` | 0.70 | ['1.29', '-0.10', '0.12']
w3.f4 |   | `too eager to` | 1.66 | ['3.10', '-0.31', '-0.77']
w3.f5 | x | `a bit too` | 5.81 | ['1.79', '3.51', '0.85']
w3.f6 |   | `bit too eager` | 1.37 | ['-1.29', '4.25', '-1.38']
w3.f7 | x | `to please .` | 4.46 | ['3.76', '1.02', '0.18']
w3.f8 |   | `bit too eager` | 0.56 | ['0.63', '0.25', '-0.03']
w3.f9 | x | `please . @@PAD@@` | 6.13 | ['5.66', '0.58', '0.00']
w3.f10 |   | `eager to please` | 2.94 | ['2.90', '1.69', '-1.50']
w3.f11 | x | `too eager to` | 7.90 | ['3.15', '2.88', '2.06']
w3.f12 |   | `bit too eager` | 3.02 | ['-1.15', '3.22', '1.08']
w3.f13 |   | `to please .` | 4.08 | ['1.07', '0.81', '2.45']
w3.f14 | x | `bit too eager` | 8.05 | ['1.15', '3.69', '3.30']
w3.f15 |   | `bit too eager` | 1.71 | ['0.32', '3.12', '-1.57']
w3.f16 |   | `bit too eager` | 3.36 | ['0.98', '-0.92', '3.68']
w3.f17 | x | `eager to please` | 7.09 | ['-0.89', '1.66', '6.48']
w3.f18 |   | `@@PAD@@ a bit` | 0.45 | ['0.00', '-0.07', '0.98']
w3.f19 |   | `too eager to` | 0.58 | ['1.09', '0.65', '-1.05']

## Original input: 
``` hey arnold ! is now stretched to barely feature length , with a little more attention paid to the animation . still , the @@UNK@@ @@UNK@@ sensibility of writer @@UNK@@ @@UNK@@ 's story is appealing . ``` 

## Marked input: 
<pre>hey arnold <span style="background-color: #6698FF">@</span>! <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>now <span style="background-color: #FFFF00">@</span>stretched <span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>barely <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>feature <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>length <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>little <span style="background-color: #6698FF">@</span>more <span style="background-color: #6698FF">@</span>attention <span style="background-color: #6698FF">@</span>paid <span style="background-color: #6698FF">@</span>to the animation . still , <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ @@UNK@@ sensibility <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>writer <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>'s <span style="background-color: #FFFF00">@</span>story <span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>appealing <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ sensibility` | 6.88 | ['1.98', '5.27']
w2.f1 |   | `arnold !` | 3.54 | ['0.79', '2.88']
w2.f2 |   | `barely feature` | 0.47 | ['0.51', '1.01']
w2.f3 | x | `of writer` | 2.43 | ['-0.30', '3.29']
w2.f4 | x | `still ,` | 10.39 | ['8.07', '2.50']
w2.f5 |   | `sensibility of` | 2.84 | ['1.38', '1.76']
w2.f6 | x | `still ,` | 6.90 | ['3.07', '3.93']
w2.f7 |   | `barely feature` | 1.65 | ['1.53', '1.03']
w2.f8 | x | `@@UNK@@ 's` | 3.81 | ['0.21', '3.82']
w2.f9 | x | `stretched to` | 9.51 | ['4.85', '4.67']
w2.f10 | x | `'s story` | 3.45 | ['2.75', '0.83']
w2.f11 | x | `feature length` | 4.84 | ['2.08', '3.03']
w2.f12 |   | `to the` | 2.81 | ['1.53', '1.32']
w2.f13 | x | `length ,` | 3.93 | ['1.90', '2.18']
w2.f14 | x | `length ,` | 4.05 | ['3.19', '0.89']
w2.f15 | x | `arnold !` | 4.98 | ['2.22', '3.03']
w2.f16 | x | `of writer` | 3.38 | ['0.18', '3.95']
w2.f17 | x | `hey arnold` | 7.01 | ['2.55', '5.08']
w2.f18 |   | `length ,` | 2.66 | ['1.89', '0.89']
w2.f19 |   | `@@UNK@@ sensibility` | 2.55 | ['0.39', '2.46']
w3.f0 | x | `stretched to barely` | 6.47 | ['1.59', '-1.42', '6.69']
w3.f1 | x | `stretched to barely` | 4.02 | ['0.81', '0.48', '3.11']
w3.f2 | x | `a little more` | 9.11 | ['1.87', '2.64', '4.68']
w3.f3 |   | `little more attention` | 0.17 | ['-0.42', '-1.00', '2.19']
w3.f4 | x | `@@UNK@@ 's story` | 3.52 | ['0.36', '2.08', '1.45']
w3.f5 | x | `is appealing .` | 7.03 | ['0.80', '2.24', '4.32']
w3.f6 |   | `more attention paid` | 2.73 | ['0.39', '1.02', '1.52']
w3.f7 |   | `is now stretched` | 4.01 | ['-0.51', '3.09', '1.93']
w3.f8 | x | `@@UNK@@ sensibility of` | 5.68 | ['0.50', '5.52', '-0.05']
w3.f9 | x | `of writer @@UNK@@` | 3.97 | ['-1.50', '3.44', '2.13']
w3.f10 | x | `of writer @@UNK@@` | 4.33 | ['2.92', '0.70', '0.86']
w3.f11 |   | `little more attention` | 3.15 | ['0.04', '0.13', '3.18']
w3.f12 | x | `length , with` | 6.00 | ['3.61', '-0.15', '2.68']
w3.f13 | x | `is appealing .` | 7.87 | ['1.15', '4.53', '2.45']
w3.f14 | x | `little more attention` | 4.82 | ['0.42', '4.60', '-0.10']
w3.f15 | x | `, with a` | 4.03 | ['1.52', '3.85', '-1.17']
w3.f16 | x | `barely feature length` | 6.36 | ['0.34', '3.02', '3.38']
w3.f17 | x | `barely feature length` | 7.76 | ['3.51', '2.32', '2.09']
w3.f18 |   | `still , the` | 3.20 | ['4.25', '-3.16', '2.57']
w3.f19 | x | `! is now` | 5.77 | ['1.75', '3.62', '0.51']

## Original input: 
``` as @@UNK@@ its title , this @@UNK@@ piffle is ultimately as @@UNK@@ as the @@UNK@@ fabric @@UNK@@ bear . ``` 

## Marked input: 
<pre>as @@UNK@@ its title <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>this <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>piffle <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>ultimately <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>as <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>as the @@UNK@@ fabric <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>bear <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ fabric` | 7.47 | ['1.98', '5.87']
w2.f1 |   | `bear .` | 0.88 | ['3.38', '-2.37']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `title ,` | 4.27 | ['4.39', '0.44']
w2.f4 | x | `title ,` | 3.90 | ['1.59', '2.50']
w2.f5 |   | `this @@UNK@@` | 1.82 | ['2.84', '-0.71']
w2.f6 | x | `its title` | 4.23 | ['0.58', '3.75']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `title ,` | 2.17 | ['3.17', '-0.79']
w2.f9 | x | `@@UNK@@ piffle` | 6.78 | ['2.38', '4.42']
w2.f10 |   | `@@UNK@@ piffle` | 0.18 | ['-0.06', '0.37']
w2.f11 | x | `@@UNK@@ bear` | 4.35 | ['-0.97', '5.59']
w2.f12 |   | `its title` | 2.20 | ['-0.82', '3.07']
w2.f13 | x | `title ,` | 4.92 | ['2.88', '2.18']
w2.f14 |   | `@@UNK@@ its` | 2.35 | ['0.69', '1.69']
w2.f15 |   | `title ,` | 1.52 | ['2.10', '-0.31']
w2.f16 |   | `@@UNK@@ bear` | 1.41 | ['-0.75', '2.92']
w2.f17 |   | `title ,` | 1.74 | ['2.74', '-0.38']
w2.f18 |   | `its title` | 1.86 | ['0.68', '1.30']
w2.f19 |   | `as the` | 1.74 | ['1.84', '0.20']
w3.f0 | x | `fabric @@UNK@@ bear` | 8.41 | ['1.10', '0.35', '7.35']
w3.f1 |   | `title , this` | 2.87 | ['3.45', '0.90', '-1.11']
w3.f2 | x | `fabric @@UNK@@ bear` | 6.20 | ['2.96', '-0.65', '3.98']
w3.f3 |   | `@@PAD@@ @@PAD@@ as` | 0.00 | ['0.00', '0.00', '-2.59']
w3.f4 |   | `@@UNK@@ piffle is` | 1.94 | ['0.36', '-0.51', '2.46']
w3.f5 |   | `@@UNK@@ bear .` | 1.69 | ['0.08', '-2.39', '4.32']
w3.f6 |   | `@@UNK@@ piffle is` | 2.27 | ['-0.28', '1.11', '1.64']
w3.f7 |   | `as @@UNK@@ its` | 3.92 | ['1.64', '-1.81', '4.59']
w3.f8 |   | `fabric @@UNK@@ bear` | 2.69 | ['1.41', '-0.27', '1.84']
w3.f9 | x | `piffle is ultimately` | 4.49 | ['2.29', '0.12', '2.18']
w3.f10 | x | `piffle is ultimately` | 4.08 | ['3.18', '0.69', '0.36']
w3.f11 |   | `piffle is ultimately` | 2.29 | ['-0.74', '-0.19', '3.42']
w3.f12 | x | `@@UNK@@ piffle is` | 5.39 | ['-0.75', '4.45', '1.82']
w3.f13 | x | `is ultimately as` | 5.69 | ['1.15', '3.90', '0.88']
w3.f14 | x | `@@UNK@@ piffle is` | 5.67 | ['-0.34', '3.47', '2.63']
w3.f15 |   | `this @@UNK@@ piffle` | 2.60 | ['2.58', '-1.69', '1.87']
w3.f16 |   | `title , this` | 2.78 | ['-1.31', '3.78', '0.68']
w3.f17 | x | `this @@UNK@@ piffle` | 8.06 | ['1.37', '1.39', '5.46']
w3.f18 |   | `@@UNK@@ as the` | 1.45 | ['-2.55', '1.90', '2.57']
w3.f19 | x | `is ultimately as` | 4.91 | ['0.33', '2.83', '1.86']

## Original input: 
``` @@UNK@@ like your @@UNK@@ scores are below @@UNK@@ and you might not notice the flaws . ``` 

## Marked input: 
<pre>@@UNK@@ <span style="background-color: #6698FF">@</span>like <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>your <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>scores <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>are <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>below <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>and you <span style="background-color: #FFFF00">@</span>might <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>not <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>notice <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>flaws <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `not notice` | 7.26 | ['-0.06', '7.69']
w2.f1 | x | `not notice` | 5.12 | ['-0.99', '6.24']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `you might` | 0.87 | ['0.42', '1.01']
w2.f4 | x | `flaws .` | 6.71 | ['6.93', '-0.03']
w2.f5 | x | `the flaws` | 5.36 | ['1.16', '4.50']
w2.f6 | x | `notice the` | 4.27 | ['4.12', '0.24']
w2.f7 | x | `like your` | 2.34 | ['-0.30', '3.55']
w2.f8 | x | `and you` | 3.78 | ['-0.15', '4.14']
w2.f9 |   | `@@UNK@@ like` | 3.15 | ['2.38', '0.78']
w2.f10 | x | `flaws .` | 4.00 | ['5.30', '-1.16']
w2.f11 | x | `are below` | 2.95 | ['-1.10', '4.32']
w2.f12 |   | `scores are` | 2.92 | ['0.38', '2.57']
w2.f13 | x | `@@UNK@@ like` | 3.49 | ['0.61', '3.03']
w2.f14 |   | `like your` | 2.34 | ['0.54', '1.83']
w2.f15 | x | `the flaws` | 4.18 | ['-0.42', '4.86']
w2.f16 |   | `notice the` | 1.27 | ['1.20', '0.83']
w2.f17 | x | `might not` | 6.26 | ['4.29', '2.58']
w2.f18 |   | `might not` | 2.28 | ['1.58', '0.82']
w2.f19 |   | `below @@UNK@@` | 2.86 | ['5.31', '-2.15']
w3.f0 |   | `scores are below` | 3.30 | ['-3.67', '1.17', '6.19']
w3.f1 | x | `notice the flaws` | 4.31 | ['-1.61', '-0.57', '6.87']
w3.f2 | x | `you might not` | 4.60 | ['0.82', '-0.52', '4.40']
w3.f3 | x | `might not notice` | 3.05 | ['1.67', '0.66', '1.31']
w3.f4 | x | `@@UNK@@ scores are` | 5.26 | ['0.36', '1.75', '3.51']
w3.f5 | x | `the flaws .` | 6.57 | ['-0.36', '2.94', '4.32']
w3.f6 |   | `flaws . @@PAD@@` | 3.56 | ['2.70', '1.07', '0.00']
w3.f7 |   | `flaws . @@PAD@@` | 2.40 | ['3.16', '-0.27', '0.00']
w3.f8 |   | `below @@UNK@@ and` | 2.50 | ['5.80', '-0.27', '-2.75']
w3.f9 |   | `scores are below` | 2.74 | ['1.24', '1.41', '0.20']
w3.f10 | x | `@@UNK@@ scores are` | 5.73 | ['0.33', '1.77', '3.78']
w3.f11 |   | `you might not` | 2.92 | ['1.07', '1.91', '0.13']
w3.f12 | x | `@@PAD@@ @@UNK@@ like` | 4.62 | ['0.00', '-0.16', '4.91']
w3.f13 |   | `the flaws .` | 4.73 | ['4.70', '-2.16', '2.45']
w3.f14 | x | `@@PAD@@ @@UNK@@ like` | 6.34 | ['0.00', '0.79', '5.65']
w3.f15 |   | `scores are below` | 3.44 | ['2.61', '-0.67', '1.65']
w3.f16 |   | `notice the flaws` | 1.91 | ['-0.10', '0.10', '2.28']
w3.f17 |   | `@@PAD@@ @@UNK@@ like` | 1.17 | ['0.00', '1.39', '-0.06']
w3.f18 |   | `not notice the` | 3.19 | ['-2.36', '3.46', '2.57']
w3.f19 | x | `@@UNK@@ like your` | 4.21 | ['-0.26', '3.53', '1.05']

## Original input: 
``` there 's a reason the studio did n't offer an advance screening . " the adventures of @@UNK@@ @@UNK@@ " is a big time @@UNK@@ . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>there <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span>a reason the studio did <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>n't <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>offer <span style="background-color: #6698FF">@</span>an <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>advance <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>screening <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>" <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>adventures <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ " is <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>big <span style="background-color: #FFFF00">@</span>time @@UNK@@ .</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ "` | 2.77 | ['1.98', '1.16']
w2.f1 | x | `offer an` | 4.10 | ['1.70', '2.54']
w2.f2 |   | `big time` | 0.60 | ['0.21', '1.43']
w2.f3 |   | `advance screening` | 1.70 | ['2.62', '-0.36']
w2.f4 | x | `an advance` | 7.19 | ['5.09', '2.29']
w2.f5 | x | `an advance` | 4.36 | ['3.50', '1.16']
w2.f6 |   | `@@UNK@@ "` | 3.00 | ['0.07', '3.03']
w2.f7 |   | `adventures of` | 0.21 | ['1.62', '-0.50']
w2.f8 |   | `there 's` | 2.88 | ['-0.72', '3.82']
w2.f9 |   | `advance screening` | 3.46 | ['5.00', '-1.53']
w2.f10 | x | `" is` | 2.99 | ['3.21', '-0.08']
w2.f11 |   | `time @@UNK@@` | 2.32 | ['2.35', '0.25']
w2.f12 |   | `reason the` | 2.74 | ['1.46', '1.32']
w2.f13 | x | `did n't` | 5.11 | ['2.18', '3.08']
w2.f14 | x | `studio did` | 4.50 | ['1.67', '2.87']
w2.f15 |   | `advance screening` | 2.65 | ['0.74', '2.18']
w2.f16 | x | `an advance` | 2.69 | ['2.54', '0.91']
w2.f17 |   | `" is` | 2.18 | ['2.00', '0.80']
w2.f18 | x | `studio did` | 4.50 | ['2.49', '2.14']
w2.f19 |   | `studio did` | 1.32 | ['1.16', '0.46']
w3.f0 |   | `'s a reason` | 3.21 | ['-1.14', '3.29', '1.45']
w3.f1 |   | `is a big` | 1.52 | ['1.18', '-0.71', '1.43']
w3.f2 |   | `there 's a` | 3.51 | ['1.89', '-0.56', '2.27']
w3.f3 |   | `did n't offer` | 1.48 | ['-0.07', '2.63', '-0.48']
w3.f4 | x | `an advance screening` | 3.93 | ['1.31', '-0.03', '3.00']
w3.f5 |   | `advance screening .` | 4.74 | ['-0.30', '1.04', '4.32']
w3.f6 | x | `screening . "` | 5.55 | ['2.58', '1.07', '2.12']
w3.f7 |   | `an advance screening` | 2.90 | ['2.46', '1.41', '-0.47']
w3.f8 | x | `" is a` | 6.25 | ['2.28', '4.71', '-0.46']
w3.f9 | x | `@@PAD@@ @@PAD@@ there` | 4.23 | ['0.00', '0.00', '4.33']
w3.f10 |   | `screening . "` | 2.86 | ['-0.52', '2.00', '1.52']
w3.f11 |   | `n't offer an` | 3.65 | ['0.77', '3.35', '-0.27']
w3.f12 | x | `the adventures of` | 7.77 | ['2.43', '4.78', '0.69']
w3.f13 |   | `the studio did` | 5.13 | ['4.70', '0.98', '-0.30']
w3.f14 | x | `studio did n't` | 4.32 | ['1.68', '-0.89', '3.62']
w3.f15 | x | `n't offer an` | 5.71 | ['3.56', '1.64', '0.67']
w3.f16 |   | `reason the studio` | 3.31 | ['0.42', '0.10', '3.17']
w3.f17 |   | `studio did n't` | 3.86 | ['0.03', '-0.54', '4.52']
w3.f18 | x | `offer an advance` | 4.57 | ['4.32', '0.28', '0.43']
w3.f19 | x | `" is a` | 4.15 | ['1.28', '3.62', '-0.64']

## Original input: 
``` a penetrating glimpse into the @@UNK@@ - thin ego of the stand - up comic . ``` 

## Marked input: 
<pre>a penetrating glimpse into <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ - thin <span style="background-color: #6698FF">@</span>ego <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>stand <span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span>up <span style="background-color: #FFFF00">@</span>comic <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `up comic` | 4.65 | ['0.73', '4.29']
w2.f1 |   | `penetrating glimpse` | 3.22 | ['0.26', '3.09']
w2.f2 |   | `- up` | 0.36 | ['-0.18', '1.59']
w2.f3 |   | `a penetrating` | 2.04 | ['-0.30', '2.90']
w2.f4 |   | `a penetrating` | 2.76 | ['2.27', '0.68']
w2.f5 |   | `a penetrating` | 3.19 | ['0.71', '2.79']
w2.f6 |   | `a penetrating` | 2.72 | ['0.54', '2.28']
w2.f7 | x | `thin ego` | 4.35 | ['3.75', '1.50']
w2.f8 |   | `thin ego` | 2.42 | ['0.55', '2.09']
w2.f9 |   | `ego of` | 3.29 | ['1.65', '1.65']
w2.f10 | x | `- up` | 7.99 | ['1.18', '6.94']
w2.f11 | x | `ego of` | 3.72 | ['3.04', '0.95']
w2.f12 |   | `penetrating glimpse` | 2.04 | ['1.56', '0.52']
w2.f13 |   | `- up` | 2.66 | ['0.59', '2.23']
w2.f14 | x | `thin ego` | 5.45 | ['3.46', '2.02']
w2.f15 | x | `thin ego` | 6.11 | ['1.57', '4.80']
w2.f16 | x | `- thin` | 3.97 | ['-1.38', '6.11']
w2.f17 | x | `up comic` | 3.59 | ['3.03', '1.17']
w2.f18 | x | `glimpse into` | 3.38 | ['1.38', '2.12']
w2.f19 |   | `into the` | 2.10 | ['2.20', '0.20']
w3.f0 | x | `up comic .` | 5.43 | ['5.35', '0.10', '0.37']
w3.f1 |   | `a penetrating glimpse` | 3.03 | ['-1.76', '3.05', '2.13']
w3.f2 | x | `- thin ego` | 7.71 | ['2.02', '5.95', '-0.17']
w3.f3 |   | `- thin ego` | 1.32 | ['-0.10', '-0.43', '2.46']
w3.f4 |   | `penetrating glimpse into` | 3.02 | ['1.68', '-1.16', '2.85']
w3.f5 | x | `thin ego of` | 5.18 | ['-0.92', '6.90', '-0.47']
w3.f6 |   | `a penetrating glimpse` | 3.54 | ['1.76', '0.65', '1.34']
w3.f7 |   | `a penetrating glimpse` | 2.34 | ['-0.02', '0.14', '2.72']
w3.f8 |   | `thin ego of` | 1.82 | ['0.81', '1.35', '-0.05']
w3.f9 |   | `comic . @@PAD@@` | 1.76 | ['1.29', '0.58', '0.00']
w3.f10 | x | `thin ego of` | 5.24 | ['2.41', '2.90', '0.08']
w3.f11 | x | `up comic .` | 5.27 | ['4.68', '0.86', '-0.08']
w3.f12 | x | `thin ego of` | 4.57 | ['6.45', '-2.43', '0.69']
w3.f13 | x | `the stand -` | 7.65 | ['4.70', '2.33', '0.87']
w3.f14 | x | `- thin ego` | 4.81 | ['-0.66', '4.21', '1.36']
w3.f15 |   | `up comic .` | 3.43 | ['3.07', '1.14', '-0.60']
w3.f16 |   | `of the stand` | 3.45 | ['1.87', '0.10', '1.86']
w3.f17 | x | `up comic .` | 3.88 | ['2.46', '0.59', '0.98']
w3.f18 | x | `ego of the` | 6.34 | ['2.14', '2.10', '2.57']
w3.f19 |   | `stand - up` | 3.45 | ['2.34', '1.48', '-0.26']

## Original input: 
``` a spooky yarn of @@UNK@@ @@UNK@@ on the high seas that works better the less the brain is engaged . ``` 

## Marked input: 
<pre>a spooky <span style="background-color: #FFFF00">@</span>yarn <span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>on the high <span style="background-color: #6698FF">@</span>seas <span style="background-color: #6698FF">@</span>that <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>works <span style="background-color: #FFFF00">@</span>better <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>less <span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>brain <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>engaged <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `on the` | 1.37 | ['3.79', '-2.05']
w2.f1 | x | `spooky yarn` | 4.56 | ['2.73', '1.95']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `engaged .` | 1.06 | ['1.67', '-0.05']
w2.f4 | x | `that works` | 7.43 | ['1.54', '6.08']
w2.f5 | x | `spooky yarn` | 8.86 | ['5.39', '3.78']
w2.f6 |   | `works better` | 3.83 | ['2.98', '0.95']
w2.f7 |   | `less the` | 0.85 | ['1.95', '-0.19']
w2.f8 | x | `that works` | 4.16 | ['0.70', '3.68']
w2.f9 |   | `yarn of` | 3.62 | ['1.98', '1.65']
w2.f10 | x | `that works` | 7.07 | ['-0.46', '7.67']
w2.f11 | x | `yarn of` | 2.86 | ['2.18', '0.95']
w2.f12 |   | `the brain` | 2.88 | ['0.53', '2.38']
w2.f13 | x | `brain is` | 4.28 | ['3.93', '0.50']
w2.f14 | x | `high seas` | 4.76 | ['1.60', '3.19']
w2.f15 | x | `spooky yarn` | 6.03 | ['1.80', '4.50']
w2.f16 | x | `is engaged` | 3.81 | ['-0.10', '4.67']
w2.f17 |   | `engaged .` | 2.63 | ['2.78', '0.47']
w2.f18 | x | `works better` | 3.96 | ['3.36', '0.72']
w2.f19 | x | `better the` | 3.37 | ['3.47', '0.20']
w3.f0 | x | `less the brain` | 4.60 | ['8.00', '-2.31', '-0.70']
w3.f1 | x | `engaged . @@PAD@@` | 6.90 | ['7.63', '-0.35', '0.00']
w3.f2 |   | `@@PAD@@ @@PAD@@ a` | 2.19 | ['0.00', '0.00', '2.27']
w3.f3 |   | `brain is engaged` | 0.29 | ['0.76', '-0.61', '0.74']
w3.f4 | x | `the brain is` | 3.96 | ['-0.24', '2.09', '2.46']
w3.f5 | x | `seas that works` | 5.17 | ['2.32', '-0.14', '3.32']
w3.f6 |   | `seas that works` | 2.44 | ['2.43', '-1.33', '1.55']
w3.f7 |   | `that works better` | 2.54 | ['3.01', '0.01', '0.02']
w3.f8 | x | `brain is engaged` | 8.01 | ['2.95', '4.71', '0.64']
w3.f9 |   | `brain is engaged` | 3.20 | ['-1.90', '0.12', '5.08']
w3.f10 |   | `that works better` | 3.54 | ['-0.64', '2.19', '2.14']
w3.f11 |   | `@@PAD@@ @@PAD@@ a` | 2.59 | ['0.00', '0.00', '2.78']
w3.f12 | x | `the high seas` | 4.74 | ['2.43', '0.04', '2.39']
w3.f13 | x | `that works better` | 9.23 | ['2.51', '4.26', '2.70']
w3.f14 | x | `brain is engaged` | 5.20 | ['1.37', '0.90', '3.03']
w3.f15 |   | `high seas that` | 3.57 | ['3.07', '2.20', '-1.54']
w3.f16 | x | `a spooky yarn` | 5.57 | ['-0.19', '3.42', '2.72']
w3.f17 |   | `better the less` | 3.38 | ['0.97', '0.47', '2.09']
w3.f18 | x | `yarn of @@UNK@@` | 4.12 | ['2.72', '2.10', '-0.23']
w3.f19 | x | `a spooky yarn` | 8.86 | ['3.70', '3.54', '1.74']

## Original input: 
``` a movie that will touch the hearts of both children and adults , as well as bring audiences to the edge of their seats . ``` 

## Marked input: 
<pre>a movie <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>will <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>touch <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hearts <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>both <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>children <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>adults <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>as <span style="background-color: #FFFF00">@</span>well as bring audiences to the <span style="background-color: #FFFF00">@</span>edge <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>their <span style="background-color: #FFFF00">@</span>seats <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `their seats` | 3.54 | ['4.53', '-0.61']
w2.f1 | x | `a movie` | 3.76 | ['2.95', '0.94']
w2.f2 |   | `as bring` | 0.17 | ['0.54', '0.68']
w2.f3 |   | `a movie` | 0.63 | ['-0.30', '1.49']
w2.f4 | x | `hearts of` | 3.96 | ['4.70', '-0.55']
w2.f5 | x | `hearts of` | 4.30 | ['2.84', '1.76']
w2.f6 |   | `will touch` | 3.22 | ['2.71', '0.61']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `@@PAD@@ a` | 2.34 | ['0.00', '2.56']
w2.f9 |   | `edge of` | 3.50 | ['1.86', '1.65']
w2.f10 | x | `adults ,` | 3.13 | ['3.63', '-0.37']
w2.f11 | x | `touch the` | 3.03 | ['2.88', '0.42']
w2.f12 |   | `to the` | 2.81 | ['1.53', '1.32']
w2.f13 |   | `well as` | 2.28 | ['1.12', '1.31']
w2.f14 |   | `the edge` | 2.93 | ['0.10', '2.86']
w2.f15 |   | `well as` | 0.99 | ['2.74', '-1.48']
w2.f16 |   | `their seats` | 1.65 | ['-0.41', '2.82']
w2.f17 | x | `seats .` | 3.45 | ['3.59', '0.47']
w2.f18 | x | `will touch` | 4.51 | ['1.88', '2.76']
w2.f19 | x | `of their` | 3.72 | ['1.68', '2.34']
w3.f0 |   | `movie that will` | 2.85 | ['1.92', '-0.36', '1.68']
w3.f1 | x | `to the edge` | 3.96 | ['-0.45', '-0.57', '5.37']
w3.f2 |   | `edge of their` | 3.46 | ['2.38', '-0.92', '2.09']
w3.f3 |   | `will touch the` | 1.01 | ['1.00', '2.65', '-2.04']
w3.f4 |   | `will touch the` | 3.32 | ['1.67', '2.38', '-0.38']
w3.f5 | x | `both children and` | 6.92 | ['1.63', '-0.19', '5.81']
w3.f6 | x | `a movie that` | 7.23 | ['1.76', '4.49', '1.19']
w3.f7 | x | `of their seats` | 4.19 | ['0.84', '3.65', '0.19']
w3.f8 | x | `that will touch` | 7.61 | ['3.58', '1.17', '3.14']
w3.f9 | x | `both children and` | 4.19 | ['0.52', '1.37', '2.40']
w3.f10 |   | `seats . @@PAD@@` | 3.04 | ['1.18', '2.00', '0.00']
w3.f11 |   | `@@PAD@@ @@PAD@@ a` | 2.59 | ['0.00', '0.00', '2.78']
w3.f12 | x | `hearts of both` | 5.64 | ['0.28', '3.24', '2.25']
w3.f13 | x | `the edge of` | 10.87 | ['4.70', '3.72', '2.71']
w3.f14 |   | `to the edge` | 1.50 | ['-0.10', '-0.32', '2.01']
w3.f15 |   | `, as well` | 1.68 | ['1.52', '0.23', '0.10']
w3.f16 | x | `to the edge` | 4.88 | ['1.59', '0.10', '3.57']
w3.f17 |   | `children and adults` | 2.72 | ['0.83', '1.30', '0.75']
w3.f18 | x | `touch the hearts` | 4.26 | ['2.90', '-0.59', '2.42']
w3.f19 | x | `edge of their` | 4.52 | ['4.28', '-1.61', '1.96']

## Original input: 
``` it 's exactly what you 'd expect . ``` 

## Marked input: 
<pre>it 's exactly what <span style="background-color: #6698FF">@</span>you <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>'d <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>expect <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@PAD@@ it` | 1.30 | ['0.00', '1.67']
w2.f1 |   | `exactly what` | 3.39 | ['0.47', '3.05']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f4 |   | `you 'd` | 1.59 | ['2.00', '-0.21']
w2.f5 | x | `what you` | 3.90 | ['2.99', '1.22']
w2.f6 |   | `'s exactly` | 0.89 | ['1.03', '-0.04']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 |   | `expect .` | 1.71 | ['1.27', '0.46']
w2.f10 | x | `you 'd` | 3.22 | ['4.16', '-0.81']
w2.f11 | x | `you 'd` | 3.16 | ['1.83', '1.60']
w2.f12 |   | `@@PAD@@ it` | 0.92 | ['0.00', '0.96']
w2.f13 |   | `what you` | 1.18 | ['-0.20', '1.53']
w2.f14 | x | `exactly what` | 3.72 | ['3.11', '0.65']
w2.f15 | x | `what you` | 8.27 | ['2.55', '5.99']
w2.f16 |   | `'d expect` | 0.43 | ['1.58', '-0.39']
w2.f17 |   | `'s exactly` | 0.77 | ['0.09', '1.30']
w2.f18 |   | `@@PAD@@ it` | 0.97 | ['0.00', '1.09']
w2.f19 |   | `'d expect` | 0.64 | ['1.29', '-0.35']
w3.f0 | x | `what you 'd` | 4.43 | ['0.03', '1.60', '3.20']
w3.f1 |   | `@@PAD@@ @@PAD@@ it` | 0.00 | ['0.00', '0.00', '-3.16']
w3.f2 |   | `@@PAD@@ it 's` | 1.72 | ['0.00', '1.70', '0.11']
w3.f3 | x | `you 'd expect` | 2.46 | ['0.34', '0.36', '2.36']
w3.f4 |   | `what you 'd` | 2.98 | ['0.34', '0.38', '2.62']
w3.f5 |   | `'d expect .` | 3.90 | ['-1.77', '1.68', '4.32']
w3.f6 |   | `you 'd expect` | 2.43 | ['2.54', '0.47', '-0.37']
w3.f7 |   | `you 'd expect` | 1.20 | ['-2.15', '-0.68', '4.52']
w3.f8 |   | `it 's exactly` | 1.99 | ['2.11', '0.26', '-0.09']
w3.f9 |   | `expect . @@PAD@@` | 1.84 | ['1.37', '0.58', '0.00']
w3.f10 |   | `expect . @@PAD@@` | 2.59 | ['0.73', '2.00', '0.00']
w3.f11 | x | `exactly what you` | 4.54 | ['3.21', '0.18', '1.34']
w3.f12 |   | `it 's exactly` | 1.14 | ['0.79', '-0.83', '1.30']
w3.f13 |   | `exactly what you` | 2.62 | ['1.02', '0.75', '1.10']
w3.f14 | x | `exactly what you` | 4.06 | ['4.16', '0.05', '-0.05']
w3.f15 |   | `what you 'd` | 3.65 | ['-2.50', '2.14', '4.17']
w3.f16 |   | `you 'd expect` | 2.53 | ['0.17', '-0.86', '3.59']
w3.f17 |   | `@@PAD@@ @@PAD@@ it` | 0.00 | ['0.00', '0.00', '-1.37']
w3.f18 |   | `@@PAD@@ @@PAD@@ it` | 0.00 | ['0.00', '0.00', '-1.03']
w3.f19 | x | `what you 'd` | 4.15 | ['2.83', '0.78', '0.65']

## Original input: 
``` though the book runs only about 300 @@UNK@@ , it is so @@UNK@@ packed . . . that even an ambitious adaptation and elaborate production like mr . @@UNK@@ 's seems @@UNK@@ and @@UNK@@ . ``` 

## Marked input: 
<pre>though the book <span style="background-color: #FFFF00">@</span>runs <span style="background-color: #FFFF00">@</span>only <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>about <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>300 <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>it <span style="background-color: #6698FF">@</span>is so @@UNK@@ <span style="background-color: #FFFF00">@</span>packed <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>. that <span style="background-color: #6698FF">@</span>even <span style="background-color: #6698FF">@</span>an <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>ambitious <span style="background-color: #FFFF00">@</span>adaptation <span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>elaborate <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>production <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>like <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>mr <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>@@UNK@@ 's <span style="background-color: #FFFF00">@</span>seems <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `ambitious adaptation` | 2.45 | ['1.05', '1.77']
w2.f1 | x | `ambitious adaptation` | 4.85 | ['1.18', '3.81']
w2.f2 |   | `ambitious adaptation` | 0.53 | ['1.08', '0.49']
w2.f3 |   | `elaborate production` | 1.73 | ['2.13', '0.16']
w2.f4 | x | `an ambitious` | 5.38 | ['5.09', '0.48']
w2.f5 | x | `like mr` | 4.75 | ['3.40', '1.66']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `adaptation and` | 0.94 | ['1.76', '0.09']
w2.f8 | x | `@@UNK@@ 's` | 3.81 | ['0.21', '3.82']
w2.f9 | x | `production like` | 5.71 | ['4.93', '0.78']
w2.f10 | x | `'s seems` | 4.46 | ['2.75', '1.85']
w2.f11 | x | `adaptation and` | 4.02 | ['4.02', '0.27']
w2.f12 | x | `elaborate production` | 5.00 | ['2.96', '2.09']
w2.f13 | x | `only about` | 5.81 | ['6.80', '-0.84']
w2.f14 | x | `runs only` | 5.54 | ['-0.36', '5.93']
w2.f15 | x | `'s seems` | 5.82 | ['1.82', '4.27']
w2.f16 |   | `an ambitious` | 1.94 | ['2.54', '0.16']
w2.f17 |   | `seems @@UNK@@` | 2.23 | ['3.94', '-1.09']
w2.f18 | x | `ambitious adaptation` | 4.60 | ['3.13', '1.59']
w2.f19 | x | `ambitious adaptation` | 3.34 | ['1.22', '2.42']
w3.f0 | x | `seems @@UNK@@ and` | 5.50 | ['4.55', '0.35', '0.99']
w3.f1 |   | `even an ambitious` | 3.44 | ['-0.52', '1.98', '2.36']
w3.f2 |   | `'s seems @@UNK@@` | 3.30 | ['0.87', '2.84', '-0.31']
w3.f3 | x | `so @@UNK@@ packed` | 3.80 | ['-0.30', '-0.06', '4.76']
w3.f4 | x | `even an ambitious` | 3.61 | ['3.48', '0.82', '-0.33']
w3.f5 | x | `@@UNK@@ packed .` | 6.82 | ['0.08', '2.75', '4.32']
w3.f6 | x | `'s seems @@UNK@@` | 3.86 | ['3.62', '0.30', '0.15']
w3.f7 |   | `even an ambitious` | 2.25 | ['0.36', '-0.17', '2.55']
w3.f8 | x | `and elaborate production` | 7.77 | ['2.47', '2.63', '2.95']
w3.f9 | x | `. that even` | 5.03 | ['0.67', '1.05', '3.42']
w3.f10 |   | `mr . @@UNK@@` | 3.78 | ['1.06', '2.00', '0.86']
w3.f11 |   | `ambitious adaptation and` | 3.01 | ['1.19', '1.43', '0.58']
w3.f12 | x | `adaptation and elaborate` | 6.01 | ['0.88', '0.95', '4.31']
w3.f13 | x | `the book runs` | 6.78 | ['4.70', '-1.98', '4.31']
w3.f14 | x | `elaborate production like` | 7.91 | ['0.77', '1.59', '5.65']
w3.f15 | x | `300 @@UNK@@ ,` | 4.49 | ['3.64', '-1.69', '2.70']
w3.f16 | x | `so @@UNK@@ packed` | 5.16 | ['2.05', '-0.81', '4.29']
w3.f17 | x | `seems @@UNK@@ and` | 6.00 | ['4.91', '1.39', '-0.15']
w3.f18 | x | `book runs only` | 5.05 | ['3.62', '3.43', '-1.53']
w3.f19 | x | `and elaborate production` | 7.64 | ['3.50', '2.01', '2.25']

## Original input: 
``` thanks to haynes ' absolute control of the film 's mood , and @@UNK@@ by three terrific performances , far from heaven actually pulls off this stylistic @@UNK@@ act . ``` 

## Marked input: 
<pre>thanks to <span style="background-color: #FFFF00">@</span>haynes <span style="background-color: #FFFF00">@</span>' <span style="background-color: #FFFF00">@</span>absolute <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>control <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>film <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span>mood <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>by three <span style="background-color: #FFFF00">@</span>terrific <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>performances <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>far <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>from <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>heaven <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>actually <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>pulls <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>off <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>this <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>stylistic <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>act .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ act` | 3.42 | ['1.98', '1.82']
w2.f1 |   | `heaven actually` | 3.61 | ['4.98', '-1.24']
w2.f2 |   | `heaven actually` | 0.43 | ['1.28', '0.20']
w2.f3 | x | `heaven actually` | 2.63 | ['0.87', '2.31']
w2.f4 |   | `'s mood` | 3.53 | ['-0.76', '4.47']
w2.f5 | x | `pulls off` | 8.96 | ['8.20', '1.06']
w2.f6 | x | `haynes '` | 4.78 | ['3.28', '1.60']
w2.f7 |   | `control of` | 1.32 | ['2.73', '-0.50']
w2.f8 |   | `haynes '` | 2.79 | ['2.75', '0.25']
w2.f9 |   | `off this` | 4.82 | ['4.76', '0.07']
w2.f10 | x | `'s mood` | 6.86 | ['2.75', '4.24']
w2.f11 | x | `absolute control` | 3.45 | ['-0.35', '4.07']
w2.f12 | x | `off this` | 3.96 | ['1.24', '2.76']
w2.f13 | x | `pulls off` | 4.78 | ['2.28', '2.65']
w2.f14 | x | `pulls off` | 3.53 | ['-0.91', '4.47']
w2.f15 | x | `terrific performances` | 3.40 | ['3.15', '0.52']
w2.f16 | x | `absolute control` | 7.02 | ['2.87', '4.91']
w2.f17 | x | `three terrific` | 3.28 | ['3.86', '0.04']
w2.f18 | x | `thanks to` | 5.99 | ['3.62', '2.50']
w2.f19 | x | `thanks to` | 4.83 | ['4.00', '1.12']
w3.f0 | x | `off this stylistic` | 5.56 | ['1.18', '1.65', '3.12']
w3.f1 | x | `, far from` | 5.90 | ['1.74', '0.46', '4.08']
w3.f2 | x | `actually pulls off` | 6.71 | ['4.70', '-0.81', '2.91']
w3.f3 | x | `three terrific performances` | 3.14 | ['0.56', '1.59', '1.60']
w3.f4 | x | `by three terrific` | 6.26 | ['1.87', '2.27', '2.48']
w3.f5 | x | `mood , and` | 8.16 | ['1.28', '1.40', '5.81']
w3.f6 |   | `performances , far` | 3.12 | ['0.94', '0.38', '2.01']
w3.f7 | x | `, far from` | 4.70 | ['1.70', '0.09', '3.40']
w3.f8 | x | `heaven actually pulls` | 5.95 | ['6.96', '-1.43', '0.71']
w3.f9 |   | `actually pulls off` | 3.53 | ['0.57', '1.21', '1.86']
w3.f10 | x | `of the film` | 4.11 | ['2.92', '-1.03', '2.36']
w3.f11 | x | `from heaven actually` | 7.26 | ['4.70', '-0.87', '3.62']
w3.f12 | x | `' absolute control` | 7.06 | ['-2.07', '2.38', '6.88']
w3.f13 | x | `haynes ' absolute` | 7.24 | ['0.00', '4.49', '2.99']
w3.f14 | x | `from heaven actually` | 7.49 | ['2.08', '0.51', '4.99']
w3.f15 | x | `, far from` | 6.66 | ['1.52', '2.49', '2.82']
w3.f16 | x | `thanks to haynes` | 6.33 | ['2.91', '-0.49', '4.29']
w3.f17 | x | `three terrific performances` | 4.25 | ['2.78', '-0.27', '1.90']
w3.f18 | x | `terrific performances ,` | 5.53 | ['4.58', '0.63', '0.79']
w3.f19 | x | `three terrific performances` | 10.27 | ['1.17', '7.12', '2.10']

## Original input: 
``` a feel - good movie that does n't give you enough to feel good about . ``` 

## Marked input: 
<pre>a feel <span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span>good <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>movie <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>does <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>n't <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>give <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>you <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>enough <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>feel <span style="background-color: #6698FF">@</span>good <span style="background-color: #FFFF00">@</span>about <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `you enough` | 3.67 | ['1.93', '2.12']
w2.f1 |   | `a feel` | 1.57 | ['2.95', '-1.25']
w2.f2 |   | `give you` | 0.40 | ['1.18', '0.26']
w2.f3 |   | `give you` | 0.85 | ['0.28', '1.13']
w2.f4 | x | `a feel` | 4.79 | ['2.27', '2.71']
w2.f5 | x | `a feel` | 3.32 | ['0.71', '2.92']
w2.f6 |   | `movie that` | 2.60 | ['1.65', '1.05']
w2.f7 |   | `does n't` | 0.24 | ['1.64', '-0.49']
w2.f8 | x | `give you` | 5.63 | ['1.70', '4.14']
w2.f9 | x | `enough to` | 6.85 | ['2.20', '4.67']
w2.f10 | x | `feel good` | 4.30 | ['1.38', '3.06']
w2.f11 |   | `does n't` | 2.50 | ['2.97', '-0.19']
w2.f12 |   | `that does` | 2.07 | ['1.55', '0.56']
w2.f13 |   | `does n't` | 2.27 | ['-0.66', '3.08']
w2.f14 |   | `does n't` | 1.84 | ['-0.44', '2.31']
w2.f15 | x | `give you` | 4.31 | ['-1.41', '5.99']
w2.f16 |   | `that does` | 1.89 | ['-0.95', '3.60']
w2.f17 |   | `that does` | 1.39 | ['0.08', '1.92']
w2.f18 |   | `enough to` | 3.03 | ['0.66', '2.50']
w2.f19 | x | `- good` | 3.99 | ['0.44', '3.85']
w3.f0 |   | `give you enough` | 2.64 | ['1.31', '1.60', '0.12']
w3.f1 | x | `good movie that` | 4.73 | ['0.34', '2.75', '2.02']
w3.f2 | x | `- good movie` | 3.93 | ['2.02', '-1.93', '3.93']
w3.f3 | x | `does n't give` | 3.79 | ['0.69', '2.63', '1.07']
w3.f4 |   | `give you enough` | 2.54 | ['0.01', '0.38', '2.51']
w3.f5 | x | `good about .` | 5.69 | ['0.93', '0.77', '4.32']
w3.f6 | x | `n't give you` | 5.53 | ['3.72', '0.27', '1.75']
w3.f7 | x | `does n't give` | 8.88 | ['2.39', '1.99', '5.00']
w3.f8 |   | `enough to feel` | 0.82 | ['1.75', '1.89', '-2.53']
w3.f9 |   | `@@PAD@@ @@PAD@@ a` | 1.03 | ['0.00', '0.00', '1.13']
w3.f10 |   | `about . @@PAD@@` | 2.89 | ['1.04', '2.00', '0.00']
w3.f11 |   | `n't give you` | 2.75 | ['0.77', '0.83', '1.34']
w3.f12 |   | `feel - good` | 2.73 | ['2.39', '2.81', '-2.34']
w3.f13 |   | `feel good about` | 2.31 | ['-0.48', '3.04', '-0.01']
w3.f14 |   | `that does n't` | 2.80 | ['-0.45', '-0.28', '3.62']
w3.f15 | x | `give you enough` | 4.39 | ['0.79', '2.14', '1.63']
w3.f16 | x | `give you enough` | 6.48 | ['1.17', '0.70', '4.99']
w3.f17 | x | `that does n't` | 6.32 | ['-0.73', '2.70', '4.52']
w3.f18 |   | `feel - good` | 2.99 | ['-1.14', '0.97', '3.62']
w3.f19 | x | `n't give you` | 4.62 | ['1.55', '0.94', '2.24']

## Original input: 
``` ' no es la @@UNK@@ cinta de la @@UNK@@ , @@UNK@@ la @@UNK@@ con brosnan a la @@UNK@@ , @@UNK@@ de que @@UNK@@ @@UNK@@ @@UNK@@ @@UNK@@ . ' ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>' <span style="background-color: #6698FF">@</span>no <span style="background-color: #6698FF">@</span>es <span style="background-color: #6698FF">@</span>la <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>cinta <span style="background-color: #6698FF">@</span>de <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>la <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, @@UNK@@ la @@UNK@@ con brosnan <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>la <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>, @@UNK@@ de <span style="background-color: #FFFF00">@</span>que <span style="background-color: #FFFF00">@</span>@@UNK@@ @@UNK@@ @@UNK@@ @@UNK@@ . '</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ de` | 4.51 | ['1.98', '2.90']
w2.f1 | x | `a la` | 3.79 | ['2.95', '0.97']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `. '` | 1.46 | ['0.52', '1.49']
w2.f4 |   | `' no` | 3.27 | ['1.10', '2.36']
w2.f5 | x | `cinta de` | 4.45 | ['2.16', '2.60']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `de que` | 0.82 | ['0.16', '1.56']
w2.f8 | x | `brosnan a` | 3.55 | ['1.20', '2.56']
w2.f9 |   | `' no` | 4.84 | ['2.80', '2.06']
w2.f10 | x | `a la` | 4.56 | ['1.97', '2.72']
w2.f11 | x | `con brosnan` | 3.29 | ['0.42', '3.14']
w2.f12 |   | `de que` | 2.57 | ['0.69', '1.92']
w2.f13 | x | `cinta de` | 4.15 | ['3.93', '0.37']
w2.f14 | x | `' no` | 5.62 | ['-0.62', '6.27']
w2.f15 |   | `' @@PAD@@` | 2.53 | ['2.81', '0.00']
w2.f16 | x | `cinta de` | 4.79 | ['4.67', '0.88']
w2.f17 |   | `' @@PAD@@` | 2.42 | ['3.04', '0.00']
w2.f18 |   | `cinta de` | 2.82 | ['2.15', '0.79']
w2.f19 | x | `a la` | 3.44 | ['0.99', '2.75']
w3.f0 | x | `la @@UNK@@ cinta` | 4.47 | ['-0.35', '0.35', '4.86']
w3.f1 |   | `, @@UNK@@ de` | 3.59 | ['1.74', '-0.73', '2.96']
w3.f2 |   | `' no es` | 3.26 | ['1.19', '2.06', '0.11']
w3.f3 |   | `@@UNK@@ de que` | 0.99 | ['-1.16', '1.50', '1.26']
w3.f4 |   | `brosnan a la` | 3.25 | ['0.43', '0.29', '2.88']
w3.f5 |   | `cinta de la` | 3.06 | ['-0.10', '1.23', '2.25']
w3.f6 |   | `@@UNK@@ cinta de` | 3.33 | ['-0.28', '2.29', '1.52']
w3.f7 |   | `con brosnan a` | 0.95 | ['0.90', '1.36', '-0.82']
w3.f8 | x | `cinta de la` | 5.18 | ['0.97', '5.66', '-1.16']
w3.f9 | x | `@@PAD@@ @@PAD@@ '` | 5.12 | ['0.00', '0.00', '5.23']
w3.f10 |   | `de la @@UNK@@` | 3.15 | ['1.48', '0.97', '0.86']
w3.f11 | x | `' no es` | 4.90 | ['0.98', '2.82', '1.30']
w3.f12 | x | `no es la` | 5.92 | ['4.16', '0.53', '1.35']
w3.f13 |   | `. ' @@PAD@@` | 3.48 | ['-0.76', '4.49', '0.00']
w3.f14 | x | `' no es` | 6.80 | ['1.53', '4.41', '0.95']
w3.f15 |   | `@@PAD@@ @@PAD@@ '` | 1.66 | ['0.00', '0.00', '1.82']
w3.f16 |   | `' no es` | 2.74 | ['1.80', '1.53', '-0.20']
w3.f17 | x | `cinta de la` | 10.79 | ['6.72', '2.09', '2.14']
w3.f18 | x | `brosnan a la` | 3.99 | ['2.70', '-0.07', '1.82']
w3.f19 |   | `cinta de la` | 2.86 | ['1.87', '1.34', '-0.24']

## Original input: 
``` works better in the conception than it does in the execution . . . winds up seeming just a little too clever . ``` 

## Marked input: 
<pre>works <span style="background-color: #FFFF00">@</span>better <span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>conception than it does in the execution . . . winds <span style="background-color: #6698FF">@</span>up <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>seeming <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>just <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>little <span style="background-color: #6698FF">@</span>too <span style="background-color: #6698FF">@</span>clever <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `it does` | 2.45 | ['-0.89', '3.71']
w2.f1 |   | `too clever` | 3.48 | ['-0.68', '4.29']
w2.f2 |   | `too clever` | 0.40 | ['0.04', '1.41']
w2.f3 | x | `little too` | 3.16 | ['-0.37', '4.09']
w2.f4 | x | `@@PAD@@ works` | 5.89 | ['0.00', '6.08']
w2.f5 | x | `works better` | 5.26 | ['4.97', '0.59']
w2.f6 |   | `works better` | 3.83 | ['2.98', '0.95']
w2.f7 | x | `winds up` | 3.27 | ['3.15', '1.03']
w2.f8 | x | `@@PAD@@ works` | 3.46 | ['0.00', '3.68']
w2.f9 | x | `clever .` | 5.35 | ['4.90', '0.46']
w2.f10 | x | `@@PAD@@ works` | 7.54 | ['0.00', '7.67']
w2.f11 | x | `. winds` | 5.31 | ['-0.51', '6.09']
w2.f12 | x | `too clever` | 6.86 | ['1.83', '5.07']
w2.f13 | x | `winds up` | 3.30 | ['1.22', '2.23']
w2.f14 | x | `too clever` | 3.62 | ['-1.57', '5.22']
w2.f15 | x | `works better` | 4.28 | ['3.10', '1.45']
w2.f16 |   | `little too` | 2.12 | ['1.14', '1.74']
w2.f17 | x | `winds up` | 4.41 | ['5.71', '-0.68']
w2.f18 | x | `works better` | 3.96 | ['3.36', '0.72']
w2.f19 |   | `works better` | 3.02 | ['1.62', '1.69']
w3.f0 | x | `winds up seeming` | 12.40 | ['6.58', '2.80', '3.41']
w3.f1 | x | `winds up seeming` | 5.08 | ['2.88', '-1.72', '4.30']
w3.f2 | x | `a little too` | 4.93 | ['1.87', '2.64', '0.50']
w3.f3 |   | `it does in` | 0.38 | ['-0.74', '1.99', '-0.25']
w3.f4 |   | `@@PAD@@ @@PAD@@ works` | 1.45 | ['0.00', '0.00', '1.81']
w3.f5 | x | `too clever .` | 8.22 | ['-0.36', '4.58', '4.32']
w3.f6 |   | `little too clever` | 2.57 | ['-1.56', '4.25', '0.09']
w3.f7 |   | `in the execution` | 0.86 | ['1.23', '-0.92', '1.05']
w3.f8 |   | `@@PAD@@ works better` | 4.04 | ['0.00', '3.44', '0.88']
w3.f9 | x | `little too clever` | 4.11 | ['1.00', '2.90', '0.32']
w3.f10 | x | `just a little` | 6.78 | ['3.43', '1.32', '2.18']
w3.f11 | x | `seeming just a` | 5.26 | ['1.49', '1.18', '2.78']
w3.f12 | x | `too clever .` | 6.19 | ['4.03', '0.69', '1.61']
w3.f13 | x | `@@PAD@@ works better` | 6.72 | ['0.00', '4.26', '2.70']
w3.f14 | x | `little too clever` | 5.97 | ['0.42', '3.69', '1.96']
w3.f15 | x | `up seeming just` | 3.95 | ['3.07', '-0.50', '1.55']
w3.f16 | x | `works better in` | 8.77 | ['5.15', '3.55', '0.44']
w3.f17 | x | `little too clever` | 4.69 | ['2.61', '2.80', '-0.56']
w3.f18 |   | `up seeming just` | 1.09 | ['-0.23', '0.83', '0.95']
w3.f19 | x | `@@PAD@@ works better` | 5.24 | ['0.00', '3.44', '1.92']

## Original input: 
``` it is interesting and fun to see @@UNK@@ and her @@UNK@@ on the bigger - than - life screen . ``` 

## Marked input: 
<pre>it is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>interesting <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>fun <span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span>see <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>her @@UNK@@ on the bigger <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>than <span style="background-color: #6698FF">@</span>- life <span style="background-color: #FFFF00">@</span>screen <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `on the` | 1.37 | ['3.79', '-2.05']
w2.f1 | x | `- life` | 3.91 | ['-0.88', '4.92']
w2.f2 |   | `life screen` | 0.35 | ['1.02', '0.37']
w2.f3 | x | `is interesting` | 2.45 | ['0.28', '2.72']
w2.f4 |   | `and fun` | 2.15 | ['-1.73', '4.07']
w2.f5 |   | `fun to` | 1.97 | ['-0.12', '2.39']
w2.f6 |   | `and her` | 0.95 | ['-0.03', '1.08']
w2.f7 |   | `life screen` | 1.00 | ['1.05', '0.85']
w2.f8 |   | `screen .` | 2.55 | ['4.11', '-1.35']
w2.f9 |   | `fun to` | 2.97 | ['-1.69', '4.67']
w2.f10 |   | `life screen` | 2.21 | ['2.33', '0.01']
w2.f11 |   | `her @@UNK@@` | 1.39 | ['1.41', '0.25']
w2.f12 | x | `the bigger` | 3.63 | ['0.53', '3.13']
w2.f13 |   | `screen .` | 1.89 | ['2.03', '0.01']
w2.f14 | x | `bigger -` | 4.26 | ['3.96', '0.33']
w2.f15 |   | `is interesting` | 2.43 | ['1.15', '1.55']
w2.f16 |   | `see @@UNK@@` | 0.50 | ['1.80', '-0.54']
w2.f17 | x | `life screen` | 4.61 | ['0.29', '4.93']
w2.f18 | x | `fun to` | 5.67 | ['3.29', '2.50']
w2.f19 | x | `and fun` | 6.09 | ['3.66', '2.72']
w3.f0 | x | `life screen .` | 4.54 | ['3.65', '0.90', '0.37']
w3.f1 | x | `fun to see` | 8.05 | ['3.19', '0.48', '4.76']
w3.f2 |   | `- life screen` | 2.47 | ['2.02', '0.10', '0.44']
w3.f3 |   | `her @@UNK@@ on` | 1.47 | ['1.56', '-0.06', '0.57']
w3.f4 |   | `life screen .` | 3.31 | ['0.90', '3.29', '-0.52']
w3.f5 | x | `is interesting and` | 5.95 | ['0.80', '-0.34', '5.81']
w3.f6 | x | `screen . @@PAD@@` | 4.30 | ['3.44', '1.07', '0.00']
w3.f7 | x | `to see @@UNK@@` | 4.80 | ['3.76', '1.61', '-0.07']
w3.f8 | x | `it is interesting` | 6.37 | ['2.11', '4.71', '-0.16']
w3.f9 | x | `screen . @@PAD@@` | 6.12 | ['5.65', '0.58', '0.00']
w3.f10 |   | `screen . @@PAD@@` | 2.94 | ['1.09', '2.00', '0.00']
w3.f11 | x | `life screen .` | 5.74 | ['2.17', '3.84', '-0.08']
w3.f12 |   | `is interesting and` | 3.63 | ['0.69', '1.93', '1.15']
w3.f13 | x | `it is interesting` | 5.95 | ['2.60', '2.81', '0.79']
w3.f14 | x | `it is interesting` | 3.64 | ['0.08', '0.90', '2.75']
w3.f15 |   | `fun to see` | 0.97 | ['0.29', '-0.50', '1.34']
w3.f16 | x | `fun to see` | 7.92 | ['5.88', '-0.49', '2.91']
w3.f17 | x | `it is interesting` | 5.46 | ['1.06', '2.35', '2.20']
w3.f18 | x | `- life screen` | 4.07 | ['-1.68', '4.78', '1.43']
w3.f19 |   | `and fun to` | 3.44 | ['3.50', '1.11', '-1.05']

## Original input: 
``` while @@UNK@@ frustratingly refuses to give @@UNK@@ 's crimes a political context , his distance from the material is mostly admirable . ``` 

## Marked input: 
<pre>while @@UNK@@ frustratingly refuses <span style="background-color: #6698FF">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>give <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>crimes <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>political <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>context <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>his <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>distance from the <span style="background-color: #6698FF">@</span>material <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>mostly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>admirable <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ frustratingly` | 3.60 | ['1.98', '2.00']
w2.f1 | x | `a political` | 5.34 | ['2.95', '2.52']
w2.f2 |   | `frustratingly refuses` | 0.39 | ['0.40', '1.03']
w2.f3 | x | `frustratingly refuses` | 4.79 | ['1.62', '3.73']
w2.f4 | x | `political context` | 6.89 | ['6.16', '0.92']
w2.f5 | x | `political context` | 6.21 | ['6.86', '-0.35']
w2.f6 |   | `political context` | 3.27 | ['2.00', '1.37']
w2.f7 | x | `frustratingly refuses` | 2.84 | ['2.43', '1.32']
w2.f8 | x | `@@UNK@@ 's` | 3.81 | ['0.21', '3.82']
w2.f9 |   | `, his` | 3.36 | ['0.68', '2.69']
w2.f10 | x | `'s crimes` | 4.28 | ['2.75', '1.67']
w2.f11 | x | `mostly admirable` | 7.45 | ['2.41', '5.31']
w2.f12 |   | `'s crimes` | 3.27 | ['0.44', '2.86']
w2.f13 | x | `context ,` | 4.77 | ['2.74', '2.18']
w2.f14 | x | `political context` | 3.68 | ['-0.99', '4.70']
w2.f15 |   | `is mostly` | 3.03 | ['1.15', '2.15']
w2.f16 | x | `mostly admirable` | 4.98 | ['1.75', '3.99']
w2.f17 |   | `admirable .` | 2.05 | ['2.20', '0.47']
w2.f18 |   | `refuses to` | 2.23 | ['-0.15', '2.50']
w2.f19 |   | `distance from` | 2.27 | ['1.38', '1.19']
w3.f0 |   | `his distance from` | 3.06 | ['0.93', '1.58', '0.94']
w3.f1 |   | `his distance from` | 3.48 | ['-1.06', '0.84', '4.08']
w3.f2 | x | `'s crimes a` | 4.43 | ['0.87', '1.38', '2.27']
w3.f3 |   | `while @@UNK@@ frustratingly` | 1.15 | ['1.73', '-0.06', '0.08']
w3.f4 |   | `the material is` | 3.22 | ['-0.24', '1.35', '2.46']
w3.f5 | x | `is mostly admirable` | 5.33 | ['0.80', '1.22', '3.63']
w3.f6 |   | `@@PAD@@ while @@UNK@@` | 2.50 | ['0.00', '2.55', '0.15']
w3.f7 | x | `refuses to give` | 7.09 | ['1.41', '1.18', '5.00']
w3.f8 | x | `material is mostly` | 6.50 | ['0.58', '4.71', '1.50']
w3.f9 | x | `frustratingly refuses to` | 7.75 | ['2.71', '5.53', '-0.38']
w3.f10 |   | `admirable . @@PAD@@` | 3.79 | ['1.93', '2.00', '0.00']
w3.f11 | x | `from the material` | 8.10 | ['4.70', '-0.67', '4.27']
w3.f12 | x | `is mostly admirable` | 8.13 | ['0.69', '2.96', '4.61']
w3.f13 |   | `material is mostly` | 2.91 | ['-0.86', '2.81', '1.21']
w3.f14 | x | `the material is` | 6.96 | ['-1.08', '5.51', '2.63']
w3.f15 |   | `frustratingly refuses to` | 2.61 | ['2.87', '0.50', '-0.59']
w3.f16 |   | `refuses to give` | 2.72 | ['-0.92', '-0.49', '4.51']
w3.f17 | x | `refuses to give` | 4.23 | ['4.07', '1.66', '-1.34']
w3.f18 | x | `political context ,` | 5.56 | ['3.73', '1.51', '0.79']
w3.f19 | x | `material is mostly` | 4.99 | ['0.40', '3.62', '1.09']

## Original input: 
``` beautifully filmed and well acted . . . but admittedly problematic in its narrative @@UNK@@ . ``` 

## Marked input: 
<pre><span style="background-color: #FFFF00">@</span>beautifully <span style="background-color: #FFFF00">@</span>filmed <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>well <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>acted <span style="background-color: #FFFF00">@</span>. . . <span style="background-color: #6698FF">@</span>but <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>admittedly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>problematic <span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>its <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>narrative <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `but admittedly` | 1.96 | ['0.91', '1.42']
w2.f1 | x | `but admittedly` | 6.30 | ['4.31', '2.13']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `. but` | 1.50 | ['0.52', '1.53']
w2.f4 |   | `but admittedly` | 1.04 | ['-1.00', '2.23']
w2.f5 |   | `problematic in` | 2.06 | ['1.45', '0.91']
w2.f6 |   | `in its` | 3.22 | ['1.77', '1.55']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `@@PAD@@ beautifully` | 2.16 | ['0.00', '2.37']
w2.f9 |   | `its narrative` | 4.71 | ['2.78', '1.94']
w2.f10 | x | `@@PAD@@ beautifully` | 9.80 | ['0.00', '9.94']
w2.f11 |   | `admittedly problematic` | 2.47 | ['0.71', '2.02']
w2.f12 |   | `narrative @@UNK@@` | 2.54 | ['2.36', '0.22']
w2.f13 |   | `but admittedly` | 1.61 | ['-0.37', '2.13']
w2.f14 |   | `acted .` | 2.63 | ['2.27', '0.39']
w2.f15 | x | `but admittedly` | 6.16 | ['2.02', '4.41']
w2.f16 |   | `admittedly problematic` | 1.72 | ['-0.42', '2.90']
w2.f17 |   | `its narrative` | 1.62 | ['-0.61', '2.85']
w2.f18 |   | `and well` | 3.18 | ['3.52', '-0.21']
w2.f19 | x | `and well` | 5.05 | ['3.66', '1.69']
w3.f0 | x | `problematic in its` | 4.13 | ['2.15', '1.29', '1.08']
w3.f1 | x | `beautifully filmed and` | 5.49 | ['4.55', '1.48', '-0.17']
w3.f2 |   | `but admittedly problematic` | 3.48 | ['1.07', '-0.13', '2.63']
w3.f3 |   | `@@PAD@@ @@PAD@@ beautifully` | 2.18 | ['0.00', '0.00', '2.78']
w3.f4 | x | `@@PAD@@ @@PAD@@ beautifully` | 4.03 | ['0.00', '0.00', '4.39']
w3.f5 |   | `its narrative @@UNK@@` | 4.20 | ['1.92', '3.54', '-0.93']
w3.f6 | x | `its narrative @@UNK@@` | 5.86 | ['0.13', '5.79', '0.15']
w3.f7 | x | `problematic in its` | 7.03 | ['2.24', '0.70', '4.59']
w3.f8 |   | `. but admittedly` | 2.49 | ['-1.05', '3.35', '0.48']
w3.f9 |   | `. . but` | 2.67 | ['0.67', '0.58', '1.53']
w3.f10 | x | `. . but` | 4.96 | ['0.09', '2.00', '3.02']
w3.f11 |   | `problematic in its` | 3.61 | ['1.54', '-0.61', '2.88']
w3.f12 | x | `beautifully filmed and` | 4.26 | ['1.22', '2.03', '1.15']
w3.f13 |   | `@@PAD@@ beautifully filmed` | 4.38 | ['0.00', '1.49', '3.14']
w3.f14 |   | `its narrative @@UNK@@` | 2.68 | ['1.26', '2.87', '-1.37']
w3.f15 |   | `. but admittedly` | 0.93 | ['0.68', '0.10', '0.31']
w3.f16 |   | `admittedly problematic in` | 2.51 | ['2.43', '0.01', '0.44']
w3.f17 |   | `admittedly problematic in` | 3.41 | ['0.20', '3.34', '0.03']
w3.f18 |   | `in its narrative` | 1.28 | ['-0.32', '1.12', '0.94']
w3.f19 | x | `. but admittedly` | 4.70 | ['0.22', '1.45', '3.14']

## Original input: 
``` @@UNK@@ @@UNK@@ - to - @@UNK@@ and @@UNK@@ - to - @@UNK@@ , hopkins and norton are a winning combination -- but fiennes steals ' red dragon ' right from under their @@UNK@@ . ``` 

## Marked input: 
<pre>@@UNK@@ @@UNK@@ - to - @@UNK@@ and @@UNK@@ - to - @@UNK@@ , hopkins and norton <span style="background-color: #FFFF00">@</span>are <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>winning <span style="background-color: #FFFF00">@</span>combination <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>-- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>but <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>fiennes <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>steals <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>' <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>red <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>dragon <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>' <span style="background-color: #FFFF00">@</span>right <span style="background-color: #FFFF00">@</span>from <span style="background-color: #FFFF00">@</span>under <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>their <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `-- but` | 4.41 | ['4.26', '0.52']
w2.f1 | x | `but fiennes` | 5.34 | ['4.31', '1.17']
w2.f2 |   | `winning combination` | 1.03 | ['0.93', '1.14']
w2.f3 | x | `steals '` | 2.66 | ['1.73', '1.49']
w2.f4 | x | `dragon '` | 4.35 | ['2.61', '1.93']
w2.f5 | x | `a winning` | 4.34 | ['0.71', '3.94']
w2.f6 | x | `and norton` | 4.13 | ['-0.03', '4.26']
w2.f7 |   | `fiennes steals` | 1.85 | ['0.82', '1.94']
w2.f8 | x | `winning combination` | 3.61 | ['3.04', '0.78']
w2.f9 | x | `' red` | 5.51 | ['2.80', '2.73']
w2.f10 | x | `combination --` | 3.56 | ['0.29', '3.41']
w2.f11 |   | `winning combination` | 2.83 | ['-0.59', '3.69']
w2.f12 | x | `but fiennes` | 3.47 | ['1.63', '1.88']
w2.f13 | x | `under their` | 4.37 | ['4.19', '0.33']
w2.f14 |   | `combination --` | 2.67 | ['0.89', '1.82']
w2.f15 |   | `' right` | 3.05 | ['2.81', '0.52']
w2.f16 |   | `under their` | 1.96 | ['1.14', '1.58']
w2.f17 | x | `steals '` | 3.60 | ['2.91', '1.31']
w2.f18 | x | `winning combination` | 5.81 | ['3.77', '2.16']
w2.f19 |   | `red dragon` | 2.76 | ['0.64', '2.42']
w3.f0 | x | `combination -- but` | 4.39 | ['4.13', '-0.93', '1.59']
w3.f1 | x | `red dragon '` | 7.79 | ['5.55', '3.17', '-0.55']
w3.f2 | x | `winning combination --` | 4.82 | ['1.51', '4.24', '-0.85']
w3.f3 |   | `combination -- but` | 2.36 | ['1.00', '1.29', '0.68']
w3.f4 | x | `and norton are` | 5.12 | ['-0.23', '2.20', '3.51']
w3.f5 |   | `, hopkins and` | 4.09 | ['-0.52', '-0.88', '5.81']
w3.f6 |   | `-- but fiennes` | 2.87 | ['-1.21', '1.90', '2.39']
w3.f7 |   | `, hopkins and` | 3.86 | ['1.70', '0.82', '1.83']
w3.f8 | x | `from under their` | 8.80 | ['5.16', '2.87', '1.06']
w3.f9 | x | `fiennes steals '` | 9.10 | ['1.95', '2.04', '5.23']
w3.f10 |   | `-- but fiennes` | 2.63 | ['-1.34', '-0.98', '5.09']
w3.f11 | x | `from under their` | 10.10 | ['4.70', '2.15', '3.45']
w3.f12 | x | `but fiennes steals` | 4.20 | ['-0.44', '2.68', '2.09']
w3.f13 | x | `dragon ' right` | 8.96 | ['3.68', '4.49', '1.03']
w3.f14 | x | `combination -- but` | 5.59 | ['3.16', '2.66', '-0.14']
w3.f15 |   | `combination -- but` | 3.70 | ['1.05', '2.85', '-0.04']
w3.f16 | x | `' right from` | 3.92 | ['1.80', '-0.84', '3.33']
w3.f17 | x | `but fiennes steals` | 5.94 | ['1.76', '3.10', '1.25']
w3.f18 | x | `fiennes steals '` | 3.48 | ['-0.04', '3.81', '0.17']
w3.f19 | x | `a winning combination` | 10.28 | ['3.70', '3.38', '3.31']

## Original input: 
``` @@UNK@@ , charming , quirky , original ``` 

## Marked input: 
<pre>@@UNK@@ , <span style="background-color: #6698FF">@</span>charming <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>quirky <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>original</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `, quirky` | 3.51 | ['-1.14', '5.02']
w2.f1 |   | `original @@PAD@@` | 2.22 | ['2.35', '0.00']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `charming ,` | 0.85 | ['0.97', '0.44']
w2.f4 |   | `original @@PAD@@` | 1.67 | ['1.86', '0.00']
w2.f5 |   | `, quirky` | 2.82 | ['1.09', '2.03']
w2.f6 | x | `quirky ,` | 4.42 | ['0.58', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `quirky ,` | 1.40 | ['2.41', '-0.79']
w2.f9 |   | `@@UNK@@ ,` | 2.70 | ['2.38', '0.34']
w2.f10 |   | `original @@PAD@@` | 2.49 | ['2.62', '0.00']
w2.f11 |   | `original @@PAD@@` | 1.59 | ['1.86', '0.00']
w2.f12 |   | `quirky ,` | 0.96 | ['1.03', '-0.03']
w2.f13 | x | `charming ,` | 3.23 | ['1.19', '2.18']
w2.f14 |   | `@@UNK@@ ,` | 1.54 | ['0.69', '0.89']
w2.f15 | x | `, quirky` | 4.87 | ['2.19', '2.95']
w2.f16 |   | `, charming` | 0.97 | ['-0.98', '2.72']
w2.f17 |   | `, quirky` | 2.81 | ['-1.63', '5.06']
w2.f18 |   | `quirky ,` | 3.10 | ['2.33', '0.89']
w2.f19 | x | `, charming` | 3.84 | ['-0.70', '4.84']
w3.f0 | x | `original @@PAD@@ @@PAD@@` | 4.66 | ['5.05', '0.00', '0.00']
w3.f1 | x | `quirky , original` | 6.28 | ['3.94', '0.90', '1.81']
w3.f2 |   | `, charming ,` | 3.39 | ['2.60', '-0.45', '1.32']
w3.f3 |   | `quirky , original` | 1.04 | ['1.32', '-0.65', '0.98']
w3.f4 |   | `quirky , original` | 2.67 | ['1.54', '0.77', '0.72']
w3.f5 |   | `quirky , original` | 2.30 | ['1.09', '1.40', '0.13']
w3.f6 |   | `@@UNK@@ , charming` | 2.43 | ['-0.28', '0.38', '2.54']
w3.f7 |   | `, original @@PAD@@` | 1.54 | ['1.70', '0.33', '0.00']
w3.f8 |   | `, quirky ,` | 2.51 | ['-2.16', '2.81', '2.14']
w3.f9 | x | `, quirky ,` | 3.66 | ['-2.20', '2.91', '3.06']
w3.f10 | x | `quirky , original` | 6.32 | ['3.97', '-0.41', '2.90']
w3.f11 | x | `original @@PAD@@ @@PAD@@` | 4.15 | ['4.34', '0.00', '0.00']
w3.f12 |   | `quirky , original` | 1.19 | ['1.10', '-0.15', '0.37']
w3.f13 |   | `charming , quirky` | 3.08 | ['-0.17', '1.92', '1.58']
w3.f14 | x | `@@UNK@@ , charming` | 3.08 | ['-0.34', '-0.37', '3.88']
w3.f15 | x | `, charming ,` | 6.25 | ['1.52', '2.19', '2.70']
w3.f16 | x | `quirky , original` | 7.10 | ['3.43', '3.78', '0.26']
w3.f17 |   | `@@UNK@@ , charming` | 3.43 | ['-2.59', '3.34', '2.84']
w3.f18 |   | `original @@PAD@@ @@PAD@@` | 1.67 | ['2.13', '0.00', '0.00']
w3.f19 | x | `, charming ,` | 6.06 | ['-2.27', '7.37', '1.08']

## Original input: 
``` there 's nothing like love to give a movie a @@UNK@@ shot , and cq @@UNK@@ with it . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>there <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span>nothing <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>like <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>love <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>give <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>movie <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>shot <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>cq <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `with it` | 4.74 | ['3.44', '1.67']
w2.f1 | x | `@@UNK@@ with` | 3.86 | ['-0.88', '4.87']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `shot ,` | 1.13 | ['1.24', '0.44']
w2.f4 | x | `like love` | 3.67 | ['-0.56', '4.42']
w2.f5 |   | `love to` | 2.28 | ['0.19', '2.39']
w2.f6 | x | `shot ,` | 5.40 | ['1.57', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 | x | `give a` | 4.05 | ['1.70', '2.56']
w2.f9 | x | `nothing like` | 5.56 | ['4.79', '0.78']
w2.f10 | x | `'s nothing` | 3.35 | ['2.75', '0.73']
w2.f11 | x | `with it` | 3.36 | ['2.35', '1.28']
w2.f12 | x | `'s nothing` | 8.36 | ['0.44', '7.96']
w2.f13 | x | `nothing like` | 6.70 | ['3.82', '3.03']
w2.f14 | x | `shot ,` | 3.47 | ['2.62', '0.89']
w2.f15 |   | `'s nothing` | 0.23 | ['1.82', '-1.32']
w2.f16 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f17 | x | `and cq` | 4.93 | ['1.02', '4.52']
w2.f18 | x | `and cq` | 3.48 | ['3.52', '0.09']
w2.f19 | x | `and cq` | 4.19 | ['3.66', '0.82']
w3.f0 | x | `cq @@UNK@@ with` | 3.85 | ['4.98', '0.35', '-1.09']
w3.f1 |   | `love to give` | 3.71 | ['0.39', '0.48', '3.23']
w3.f2 | x | `a movie a` | 5.27 | ['1.87', '1.21', '2.27']
w3.f3 |   | `a @@UNK@@ shot` | 0.07 | ['-0.28', '-0.06', '1.01']
w3.f4 |   | `there 's nothing` | 2.52 | ['0.53', '2.08', '0.27']
w3.f5 | x | `with it .` | 7.25 | ['4.85', '-1.59', '4.32']
w3.f6 | x | `a movie a` | 3.85 | ['1.76', '4.49', '-2.18']
w3.f7 | x | `love to give` | 6.34 | ['0.66', '1.18', '5.00']
w3.f8 | x | `and cq @@UNK@@` | 7.30 | ['2.47', '5.65', '-0.54']
w3.f9 | x | `@@PAD@@ @@PAD@@ there` | 4.23 | ['0.00', '0.00', '4.33']
w3.f10 |   | `and cq @@UNK@@` | 2.08 | ['-1.89', '3.26', '0.86']
w3.f11 |   | `love to give` | 3.03 | ['3.30', '-1.67', '1.59']
w3.f12 | x | `nothing like love` | 4.48 | ['3.70', '0.73', '0.18']
w3.f13 |   | `like love to` | 3.49 | ['0.87', '2.66', '0.20']
w3.f14 | x | `there 's nothing` | 4.63 | ['-0.30', '1.15', '3.87']
w3.f15 | x | `@@UNK@@ shot ,` | 5.05 | ['-0.51', '3.02', '2.70']
w3.f16 | x | `love to give` | 7.46 | ['3.82', '-0.49', '4.51']
w3.f17 |   | `there 's nothing` | 3.47 | ['-1.13', '-0.23', '4.98']
w3.f18 |   | `give a movie` | 0.43 | ['0.25', '-0.07', '0.71']
w3.f19 |   | `nothing like love` | 0.70 | ['-0.91', '3.53', '-1.81']

## Original input: 
``` the santa clause 2 's plot may sound like it was co - written by @@UNK@@ @@UNK@@ and @@UNK@@ for the @@UNK@@ industry . ``` 

## Marked input: 
<pre>the santa clause <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>2 <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>'s <span style="background-color: #FFFF00">@</span>plot <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>may <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>sound <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>like <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>was <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>co <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>written by <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>and @@UNK@@ for <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>@@UNK@@ industry <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ for` | 3.71 | ['1.98', '2.10']
w2.f1 |   | `written by` | 2.78 | ['2.66', '0.26']
w2.f2 |   | `santa clause` | 0.04 | ['0.68', '0.41']
w2.f3 | x | `santa clause` | 2.95 | ['2.71', '0.79']
w2.f4 | x | `written by` | 3.82 | ['3.98', '0.03']
w2.f5 | x | `like it` | 3.32 | ['3.40', '0.23']
w2.f6 |   | `like it` | 2.60 | ['2.29', '0.41']
w2.f7 | x | `plot may` | 2.48 | ['2.55', '0.84']
w2.f8 | x | `plot may` | 3.61 | ['3.62', '0.21']
w2.f9 |   | `co -` | 3.68 | ['3.24', '0.46']
w2.f10 |   | `@@UNK@@ industry` | 2.89 | ['-0.06', '3.08']
w2.f11 | x | `santa clause` | 7.32 | ['2.49', '5.10']
w2.f12 | x | `written by` | 3.52 | ['-0.14', '3.71']
w2.f13 | x | `@@UNK@@ for` | 3.24 | ['0.61', '2.78']
w2.f14 | x | `it was` | 7.04 | ['1.93', '5.14']
w2.f15 | x | `2 's` | 3.94 | ['4.85', '-0.64']
w2.f16 | x | `was co` | 5.71 | ['3.28', '3.19']
w2.f17 | x | `plot may` | 3.25 | ['4.14', '-0.27']
w2.f18 | x | `santa clause` | 3.79 | ['2.37', '1.55']
w2.f19 |   | `sound like` | 1.89 | ['0.91', '1.28']
w3.f0 |   | `may sound like` | 2.44 | ['1.40', '2.19', '-0.76']
w3.f1 |   | `like it was` | 2.91 | ['3.51', '-0.10', '-0.13']
w3.f2 | x | `'s plot may` | 5.32 | ['0.87', '2.59', '1.95']
w3.f3 |   | `written by @@UNK@@` | 1.36 | ['2.18', '-0.28', '0.07']
w3.f4 |   | `2 's plot` | 3.19 | ['1.81', '2.08', '-0.34']
w3.f5 | x | `@@UNK@@ industry .` | 6.76 | ['0.08', '2.68', '4.32']
w3.f6 | x | `'s plot may` | 5.31 | ['3.62', '1.86', '0.04']
w3.f7 |   | `- written by` | 3.18 | ['0.04', '2.35', '1.30']
w3.f8 |   | `and @@UNK@@ for` | 3.69 | ['2.47', '-0.27', '1.77']
w3.f9 | x | `written by @@UNK@@` | 5.63 | ['3.40', '0.20', '2.13']
w3.f10 | x | `industry . @@PAD@@` | 4.52 | ['2.66', '2.00', '0.00']
w3.f11 | x | `plot may sound` | 3.84 | ['0.57', '1.18', '2.29']
w3.f12 | x | `may sound like` | 6.10 | ['1.32', '0.00', '4.91']
w3.f13 |   | `2 's plot` | 3.72 | ['5.11', '-0.82', '-0.33']
w3.f14 | x | `may sound like` | 5.85 | ['-1.15', '1.45', '5.65']
w3.f15 | x | `it was co` | 5.44 | ['0.62', '3.01', '1.98']
w3.f16 | x | `'s plot may` | 4.82 | ['2.11', '-0.30', '3.38']
w3.f17 |   | `@@UNK@@ for the` | 3.62 | ['-2.59', '5.11', '1.25']
w3.f18 |   | `santa clause 2` | 2.78 | ['2.36', '-0.09', '0.98']
w3.f19 | x | `sound like it` | 6.09 | ['1.65', '3.53', '1.02']

## Original input: 
``` @@UNK@@ . . . @@UNK@@ ' a fool of himself . . . @@UNK@@ ' his fan base . . . ``` 

## Marked input: 
<pre>@@UNK@@ . . . @@UNK@@ ' a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>fool <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>himself <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>' <span style="background-color: #6698FF">@</span>his <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>fan <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>base <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `a fool` | 4.70 | ['1.11', '3.96']
w2.f1 |   | `a fool` | 0.10 | ['2.95', '-2.72']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `of himself` | 2.03 | ['-0.30', '2.88']
w2.f4 |   | `a fool` | 2.04 | ['2.27', '-0.04']
w2.f5 | x | `fan base` | 6.58 | ['6.29', '0.60']
w2.f6 |   | `' his` | 2.17 | ['1.34', '0.93']
w2.f7 |   | `of himself` | 0.85 | ['0.11', '1.65']
w2.f8 | x | `' a` | 3.29 | ['0.95', '2.56']
w2.f9 | x | `' his` | 5.48 | ['2.80', '2.69']
w2.f10 |   | `his fan` | 2.00 | ['0.58', '1.56']
w2.f11 |   | `fool of` | 2.17 | ['1.50', '0.95']
w2.f12 |   | `' his` | 2.36 | ['2.20', '0.20']
w2.f13 |   | `@@UNK@@ '` | 1.75 | ['0.61', '1.29']
w2.f14 |   | `his fan` | 1.87 | ['0.84', '1.07']
w2.f15 |   | `' a` | 2.79 | ['2.81', '0.25']
w2.f16 |   | `a fool` | 0.07 | ['-0.39', '1.22']
w2.f17 |   | `himself .` | 0.79 | ['0.94', '0.47']
w2.f18 | x | `' his` | 3.33 | ['2.45', '1.01']
w2.f19 |   | `his fan` | 1.69 | ['1.37', '0.63']
w3.f0 | x | `his fan base` | 4.78 | ['0.93', '2.50', '1.74']
w3.f1 |   | `' his fan` | 1.01 | ['0.51', '-0.83', '1.71']
w3.f2 |   | `' a fool` | 1.95 | ['1.19', '-0.88', '1.72']
w3.f3 |   | `fan base .` | 0.42 | ['0.28', '1.50', '-0.75']
w3.f4 |   | `' his fan` | 1.97 | ['-0.82', '-0.28', '3.42']
w3.f5 | x | `himself . .` | 5.81 | ['2.21', '-0.40', '4.32']
w3.f6 |   | `himself . .` | 1.28 | ['1.71', '1.07', '-1.28']
w3.f7 |   | `his fan base` | 2.23 | ['1.44', '-0.20', '1.49']
w3.f8 |   | `@@UNK@@ ' a` | 2.08 | ['0.50', '2.32', '-0.46']
w3.f9 | x | `. @@UNK@@ '` | 3.70 | ['0.67', '-2.09', '5.23']
w3.f10 |   | `. . @@UNK@@` | 2.80 | ['0.09', '2.00', '0.86']
w3.f11 | x | `' a fool` | 5.98 | ['0.98', '0.22', '4.98']
w3.f12 | x | `fool of himself` | 4.45 | ['2.07', '3.24', '-0.74']
w3.f13 |   | `@@UNK@@ ' his` | 4.79 | ['-0.04', '4.49', '0.58']
w3.f14 |   | `' a fool` | 0.06 | ['1.53', '-2.45', '1.08']
w3.f15 |   | `a fool of` | 2.01 | ['-2.48', '2.65', '2.01']
w3.f16 | x | `his fan base` | 4.20 | ['0.62', '2.77', '1.19']
w3.f17 |   | `' a fool` | 2.22 | ['2.63', '-1.45', '1.19']
w3.f18 | x | `fan base .` | 4.97 | ['4.46', '1.93', '-0.95']
w3.f19 | x | `a fool of` | 4.54 | ['3.70', '-1.70', '2.66']

## Original input: 
``` it 's a technically superb film , shining with all the usual spielberg flair , expertly @@UNK@@ the talents of his top - notch creative team . ``` 

## Marked input: 
<pre>it 's <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>technically <span style="background-color: #6698FF">@</span>superb <span style="background-color: #6698FF">@</span>film <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>shining <span style="background-color: #FFFF00">@</span>with <span style="background-color: #FFFF00">@</span>all <span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>usual <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>spielberg <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>flair <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>expertly <span style="background-color: #FFFF00">@</span>@@UNK@@ the talents <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>his <span style="background-color: #FFFF00">@</span>top - <span style="background-color: #FFFF00">@</span>notch <span style="background-color: #FFFF00">@</span>creative <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>team <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `with all` | 4.65 | ['3.44', '1.58']
w2.f1 | x | `notch creative` | 6.26 | ['1.09', '5.30']
w2.f2 |   | `usual spielberg` | 1.57 | ['1.88', '0.73']
w2.f3 |   | `- notch` | 1.70 | ['0.84', '1.41']
w2.f4 | x | `film ,` | 3.64 | ['1.33', '2.50']
w2.f5 | x | `spielberg flair` | 7.09 | ['7.67', '-0.28']
w2.f6 | x | `flair ,` | 5.45 | ['1.62', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 | x | `usual spielberg` | 3.84 | ['1.90', '2.15']
w2.f9 |   | `talents of` | 4.89 | ['3.25', '1.65']
w2.f10 | x | `usual spielberg` | 6.14 | ['-0.40', '6.67']
w2.f11 |   | `expertly @@UNK@@` | 2.78 | ['2.81', '0.25']
w2.f12 |   | `all the` | 2.78 | ['1.50', '1.32']
w2.f13 |   | `top -` | 2.47 | ['1.42', '1.20']
w2.f14 | x | `usual spielberg` | 4.61 | ['2.04', '2.60']
w2.f15 | x | `spielberg flair` | 12.70 | ['7.55', '5.42']
w2.f16 | x | `all the` | 3.95 | ['3.88', '0.83']
w2.f17 |   | `notch creative` | 2.14 | ['1.31', '1.44']
w2.f18 | x | `superb film` | 3.48 | ['2.65', '0.95']
w2.f19 | x | `creative team` | 3.23 | ['0.27', '3.26']
w3.f0 | x | `notch creative team` | 4.22 | ['2.72', '2.50', '-0.61']
w3.f1 | x | `all the usual` | 9.21 | ['-1.74', '-0.57', '11.90']
w3.f2 | x | `a technically superb` | 5.09 | ['1.87', '1.38', '1.92']
w3.f3 | x | `shining with all` | 2.52 | ['1.45', '-1.25', '2.93']
w3.f4 |   | `usual spielberg flair` | 2.95 | ['2.46', '-1.35', '2.19']
w3.f5 | x | `creative team .` | 8.64 | ['0.59', '4.06', '4.32']
w3.f6 |   | `all the usual` | 2.44 | ['-0.31', '0.45', '2.51']
w3.f7 |   | `flair , expertly` | 3.56 | ['2.58', '-0.37', '1.86']
w3.f8 | x | `usual spielberg flair` | 6.39 | ['2.59', '2.05', '2.03']
w3.f9 |   | `usual spielberg flair` | 2.46 | ['2.12', '1.32', '-0.86']
w3.f10 | x | `usual spielberg flair` | 6.05 | ['4.59', '0.60', '1.00']
w3.f11 | x | `it 's a` | 4.07 | ['1.01', '0.46', '2.78']
w3.f12 | x | `all the usual` | 4.58 | ['2.76', '-0.17', '2.11']
w3.f13 | x | `the talents of` | 8.49 | ['4.70', '1.33', '2.71']
w3.f14 |   | `technically superb film` | 3.01 | ['2.98', '0.25', '-0.13']
w3.f15 |   | `superb film ,` | 3.33 | ['0.72', '0.07', '2.70']
w3.f16 | x | `all the usual` | 8.25 | ['1.41', '0.10', '7.11']
w3.f17 |   | `all the usual` | 3.50 | ['-0.00', '0.47', '3.19']
w3.f18 | x | `usual spielberg flair` | 7.48 | ['6.76', '0.57', '0.62']
w3.f19 | x | `top - notch` | 5.87 | ['1.17', '1.48', '3.33']

## Original input: 
``` . . . a rather bland affair . ``` 

## Marked input: 
<pre>. . . a rather <span style="background-color: #6698FF">@</span>bland <span style="background-color: #6698FF">@</span>affair <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f1 |   | `a rather` | 3.52 | ['2.95', '0.71']
w2.f2 |   | `bland affair` | 0.22 | ['0.43', '0.84']
w2.f3 | x | `rather bland` | 3.40 | ['0.11', '3.85']
w2.f4 |   | `affair .` | 2.29 | ['2.51', '-0.03']
w2.f5 |   | `. @@PAD@@` | 0.37 | ['0.67', '0.00']
w2.f6 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f7 |   | `rather bland` | 1.46 | ['-0.31', '2.69']
w2.f8 |   | `a rather` | 0.74 | ['0.88', '0.07']
w2.f9 |   | `affair .` | 1.50 | ['1.05', '0.46']
w2.f10 |   | `a rather` | 2.10 | ['1.97', '0.27']
w2.f11 |   | `rather bland` | 2.74 | ['1.17', '1.84']
w2.f12 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f13 |   | `affair .` | 2.87 | ['3.01', '0.01']
w2.f14 | x | `rather bland` | 4.49 | ['2.36', '2.16']
w2.f15 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f16 |   | `bland affair` | 1.02 | ['1.42', '0.37']
w2.f17 |   | `rather bland` | 0.15 | ['-1.25', '2.02']
w2.f18 |   | `. .` | 1.09 | ['0.99', '0.22']
w2.f19 |   | `a rather` | 1.13 | ['0.99', '0.44']
w3.f0 | x | `a rather bland` | 7.32 | ['-0.19', '2.68', '5.22']
w3.f1 |   | `affair . @@PAD@@` | 1.81 | ['2.55', '-0.35', '0.00']
w3.f2 | x | `a rather bland` | 4.08 | ['1.87', '1.75', '0.54']
w3.f3 |   | `@@PAD@@ @@PAD@@ .` | 0.00 | ['0.00', '0.00', '-0.75']
w3.f4 |   | `. a rather` | 0.36 | ['-0.66', '0.29', '1.10']
w3.f5 |   | `@@PAD@@ @@PAD@@ .` | 3.99 | ['0.00', '0.00', '4.32']
w3.f6 |   | `affair . @@PAD@@` | 2.94 | ['2.08', '1.07', '0.00']
w3.f7 |   | `@@PAD@@ @@PAD@@ .` | 0.00 | ['0.00', '0.00', '0.18']
w3.f8 |   | `a rather bland` | 2.89 | ['0.66', '1.32', '1.20']
w3.f9 |   | `. . a` | 2.28 | ['0.67', '0.58', '1.13']
w3.f10 |   | `. a rather` | 3.35 | ['0.09', '1.32', '2.09']
w3.f11 | x | `bland affair .` | 3.74 | ['5.37', '-1.35', '-0.08']
w3.f12 | x | `rather bland affair` | 4.61 | ['-0.17', '4.58', '0.33']
w3.f13 |   | `@@PAD@@ @@PAD@@ .` | 2.20 | ['0.00', '0.00', '2.45']
w3.f14 | x | `rather bland affair` | 7.47 | ['4.27', '-0.11', '3.40']
w3.f15 | x | `a rather bland` | 3.92 | ['-2.48', '3.59', '2.97']
w3.f16 |   | `@@PAD@@ @@PAD@@ .` | 0.00 | ['0.00', '0.00', '-2.29']
w3.f17 | x | `rather bland affair` | 4.28 | ['2.30', '0.79', '1.35']
w3.f18 |   | `rather bland affair` | 0.32 | ['0.18', '0.98', '-0.38']
w3.f19 |   | `a rather bland` | 2.23 | ['3.70', '-1.77', '0.42']

## Original input: 
``` it 's the kind of movie you ca n't quite recommend because it is all @@UNK@@ and not much of a pitch , yet you ca n't bring yourself to @@UNK@@ it . ``` 

## Marked input: 
<pre>it 's the kind <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>movie <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>you <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>ca <span style="background-color: #6698FF">@</span>n't <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>quite <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>recommend <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>because <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>all <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>and not <span style="background-color: #FFFF00">@</span>much <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>pitch <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>yet <span style="background-color: #6698FF">@</span>you <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>ca <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>n't bring yourself to <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>it .</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `because it` | 4.86 | ['3.57', '1.67']
w2.f1 | x | `quite recommend` | 5.39 | ['1.18', '4.34']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `quite recommend` | 2.77 | ['3.11', '0.22']
w2.f4 |   | `movie you` | 3.31 | ['3.31', '0.19']
w2.f5 | x | `much of` | 6.33 | ['4.87', '1.76']
w2.f6 | x | `because it` | 4.10 | ['3.79', '0.41']
w2.f7 |   | `yet you` | 1.68 | ['1.83', '0.76']
w2.f8 | x | `quite recommend` | 6.36 | ['4.29', '2.28']
w2.f9 | x | `yourself to` | 6.22 | ['1.56', '4.67']
w2.f10 | x | `recommend because` | 4.13 | ['4.28', '-0.01']
w2.f11 |   | `kind of` | 1.85 | ['1.18', '0.95']
w2.f12 | x | `, yet` | 3.67 | ['-0.98', '4.69']
w2.f13 | x | `ca n't` | 5.10 | ['2.17', '3.08']
w2.f14 | x | `quite recommend` | 7.65 | ['2.46', '5.22']
w2.f15 | x | `yet you` | 5.55 | ['-0.17', '5.99']
w2.f16 | x | `n't quite` | 8.12 | ['2.24', '6.65']
w2.f17 | x | `quite recommend` | 7.26 | ['7.03', '0.85']
w2.f18 | x | `and not` | 4.21 | ['3.52', '0.82']
w2.f19 | x | `a pitch` | 3.39 | ['0.99', '2.70']
w3.f0 | x | `of a pitch` | 4.39 | ['-0.27', '3.29', '1.76']
w3.f1 | x | `ca n't quite` | 6.59 | ['1.14', '-1.00', '6.83']
w3.f2 | x | `, yet you` | 3.68 | ['2.60', '1.15', '0.02']
w3.f3 | x | `ca n't quite` | 3.54 | ['1.30', '2.63', '0.22']
w3.f4 |   | `quite recommend because` | 2.98 | ['0.54', '1.43', '1.37']
w3.f5 |   | `yet you ca` | 2.87 | ['0.74', '0.90', '1.56']
w3.f6 | x | `of movie you` | 5.88 | ['-0.15', '4.49', '1.75']
w3.f7 | x | `quite recommend because` | 5.99 | ['0.82', '2.37', '3.29']
w3.f8 | x | `it is all` | 5.20 | ['2.11', '4.71', '-1.33']
w3.f9 | x | `quite recommend because` | 5.63 | ['3.69', '0.37', '1.68']
w3.f10 | x | `of movie you` | 4.86 | ['2.92', '1.31', '0.77']
w3.f11 | x | `quite recommend because` | 5.95 | ['0.80', '1.97', '3.37']
w3.f12 | x | `much of a` | 4.69 | ['2.25', '3.24', '-0.67']
w3.f13 | x | `the kind of` | 5.48 | ['4.70', '-1.67', '2.71']
w3.f14 |   | `it 's the` | 2.39 | ['0.08', '1.15', '1.24']
w3.f15 | x | `not much of` | 5.36 | ['-0.07', '3.59', '2.01']
w3.f16 | x | `ca n't quite` | 4.43 | ['-3.47', '2.52', '5.77']
w3.f17 |   | `@@UNK@@ and not` | 2.89 | ['-2.59', '1.30', '4.34']
w3.f18 | x | `kind of movie` | 5.54 | ['3.20', '2.10', '0.71']
w3.f19 | x | `recommend because it` | 6.72 | ['1.95', '3.87', '1.02']

## Original input: 
``` either a fascinating study of the relationship between @@UNK@@ and their children or a disturbing story about @@UNK@@ and their marks . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>either <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>fascinating <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>study <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>the relationship <span style="background-color: #FFFF00">@</span>between <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and their children <span style="background-color: #FFFF00">@</span>or <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>disturbing <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>story <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>about <span style="background-color: #FFFF00">@</span>@@UNK@@ and their <span style="background-color: #FFFF00">@</span>marks <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `their children` | 6.82 | ['4.53', '2.67']
w2.f1 | x | `a fascinating` | 7.52 | ['2.95', '4.70']
w2.f2 |   | `fascinating study` | 0.36 | ['0.76', '0.65']
w2.f3 | x | `relationship between` | 3.65 | ['2.90', '1.31']
w2.f4 | x | `fascinating study` | 4.73 | ['2.43', '2.48']
w2.f5 | x | `relationship between` | 7.72 | ['5.03', '3.00']
w2.f6 |   | `a disturbing` | 3.16 | ['0.54', '2.71']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `either a` | 2.57 | ['0.23', '2.56']
w2.f9 |   | `study of` | 3.24 | ['1.60', '1.65']
w2.f10 | x | `a fascinating` | 3.19 | ['1.97', '1.36']
w2.f11 |   | `study of` | 2.76 | ['2.08', '0.95']
w2.f12 |   | `their marks` | 1.75 | ['-0.45', '2.23']
w2.f13 |   | `marks .` | 1.94 | ['2.08', '0.01']
w2.f14 |   | `the relationship` | 1.71 | ['0.10', '1.64']
w2.f15 | x | `marks .` | 4.30 | ['6.73', '-2.16']
w2.f16 | x | `children or` | 5.17 | ['1.98', '3.95']
w2.f17 | x | `marks .` | 3.42 | ['3.57', '0.47']
w2.f18 | x | `and their` | 9.38 | ['3.52', '5.98']
w2.f19 | x | `a disturbing` | 6.87 | ['0.99', '6.17']
w3.f0 | x | `or a disturbing` | 3.87 | ['1.69', '3.29', '-0.72']
w3.f1 | x | `@@PAD@@ @@PAD@@ either` | 7.45 | ['0.00', '0.00', '7.83']
w3.f2 | x | `children or a` | 5.51 | ['1.24', '2.08', '2.27']
w3.f3 |   | `marks . @@PAD@@` | 1.01 | ['1.76', '-0.14', '0.00']
w3.f4 |   | `their marks .` | 2.98 | ['0.33', '3.53', '-0.52']
w3.f5 | x | `a disturbing story` | 8.00 | ['1.79', '4.54', '2.00']
w3.f6 |   | `a disturbing story` | 2.71 | ['1.76', '0.32', '0.84']
w3.f7 | x | `or a disturbing` | 6.15 | ['-0.10', '0.48', '6.27']
w3.f8 |   | `and their marks` | 2.63 | ['2.47', '-1.76', '2.20']
w3.f9 |   | `their children or` | 3.09 | ['1.77', '1.37', '0.05']
w3.f10 | x | `either a fascinating` | 7.54 | ['6.80', '1.32', '-0.43']
w3.f11 |   | `@@PAD@@ either a` | 3.32 | ['0.00', '0.73', '2.78']
w3.f12 | x | `@@PAD@@ @@PAD@@ either` | 4.65 | ['0.00', '0.00', '4.78']
w3.f13 | x | `the relationship between` | 5.49 | ['4.70', '0.69', '0.34']
w3.f14 |   | `relationship between @@UNK@@` | 2.73 | ['0.74', '3.45', '-1.37']
w3.f15 |   | `or a disturbing` | 2.80 | ['1.61', '-0.09', '1.45']
w3.f16 | x | `a disturbing story` | 4.12 | ['-0.19', '3.10', '1.59']
w3.f17 |   | `@@PAD@@ @@PAD@@ either` | 3.06 | ['0.00', '0.00', '3.22']
w3.f18 |   | `study of the` | 3.15 | ['-1.05', '2.10', '2.57']
w3.f19 | x | `a fascinating study` | 6.17 | ['3.70', '2.97', '-0.38']

## Original input: 
``` it is nature against progress . in @@UNK@@ 's horror @@UNK@@ , this theme has proved important to him and is especially so in the finale . ``` 

## Marked input: 
<pre>it is <span style="background-color: #FFFF00">@</span>nature <span style="background-color: #FFFF00">@</span>against <span style="background-color: #FFFF00">@</span>progress <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>@@UNK@@ 's <span style="background-color: #FFFF00">@</span>horror <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>this theme has <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>proved <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>important <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>him <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>especially <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>so in <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>finale <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `'s horror` | 2.33 | ['-0.21', '2.91']
w2.f1 |   | `this theme` | 2.95 | ['-0.19', '3.28']
w2.f2 |   | `against progress` | 0.83 | ['0.90', '0.97']
w2.f3 | x | `has proved` | 3.92 | ['1.03', '3.44']
w2.f4 |   | `progress .` | 3.57 | ['3.78', '-0.03']
w2.f5 | x | `nature against` | 3.63 | ['-0.93', '4.87']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `progress .` | 2.00 | ['2.77', '0.14']
w2.f8 | x | `@@UNK@@ 's` | 3.81 | ['0.21', '3.82']
w2.f9 | x | `important to` | 6.92 | ['2.26', '4.67']
w2.f10 |   | `has proved` | 2.62 | ['0.16', '2.60']
w2.f11 | x | `horror @@UNK@@` | 3.38 | ['3.40', '0.25']
w2.f12 | x | `so in` | 4.35 | ['2.41', '1.97']
w2.f13 |   | `progress .` | 3.10 | ['3.24', '0.01']
w2.f14 | x | `progress .` | 4.84 | ['4.48', '0.39']
w2.f15 | x | `theme has` | 6.09 | ['7.18', '-0.82']
w2.f16 |   | `against progress` | 1.43 | ['-1.14', '3.32']
w2.f17 | x | `finale .` | 4.09 | ['4.24', '0.47']
w2.f18 |   | `and is` | 3.06 | ['3.52', '-0.34']
w2.f19 | x | `and is` | 4.05 | ['3.66', '0.69']
w3.f0 | x | `has proved important` | 4.76 | ['1.40', '1.63', '2.12']
w3.f1 | x | `is nature against` | 5.42 | ['1.18', '2.59', '2.02']
w3.f2 | x | `theme has proved` | 6.59 | ['0.78', '-0.37', '6.27']
w3.f3 |   | `important to him` | 2.32 | ['2.43', '-1.32', '1.81']
w3.f4 |   | `@@PAD@@ it is` | 1.65 | ['0.00', '-0.45', '2.46']
w3.f5 | x | `to him and` | 6.53 | ['0.53', '0.51', '5.81']
w3.f6 | x | `has proved important` | 5.93 | ['-0.81', '2.78', '4.17']
w3.f7 | x | `to him and` | 6.25 | ['3.76', '1.14', '1.83']
w3.f8 | x | `it is nature` | 6.87 | ['2.11', '4.71', '0.34']
w3.f9 | x | `important to him` | 3.72 | ['4.14', '0.70', '-1.02']
w3.f10 | x | `finale . @@PAD@@` | 4.88 | ['3.03', '2.00', '0.00']
w3.f11 | x | `theme has proved` | 4.06 | ['0.78', '-1.97', '5.44']
w3.f12 | x | `him and is` | 5.08 | ['2.44', '0.95', '1.82']
w3.f13 | x | `the finale .` | 8.90 | ['4.70', '2.00', '2.45']
w3.f14 | x | `so in the` | 6.65 | ['6.10', '-0.60', '1.24']
w3.f15 |   | `this theme has` | 3.67 | ['2.58', '1.22', '0.04']
w3.f16 |   | `has proved important` | 2.76 | ['1.52', '-0.77', '2.38']
w3.f17 |   | `important to him` | 3.28 | ['-0.08', '1.66', '1.86']
w3.f18 |   | `important to him` | 2.78 | ['3.94', '-2.41', '1.72']
w3.f19 | x | `nature against progress` | 5.40 | ['2.63', '4.00', '-1.11']

## Original input: 
``` @@UNK@@ 's narrative is just as much about the @@UNK@@ and @@UNK@@ of @@UNK@@ as it is about a domestic @@UNK@@ finding their way to joy . ``` 

## Marked input: 
<pre>@@UNK@@ 's <span style="background-color: #FFFF00">@</span>narrative <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>just <span style="background-color: #6698FF">@</span>as <span style="background-color: #6698FF">@</span>much <span style="background-color: #6698FF">@</span>about <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ and @@UNK@@ of @@UNK@@ as it is about <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>domestic <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>finding <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>their <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>way <span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span>joy <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ finding` | 3.32 | ['1.98', '1.71']
w2.f1 | x | `a domestic` | 8.49 | ['2.95', '5.68']
w2.f2 |   | `as much` | 0.42 | ['0.54', '0.92']
w2.f3 |   | `just as` | 0.90 | ['1.31', '0.15']
w2.f4 | x | `way to` | 4.72 | ['5.36', '-0.45']
w2.f5 | x | `much about` | 3.96 | ['4.87', '-0.61']
w2.f6 | x | `finding their` | 4.44 | ['2.35', '2.18']
w2.f7 |   | `joy .` | 0.74 | ['1.51', '0.14']
w2.f8 | x | `@@UNK@@ 's` | 3.81 | ['0.21', '3.82']
w2.f9 |   | `way to` | 4.62 | ['-0.03', '4.67']
w2.f10 | x | `'s narrative` | 7.32 | ['2.75', '4.70']
w2.f11 |   | `as it` | 1.65 | ['0.63', '1.28']
w2.f12 |   | `a domestic` | 0.78 | ['-1.91', '2.73']
w2.f13 |   | `@@UNK@@ finding` | 3.06 | ['0.61', '2.61']
w2.f14 |   | `@@UNK@@ finding` | 2.25 | ['0.69', '1.60']
w2.f15 | x | `finding their` | 7.21 | ['4.58', '2.90']
w2.f16 |   | `finding their` | 0.81 | ['-0.01', '1.58']
w2.f17 |   | `'s narrative` | 2.32 | ['0.09', '2.85']
w2.f18 | x | `finding their` | 4.86 | ['-1.00', '5.98']
w2.f19 |   | `way to` | 2.80 | ['1.97', '1.12']
w3.f0 |   | `joy . @@PAD@@` | 3.63 | ['4.02', '-0.01', '0.00']
w3.f1 |   | `@@PAD@@ @@PAD@@ @@UNK@@` | 0.00 | ['0.00', '0.00', '-2.93']
w3.f2 | x | `about a domestic` | 5.45 | ['1.90', '-0.88', '4.51']
w3.f3 |   | `finding their way` | 0.89 | ['1.40', '-0.20', '0.30']
w3.f4 |   | `@@UNK@@ 's narrative` | 3.04 | ['0.36', '2.08', '0.96']
w3.f5 |   | `to joy .` | 4.24 | ['0.53', '-0.28', '4.32']
w3.f6 | x | `'s narrative is` | 10.84 | ['3.62', '5.79', '1.64']
w3.f7 | x | `finding their way` | 4.61 | ['2.82', '3.65', '-1.36']
w3.f8 |   | `it is about` | 3.32 | ['2.11', '4.71', '-3.20']
w3.f9 |   | `@@PAD@@ @@PAD@@ @@UNK@@` | 2.03 | ['0.00', '0.00', '2.13']
w3.f10 | x | `joy . @@PAD@@` | 4.47 | ['2.62', '2.00', '0.00']
w3.f11 | x | `is about a` | 4.12 | ['0.29', '1.24', '2.78']
w3.f12 | x | `just as much` | 6.73 | ['0.72', '4.53', '1.60']
w3.f13 |   | `it is about` | 5.14 | ['2.60', '2.81', '-0.01']
w3.f14 |   | `domestic @@UNK@@ finding` | 2.97 | ['0.98', '0.79', '1.30']
w3.f15 |   | `domestic @@UNK@@ finding` | 2.18 | ['3.78', '-1.69', '0.25']
w3.f16 |   | `finding their way` | 1.82 | ['-0.35', '4.21', '-1.66']
w3.f17 | x | `domestic @@UNK@@ finding` | 6.11 | ['2.90', '1.39', '1.99']
w3.f18 | x | `their way to` | 5.51 | ['2.40', '2.05', '1.52']
w3.f19 | x | `@@UNK@@ finding their` | 4.87 | ['-0.26', '3.28', '1.96']

## Original input: 
``` leaves us wondering less about its ideas and more about its characterization of hitler and the contrived nature of its provocative conclusion . ``` 

## Marked input: 
<pre>leaves us <span style="background-color: #FFFF00">@</span>wondering <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>less <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>about <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>its <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>ideas <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span>more <span style="background-color: #FFFF00">@</span>about <span style="background-color: #FFFF00">@</span>its <span style="background-color: #FFFF00">@</span>characterization <span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span>hitler <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>contrived <span style="background-color: #6698FF">@</span>nature <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>its <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>provocative <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>conclusion <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `leaves us` | 4.11 | ['0.75', '3.73']
w2.f1 |   | `of hitler` | 3.42 | ['-1.02', '4.57']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `contrived nature` | 2.27 | ['0.32', '2.51']
w2.f4 | x | `contrived nature` | 4.95 | ['1.84', '3.30']
w2.f5 |   | `of hitler` | 1.68 | ['0.65', '1.33']
w2.f6 |   | `its provocative` | 2.56 | ['0.58', '2.07']
w2.f7 |   | `of hitler` | 1.46 | ['0.11', '2.26']
w2.f8 |   | `contrived nature` | 1.28 | ['1.68', '-0.19']
w2.f9 | x | `nature of` | 7.25 | ['5.61', '1.65']
w2.f10 | x | `us wondering` | 4.94 | ['1.00', '4.08']
w2.f11 | x | `hitler and` | 4.26 | ['4.26', '0.27']
w2.f12 | x | `the contrived` | 4.82 | ['0.53', '4.32']
w2.f13 | x | `its provocative` | 3.71 | ['0.67', '3.18']
w2.f14 | x | `contrived nature` | 4.09 | ['-0.19', '4.32']
w2.f15 | x | `contrived nature` | 3.26 | ['2.97', '0.56']
w2.f16 | x | `wondering less` | 2.97 | ['1.55', '2.18']
w2.f17 | x | `contrived nature` | 6.13 | ['7.43', '-0.69']
w2.f18 | x | `contrived nature` | 3.89 | ['1.91', '2.10']
w2.f19 | x | `provocative conclusion` | 4.47 | ['2.98', '1.79']
w3.f0 | x | `less about its` | 6.96 | ['8.00', '-1.73', '1.08']
w3.f1 | x | `wondering less about` | 6.70 | ['4.82', '-0.47', '2.72']
w3.f2 | x | `wondering less about` | 5.85 | ['2.60', '3.93', '-0.58']
w3.f3 |   | `its provocative conclusion` | 0.61 | ['0.42', '0.81', '-0.02']
w3.f4 |   | `leaves us wondering` | 3.32 | ['1.55', '-0.29', '2.42']
w3.f5 | x | `its ideas and` | 10.31 | ['1.92', '2.91', '5.81']
w3.f6 |   | `ideas and more` | 3.02 | ['0.49', '0.25', '2.49']
w3.f7 | x | `more about its` | 5.09 | ['-0.02', '1.02', '4.59']
w3.f8 | x | `of its provocative` | 4.80 | ['1.71', '0.98', '2.40']
w3.f9 | x | `less about its` | 3.75 | ['1.97', '-1.42', '3.30']
w3.f10 | x | `contrived nature of` | 6.56 | ['5.21', '1.42', '0.08']
w3.f11 | x | `less about its` | 3.86 | ['-0.07', '1.24', '2.88']
w3.f12 | x | `characterization of hitler` | 7.57 | ['0.45', '3.24', '4.01']
w3.f13 | x | `contrived nature of` | 7.08 | ['0.44', '4.18', '2.71']
w3.f14 | x | `us wondering less` | 5.78 | ['0.45', '3.35', '2.07']
w3.f15 |   | `contrived nature of` | 2.59 | ['-1.30', '2.05', '2.01']
w3.f16 | x | `of its provocative` | 7.48 | ['1.87', '2.21', '3.78']
w3.f17 |   | `hitler and the` | 2.34 | ['-0.06', '1.30', '1.25']
w3.f18 | x | `leaves us wondering` | 3.80 | ['0.94', '0.97', '2.36']
w3.f19 | x | `its provocative conclusion` | 11.26 | ['3.31', '5.56', '2.51']

## Original input: 
``` harmless fun . ``` 

## Marked input: 
<pre>harmless <span style="background-color: #6698FF">@</span>fun <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f1 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `harmless fun` | 1.43 | ['3.12', '-1.13']
w2.f4 |   | `harmless fun` | 0.98 | ['-2.90', '4.07']
w2.f5 |   | `. @@PAD@@` | 0.37 | ['0.67', '0.00']
w2.f6 |   | `@@PAD@@ harmless` | 1.65 | ['0.00', '1.75']
w2.f7 |   | `harmless fun` | 0.74 | ['2.20', '-0.55']
w2.f8 |   | `harmless fun` | 0.32 | ['-1.84', '2.37']
w2.f9 |   | `harmless fun` | 1.09 | ['2.03', '-0.93']
w2.f10 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f11 |   | `@@PAD@@ harmless` | 0.33 | ['0.00', '0.60']
w2.f12 |   | `@@PAD@@ harmless` | 0.93 | ['0.00', '0.97']
w2.f13 |   | `@@PAD@@ harmless` | 2.10 | ['0.00', '2.25']
w2.f14 |   | `harmless fun` | 0.60 | ['1.80', '-1.17']
w2.f15 | x | `harmless fun` | 3.42 | ['0.15', '3.55']
w2.f16 | x | `@@PAD@@ harmless` | 3.69 | ['0.00', '4.45']
w2.f17 | x | `fun .` | 3.45 | ['3.60', '0.47']
w2.f18 | x | `fun .` | 3.39 | ['3.29', '0.22']
w2.f19 |   | `harmless fun` | 2.01 | ['-0.42', '2.72']
w3.f0 |   | `@@PAD@@ harmless fun` | 1.48 | ['0.00', '2.67', '-0.80']
w3.f1 |   | `@@PAD@@ harmless fun` | 2.82 | ['0.00', '-0.32', '3.53']
w3.f2 |   | `@@PAD@@ @@PAD@@ harmless` | 2.32 | ['0.00', '0.00', '2.41']
w3.f3 |   | `@@PAD@@ harmless fun` | 0.83 | ['0.00', '0.06', '1.38']
w3.f4 |   | `@@PAD@@ harmless fun` | 1.96 | ['0.00', '-0.69', '3.01']
w3.f5 | x | `harmless fun .` | 7.17 | ['-1.40', '4.58', '4.32']
w3.f6 |   | `@@PAD@@ @@PAD@@ harmless` | 0.00 | ['0.00', '0.00', '0.02']
w3.f7 |   | `@@PAD@@ @@PAD@@ harmless` | 0.18 | ['0.00', '0.00', '0.68']
w3.f8 |   | `@@PAD@@ @@PAD@@ harmless` | 0.00 | ['0.00', '0.00', '-1.60']
w3.f9 |   | `harmless fun .` | 2.26 | ['3.39', '1.26', '-2.28']
w3.f10 |   | `harmless fun .` | 3.05 | ['3.70', '1.76', '-2.27']
w3.f11 |   | `harmless fun .` | 0.59 | ['1.51', '-0.64', '-0.08']
w3.f12 |   | `@@PAD@@ harmless fun` | 2.11 | ['0.00', '3.46', '-1.22']
w3.f13 |   | `harmless fun .` | 1.82 | ['-2.88', '2.50', '2.45']
w3.f14 |   | `@@PAD@@ @@PAD@@ harmless` | 0.09 | ['0.00', '0.00', '0.19']
w3.f15 |   | `. @@PAD@@ @@PAD@@` | 0.52 | ['0.68', '0.00', '0.00']
w3.f16 | x | `fun . @@PAD@@` | 4.49 | ['5.88', '-1.01', '0.00']
w3.f17 |   | `@@PAD@@ @@PAD@@ harmless` | 0.35 | ['0.00', '0.00', '0.50']
w3.f18 |   | `@@PAD@@ harmless fun` | 0.31 | ['0.00', '-1.29', '2.06']
w3.f19 |   | `@@PAD@@ harmless fun` | 1.34 | ['0.00', '1.39', '0.07']

## Original input: 
``` even before it builds up to its insanely staged @@UNK@@ scene , in which 3000 actors appear in full @@UNK@@ , it 's @@UNK@@ itself into the art film pantheon . ``` 

## Marked input: 
<pre>even <span style="background-color: #6698FF">@</span>before <span style="background-color: #6698FF">@</span>it <span style="background-color: #6698FF">@</span>builds <span style="background-color: #FFFF00">@</span>up <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>its <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>insanely <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>staged <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>scene <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span>which <span style="background-color: #6698FF">@</span>3000 <span style="background-color: #6698FF">@</span>actors <span style="background-color: #6698FF">@</span>appear <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>in <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>full <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>, it 's @@UNK@@ itself <span style="background-color: #6698FF">@</span>into <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>art <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>film <span style="background-color: #FFFF00">@</span>pantheon <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ scene` | 5.72 | ['1.98', '4.11']
w2.f1 | x | `actors appear` | 3.92 | ['-0.63', '4.68']
w2.f2 |   | `builds up` | 1.45 | ['0.90', '1.59']
w2.f3 | x | `@@PAD@@ even` | 2.19 | ['0.00', '2.75']
w2.f4 |   | `which 3000` | 3.08 | ['2.00', '1.27']
w2.f5 |   | `the art` | 3.00 | ['1.16', '2.15']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 | x | `insanely staged` | 3.38 | ['0.82', '3.47']
w2.f8 |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 | x | `@@UNK@@ itself` | 6.71 | ['2.38', '4.35']
w2.f10 | x | `builds up` | 8.77 | ['1.97', '6.94']
w2.f11 | x | `builds up` | 3.68 | ['1.37', '2.58']
w2.f12 | x | `staged @@UNK@@` | 4.91 | ['4.72', '0.22']
w2.f13 |   | `@@UNK@@ ,` | 2.64 | ['0.61', '2.18']
w2.f14 | x | `in which` | 5.13 | ['-0.13', '5.29']
w2.f15 | x | `it builds` | 5.23 | ['1.16', '4.35']
w2.f16 | x | `in full` | 3.01 | ['1.01', '2.76']
w2.f17 | x | `3000 actors` | 3.82 | ['-0.22', '4.66']
w2.f18 |   | `itself into` | 3.09 | ['1.09', '2.12']
w2.f19 |   | `builds up` | 2.62 | ['3.29', '-0.37']
w3.f0 | x | `up to its` | 4.62 | ['5.35', '-1.42', '1.08']
w3.f1 | x | `actors appear in` | 6.18 | ['2.45', '2.68', '1.42']
w3.f2 | x | `actors appear in` | 4.42 | ['4.19', '0.16', '0.16']
w3.f3 | x | `insanely staged @@UNK@@` | 3.48 | ['2.23', '1.79', '0.07']
w3.f4 |   | `@@UNK@@ itself into` | 3.40 | ['0.36', '0.55', '2.85']
w3.f5 |   | `@@PAD@@ even before` | 4.48 | ['0.00', '1.43', '3.37']
w3.f6 | x | `insanely staged @@UNK@@` | 8.40 | ['3.26', '5.20', '0.15']
w3.f7 | x | `to its insanely` | 5.40 | ['3.76', '-0.70', '2.83']
w3.f8 | x | `@@UNK@@ scene ,` | 5.09 | ['0.50', '2.74', '2.14']
w3.f9 | x | `up to its` | 6.18 | ['2.28', '0.70', '3.30']
w3.f10 | x | `pantheon . @@PAD@@` | 7.36 | ['5.50', '2.00', '0.00']
w3.f11 | x | `up to its` | 5.70 | ['4.68', '-1.67', '2.88']
w3.f12 | x | `staged @@UNK@@ scene` | 6.11 | ['0.74', '-0.16', '5.66']
w3.f13 | x | `the art film` | 5.74 | ['4.70', '1.45', '-0.16']
w3.f14 | x | `@@PAD@@ even before` | 6.78 | ['0.00', '2.95', '3.92']
w3.f15 | x | `itself into the` | 4.65 | ['5.08', '0.52', '-0.79']
w3.f16 | x | `to its insanely` | 8.76 | ['1.59', '2.21', '5.34']
w3.f17 | x | `3000 actors appear` | 7.43 | ['8.08', '2.81', '-3.30']
w3.f18 | x | `builds up to` | 5.04 | ['2.69', '1.30', '1.52']
w3.f19 | x | `its insanely staged` | 4.03 | ['3.31', '3.19', '-2.36']

## Original input: 
``` as with so many @@UNK@@ - to - the - max movies of this type , more time appears to have gone into @@UNK@@ the right @@UNK@@ for the @@UNK@@ and the @@UNK@@ of the stars than into the script , which has a handful of smart jokes and not much else . ``` 

## Marked input: 
<pre>as with <span style="background-color: #FFFF00">@</span>so <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>many <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #6698FF">@</span>to - the - max movies <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>this <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>type <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>more <span style="background-color: #6698FF">@</span>time <span style="background-color: #FFFF00">@</span>appears <span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>have <span style="background-color: #6698FF">@</span>gone <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>into <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>right @@UNK@@ for the @@UNK@@ and the <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>stars than <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>into <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>script <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>which has a <span style="background-color: #6698FF">@</span>handful <span style="background-color: #6698FF">@</span>of smart <span style="background-color: #FFFF00">@</span>jokes <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>not <span style="background-color: #FFFF00">@</span>much <span style="background-color: #FFFF00">@</span>else <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ for` | 3.71 | ['1.98', '2.10']
w2.f1 | x | `as with` | 4.46 | ['-0.28', '4.87']
w2.f2 |   | `of smart` | 0.32 | ['-0.19', '1.56']
w2.f3 | x | `much else` | 3.89 | ['0.48', '3.96']
w2.f4 | x | `of smart` | 5.31 | ['1.04', '4.46']
w2.f5 | x | `this type` | 5.41 | ['2.84', '2.87']
w2.f6 |   | `type ,` | 3.29 | ['-0.55', '3.93']
w2.f7 |   | `gone into` | 0.94 | ['0.90', '0.95']
w2.f8 |   | `not much` | 2.66 | ['0.34', '2.54']
w2.f9 | x | `type ,` | 7.20 | ['6.88', '0.34']
w2.f10 |   | `so many` | 2.82 | ['1.41', '1.54']
w2.f11 | x | `stars than` | 3.60 | ['3.73', '0.14']
w2.f12 | x | `smart jokes` | 7.74 | ['-1.00', '8.77']
w2.f13 | x | `this type` | 4.97 | ['2.32', '2.80']
w2.f14 | x | `has a` | 3.42 | ['3.08', '0.38']
w2.f15 | x | `of smart` | 4.33 | ['-3.18', '7.78']
w2.f16 |   | `which has` | 1.89 | ['2.59', '0.07']
w2.f17 |   | `and not` | 2.99 | ['1.02', '2.58']
w2.f18 | x | `and not` | 4.21 | ['3.52', '0.82']
w2.f19 | x | `and the` | 3.56 | ['3.66', '0.20']
w3.f0 |   | `smart jokes and` | 3.04 | ['-0.85', '3.29', '0.99']
w3.f1 | x | `more time appears` | 6.51 | ['4.72', '1.22', '0.95']
w3.f2 | x | `into the script` | 7.93 | ['1.98', '0.94', '5.10']
w3.f3 |   | `so many @@UNK@@` | 0.28 | ['-0.30', '1.13', '0.07']
w3.f4 | x | `have gone into` | 4.82 | ['1.11', '1.22', '2.85']
w3.f5 | x | `with so many` | 7.02 | ['4.85', '-1.15', '3.65']
w3.f6 | x | `with so many` | 5.23 | ['2.33', '1.79', '1.31']
w3.f7 |   | `, which has` | 3.91 | ['1.70', '1.49', '1.21']
w3.f8 |   | `- max movies` | 3.50 | ['0.22', '3.90', '-0.34']
w3.f9 | x | `appears to have` | 4.45 | ['2.46', '0.70', '1.40']
w3.f10 | x | `have gone into` | 5.96 | ['2.81', '2.06', '1.24']
w3.f11 | x | `gone into @@UNK@@` | 5.91 | ['6.92', '-0.07', '-0.75']
w3.f12 | x | `much else .` | 7.70 | ['2.25', '3.98', '1.61']
w3.f13 | x | `the @@UNK@@ of` | 5.41 | ['4.70', '-1.74', '2.71']
w3.f14 | x | `so many @@UNK@@` | 6.60 | ['6.10', '1.97', '-1.37']
w3.f15 | x | `much else .` | 7.08 | ['4.15', '3.70', '-0.60']
w3.f16 | x | `smart jokes and` | 5.32 | ['8.49', '-0.10', '-2.69']
w3.f17 | x | `max movies of` | 6.63 | ['4.79', '0.12', '1.87']
w3.f18 | x | `stars than into` | 5.13 | ['4.90', '0.66', '0.04']
w3.f19 | x | `max movies of` | 9.00 | ['3.54', '2.91', '2.66']

## Original input: 
``` its use of the thriller form to examine the @@UNK@@ ways in which people 's lives cross and change , @@UNK@@ by events seemingly out of their control , is intriguing , provocative stuff . ``` 

## Marked input: 
<pre>its use <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>thriller <span style="background-color: #FFFF00">@</span>form to <span style="background-color: #6698FF">@</span>examine <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>ways <span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span>which <span style="background-color: #6698FF">@</span>people <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>lives <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>cross <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>change <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, @@UNK@@ <span style="background-color: #6698FF">@</span>by <span style="background-color: #6698FF">@</span>events <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>seemingly <span style="background-color: #FFFF00">@</span>out <span style="background-color: #FFFF00">@</span>of their <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>control <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>intriguing <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>provocative <span style="background-color: #FFFF00">@</span>stuff <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `provocative stuff` | 6.77 | ['2.23', '4.92']
w2.f1 |   | `stuff .` | 2.43 | ['4.93', '-2.37']
w2.f2 |   | `thriller form` | 0.07 | ['-0.04', '1.15']
w2.f3 |   | `by events` | 0.75 | ['0.52', '0.79']
w2.f4 | x | `intriguing ,` | 4.07 | ['1.75', '2.50']
w2.f5 | x | `by events` | 3.48 | ['-0.80', '4.59']
w2.f6 | x | `control ,` | 4.85 | ['1.01', '3.93']
w2.f7 |   | `control ,` | 0.88 | ['2.73', '-0.94']
w2.f8 | x | `people 's` | 3.42 | ['-0.19', '3.82']
w2.f9 | x | `form to` | 5.50 | ['0.85', '4.67']
w2.f10 | x | `intriguing ,` | 3.31 | ['3.81', '-0.37']
w2.f11 | x | `examine the` | 3.00 | ['2.84', '0.42']
w2.f12 | x | `to examine` | 4.12 | ['1.53', '2.62']
w2.f13 | x | `@@UNK@@ by` | 3.93 | ['0.61', '3.48']
w2.f14 | x | `in which` | 5.13 | ['-0.13', '5.29']
w2.f15 | x | `events seemingly` | 4.62 | ['4.08', '0.82']
w2.f16 | x | `which people` | 4.10 | ['2.59', '2.28']
w2.f17 |   | `to examine` | 1.42 | ['-1.19', '3.22']
w2.f18 | x | `of their` | 4.40 | ['-1.46', '5.98']
w2.f19 | x | `of their` | 3.72 | ['1.68', '2.34']
w3.f0 |   | `of their control` | 2.31 | ['-0.27', '0.13', '2.84']
w3.f1 | x | `, provocative stuff` | 5.97 | ['1.74', '1.88', '2.73']
w3.f2 |   | `'s lives cross` | 3.29 | ['0.87', '2.39', '0.13']
w3.f3 |   | `stuff . @@PAD@@` | 2.16 | ['2.91', '-0.14', '0.00']
w3.f4 | x | `the @@UNK@@ ways` | 3.64 | ['-0.24', '-0.29', '4.53']
w3.f5 | x | `lives cross and` | 6.64 | ['0.11', '1.04', '5.81']
w3.f6 | x | `'s lives cross` | 4.91 | ['3.62', '0.45', '1.05']
w3.f7 |   | `@@PAD@@ @@PAD@@ its` | 4.09 | ['0.00', '0.00', '4.59']
w3.f8 | x | `by events seemingly` | 6.26 | ['1.21', '3.93', '1.40']
w3.f9 | x | `form to examine` | 4.07 | ['0.47', '0.70', '3.01']
w3.f10 | x | `lives cross and` | 6.19 | ['4.07', '2.54', '-0.27']
w3.f11 | x | `which people 's` | 4.96 | ['-0.30', '4.18', '1.27']
w3.f12 | x | `of their control` | 6.61 | ['-0.72', '0.58', '6.88']
w3.f13 | x | `by events seemingly` | 8.73 | ['1.08', '3.99', '3.91']
w3.f14 | x | `, @@UNK@@ by` | 3.10 | ['-0.18', '0.79', '2.59']
w3.f15 | x | `, is intriguing` | 3.99 | ['1.52', '-0.65', '3.28']
w3.f16 | x | `intriguing , provocative` | 10.61 | ['3.42', '3.78', '3.78']
w3.f17 | x | `form to examine` | 4.29 | ['1.67', '1.66', '1.11']
w3.f18 | x | `use of the` | 5.37 | ['1.17', '2.10', '2.57']
w3.f19 | x | `its use of` | 12.01 | ['3.31', '6.15', '2.66']

## Original input: 
``` @@UNK@@ from laugh - out - loud hilarious to wonder - @@UNK@@ time - it - is tedious . ``` 

## Marked input: 
<pre>@@UNK@@ from laugh <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>out <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>loud <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hilarious <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>wonder <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>- <span style="background-color: #FFFF00">@</span>@@UNK@@ time - it - is <span style="background-color: #6698FF">@</span>tedious <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `loud hilarious` | 3.23 | ['0.68', '2.93']
w2.f1 | x | `loud hilarious` | 6.19 | ['1.04', '5.29']
w2.f2 |   | `loud hilarious` | 0.79 | ['0.69', '1.15']
w2.f3 |   | `is tedious` | 2.03 | ['0.28', '2.30']
w2.f4 |   | `loud hilarious` | 2.51 | ['1.05', '1.65']
w2.f5 | x | `loud hilarious` | 6.14 | ['1.66', '4.78']
w2.f6 |   | `from laugh` | 1.78 | ['-0.44', '2.31']
w2.f7 |   | `tedious .` | 2.02 | ['2.79', '0.14']
w2.f8 |   | `loud hilarious` | 3.03 | ['-0.51', '3.75']
w2.f9 | x | `hilarious to` | 7.28 | ['2.62', '4.67']
w2.f10 |   | `@@UNK@@ from` | 1.15 | ['-0.06', '1.34']
w2.f11 |   | `is tedious` | 1.22 | ['-1.67', '3.16']
w2.f12 |   | `loud hilarious` | 2.84 | ['-1.40', '4.29']
w2.f13 | x | `tedious .` | 4.38 | ['4.52', '0.01']
w2.f14 | x | `is tedious` | 4.34 | ['-0.15', '4.52']
w2.f15 | x | `from laugh` | 3.41 | ['1.33', '2.35']
w2.f16 | x | `is tedious` | 2.79 | ['-0.10', '3.66']
w2.f17 | x | `tedious .` | 3.67 | ['3.82', '0.47']
w2.f18 | x | `loud hilarious` | 3.96 | ['2.01', '2.07']
w2.f19 |   | `loud hilarious` | 1.74 | ['1.03', '1.01']
w3.f0 | x | `out - loud` | 5.94 | ['0.19', '1.13', '5.01']
w3.f1 |   | `@@PAD@@ @@UNK@@ from` | 2.97 | ['0.00', '-0.73', '4.08']
w3.f2 | x | `- out -` | 4.60 | ['2.02', '2.13', '0.54']
w3.f3 |   | `from laugh -` | 0.64 | ['0.06', '1.82', '-0.63']
w3.f4 |   | `@@UNK@@ time -` | 1.33 | ['0.36', '2.07', '-0.73']
w3.f5 | x | `is tedious .` | 5.14 | ['0.80', '0.34', '4.32']
w3.f6 | x | `is tedious .` | 3.68 | ['-0.04', '5.21', '-1.28']
w3.f7 | x | `hilarious to wonder` | 4.40 | ['1.74', '1.18', '1.98']
w3.f8 |   | `from laugh -` | 4.06 | ['5.16', '1.60', '-2.42']
w3.f9 | x | `- loud hilarious` | 6.43 | ['-2.42', '6.37', '2.58']
w3.f10 | x | `tedious . @@PAD@@` | 9.82 | ['7.96', '2.00', '0.00']
w3.f11 | x | `from laugh -` | 5.92 | ['4.70', '2.72', '-1.30']
w3.f12 | x | `is tedious .` | 5.65 | ['0.69', '3.49', '1.61']
w3.f13 |   | `to wonder -` | 2.29 | ['1.07', '0.60', '0.87']
w3.f14 | x | `- is tedious` | 9.48 | ['-0.66', '0.90', '9.33']
w3.f15 |   | `time - it` | 1.97 | ['2.01', '-0.37', '0.49']
w3.f16 | x | `- loud hilarious` | 5.09 | ['1.48', '2.08', '1.91']
w3.f17 | x | `- is tedious` | 9.07 | ['-0.63', '2.35', '7.50']
w3.f18 | x | `loud hilarious to` | 5.38 | ['0.33', '3.99', '1.52']
w3.f19 | x | `from laugh -` | 4.40 | ['3.07', '2.95', '-1.51']

## Original input: 
``` fairy - tale formula , serves as a paper @@UNK@@ for some very good acting , dialogue , comedy , direction and especially charm . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>fairy <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>tale <span style="background-color: #6698FF">@</span>formula <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>serves <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>as <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>paper <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>for some <span style="background-color: #6698FF">@</span>very <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>good <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>acting <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>dialogue <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>comedy <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>direction <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and especially <span style="background-color: #FFFF00">@</span>charm <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `for some` | 3.95 | ['1.57', '2.75']
w2.f1 | x | `a paper` | 6.13 | ['2.95', '3.31']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `- tale` | 3.48 | ['0.84', '3.19']
w2.f4 | x | `comedy ,` | 3.93 | ['1.62', '2.50']
w2.f5 | x | `charm .` | 5.41 | ['8.12', '-2.41']
w2.f6 | x | `formula ,` | 4.82 | ['0.98', '3.93']
w2.f7 |   | `a paper` | 0.54 | ['-2.07', '3.52']
w2.f8 |   | `acting ,` | 1.89 | ['2.90', '-0.79']
w2.f9 |   | `dialogue ,` | 4.32 | ['4.00', '0.34']
w2.f10 |   | `a paper` | 1.82 | ['1.97', '-0.01']
w2.f11 | x | `for some` | 3.08 | ['-0.47', '3.82']
w2.f12 | x | `, dialogue` | 5.98 | ['-0.98', '6.99']
w2.f13 | x | `serves as` | 4.25 | ['3.10', '1.31']
w2.f14 | x | `a paper` | 6.02 | ['-2.64', '8.69']
w2.f15 | x | `acting ,` | 5.05 | ['5.63', '-0.31']
w2.f16 | x | `good acting` | 3.12 | ['2.10', '1.78']
w2.f17 | x | `good acting` | 3.72 | ['-1.76', '6.09']
w2.f18 |   | `and especially` | 2.57 | ['3.52', '-0.82']
w2.f19 | x | `and especially` | 4.53 | ['3.66', '1.17']
w3.f0 | x | `- tale formula` | 5.64 | ['0.15', '3.79', '2.09']
w3.f1 | x | `acting , dialogue` | 5.52 | ['4.42', '0.90', '0.58']
w3.f2 | x | `, dialogue ,` | 6.40 | ['2.60', '2.56', '1.32']
w3.f3 |   | `some very good` | 1.05 | ['-2.30', '1.66', '2.29']
w3.f4 | x | `some very good` | 3.52 | ['0.52', '-0.56', '3.93']
w3.f5 |   | `especially charm .` | 3.19 | ['-0.78', '-0.02', '4.32']
w3.f6 | x | `tale formula ,` | 4.43 | ['4.89', '1.33', '-1.59']
w3.f7 |   | `very good acting` | 3.19 | ['-0.88', '1.93', '2.63']
w3.f8 | x | `good acting ,` | 7.68 | ['0.03', '5.80', '2.14']
w3.f9 | x | `very good acting` | 4.95 | ['4.11', '-2.37', '3.32']
w3.f10 | x | `- tale formula` | 5.38 | ['-0.37', '3.86', '2.04']
w3.f11 | x | `serves as a` | 4.62 | ['0.61', '1.42', '2.78']
w3.f12 | x | `fairy - tale` | 8.37 | ['2.41', '2.81', '3.27']
w3.f13 |   | `direction and especially` | 4.04 | ['1.05', '0.60', '2.64']
w3.f14 | x | `@@PAD@@ @@PAD@@ fairy` | 5.33 | ['0.00', '0.00', '5.42']
w3.f15 | x | `, comedy ,` | 5.18 | ['1.52', '1.12', '2.70']
w3.f16 | x | `formula , serves` | 6.15 | ['1.52', '3.78', '1.23']
w3.f17 | x | `for some very` | 7.02 | ['0.84', '4.63', '1.70']
w3.f18 |   | `very good acting` | 2.86 | ['1.40', '0.40', '1.53']
w3.f19 | x | `good acting ,` | 5.57 | ['1.75', '2.85', '1.08']

## Original input: 
``` there has always been something likable about the marquis de sade . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>there <span style="background-color: #6698FF">@</span>has <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>always <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>been <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>something <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>likable <span style="background-color: #6698FF">@</span>about <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>marquis <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>de <span style="background-color: #6698FF">@</span>sade <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `always been` | 10.64 | ['5.64', '5.38']
w2.f1 | x | `always been` | 5.44 | ['6.95', '-1.38']
w2.f2 |   | `de sade` | 0.37 | ['0.36', '1.06']
w2.f3 |   | `always been` | 1.72 | ['-0.08', '2.35']
w2.f4 |   | `always been` | 1.99 | ['6.10', '-3.92']
w2.f5 |   | `been something` | 2.14 | ['-0.69', '3.14']
w2.f6 |   | `something likable` | 2.62 | ['1.71', '1.01']
w2.f7 |   | `de sade` | 0.89 | ['0.16', '1.63']
w2.f8 | x | `always been` | 3.89 | ['3.28', '0.83']
w2.f9 |   | `something likable` | 3.19 | ['2.99', '0.21']
w2.f10 |   | `something likable` | 2.75 | ['0.61', '2.28']
w2.f11 |   | `likable about` | 2.83 | ['3.20', '-0.09']
w2.f12 | x | `been something` | 3.92 | ['-1.86', '5.82']
w2.f13 |   | `been something` | 2.14 | ['2.92', '-0.63']
w2.f14 |   | `has always` | 3.18 | ['3.08', '0.13']
w2.f15 |   | `something likable` | 2.34 | ['-1.66', '4.28']
w2.f16 |   | `something likable` | 2.64 | ['1.03', '2.38']
w2.f17 | x | `there has` | 4.11 | ['2.47', '2.26']
w2.f18 |   | `. @@PAD@@` | 0.86 | ['0.99', '0.00']
w2.f19 |   | `marquis de` | 2.40 | ['-0.24', '2.94']
w3.f0 |   | `has always been` | 2.36 | ['1.40', '1.05', '0.30']
w3.f1 |   | `been something likable` | 2.34 | ['1.71', '1.29', '-0.28']
w3.f2 | x | `has always been` | 5.14 | ['-0.05', '4.22', '1.06']
w3.f3 |   | `has always been` | 0.13 | ['-0.86', '0.72', '0.87']
w3.f4 |   | `has always been` | 2.74 | ['0.79', '1.93', '0.37']
w3.f5 |   | `de sade .` | 1.46 | ['-1.82', '-0.72', '4.32']
w3.f6 |   | `the marquis de` | 2.30 | ['-0.32', '1.31', '1.52']
w3.f7 |   | `@@PAD@@ there has` | 1.83 | ['0.00', '1.12', '1.21']
w3.f8 | x | `there has always` | 5.00 | ['-0.38', '3.82', '1.85']
w3.f9 | x | `@@PAD@@ @@PAD@@ there` | 4.23 | ['0.00', '0.00', '4.33']
w3.f10 |   | `always been something` | 2.65 | ['0.13', '2.71', '-0.04']
w3.f11 | x | `has always been` | 8.60 | ['2.49', '2.43', '3.87']
w3.f12 | x | `the marquis de` | 5.99 | ['2.43', '1.90', '1.79']
w3.f13 |   | `the marquis de` | 4.31 | ['4.70', '2.09', '-2.24']
w3.f14 | x | `has always been` | 6.00 | ['2.46', '0.12', '3.51']
w3.f15 |   | `de sade .` | 3.37 | ['-0.49', '4.63', '-0.60']
w3.f16 |   | `@@PAD@@ there has` | 1.53 | ['0.00', '-1.00', '2.91']
w3.f17 |   | `the marquis de` | 3.70 | ['-1.17', '3.60', '1.43']
w3.f18 | x | `likable about the` | 6.44 | ['2.97', '1.36', '2.57']
w3.f19 |   | `been something likable` | 2.94 | ['-0.40', '0.38', '3.09']

## Original input: 
``` a gangster movie with the capacity to surprise . ``` 

## Marked input: 
<pre>a <span style="background-color: #6698FF">@</span>gangster <span style="background-color: #6698FF">@</span>movie <span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>capacity to <span style="background-color: #6698FF">@</span>surprise <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `a gangster` | 3.63 | ['1.11', '2.89']
w2.f1 | x | `movie with` | 4.84 | ['0.10', '4.87']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `gangster movie` | 0.15 | ['-0.78', '1.49']
w2.f4 |   | `capacity to` | 2.34 | ['2.98', '-0.45']
w2.f5 |   | `the capacity` | 1.85 | ['1.16', '1.00']
w2.f6 |   | `with the` | 1.29 | ['1.15', '0.24']
w2.f7 |   | `gangster movie` | 1.95 | ['0.85', '2.01']
w2.f8 |   | `@@PAD@@ a` | 2.34 | ['0.00', '2.56']
w2.f9 | x | `capacity to` | 7.11 | ['2.45', '4.67']
w2.f10 |   | `movie with` | 0.71 | ['0.59', '0.25']
w2.f11 |   | `with the` | 2.51 | ['2.35', '0.42']
w2.f12 | x | `gangster movie` | 4.47 | ['3.28', '1.23']
w2.f13 |   | `movie with` | 2.04 | ['3.71', '-1.53']
w2.f14 |   | `gangster movie` | 0.89 | ['0.26', '0.66']
w2.f15 |   | `gangster movie` | 0.11 | ['1.73', '-1.35']
w2.f16 |   | `to surprise` | 0.89 | ['-1.25', '2.91']
w2.f17 |   | `to surprise` | 0.63 | ['-1.19', '2.43']
w2.f18 |   | `capacity to` | 3.13 | ['0.76', '2.50']
w2.f19 |   | `capacity to` | 1.88 | ['1.06', '1.12']
w3.f0 | x | `capacity to surprise` | 4.50 | ['3.28', '-1.42', '3.03']
w3.f1 |   | `gangster movie with` | 2.44 | ['0.93', '2.75', '-0.87']
w3.f2 | x | `a gangster movie` | 4.80 | ['1.87', '-0.91', '3.93']
w3.f3 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.45']
w3.f4 |   | `movie with the` | 2.75 | ['2.80', '0.70', '-0.38']
w3.f5 |   | `capacity to surprise` | 3.65 | ['0.42', '-0.47', '4.03']
w3.f6 | x | `gangster movie with` | 5.86 | ['3.83', '4.49', '-2.25']
w3.f7 |   | `gangster movie with` | 2.64 | ['0.77', '2.56', '-0.19']
w3.f8 |   | `a gangster movie` | 3.41 | ['0.66', '3.37', '-0.34']
w3.f9 |   | `@@PAD@@ @@PAD@@ a` | 1.03 | ['0.00', '0.00', '1.13']
w3.f10 |   | `surprise . @@PAD@@` | 2.54 | ['0.68', '2.00', '0.00']
w3.f11 |   | `gangster movie with` | 3.56 | ['0.66', '0.39', '2.70']
w3.f12 | x | `@@PAD@@ a gangster` | 5.95 | ['0.00', '-0.46', '6.54']
w3.f13 |   | `the capacity to` | 3.36 | ['4.70', '-1.29', '0.20']
w3.f14 |   | `gangster movie with` | 2.00 | ['1.85', '1.53', '-1.29']
w3.f15 |   | `movie with the` | 0.76 | ['-2.13', '3.85', '-0.79']
w3.f16 |   | `@@PAD@@ a gangster` | 0.47 | ['0.00', '0.35', '0.49']
w3.f17 | x | `capacity to surprise` | 5.82 | ['0.64', '1.66', '3.68']
w3.f18 |   | `movie with the` | 3.09 | ['-1.34', '2.32', '2.57']
w3.f19 |   | `with the capacity` | 2.32 | ['3.68', '-2.27', '1.03']

## Original input: 
``` a tone poem of @@UNK@@ . ``` 

## Marked input: 
<pre>a tone <span style="background-color: #FFFF00">@</span>poem <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>@@UNK@@ .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `tone poem` | 1.37 | ['1.69', '0.05']
w2.f1 | x | `tone poem` | 4.89 | ['1.95', '3.07']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f4 |   | `a tone` | 2.29 | ['2.27', '0.20']
w2.f5 |   | `poem of` | 1.33 | ['-0.13', '1.76']
w2.f6 |   | `a tone` | 1.34 | ['0.54', '0.90']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `@@PAD@@ a` | 2.34 | ['0.00', '2.56']
w2.f9 |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 |   | `tone poem` | 0.88 | ['-1.36', '2.38']
w2.f11 |   | `a tone` | 1.24 | ['0.43', '1.08']
w2.f12 |   | `tone poem` | 0.91 | ['0.74', '0.21']
w2.f13 |   | `@@PAD@@ a` | 1.30 | ['0.00', '1.45']
w2.f14 |   | `@@UNK@@ .` | 1.04 | ['0.69', '0.39']
w2.f15 |   | `tone poem` | 2.19 | ['-0.59', '3.05']
w2.f16 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f17 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f18 |   | `a tone` | 1.98 | ['0.76', '1.34']
w2.f19 | x | `tone poem` | 3.24 | ['0.40', '3.14']
w3.f0 |   | `@@PAD@@ a tone` | 0.88 | ['0.00', '3.29', '-2.02']
w3.f1 |   | `a tone poem` | 3.27 | ['-1.76', '2.16', '3.25']
w3.f2 |   | `@@PAD@@ @@PAD@@ a` | 2.19 | ['0.00', '0.00', '2.27']
w3.f3 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.45']
w3.f4 |   | `a tone poem` | 2.29 | ['-1.11', '2.44', '1.31']
w3.f5 |   | `tone poem of` | 2.65 | ['0.28', '3.18', '-0.47']
w3.f6 |   | `a tone poem` | 2.53 | ['1.76', '1.12', '-0.15']
w3.f7 |   | `poem of @@UNK@@` | 1.57 | ['1.97', '0.18', '-0.07']
w3.f8 |   | `tone poem of` | 0.33 | ['0.43', '0.23', '-0.05']
w3.f9 |   | `@@PAD@@ @@PAD@@ a` | 1.03 | ['0.00', '0.00', '1.13']
w3.f10 |   | `@@UNK@@ . @@PAD@@` | 2.18 | ['0.33', '2.00', '0.00']
w3.f11 |   | `@@PAD@@ @@PAD@@ a` | 2.59 | ['0.00', '0.00', '2.78']
w3.f12 |   | `tone poem of` | 1.68 | ['-0.29', '1.41', '0.69']
w3.f13 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '0.18']
w3.f14 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-2.42']
w3.f15 |   | `@@PAD@@ a tone` | 0.72 | ['0.00', '-0.09', '0.98']
w3.f16 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-2.12']
w3.f17 |   | `of @@UNK@@ .` | 0.57 | ['-1.64', '1.39', '0.98']
w3.f18 |   | `tone poem of` | 2.45 | ['1.54', '1.62', '-0.25']
w3.f19 | x | `a tone poem` | 4.49 | ['3.70', '-0.20', '1.11']

## Original input: 
``` the film just might turn on many people to opera , in general , an art form at once visceral and spiritual , wonderfully vulgar and @@UNK@@ lofty -- and as emotionally grand as life . ``` 

## Marked input: 
<pre>the film just might <span style="background-color: #6698FF">@</span>turn <span style="background-color: #6698FF">@</span>on <span style="background-color: #6698FF">@</span>many <span style="background-color: #FFFF00">@</span>people <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span>opera <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span>general <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>an <span style="background-color: #6698FF">@</span>art <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>form <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>at <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>once <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>visceral <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>spiritual <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>wonderfully <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>vulgar <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span>@@UNK@@ lofty -- and as emotionally grand <span style="background-color: #FFFF00">@</span>as <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>life <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `on many` | 4.80 | ['3.79', '1.38']
w2.f1 | x | `emotionally grand` | 5.14 | ['0.62', '4.66']
w2.f2 |   | `art form` | 0.92 | ['0.82', '1.15']
w2.f3 |   | `just might` | 1.76 | ['1.31', '1.01']
w2.f4 | x | `grand as` | 5.12 | ['6.46', '-1.15']
w2.f5 | x | `an art` | 5.34 | ['3.50', '2.15']
w2.f6 | x | `spiritual ,` | 6.42 | ['2.59', '3.93']
w2.f7 |   | `once visceral` | 1.58 | ['-0.02', '2.51']
w2.f8 |   | `in general` | 2.36 | ['-0.37', '2.95']
w2.f9 |   | `people to` | 4.52 | ['-0.14', '4.67']
w2.f10 | x | `, wonderfully` | 4.66 | ['-0.72', '5.52']
w2.f11 | x | `wonderfully vulgar` | 3.02 | ['1.07', '2.23']
w2.f12 | x | `at once` | 3.66 | ['-0.03', '3.73']
w2.f13 |   | `spiritual ,` | 2.97 | ['0.94', '2.18']
w2.f14 | x | `form at` | 3.65 | ['0.69', '2.99']
w2.f15 | x | `emotionally grand` | 6.15 | ['3.05', '3.37']
w2.f16 | x | `once visceral` | 3.59 | ['1.07', '3.28']
w2.f17 | x | `once visceral` | 4.97 | ['1.62', '3.97']
w2.f18 |   | `art form` | 2.63 | ['0.05', '2.70']
w2.f19 | x | `form at` | 3.41 | ['2.00', '1.70']
w3.f0 | x | `just might turn` | 5.02 | ['3.41', '0.19', '1.81']
w3.f1 | x | `spiritual , wonderfully` | 9.97 | ['4.39', '0.90', '5.07']
w3.f2 | x | `, an art` | 4.68 | ['2.60', '1.76', '0.41']
w3.f3 |   | `might turn on` | 2.33 | ['1.67', '0.69', '0.57']
w3.f4 | x | `art form at` | 4.21 | ['0.88', '1.80', '1.89']
w3.f5 | x | `once visceral and` | 8.15 | ['-1.09', '3.75', '5.81']
w3.f6 | x | `form at once` | 3.92 | ['0.50', '1.79', '1.84']
w3.f7 | x | `to opera ,` | 5.20 | ['3.76', '0.75', '1.18']
w3.f8 |   | `an art form` | 4.28 | ['1.44', '2.12', '1.01']
w3.f9 | x | `in general ,` | 5.16 | ['1.57', '0.64', '3.06']
w3.f10 | x | `people to opera` | 6.61 | ['3.67', '1.69', '1.40']
w3.f11 | x | `many people to` | 5.71 | ['-0.33', '4.18', '2.06']
w3.f12 | x | `grand as life` | 5.29 | ['0.61', '4.53', '0.28']
w3.f13 |   | `the film just` | 4.38 | ['4.70', '-1.39', '1.32']
w3.f14 | x | `visceral and spiritual` | 5.08 | ['1.13', '1.09', '2.96']
w3.f15 | x | `an art form` | 3.93 | ['-0.98', '1.14', '3.94']
w3.f16 | x | `spiritual , wonderfully` | 5.00 | ['-0.51', '3.78', '2.10']
w3.f17 | x | `spiritual , wonderfully` | 5.50 | ['0.66', '3.34', '1.66']
w3.f18 | x | `an art form` | 4.32 | ['0.67', '0.59', '3.53']
w3.f19 | x | `and spiritual ,` | 4.58 | ['3.50', '0.12', '1.08']

## Original input: 
``` @@UNK@@ . . . revenge is sweet ! ``` 

## Marked input: 
<pre>@@UNK@@ . . . revenge is sweet <span style="background-color: #6698FF">@</span>!</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `revenge is` | 2.96 | ['4.11', '-0.78']
w2.f1 | x | `sweet !` | 5.87 | ['3.11', '2.88']
w2.f2 |   | `sweet !` | 0.69 | ['0.85', '0.88']
w2.f3 |   | `is sweet` | 1.30 | ['0.28', '1.57']
w2.f4 |   | `revenge is` | 0.85 | ['3.20', '-2.16']
w2.f5 |   | `. revenge` | 1.18 | ['0.67', '0.81']
w2.f6 |   | `! @@PAD@@` | 1.60 | ['1.70', '0.00']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `sweet !` | 1.65 | ['-0.76', '2.63']
w2.f9 |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 | x | `sweet !` | 4.42 | ['2.07', '2.48']
w2.f11 |   | `revenge is` | 2.29 | ['2.94', '-0.39']
w2.f12 |   | `is sweet` | 0.19 | ['-0.59', '0.82']
w2.f13 |   | `revenge is` | 1.14 | ['0.79', '0.50']
w2.f14 |   | `@@UNK@@ .` | 1.04 | ['0.69', '0.39']
w2.f15 | x | `sweet !` | 4.82 | ['2.06', '3.03']
w2.f16 |   | `sweet !` | 0.82 | ['2.10', '-0.52']
w2.f17 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f18 |   | `. revenge` | 1.57 | ['0.99', '0.71']
w2.f19 |   | `is sweet` | 0.92 | ['0.37', '0.85']
w3.f0 |   | `revenge is sweet` | 2.32 | ['0.26', '2.08', '0.37']
w3.f1 |   | `is sweet !` | 1.55 | ['1.18', '0.67', '0.07']
w3.f2 |   | `sweet ! @@PAD@@` | 1.88 | ['1.98', '-0.02', '0.00']
w3.f3 |   | `! @@PAD@@ @@PAD@@` | 0.27 | ['0.87', '0.00', '0.00']
w3.f4 | x | `sweet ! @@PAD@@` | 4.21 | ['3.34', '1.24', '0.00']
w3.f5 |   | `@@UNK@@ . .` | 3.67 | ['0.08', '-0.40', '4.32']
w3.f6 | x | `is sweet !` | 6.30 | ['-0.04', '3.26', '3.29']
w3.f7 |   | `revenge is sweet` | 1.54 | ['0.06', '-1.18', '3.16']
w3.f8 |   | `revenge is sweet` | 4.09 | ['0.50', '4.71', '-0.83']
w3.f9 |   | `. revenge is` | 2.95 | ['0.67', '1.89', '0.49']
w3.f10 |   | `. . revenge` | 2.31 | ['0.09', '2.00', '0.37']
w3.f11 |   | `. revenge is` | 1.89 | ['-0.15', '1.09', '1.14']
w3.f12 |   | `revenge is sweet` | 1.66 | ['2.28', '1.47', '-1.95']
w3.f13 |   | `is sweet !` | 2.46 | ['1.15', '1.28', '0.28']
w3.f14 |   | `. revenge is` | 1.71 | ['-1.71', '0.88', '2.63']
w3.f15 |   | `revenge is sweet` | 0.65 | ['1.51', '-0.65', '-0.05']
w3.f16 |   | `sweet ! @@PAD@@` | 0.90 | ['-0.58', '1.86', '0.00']
w3.f17 |   | `@@PAD@@ @@UNK@@ .` | 2.21 | ['0.00', '1.39', '0.98']
w3.f18 |   | `@@PAD@@ @@PAD@@ @@UNK@@` | 0.00 | ['0.00', '0.00', '-0.23']
w3.f19 |   | `revenge is sweet` | 2.72 | ['-0.80', '3.62', '0.02']

## Original input: 
``` the @@UNK@@ @@UNK@@ that [ deniro ] brings to this part only @@UNK@@ the fuzzy sentimentality of the movie itself , which feels , as it @@UNK@@ toward the end , less like a movie than like the filmed reading of a script in need of @@UNK@@ . ``` 

## Marked input: 
<pre>the @@UNK@@ @@UNK@@ that [ <span style="background-color: #6698FF">@</span>deniro <span style="background-color: #6698FF">@</span>] <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>brings <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>this <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>part <span style="background-color: #FFFF00">@</span>only <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>fuzzy <span style="background-color: #FFFF00">@</span>sentimentality <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>movie itself , which feels <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>as it @@UNK@@ toward the <span style="background-color: #FFFF00">@</span>end <span style="background-color: #FFFF00">@</span>, less like <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>movie <span style="background-color: #6698FF">@</span>than <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>like <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span>filmed <span style="background-color: #6698FF">@</span>reading <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>a script <span style="background-color: #FFFF00">@</span>in <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>need <span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `deniro ]` | 5.01 | ['-1.00', '6.38']
w2.f1 | x | `brings to` | 5.50 | ['6.27', '-0.64']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `this part` | 0.82 | ['0.36', '1.02']
w2.f4 | x | `a script` | 4.01 | ['2.27', '1.93']
w2.f5 | x | `need of` | 5.44 | ['3.98', '1.76']
w2.f6 |   | `end ,` | 3.46 | ['-0.37', '3.93']
w2.f7 | x | `] brings` | 2.88 | ['1.67', '2.12']
w2.f8 | x | `a script` | 3.85 | ['0.88', '3.18']
w2.f9 | x | `script in` | 8.47 | ['6.59', '1.89']
w2.f10 |   | `] brings` | 1.43 | ['2.01', '-0.44']
w2.f11 |   | `reading of` | 2.08 | ['1.41', '0.95']
w2.f12 | x | `which feels` | 4.55 | ['-1.03', '5.62']
w2.f13 | x | `only @@UNK@@` | 6.55 | ['6.80', '-0.10']
w2.f14 | x | `[ deniro` | 7.61 | ['3.78', '3.87']
w2.f15 |   | `this part` | 2.96 | ['3.03', '0.21']
w2.f16 |   | `deniro ]` | 1.74 | ['0.95', '1.55']
w2.f17 | x | `that [` | 5.12 | ['0.08', '5.65']
w2.f18 |   | `] brings` | 3.22 | ['2.35', '0.99']
w2.f19 | x | `toward the` | 3.43 | ['3.53', '0.20']
w3.f0 | x | `less like a` | 5.59 | ['8.00', '0.78', '-2.80']
w3.f1 | x | `brings to this` | 5.44 | ['6.45', '0.48', '-1.11']
w3.f2 | x | `a movie than` | 4.68 | ['1.87', '1.21', '1.68']
w3.f3 | x | `part only @@UNK@@` | 2.84 | ['0.55', '2.83', '0.07']
w3.f4 | x | `movie than like` | 5.28 | ['2.80', '-0.39', '3.23']
w3.f5 |   | `this part only` | 2.57 | ['0.94', '0.61', '1.35']
w3.f6 | x | `a movie than` | 3.83 | ['1.76', '4.49', '-2.20']
w3.f7 | x | `to this part` | 5.47 | ['3.76', '0.43', '1.77']
w3.f8 | x | `the fuzzy sentimentality` | 6.71 | ['1.05', '4.28', '1.66']
w3.f9 |   | `toward the end` | 3.10 | ['1.93', '-0.12', '1.39']
w3.f10 |   | `of a script` | 3.81 | ['2.92', '1.32', '-0.28']
w3.f11 | x | `] brings to` | 4.31 | ['2.11', '0.33', '2.06']
w3.f12 | x | `the filmed reading` | 5.31 | ['2.43', '2.03', '0.98']
w3.f13 |   | `the fuzzy sentimentality` | 4.67 | ['4.70', '0.52', '-0.30']
w3.f14 | x | `[ deniro ]` | 6.10 | ['3.25', '2.23', '0.71']
w3.f15 |   | `the end ,` | 3.29 | ['-0.02', '0.78', '2.70']
w3.f16 | x | `to this part` | 4.67 | ['1.59', '1.31', '2.15']
w3.f17 | x | `fuzzy sentimentality of` | 5.35 | ['0.91', '2.73', '1.87']
w3.f18 |   | `sentimentality of the` | 3.18 | ['-1.02', '2.10', '2.57']
w3.f19 | x | `deniro ] brings` | 4.49 | ['1.52', '0.09', '2.99']

## Original input: 
``` @@UNK@@ you with its open - @@UNK@@ and surprises . ``` 

## Marked input: 
<pre>@@UNK@@ you <span style="background-color: #FFFF00">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>its <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>open <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>surprises <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ you` | 2.94 | ['1.98', '1.33']
w2.f1 | x | `you with` | 6.71 | ['1.97', '4.87']
w2.f2 |   | `you with` | 0.09 | ['0.78', '0.36']
w2.f3 |   | `its open` | 0.68 | ['-0.44', '1.68']
w2.f4 |   | `surprises .` | 1.43 | ['1.64', '-0.03']
w2.f5 |   | `with its` | 1.76 | ['0.84', '1.22']
w2.f6 |   | `with its` | 2.60 | ['1.15', '1.55']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 | x | `you with` | 5.61 | ['2.33', '3.50']
w2.f9 |   | `@@UNK@@ and` | 1.85 | ['2.38', '-0.51']
w2.f10 | x | `you with` | 4.28 | ['4.16', '0.25']
w2.f11 |   | `and surprises` | 1.99 | ['0.34', '1.92']
w2.f12 |   | `its open` | 0.80 | ['-0.82', '1.66']
w2.f13 | x | `surprises .` | 3.20 | ['3.34', '0.01']
w2.f14 |   | `with its` | 2.35 | ['0.69', '1.69']
w2.f15 | x | `@@UNK@@ you` | 4.13 | ['-1.59', '5.99']
w2.f16 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f17 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f18 | x | `and surprises` | 4.04 | ['3.52', '0.65']
w2.f19 |   | `and surprises` | 2.97 | ['3.66', '-0.40']
w3.f0 |   | `you with its` | 1.48 | ['-2.55', '3.34', '1.08']
w3.f1 | x | `its open -` | 4.34 | ['0.80', '2.27', '1.66']
w3.f2 |   | `- @@UNK@@ and` | 1.75 | ['2.02', '-0.65', '0.47']
w3.f3 |   | `and surprises .` | 0.22 | ['-0.66', '2.24', '-0.75']
w3.f4 |   | `@@PAD@@ @@UNK@@ you` | 1.82 | ['0.00', '-0.29', '2.46']
w3.f5 | x | `with its open` | 5.52 | ['4.85', '-0.89', '1.89']
w3.f6 |   | `with its open` | 2.43 | ['2.33', '0.89', '-0.59']
w3.f7 |   | `and surprises .` | 1.60 | ['-0.53', '2.45', '0.18']
w3.f8 |   | `@@UNK@@ and surprises` | 4.18 | ['0.50', '0.71', '3.26']
w3.f9 |   | `you with its` | 2.74 | ['-0.60', '0.14', '3.30']
w3.f10 |   | `surprises . @@PAD@@` | 3.15 | ['1.29', '2.00', '0.00']
w3.f11 | x | `you with its` | 5.06 | ['1.07', '1.30', '2.88']
w3.f12 |   | `@@UNK@@ you with` | 2.64 | ['-0.75', '0.84', '2.68']
w3.f13 |   | `@@UNK@@ and surprises` | 3.01 | ['-0.04', '0.60', '2.70']
w3.f14 |   | `@@UNK@@ and surprises` | 1.11 | ['-0.34', '1.09', '0.45']
w3.f15 |   | `you with its` | 2.30 | ['-1.55', '3.85', '0.17']
w3.f16 |   | `@@PAD@@ @@PAD@@ @@UNK@@` | 0.00 | ['0.00', '0.00', '-3.52']
w3.f17 |   | `@@PAD@@ @@UNK@@ you` | 1.02 | ['0.00', '1.39', '-0.21']
w3.f18 | x | `open - @@UNK@@` | 3.77 | ['3.49', '0.97', '-0.23']
w3.f19 | x | `with its open` | 6.64 | ['3.68', '0.85', '2.22']

## Original input: 
``` @@UNK@@ rude , @@UNK@@ funny , @@UNK@@ sympathetic to the damage it @@UNK@@ , the film has in @@UNK@@ @@UNK@@ a pitch - perfect @@UNK@@ . ``` 

## Marked input: 
<pre>@@UNK@@ rude <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>funny <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>sympathetic <span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>damage <span style="background-color: #6698FF">@</span>it <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>, the film has in <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ a pitch - <span style="background-color: #FFFF00">@</span>perfect <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `a pitch` | 2.37 | ['1.11', '1.64']
w2.f1 | x | `@@UNK@@ funny` | 3.77 | ['-0.88', '4.79']
w2.f2 |   | `damage it` | 0.37 | ['1.12', '0.30']
w2.f3 |   | `sympathetic to` | 0.89 | ['1.49', '-0.04']
w2.f4 | x | `- perfect` | 4.29 | ['-1.35', '5.82']
w2.f5 | x | `sympathetic to` | 4.33 | ['2.25', '2.39']
w2.f6 | x | `funny ,` | 5.60 | ['1.77', '3.93']
w2.f7 |   | `damage it` | 1.50 | ['2.62', '-0.22']
w2.f8 |   | `a pitch` | 2.61 | ['0.88', '1.94']
w2.f9 |   | `@@UNK@@ funny` | 3.83 | ['2.38', '1.46']
w2.f10 |   | `- perfect` | 2.24 | ['1.18', '1.19']
w2.f11 |   | `damage it` | 1.36 | ['0.35', '1.28']
w2.f12 | x | `the damage` | 4.69 | ['0.53', '4.19']
w2.f13 | x | `damage it` | 3.93 | ['3.11', '0.96']
w2.f14 | x | `has in` | 3.65 | ['3.08', '0.61']
w2.f15 |   | `funny ,` | 1.97 | ['2.55', '-0.31']
w2.f16 |   | `film has` | 0.21 | ['0.91', '0.07']
w2.f17 |   | `film has` | 0.33 | ['-1.32', '2.26']
w2.f18 |   | `sympathetic to` | 2.03 | ['-0.34', '2.50']
w2.f19 | x | `@@UNK@@ funny` | 3.49 | ['0.39', '3.39']
w3.f0 |   | `@@UNK@@ a pitch` | 2.50 | ['-2.16', '3.29', '1.76']
w3.f1 |   | `, @@UNK@@ sympathetic` | 1.33 | ['1.74', '-0.73', '0.69']
w3.f2 |   | `perfect @@UNK@@ .` | 0.74 | ['0.64', '-0.65', '0.84']
w3.f3 |   | `@@PAD@@ @@UNK@@ rude` | 0.79 | ['0.00', '-0.06', '1.46']
w3.f4 |   | `the damage it` | 1.44 | ['-0.24', '1.70', '0.34']
w3.f5 |   | `- perfect @@UNK@@` | 2.62 | ['0.99', '2.89', '-0.93']
w3.f6 |   | `a pitch -` | 1.61 | ['1.76', '0.61', '-0.54']
w3.f7 |   | `to the damage` | 3.27 | ['3.76', '-0.92', '0.92']
w3.f8 | x | `@@UNK@@ rude ,` | 4.51 | ['0.50', '2.16', '2.14']
w3.f9 |   | `@@PAD@@ @@PAD@@ @@UNK@@` | 2.03 | ['0.00', '0.00', '2.13']
w3.f10 |   | `@@UNK@@ . @@PAD@@` | 2.18 | ['0.33', '2.00', '0.00']
w3.f11 |   | `damage it @@UNK@@` | 1.48 | ['1.51', '0.91', '-0.75']
w3.f12 |   | `the damage it` | 2.96 | ['2.43', '-0.28', '0.94']
w3.f13 | x | `funny , @@UNK@@` | 5.96 | ['5.96', '1.92', '-1.67']
w3.f14 | x | `sympathetic to the` | 3.24 | ['2.50', '-0.41', '1.24']
w3.f15 |   | `pitch - perfect` | 3.26 | ['0.59', '-0.37', '3.20']
w3.f16 |   | `to the damage` | 2.26 | ['1.59', '0.10', '0.96']
w3.f17 |   | `sympathetic to the` | 3.61 | ['0.86', '1.66', '1.25']
w3.f18 |   | `@@UNK@@ sympathetic to` | 0.49 | ['-2.55', '1.99', '1.52']
w3.f19 | x | `pitch - perfect` | 5.14 | ['2.15', '1.48', '1.62']

## Original input: 
``` the merchant - @@UNK@@ team continues to @@UNK@@ @@UNK@@ everything we hold dear about cinema , only now it 's @@UNK@@ to @@UNK@@ up so that it can do even more damage . ``` 

## Marked input: 
<pre>the merchant <span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>team <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>continues <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>@@UNK@@ everything <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>we <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hold <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>dear <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>about <span style="background-color: #FFFF00">@</span>cinema <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>only <span style="background-color: #FFFF00">@</span>now <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>it <span style="background-color: #6698FF">@</span>'s @@UNK@@ to <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>up <span style="background-color: #FFFF00">@</span>so <span style="background-color: #FFFF00">@</span>that it <span style="background-color: #6698FF">@</span>can <span style="background-color: #6698FF">@</span>do <span style="background-color: #6698FF">@</span>even <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>more <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>damage <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ team` | 6.00 | ['1.98', '4.40']
w2.f1 | x | `hold dear` | 5.49 | ['3.50', '2.12']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `do even` | 2.62 | ['0.43', '2.75']
w2.f4 | x | `do even` | 4.86 | ['3.16', '1.88']
w2.f5 | x | `we hold` | 6.11 | ['4.53', '1.89']
w2.f6 | x | `cinema ,` | 5.53 | ['1.70', '3.93']
w2.f7 | x | `only now` | 3.55 | ['1.26', '3.20']
w2.f8 |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 | x | `@@UNK@@ to` | 7.04 | ['2.38', '4.67']
w2.f10 | x | `@@UNK@@ up` | 6.74 | ['-0.06', '6.94']
w2.f11 | x | `we hold` | 3.15 | ['1.82', '1.61']
w2.f12 | x | `more damage` | 5.49 | ['1.33', '4.19']
w2.f13 | x | `only now` | 6.37 | ['6.80', '-0.28']
w2.f14 | x | `@@UNK@@ everything` | 4.27 | ['0.69', '3.61']
w2.f15 | x | `about cinema` | 8.83 | ['-3.14', '12.24']
w2.f16 | x | `team continues` | 3.26 | ['0.55', '3.48']
w2.f17 |   | `everything we` | 2.31 | ['1.03', '1.90']
w2.f18 | x | `continues to` | 4.04 | ['1.66', '2.50']
w2.f19 | x | `@@UNK@@ team` | 3.35 | ['0.39', '3.26']
w3.f0 | x | `even more damage` | 4.83 | ['1.87', '4.04', '-0.68']
w3.f1 |   | `up so that` | 3.47 | ['1.84', '-0.01', '2.02']
w3.f2 | x | `- @@UNK@@ team` | 6.72 | ['2.02', '-0.65', '5.45']
w3.f3 |   | `, only now` | 1.98 | ['-0.33', '2.83', '0.09']
w3.f4 | x | `dear about cinema` | 5.46 | ['2.37', '-0.47', '3.91']
w3.f5 | x | `@@UNK@@ everything we` | 5.05 | ['0.08', '-0.58', '5.88']
w3.f6 | x | `do even more` | 5.56 | ['1.05', '2.23', '2.49']
w3.f7 |   | `to @@UNK@@ up` | 2.58 | ['3.76', '-1.81', '1.13']
w3.f8 |   | `that it can` | 3.67 | ['3.58', '0.83', '-0.46']
w3.f9 | x | `do even more` | 4.72 | ['1.69', '2.56', '0.58']
w3.f10 | x | `everything we hold` | 5.41 | ['0.30', '1.58', '3.68']
w3.f11 | x | `- @@UNK@@ team` | 4.98 | ['1.42', '-1.29', '5.04']
w3.f12 | x | `that it can` | 5.77 | ['2.12', '0.42', '3.36']
w3.f13 | x | `the merchant -` | 6.16 | ['4.70', '0.84', '0.87']
w3.f14 | x | `even more damage` | 7.34 | ['1.00', '4.60', '1.84']
w3.f15 |   | `about cinema ,` | 2.95 | ['-0.53', '0.94', '2.70']
w3.f16 | x | `cinema , only` | 9.43 | ['6.76', '3.78', '-0.74']
w3.f17 | x | `it can do` | 5.72 | ['1.06', '0.09', '4.72']
w3.f18 |   | `@@PAD@@ @@PAD@@ the` | 2.10 | ['0.00', '0.00', '2.57']
w3.f19 | x | `team continues to` | 7.38 | ['3.31', '5.23', '-1.05']

## Original input: 
``` the actors do n't inhabit their roles -- they 're trapped by them , forced to change behavior in bizarre @@UNK@@ fashion and @@UNK@@ @@UNK@@ that @@UNK@@ mostly of @@UNK@@ . ``` 

## Marked input: 
<pre>the actors <span style="background-color: #6698FF">@</span>do <span style="background-color: #6698FF">@</span>n't <span style="background-color: #6698FF">@</span>inhabit <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>their <span style="background-color: #FFFF00">@</span>roles <span style="background-color: #FFFF00">@</span>-- <span style="background-color: #FFFF00">@</span>they <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>'re <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>trapped <span style="background-color: #6698FF">@</span>by <span style="background-color: #6698FF">@</span>them <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>forced <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span>change <span style="background-color: #6698FF">@</span>behavior <span style="background-color: #6698FF">@</span>in bizarre <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>fashion <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ that @@UNK@@ <span style="background-color: #FFFF00">@</span>mostly <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `their roles` | 6.47 | ['4.53', '2.31']
w2.f1 |   | `@@UNK@@ mostly` | 2.25 | ['-0.88', '3.27']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `-- they` | 2.79 | ['1.37', '1.98']
w2.f4 | x | `them ,` | 4.44 | ['2.13', '2.50']
w2.f5 | x | `roles --` | 4.90 | ['3.34', '1.87']
w2.f6 | x | `them ,` | 6.37 | ['2.53', '3.93']
w2.f7 |   | `their roles` | 0.97 | ['-1.03', '2.91']
w2.f8 |   | `their roles` | 2.14 | ['1.04', '1.32']
w2.f9 | x | `forced to` | 9.29 | ['4.63', '4.67']
w2.f10 | x | `inhabit their` | 3.03 | ['3.27', '-0.11']
w2.f11 | x | `fashion and` | 3.25 | ['3.26', '0.27']
w2.f12 | x | `trapped by` | 5.01 | ['1.35', '3.71']
w2.f13 | x | `trapped by` | 7.79 | ['4.47', '3.48']
w2.f14 | x | `in bizarre` | 3.22 | ['-0.13', '3.38']
w2.f15 |   | `change behavior` | 2.81 | ['-0.56', '3.64']
w2.f16 | x | `, forced` | 4.25 | ['-0.98', '6.00']
w2.f17 |   | `their roles` | 2.86 | ['-0.56', '4.03']
w2.f18 | x | `inhabit their` | 5.63 | ['-0.23', '5.98']
w2.f19 | x | `inhabit their` | 4.79 | ['2.75', '2.34']
w3.f0 |   | `roles -- they` | 3.42 | ['1.92', '-0.93', '2.82']
w3.f1 | x | `roles -- they` | 3.82 | ['1.31', '3.00', '-0.11']
w3.f2 | x | `, forced to` | 6.02 | ['2.60', '4.88', '-1.37']
w3.f3 |   | `in bizarre @@UNK@@` | 2.35 | ['1.23', '1.66', '0.07']
w3.f4 |   | `-- they 're` | 1.89 | ['1.64', '0.90', '-0.29']
w3.f5 | x | `@@UNK@@ fashion and` | 5.03 | ['0.08', '-0.53', '5.81']
w3.f6 | x | `they 're trapped` | 3.78 | ['1.47', '3.18', '-0.66']
w3.f7 | x | `inhabit their roles` | 5.78 | ['0.72', '3.65', '1.91']
w3.f8 | x | `that @@UNK@@ mostly` | 4.53 | ['3.58', '-0.27', '1.50']
w3.f9 | x | `@@UNK@@ fashion and` | 6.88 | ['-1.38', '5.97', '2.40']
w3.f10 |   | `do n't inhabit` | 2.82 | ['2.33', '-0.81', '1.44']
w3.f11 | x | `actors do n't` | 4.32 | ['1.74', '2.01', '0.77']
w3.f12 | x | `the actors do` | 5.20 | ['2.43', '0.92', '1.98']
w3.f13 |   | `the actors do` | 3.94 | ['4.70', '-0.11', '-0.41']
w3.f14 | x | `trapped by them` | 4.03 | ['1.24', '2.00', '0.87']
w3.f15 |   | `trapped by them` | 3.32 | ['0.07', '3.36', '0.06']
w3.f16 | x | `inhabit their roles` | 10.36 | ['2.75', '4.21', '3.78']
w3.f17 | x | `forced to change` | 7.03 | ['3.92', '1.66', '1.61']
w3.f18 | x | `mostly of @@UNK@@` | 3.68 | ['2.27', '2.10', '-0.23']
w3.f19 | x | `n't inhabit their` | 4.13 | ['1.55', '0.74', '1.96']

## Original input: 
``` @@UNK@@ affecting . . . while clearly a manipulative film , emerges as powerful rather than cloying . ``` 

## Marked input: 
<pre>@@UNK@@ <span style="background-color: #FFFF00">@</span>affecting <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>. while <span style="background-color: #FFFF00">@</span>clearly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>manipulative <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>film <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>emerges <span style="background-color: #6698FF">@</span>as <span style="background-color: #6698FF">@</span>powerful <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>rather <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>than <span style="background-color: #6698FF">@</span>cloying <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `while clearly` | 4.80 | ['2.89', '2.28']
w2.f1 | x | `. while` | 4.76 | ['-0.03', '4.92']
w2.f2 |   | `as powerful` | 1.32 | ['0.54', '1.82']
w2.f3 |   | `emerges as` | 1.64 | ['2.04', '0.15']
w2.f4 | x | `as powerful` | 5.97 | ['0.47', '5.70']
w2.f5 | x | `manipulative film` | 4.18 | ['3.51', '0.98']
w2.f6 |   | `film ,` | 3.99 | ['0.16', '3.93']
w2.f7 | x | `while clearly` | 2.22 | ['0.16', '2.97']
w2.f8 |   | `@@UNK@@ affecting` | 2.43 | ['0.21', '2.43']
w2.f9 |   | `affecting .` | 2.26 | ['1.81', '0.46']
w2.f10 | x | `as powerful` | 8.26 | ['0.38', '8.02']
w2.f11 |   | `emerges as` | 1.64 | ['1.72', '0.19']
w2.f12 |   | `while clearly` | 2.23 | ['0.86', '1.40']
w2.f13 |   | `as powerful` | 2.96 | ['0.84', '2.27']
w2.f14 |   | `affecting .` | 1.44 | ['1.08', '0.39']
w2.f15 |   | `, emerges` | 1.90 | ['2.19', '-0.02']
w2.f16 |   | `cloying .` | 0.29 | ['2.58', '-1.53']
w2.f17 |   | `cloying .` | 2.17 | ['2.32', '0.47']
w2.f18 | x | `affecting .` | 3.47 | ['3.37', '0.22']
w2.f19 |   | `@@UNK@@ affecting` | 2.99 | ['0.39', '2.89']
w3.f0 | x | `rather than cloying` | 4.33 | ['1.32', '-0.42', '3.82']
w3.f1 |   | `@@PAD@@ @@UNK@@ affecting` | 3.30 | ['0.00', '-0.73', '4.41']
w3.f2 | x | `while clearly a` | 5.18 | ['4.03', '-1.04', '2.27']
w3.f3 |   | `while clearly a` | 1.15 | ['1.73', '0.48', '-0.45']
w3.f4 |   | `. while clearly` | 1.47 | ['-0.66', '1.85', '0.64']
w3.f5 | x | `@@UNK@@ affecting .` | 5.64 | ['0.08', '1.57', '4.32']
w3.f6 |   | `a manipulative film` | 2.83 | ['1.76', '1.03', '0.25']
w3.f7 |   | `manipulative film ,` | 1.86 | ['-1.35', '2.52', '1.18']
w3.f8 |   | `rather than cloying` | 2.47 | ['1.31', '1.81', '-0.37']
w3.f9 | x | `manipulative film ,` | 4.39 | ['1.89', '-0.46', '3.06']
w3.f10 | x | `cloying . @@PAD@@` | 5.48 | ['3.63', '2.00', '0.00']
w3.f11 |   | `while clearly a` | 1.48 | ['0.39', '-1.50', '2.78']
w3.f12 | x | `emerges as powerful` | 4.10 | ['0.43', '4.53', '-0.74']
w3.f13 | x | `@@UNK@@ affecting .` | 5.57 | ['-0.04', '3.42', '2.45']
w3.f14 | x | `rather than cloying` | 5.38 | ['4.27', '-2.82', '4.03']
w3.f15 | x | `, emerges as` | 5.96 | ['1.52', '3.57', '1.03']
w3.f16 | x | `@@PAD@@ @@UNK@@ affecting` | 3.60 | ['0.00', '-0.81', '4.79']
w3.f17 | x | `rather than cloying` | 4.79 | ['2.30', '-0.54', '3.19']
w3.f18 |   | `emerges as powerful` | 2.73 | ['-0.96', '1.90', '2.26']
w3.f19 | x | `a manipulative film` | 5.98 | ['3.70', '-1.11', '3.51']

## Original input: 
``` very predictable but still entertaining ``` 

## Marked input: 
<pre>very <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>predictable <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>but <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>still <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>entertaining</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `very predictable` | 4.31 | ['4.99', '-0.31']
w2.f1 | x | `but still` | 6.51 | ['4.31', '2.34']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `very predictable` | 2.87 | ['2.65', '0.77']
w2.f4 | x | `still entertaining` | 12.57 | ['8.07', '4.69']
w2.f5 | x | `still entertaining` | 5.31 | ['3.13', '2.49']
w2.f6 |   | `still entertaining` | 2.86 | ['3.07', '-0.11']
w2.f7 |   | `predictable but` | 0.57 | ['0.96', '0.51']
w2.f8 |   | `very predictable` | 1.20 | ['0.89', '0.53']
w2.f9 |   | `@@PAD@@ very` | 2.90 | ['0.00', '2.91']
w2.f10 | x | `still entertaining` | 3.93 | ['1.74', '2.33']
w2.f11 | x | `predictable but` | 3.38 | ['1.27', '2.37']
w2.f12 |   | `but still` | 1.25 | ['1.63', '-0.35']
w2.f13 |   | `very predictable` | 0.05 | ['0.86', '-0.66']
w2.f14 |   | `@@PAD@@ very` | 1.64 | ['0.00', '1.67']
w2.f15 | x | `but still` | 3.72 | ['2.02', '1.97']
w2.f16 |   | `very predictable` | 1.79 | ['1.70', '0.86']
w2.f17 |   | `entertaining @@PAD@@` | 0.17 | ['0.79', '0.00']
w2.f18 | x | `@@PAD@@ very` | 4.77 | ['0.00', '4.89']
w2.f19 |   | `@@PAD@@ very` | 2.68 | ['0.00', '2.97']
w3.f0 |   | `@@PAD@@ very predictable` | 2.89 | ['0.00', '1.05', '2.22']
w3.f1 |   | `but still entertaining` | 2.60 | ['-1.34', '2.21', '2.11']
w3.f2 |   | `@@PAD@@ @@PAD@@ very` | 1.48 | ['0.00', '0.00', '1.57']
w3.f3 | x | `still entertaining @@PAD@@` | 2.74 | ['2.44', '0.91', '0.00']
w3.f4 | x | `but still entertaining` | 5.67 | ['1.41', '3.04', '1.58']
w3.f5 |   | `still entertaining @@PAD@@` | 2.85 | ['2.42', '0.76', '0.00']
w3.f6 | x | `@@PAD@@ very predictable` | 4.48 | ['0.00', '1.59', '3.10']
w3.f7 |   | `still entertaining @@PAD@@` | 3.55 | ['4.62', '-0.57', '0.00']
w3.f8 | x | `predictable but still` | 9.05 | ['1.15', '3.35', '4.83']
w3.f9 | x | `very predictable but` | 8.78 | ['4.11', '3.25', '1.53']
w3.f10 | x | `@@PAD@@ very predictable` | 5.20 | ['0.00', '1.74', '3.60']
w3.f11 |   | `predictable but still` | 2.20 | ['1.55', '-0.21', '1.05']
w3.f12 |   | `but still entertaining` | 1.91 | ['-0.44', '2.50', '-0.02']
w3.f13 |   | `predictable but still` | 4.71 | ['2.86', '0.37', '1.72']
w3.f14 | x | `predictable but still` | 4.76 | ['3.47', '3.83', '-2.44']
w3.f15 | x | `@@PAD@@ very predictable` | 8.07 | ['0.00', '4.81', '3.43']
w3.f16 | x | `entertaining @@PAD@@ @@PAD@@` | 4.38 | ['4.76', '0.00', '0.00']
w3.f17 | x | `predictable but still` | 6.47 | ['5.09', '2.96', '-1.43']
w3.f18 | x | `still entertaining @@PAD@@` | 5.87 | ['4.25', '2.09', '0.00']
w3.f19 |   | `predictable but still` | 3.19 | ['-1.73', '1.45', '3.58']

## Original input: 
``` it 's rare to find a film to which the @@UNK@@ ' gentle ' @@UNK@@ , but the word perfectly @@UNK@@ pauline & paulette . ``` 

## Marked input: 
<pre>it 's rare <span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span>find <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span>film <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>which <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>' <span style="background-color: #FFFF00">@</span>gentle <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>' <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>, but <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>word <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>perfectly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>pauline <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>& <span style="background-color: #FFFF00">@</span>paulette <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `rare to` | 6.42 | ['7.25', '-0.45']
w2.f1 | x | `& paulette` | 4.49 | ['2.70', '1.92']
w2.f2 |   | `word perfectly` | 0.32 | ['0.11', '1.25']
w2.f3 |   | `find a` | 1.02 | ['1.34', '0.24']
w2.f4 | x | `'s rare` | 5.83 | ['-0.76', '6.78']
w2.f5 | x | `& paulette` | 4.80 | ['6.22', '-1.11']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `find a` | 1.29 | ['2.49', '-0.29']
w2.f8 | x | `& paulette` | 3.56 | ['4.45', '-0.67']
w2.f9 |   | `rare to` | 4.84 | ['0.18', '4.67']
w2.f10 | x | `word perfectly` | 4.21 | ['0.05', '4.29']
w2.f11 |   | `find a` | 2.64 | ['4.66', '-1.75']
w2.f12 |   | `pauline &` | 2.97 | ['2.74', '0.27']
w2.f13 | x | `find a` | 3.87 | ['2.58', '1.45']
w2.f14 | x | `perfectly @@UNK@@` | 4.48 | ['4.21', '0.30']
w2.f15 | x | `' gentle` | 4.87 | ['2.81', '2.34']
w2.f16 | x | `to find` | 2.69 | ['-1.25', '4.71']
w2.f17 |   | `' @@UNK@@` | 1.33 | ['3.04', '-1.09']
w2.f18 | x | `pauline &` | 5.86 | ['3.91', '2.08']
w2.f19 |   | `' gentle` | 1.86 | ['-0.31', '2.46']
w3.f0 |   | `perfectly @@UNK@@ pauline` | 3.17 | ['1.80', '0.35', '1.40']
w3.f1 |   | `pauline & paulette` | 3.22 | ['1.04', '3.69', '-1.13']
w3.f2 | x | `but the word` | 5.38 | ['1.07', '0.94', '3.47']
w3.f3 | x | `& paulette .` | 3.31 | ['3.47', '1.20', '-0.75']
w3.f4 | x | `pauline & paulette` | 6.28 | ['1.84', '3.70', '1.10']
w3.f5 | x | `& paulette .` | 6.23 | ['-0.07', '2.30', '4.32']
w3.f6 |   | `the word perfectly` | 3.09 | ['-0.32', '2.53', '1.08']
w3.f7 | x | `& paulette .` | 4.41 | ['1.62', '3.11', '0.18']
w3.f8 | x | `@@UNK@@ pauline &` | 8.45 | ['0.50', '1.63', '6.61']
w3.f9 | x | `' gentle '` | 4.82 | ['-2.03', '1.73', '5.23']
w3.f10 | x | `find a film` | 6.42 | ['2.88', '1.32', '2.36']
w3.f11 | x | `to find a` | 3.79 | ['-1.19', '2.39', '2.78']
w3.f12 | x | `to which the` | 4.21 | ['1.38', '3.12', '-0.17']
w3.f13 | x | `@@UNK@@ ' gentle` | 5.29 | ['-0.04', '4.49', '1.08']
w3.f14 | x | `, but the` | 4.81 | ['-0.18', '3.83', '1.24']
w3.f15 |   | `@@PAD@@ it 's` | 2.22 | ['0.00', '2.22', '0.17']
w3.f16 | x | `the word perfectly` | 5.22 | ['-1.70', '2.73', '4.56']
w3.f17 | x | `but the word` | 4.81 | ['1.76', '0.47', '2.74']
w3.f18 | x | `& paulette .` | 3.66 | ['3.48', '1.60', '-0.95']
w3.f19 |   | `@@UNK@@ ' gentle` | 2.63 | ['-0.26', '0.95', '2.05']

## Original input: 
``` . . . quite good at providing some good old fashioned @@UNK@@ . ``` 

## Marked input: 
<pre>. . . <span style="background-color: #FFFF00">@</span>quite <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>good <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>at <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>providing <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>some <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>good <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>old <span style="background-color: #FFFF00">@</span>fashioned <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `providing some` | 3.42 | ['1.04', '2.75']
w2.f1 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f2 |   | `providing some` | 0.66 | ['1.57', '0.13']
w2.f3 | x | `providing some` | 2.76 | ['1.89', '1.43']
w2.f4 |   | `quite good` | 1.61 | ['1.78', '0.02']
w2.f5 | x | `old fashioned` | 3.32 | ['1.76', '1.87']
w2.f6 |   | `at providing` | 3.96 | ['2.94', '1.12']
w2.f7 | x | `at providing` | 4.20 | ['1.98', '3.14']
w2.f8 |   | `quite good` | 3.02 | ['4.29', '-1.06']
w2.f9 |   | `at providing` | 3.07 | ['4.66', '-1.57']
w2.f10 |   | `quite good` | 2.33 | ['-0.60', '3.06']
w2.f11 | x | `providing some` | 3.61 | ['0.06', '3.82']
w2.f12 |   | `old fashioned` | 1.83 | ['0.42', '1.45']
w2.f13 |   | `fashioned @@UNK@@` | 2.29 | ['2.55', '-0.10']
w2.f14 | x | `good at` | 3.40 | ['0.44', '2.99']
w2.f15 |   | `old fashioned` | 0.22 | ['1.05', '-0.56']
w2.f16 | x | `. quite` | 5.37 | ['-0.51', '6.65']
w2.f17 | x | `quite good` | 6.95 | ['7.03', '0.54']
w2.f18 | x | `quite good` | 5.26 | ['3.81', '1.57']
w2.f19 | x | `quite good` | 5.11 | ['1.56', '3.85']
w3.f0 |   | `at providing some` | 2.80 | ['1.31', '0.05', '1.83']
w3.f1 | x | `at providing some` | 6.30 | ['7.39', '-0.17', '-0.54']
w3.f2 |   | `old fashioned @@UNK@@` | 1.37 | ['2.89', '-1.12', '-0.31']
w3.f3 | x | `quite good at` | 2.50 | ['1.41', '-0.95', '2.65']
w3.f4 | x | `. quite good` | 3.52 | ['-0.66', '0.61', '3.93']
w3.f5 |   | `@@PAD@@ @@PAD@@ .` | 3.99 | ['0.00', '0.00', '4.32']
w3.f6 |   | `providing some good` | 2.54 | ['1.74', '1.01', '-0.00']
w3.f7 | x | `quite good at` | 4.64 | ['0.82', '1.93', '2.38']
w3.f8 |   | `at providing some` | 3.03 | ['-3.37', '4.00', '2.68']
w3.f9 |   | `at providing some` | 2.43 | ['2.41', '0.44', '-0.31']
w3.f10 |   | `. . quite` | 2.74 | ['0.09', '2.00', '0.80']
w3.f11 |   | `. quite good` | 0.41 | ['-0.15', '1.63', '-0.88']
w3.f12 |   | `at providing some` | 2.48 | ['-0.68', '-0.42', '3.71']
w3.f13 | x | `some good old` | 6.64 | ['4.29', '3.04', '-0.45']
w3.f14 | x | `good at providing` | 3.94 | ['1.47', '-0.15', '2.71']
w3.f15 |   | `. @@PAD@@ @@PAD@@` | 0.52 | ['0.68', '0.00', '0.00']
w3.f16 | x | `. . quite` | 4.26 | ['-0.12', '-1.01', '5.77']
w3.f17 |   | `at providing some` | 2.92 | ['-0.24', '1.17', '2.14']
w3.f18 | x | `providing some good` | 6.43 | ['3.95', '-0.67', '3.62']
w3.f19 | x | `good at providing` | 6.18 | ['1.75', '2.38', '2.16']

## Original input: 
``` one of those rare films that come by once in a while with @@UNK@@ amounts of acting , direction , story and pace . ``` 

## Marked input: 
<pre>one of those rare <span style="background-color: #FFFF00">@</span>films <span style="background-color: #FFFF00">@</span>that <span style="background-color: #FFFF00">@</span>come <span style="background-color: #FFFF00">@</span>by <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>once <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>in a while <span style="background-color: #FFFF00">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>amounts <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>acting <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>direction <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>story <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>pace <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `rare films` | 5.30 | ['7.25', '-1.57']
w2.f1 | x | `a while` | 7.74 | ['2.95', '4.92']
w2.f2 |   | `once in` | 0.17 | ['1.09', '0.12']
w2.f3 |   | `of acting` | 0.71 | ['-0.30', '1.56']
w2.f4 | x | `those rare` | 6.16 | ['-0.43', '6.78']
w2.f5 |   | `of acting` | 2.95 | ['0.65', '2.60']
w2.f6 | x | `direction ,` | 5.78 | ['1.95', '3.93']
w2.f7 | x | `pace .` | 3.56 | ['4.33', '0.14']
w2.f8 | x | `those rare` | 5.62 | ['4.07', '1.77']
w2.f9 |   | `those rare` | 3.33 | ['2.12', '1.23']
w2.f10 | x | `a while` | 3.63 | ['1.97', '1.79']
w2.f11 |   | `and pace` | 2.35 | ['0.34', '2.28']
w2.f12 |   | `acting ,` | 2.82 | ['2.89', '-0.03']
w2.f13 | x | `come by` | 5.22 | ['1.89', '3.48']
w2.f14 | x | `acting ,` | 3.67 | ['2.81', '0.89']
w2.f15 | x | `acting ,` | 5.05 | ['5.63', '-0.31']
w2.f16 |   | `of acting` | 1.20 | ['0.18', '1.78']
w2.f17 | x | `of acting` | 3.60 | ['-1.87', '6.09']
w2.f18 | x | `those rare` | 5.09 | ['0.62', '4.59']
w2.f19 | x | `those rare` | 5.40 | ['3.67', '2.03']
w3.f0 |   | `story and pace` | 3.64 | ['3.91', '-1.09', '1.20']
w3.f1 |   | `rare films that` | 2.65 | ['0.03', '0.98', '2.02']
w3.f2 | x | `, story and` | 3.76 | ['2.60', '0.78', '0.47']
w3.f3 |   | `and pace .` | 0.63 | ['-0.66', '2.65', '-0.75']
w3.f4 |   | `those rare films` | 1.82 | ['1.56', '0.22', '0.40']
w3.f5 | x | `a while with` | 5.62 | ['1.79', '2.70', '1.46']
w3.f6 | x | `direction , story` | 4.66 | ['3.65', '0.38', '0.84']
w3.f7 | x | `that come by` | 4.26 | ['3.01', '0.45', '1.30']
w3.f8 | x | `of acting ,` | 9.36 | ['1.71', '5.80', '2.14']
w3.f9 |   | `in a while` | 3.46 | ['1.57', '-0.16', '2.16']
w3.f10 | x | `pace . @@PAD@@` | 6.91 | ['5.06', '2.00', '0.00']
w3.f11 |   | `one of those` | 3.24 | ['3.14', '-2.01', '2.30']
w3.f12 | x | `amounts of acting` | 5.70 | ['1.77', '3.24', '0.82']
w3.f13 | x | `acting , direction` | 5.45 | ['1.37', '1.92', '2.41']
w3.f14 | x | `story and pace` | 6.09 | ['0.03', '1.09', '5.07']
w3.f15 | x | `while with @@UNK@@` | 4.43 | ['2.80', '3.85', '-2.05']
w3.f16 | x | `direction , story` | 6.58 | ['1.59', '3.78', '1.59']
w3.f17 | x | `acting , direction` | 6.08 | ['2.02', '3.34', '0.87']
w3.f18 |   | `of those rare` | 3.27 | ['-0.21', '-0.82', '4.76']
w3.f19 | x | `story and pace` | 5.90 | ['1.76', '1.18', '3.08']

## Original input: 
``` most of crush is a clever and captivating romantic comedy with a welcome @@UNK@@ of @@UNK@@ . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>most <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>crush <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>clever <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>captivating <span style="background-color: #FFFF00">@</span>romantic <span style="background-color: #FFFF00">@</span>comedy <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>welcome <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>@@UNK@@ .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `with a` | 2.46 | ['3.44', '-0.61']
w2.f1 | x | `comedy with` | 7.14 | ['2.40', '4.87']
w2.f2 |   | `a clever` | 0.47 | ['0.10', '1.41']
w2.f3 | x | `of crush` | 3.21 | ['-0.30', '4.06']
w2.f4 | x | `captivating romantic` | 6.59 | ['1.33', '5.45']
w2.f5 | x | `romantic comedy` | 3.37 | ['2.45', '1.22']
w2.f6 |   | `a welcome` | 3.05 | ['0.54', '2.61']
w2.f7 |   | `of crush` | 1.65 | ['0.11', '2.45']
w2.f8 | x | `captivating romantic` | 3.50 | ['1.30', '2.41']
w2.f9 |   | `clever and` | 4.37 | ['4.90', '-0.51']
w2.f10 | x | `a welcome` | 6.04 | ['1.97', '4.21']
w2.f11 |   | `welcome @@UNK@@` | 2.43 | ['2.45', '0.25']
w2.f12 |   | `a clever` | 3.12 | ['-1.91', '5.07']
w2.f13 |   | `crush is` | 2.29 | ['1.94', '0.50']
w2.f14 |   | `a clever` | 2.55 | ['-2.64', '5.22']
w2.f15 |   | `romantic comedy` | 1.23 | ['2.18', '-0.68']
w2.f16 |   | `captivating romantic` | 1.52 | ['1.07', '1.21']
w2.f17 |   | `welcome @@UNK@@` | 0.47 | ['2.18', '-1.09']
w2.f18 |   | `and captivating` | 3.14 | ['3.52', '-0.26']
w2.f19 |   | `and captivating` | 3.02 | ['3.66', '-0.34']
w3.f0 |   | `welcome @@UNK@@ of` | 3.06 | ['2.86', '0.35', '0.24']
w3.f1 |   | `with a welcome` | 2.31 | ['-1.34', '-0.71', '4.74']
w3.f2 |   | `crush is a` | 2.75 | ['1.93', '-1.36', '2.27']
w3.f3 |   | `a welcome @@UNK@@` | 0.19 | ['-0.28', '1.01', '0.07']
w3.f4 |   | `of crush is` | 1.02 | ['-1.60', '0.51', '2.46']
w3.f5 | x | `a clever and` | 11.85 | ['1.79', '4.58', '5.81']
w3.f6 |   | `a clever and` | 0.68 | ['1.76', '-1.82', '0.95']
w3.f7 |   | `a clever and` | 1.52 | ['-0.02', '0.20', '1.83']
w3.f8 | x | `clever and captivating` | 6.25 | ['-0.35', '0.71', '6.18']
w3.f9 |   | `comedy with a` | 2.98 | ['1.81', '0.14', '1.13']
w3.f10 | x | `of crush is` | 6.22 | ['2.92', '2.42', '1.03']
w3.f11 | x | `most of crush` | 5.51 | ['2.02', '-2.01', '5.69']
w3.f12 | x | `romantic comedy with` | 5.14 | ['1.66', '0.93', '2.68']
w3.f13 |   | `clever and captivating` | 4.27 | ['1.70', '0.60', '2.21']
w3.f14 |   | `captivating romantic comedy` | 2.19 | ['0.35', '0.07', '1.86']
w3.f15 |   | `captivating romantic comedy` | 1.33 | ['1.26', '0.20', '0.04']
w3.f16 |   | `and captivating romantic` | 1.73 | ['-1.34', '0.96', '2.49']
w3.f17 | x | `@@PAD@@ @@PAD@@ most` | 5.16 | ['0.00', '0.00', '5.32']
w3.f18 |   | `with a welcome` | 1.38 | ['0.27', '-0.07', '1.64']
w3.f19 | x | `a welcome @@UNK@@` | 5.27 | ['3.70', '3.71', '-2.02']

## Original input: 
``` an empty , @@UNK@@ exercise . ``` 

## Marked input: 
<pre>an <span style="background-color: #FFFF00">@</span>empty <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>exercise <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ exercise` | 3.01 | ['1.98', '1.40']
w2.f1 |   | `@@PAD@@ an` | 2.40 | ['0.00', '2.54']
w2.f2 |   | `an empty` | 0.04 | ['0.10', '0.99']
w2.f3 | x | `empty ,` | 2.74 | ['2.85', '0.44']
w2.f4 |   | `an empty` | 2.27 | ['5.09', '-2.63']
w2.f5 | x | `an empty` | 3.43 | ['3.50', '0.23']
w2.f6 |   | `empty ,` | 3.93 | ['0.10', '3.93']
w2.f7 |   | `exercise .` | 1.64 | ['2.40', '0.14']
w2.f8 |   | `empty ,` | 0.96 | ['1.96', '-0.79']
w2.f9 |   | `empty ,` | 2.57 | ['2.25', '0.34']
w2.f10 | x | `an empty` | 3.61 | ['1.91', '1.83']
w2.f11 | x | `exercise .` | 5.29 | ['7.46', '-1.89']
w2.f12 | x | `@@UNK@@ exercise` | 5.32 | ['-0.28', '5.64']
w2.f13 |   | `empty ,` | 2.66 | ['0.63', '2.18']
w2.f14 |   | `exercise .` | 2.12 | ['1.77', '0.39']
w2.f15 |   | `an empty` | 2.23 | ['0.76', '1.74']
w2.f16 | x | `an empty` | 3.49 | ['2.54', '1.71']
w2.f17 | x | `exercise .` | 5.05 | ['5.20', '0.47']
w2.f18 |   | `exercise .` | 2.99 | ['2.89', '0.22']
w2.f19 |   | `exercise .` | 1.68 | ['3.26', '-1.28']
w3.f0 |   | `exercise . @@PAD@@` | 3.31 | ['3.70', '-0.01', '0.00']
w3.f1 | x | `@@PAD@@ an empty` | 5.44 | ['0.00', '1.98', '3.83']
w3.f2 | x | `@@UNK@@ exercise .` | 3.64 | ['-2.33', '5.21', '0.84']
w3.f3 |   | `@@PAD@@ @@PAD@@ an` | 0.00 | ['0.00', '0.00', '-0.26']
w3.f4 |   | `@@PAD@@ an empty` | 0.38 | ['0.00', '0.82', '-0.08']
w3.f5 |   | `empty , @@UNK@@` | 2.14 | ['1.99', '1.40', '-0.93']
w3.f6 |   | `@@PAD@@ an empty` | 2.11 | ['0.00', '0.72', '1.60']
w3.f7 |   | `an empty ,` | 3.86 | ['2.46', '0.72', '1.18']
w3.f8 |   | `an empty ,` | 3.51 | ['1.44', '0.21', '2.14']
w3.f9 |   | `empty , @@UNK@@` | 3.22 | ['2.52', '-1.33', '2.13']
w3.f10 |   | `empty , @@UNK@@` | 3.72 | ['3.42', '-0.41', '0.86']
w3.f11 |   | `an empty ,` | 1.65 | ['-0.26', '1.92', '0.19']
w3.f12 |   | `@@PAD@@ an empty` | 1.99 | ['0.00', '1.18', '0.93']
w3.f13 |   | `@@UNK@@ exercise .` | 3.59 | ['-0.04', '1.43', '2.45']
w3.f14 |   | `@@PAD@@ an empty` | 2.13 | ['0.00', '0.23', '1.98']
w3.f15 |   | `@@PAD@@ an empty` | 2.04 | ['0.00', '1.61', '0.60']
w3.f16 |   | `@@PAD@@ @@PAD@@ an` | 0.00 | ['0.00', '0.00', '-1.14']
w3.f17 | x | `, @@UNK@@ exercise` | 4.99 | ['0.73', '1.39', '3.03']
w3.f18 |   | `an empty ,` | 1.97 | ['0.67', '0.97', '0.79']
w3.f19 |   | `@@PAD@@ @@PAD@@ an` | 1.95 | ['0.00', '0.00', '2.07']

## Original input: 
``` showtime is a fine - looking film with a bouncy score and a @@UNK@@ of lively songs for deft @@UNK@@ . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>showtime <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>fine <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span>looking <span style="background-color: #FFFF00">@</span>film <span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>bouncy <span style="background-color: #FFFF00">@</span>score <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>of lively <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>songs <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>for <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>deft <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `a fine` | 5.97 | ['1.11', '5.23']
w2.f1 | x | `film with` | 5.02 | ['0.28', '4.87']
w2.f2 |   | `bouncy score` | 1.46 | ['1.32', '1.19']
w2.f3 | x | `showtime is` | 3.51 | ['3.47', '0.59']
w2.f4 | x | `of lively` | 5.83 | ['1.04', '4.98']
w2.f5 | x | `lively songs` | 3.63 | ['4.81', '-0.88']
w2.f6 |   | `lively songs` | 2.73 | ['1.24', '1.59']
w2.f7 |   | `showtime is` | 1.80 | ['3.81', '-1.10']
w2.f8 | x | `fine -` | 3.96 | ['2.33', '1.85']
w2.f9 | x | `bouncy score` | 5.78 | ['3.01', '2.79']
w2.f10 | x | `for deft` | 6.95 | ['1.34', '5.74']
w2.f11 | x | `showtime is` | 3.27 | ['3.93', '-0.39']
w2.f12 |   | `bouncy score` | 1.27 | ['-0.16', '1.46']
w2.f13 | x | `looking film` | 4.51 | ['5.06', '-0.40']
w2.f14 | x | `bouncy score` | 5.47 | ['2.57', '2.93']
w2.f15 | x | `of lively` | 3.81 | ['-3.18', '7.26']
w2.f16 | x | `@@PAD@@ showtime` | 5.18 | ['0.00', '5.94']
w2.f17 |   | `showtime is` | 3.18 | ['3.00', '0.80']
w2.f18 | x | `and a` | 3.49 | ['3.52', '0.10']
w2.f19 |   | `a bouncy` | 2.77 | ['0.99', '2.08']
w3.f0 | x | `@@PAD@@ @@PAD@@ showtime` | 4.54 | ['0.00', '0.00', '4.93']
w3.f1 | x | `bouncy score and` | 6.50 | ['5.86', '1.18', '-0.17']
w3.f2 | x | `@@PAD@@ @@PAD@@ showtime` | 6.46 | ['0.00', '0.00', '6.55']
w3.f3 | x | `songs for deft` | 4.09 | ['3.21', '0.98', '0.51']
w3.f4 | x | `with a bouncy` | 3.87 | ['0.19', '0.29', '3.75']
w3.f5 | x | `of lively songs` | 6.82 | ['-0.94', '6.94', '1.15']
w3.f6 | x | `@@PAD@@ showtime is` | 3.82 | ['0.00', '2.39', '1.64']
w3.f7 |   | `of lively songs` | 2.29 | ['0.84', '0.98', '0.97']
w3.f8 | x | `a fine -` | 4.79 | ['0.66', '6.83', '-2.42']
w3.f9 | x | `showtime is a` | 4.98 | ['3.83', '0.12', '1.13']
w3.f10 | x | `of lively songs` | 4.42 | ['2.92', '3.30', '-1.66']
w3.f11 | x | `showtime is a` | 4.57 | ['2.18', '-0.19', '2.78']
w3.f12 | x | `looking film with` | 5.05 | ['1.97', '0.53', '2.68']
w3.f13 |   | `lively songs for` | 3.12 | ['0.71', '2.43', '0.23']
w3.f14 |   | `@@PAD@@ showtime is` | 2.69 | ['0.00', '0.15', '2.63']
w3.f15 |   | `@@PAD@@ @@PAD@@ showtime` | 2.92 | ['0.00', '0.00', '3.08']
w3.f16 | x | `songs for deft` | 7.54 | ['2.63', '3.80', '1.48']
w3.f17 | x | `songs for deft` | 6.23 | ['0.71', '5.11', '0.56']
w3.f18 | x | `songs for deft` | 4.80 | ['4.17', '-1.64', '2.73']
w3.f19 | x | `a fine -` | 8.33 | ['3.70', '6.25', '-1.51']

## Original input: 
``` a low - key @@UNK@@ of love that strikes a very resonant chord . ``` 

## Marked input: 
<pre>a low <span style="background-color: #FFFF00">@</span>- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>key <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>love <span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>strikes <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>very <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>resonant <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>chord <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `very resonant` | 3.85 | ['4.99', '-0.76']
w2.f1 | x | `a low` | 5.14 | ['2.95', '2.32']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `resonant chord` | 0.73 | ['0.41', '0.87']
w2.f4 | x | `of love` | 5.27 | ['1.04', '4.42']
w2.f5 | x | `very resonant` | 7.70 | ['2.67', '5.34']
w2.f6 | x | `resonant chord` | 4.88 | ['4.89', '0.08']
w2.f7 |   | `of love` | 0.20 | ['0.11', '1.00']
w2.f8 |   | `strikes a` | 3.10 | ['0.76', '2.56']
w2.f9 |   | `@@UNK@@ of` | 4.02 | ['2.38', '1.65']
w2.f10 | x | `of love` | 4.75 | ['-0.14', '5.03']
w2.f11 |   | `a very` | 0.79 | ['0.43', '0.63']
w2.f12 |   | `love that` | 1.46 | ['1.26', '0.24']
w2.f13 | x | `low -` | 4.31 | ['3.26', '1.20']
w2.f14 |   | `resonant chord` | 1.04 | ['0.84', '0.24']
w2.f15 | x | `that strikes` | 4.16 | ['-0.23', '4.66']
w2.f16 |   | `very resonant` | 2.18 | ['1.70', '1.24']
w2.f17 |   | `very resonant` | 1.29 | ['-0.66', '2.57']
w2.f18 | x | `a very` | 5.53 | ['0.76', '4.89']
w2.f19 | x | `a very` | 3.67 | ['0.99', '2.97']
w3.f0 |   | `strikes a very` | 2.49 | ['-2.03', '3.29', '1.62']
w3.f1 | x | `key @@UNK@@ of` | 6.15 | ['7.40', '-0.73', '-0.14']
w3.f2 |   | `strikes a very` | 2.73 | ['2.13', '-0.88', '1.57']
w3.f3 | x | `a very resonant` | 3.09 | ['-0.28', '1.66', '2.31']
w3.f4 |   | `low - key` | 2.11 | ['0.55', '-0.47', '2.38']
w3.f5 |   | `resonant chord .` | 4.74 | ['-0.05', '0.79', '4.32']
w3.f6 | x | `a very resonant` | 4.83 | ['1.76', '1.59', '1.69']
w3.f7 |   | `that strikes a` | 2.44 | ['3.01', '0.75', '-0.82']
w3.f8 | x | `love that strikes` | 4.81 | ['1.08', '2.35', '1.67']
w3.f9 |   | `very resonant chord` | 2.70 | ['4.11', '-2.55', '1.25']
w3.f10 |   | `chord . @@PAD@@` | 3.11 | ['1.26', '2.00', '0.00']
w3.f11 | x | `love that strikes` | 6.41 | ['3.30', '0.56', '2.74']
w3.f12 |   | `that strikes a` | 2.80 | ['2.12', '1.49', '-0.67']
w3.f13 |   | `resonant chord .` | 4.01 | ['1.96', '-0.15', '2.45']
w3.f14 |   | `love that strikes` | 1.86 | ['0.39', '0.30', '1.27']
w3.f15 |   | `very resonant chord` | 3.04 | ['2.73', '-2.70', '3.18']
w3.f16 | x | `a very resonant` | 5.59 | ['-0.19', '1.36', '4.80']
w3.f17 | x | `very resonant chord` | 4.87 | ['2.21', '1.26', '1.55']
w3.f18 | x | `very resonant chord` | 7.96 | ['1.40', '4.92', '2.11']
w3.f19 | x | `low - key` | 8.15 | ['2.37', '1.48', '4.41']

## Original input: 
``` showtime is n't particularly @@UNK@@ , but it can still make you feel that you never want to see another car chase , explosion or @@UNK@@ again . ``` 

## Marked input: 
<pre>showtime <span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>n't <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>particularly <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ , but it <span style="background-color: #FFFF00">@</span>can <span style="background-color: #FFFF00">@</span>still make <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>you <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>feel <span style="background-color: #FFFF00">@</span>that <span style="background-color: #FFFF00">@</span>you <span style="background-color: #FFFF00">@</span>never <span style="background-color: #FFFF00">@</span>want <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>see <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>another <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>car <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>chase <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>explosion <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>or <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>again <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `another car` | 4.91 | ['3.18', '2.10']
w2.f1 | x | `but it` | 5.95 | ['4.31', '1.78']
w2.f2 |   | `car chase` | 0.36 | ['0.48', '0.92']
w2.f3 | x | `see another` | 4.16 | ['1.32', '3.39']
w2.f4 | x | `still make` | 7.29 | ['8.07', '-0.60']
w2.f5 | x | `still make` | 4.45 | ['3.13', '1.63']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 | x | `car chase` | 2.41 | ['2.60', '0.72']
w2.f8 | x | `make you` | 5.39 | ['1.47', '4.14']
w2.f9 | x | `want to` | 5.09 | ['0.43', '4.67']
w2.f10 | x | `you never` | 6.92 | ['4.16', '2.89']
w2.f11 | x | `car chase` | 5.80 | ['2.44', '3.63']
w2.f12 | x | `still make` | 4.30 | ['1.28', '3.06']
w2.f13 | x | `showtime is` | 3.63 | ['3.28', '0.50']
w2.f14 | x | `car chase` | 8.01 | ['5.20', '2.85']
w2.f15 | x | `make you` | 6.58 | ['0.86', '5.99']
w2.f16 | x | `@@PAD@@ showtime` | 5.18 | ['0.00', '5.94']
w2.f17 |   | `showtime is` | 3.18 | ['3.00', '0.80']
w2.f18 | x | `again .` | 3.28 | ['3.18', '0.22']
w2.f19 |   | `@@UNK@@ again` | 2.59 | ['0.39', '2.49']
w3.f0 | x | `another car chase` | 11.55 | ['3.80', '2.22', '5.92']
w3.f1 |   | `can still make` | 3.66 | ['0.99', '2.21', '0.84']
w3.f2 | x | `, explosion or` | 7.57 | ['2.60', '1.75', '3.30']
w3.f3 | x | `that you never` | 2.72 | ['2.19', '0.23', '0.90']
w3.f4 | x | `still make you` | 4.83 | ['1.03', '1.70', '2.46']
w3.f5 | x | `@@UNK@@ again .` | 5.03 | ['0.08', '0.96', '4.32']
w3.f6 | x | `want to see` | 5.01 | ['1.54', '0.76', '2.91']
w3.f7 | x | `to see another` | 5.60 | ['3.76', '1.61', '0.72']
w3.f8 | x | `car chase ,` | 5.17 | ['1.63', '1.69', '2.14']
w3.f9 | x | `car chase ,` | 5.79 | ['1.58', '1.26', '3.06']
w3.f10 | x | `chase , explosion` | 5.86 | ['2.81', '-0.41', '3.60']
w3.f11 | x | `never want to` | 9.65 | ['3.52', '4.27', '2.06']
w3.f12 | x | `car chase ,` | 6.44 | ['4.12', '2.29', '0.16']
w3.f13 | x | `@@UNK@@ again .` | 7.41 | ['-0.04', '5.25', '2.45']
w3.f14 | x | `showtime is n't` | 6.05 | ['1.62', '0.90', '3.62']
w3.f15 | x | `, explosion or` | 6.84 | ['1.52', '2.84', '2.65']
w3.f16 | x | `feel that you` | 3.76 | ['1.76', '2.04', '0.34']
w3.f17 | x | `showtime is n't` | 11.94 | ['5.23', '2.35', '4.52']
w3.f18 | x | `never want to` | 5.43 | ['1.32', '3.06', '1.52']
w3.f19 | x | `showtime is n't` | 4.13 | ['2.78', '3.62', '-2.16']

## Original input: 
``` that old @@UNK@@ about women being @@UNK@@ gets an exhilarating new interpretation in morvern callar . ``` 

## Marked input: 
<pre>that <span style="background-color: #FFFF00">@</span>old <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>about <span style="background-color: #FFFF00">@</span>women <span style="background-color: #6698FF">@</span>being <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>gets <span style="background-color: #6698FF">@</span>an <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>exhilarating <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>new <span style="background-color: #FFFF00">@</span>interpretation <span style="background-color: #FFFF00">@</span>in morvern callar <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `an exhilarating` | 2.68 | ['-0.70', '3.75']
w2.f1 | x | `gets an` | 6.55 | ['4.15', '2.54']
w2.f2 |   | `morvern callar` | 0.03 | ['0.44', '0.64']
w2.f3 |   | `@@UNK@@ gets` | 0.69 | ['-0.08', '1.33']
w2.f4 | x | `that old` | 4.75 | ['1.54', '3.39']
w2.f5 | x | `an exhilarating` | 5.55 | ['3.50', '2.35']
w2.f6 |   | `new interpretation` | 3.23 | ['1.61', '1.72']
w2.f7 |   | `@@UNK@@ gets` | 1.88 | ['-0.69', '3.48']
w2.f8 | x | `gets an` | 3.33 | ['2.41', '1.13']
w2.f9 |   | `@@UNK@@ about` | 3.01 | ['2.38', '0.64']
w2.f10 | x | `morvern callar` | 4.74 | ['2.36', '2.52']
w2.f11 |   | `morvern callar` | 0.91 | ['-0.39', '1.56']
w2.f12 |   | `gets an` | 2.51 | ['3.71', '-1.16']
w2.f13 | x | `morvern callar` | 3.77 | ['2.70', '1.22']
w2.f14 | x | `gets an` | 4.64 | ['2.62', '2.05']
w2.f15 |   | `exhilarating new` | 3.01 | ['2.27', '1.01']
w2.f16 | x | `women being` | 4.14 | ['2.52', '2.38']
w2.f17 |   | `callar .` | 2.53 | ['2.68', '0.47']
w2.f18 | x | `that old` | 4.38 | ['2.33', '2.17']
w2.f19 | x | `morvern callar` | 3.55 | ['0.30', '3.55']
w3.f0 |   | `interpretation in morvern` | 3.67 | ['2.22', '1.29', '0.56']
w3.f1 |   | `gets an exhilarating` | 3.43 | ['-0.27', '1.98', '2.09']
w3.f2 |   | `@@PAD@@ that old` | 3.25 | ['0.00', '1.53', '1.82']
w3.f3 | x | `an exhilarating new` | 2.78 | ['0.82', '0.65', '1.91']
w3.f4 |   | `exhilarating new interpretation` | 3.43 | ['2.21', '0.80', '0.79']
w3.f5 | x | `morvern callar .` | 5.73 | ['0.61', '1.13', '4.32']
w3.f6 |   | `@@UNK@@ gets an` | 3.47 | ['-0.28', '2.92', '1.04']
w3.f7 | x | `that old @@UNK@@` | 5.87 | ['3.01', '3.43', '-0.07']
w3.f8 | x | `an exhilarating new` | 10.74 | ['1.44', '6.99', '2.59']
w3.f9 |   | `callar . @@PAD@@` | 3.49 | ['3.02', '0.58', '0.00']
w3.f10 | x | `women being @@UNK@@` | 4.34 | ['2.34', '1.29', '0.86']
w3.f11 |   | `gets an exhilarating` | 2.59 | ['1.65', '-0.63', '1.76']
w3.f12 | x | `about women being` | 6.04 | ['0.83', '1.70', '3.63']
w3.f13 | x | `morvern callar .` | 5.40 | ['2.83', '0.37', '2.45']
w3.f14 | x | `@@UNK@@ gets an` | 3.44 | ['-0.34', '3.74', '0.13']
w3.f15 |   | `. @@PAD@@ @@PAD@@` | 0.52 | ['0.68', '0.00', '0.00']
w3.f16 | x | `gets an exhilarating` | 5.24 | ['1.93', '0.18', '3.51']
w3.f17 |   | `@@PAD@@ @@PAD@@ that` | 0.05 | ['0.00', '0.00', '0.21']
w3.f18 | x | `@@PAD@@ that old` | 4.08 | ['0.00', '0.23', '4.31']
w3.f19 |   | `exhilarating new interpretation` | 3.52 | ['2.27', '0.45', '0.92']

## Original input: 
``` it 's as if solondz had two ideas for two movies , could n't really figure out how to flesh either out , so he just @@UNK@@ ‘ em together here . ``` 

## Marked input: 
<pre>it 's as if solondz had two <span style="background-color: #6698FF">@</span>ideas <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>for <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>two <span style="background-color: #FFFF00">@</span>movies <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>could <span style="background-color: #FFFF00">@</span>n't <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>really <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>figure <span style="background-color: #6698FF">@</span>out <span style="background-color: #6698FF">@</span>how <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>flesh <span style="background-color: #6698FF">@</span>either <span style="background-color: #6698FF">@</span>out <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>so <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>he <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>just <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>‘ <span style="background-color: #6698FF">@</span>em <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>together <span style="background-color: #FFFF00">@</span>here <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `either out` | 3.49 | ['0.08', '3.77']
w2.f1 | x | `em together` | 6.12 | ['1.05', '5.21']
w2.f2 |   | `two ideas` | 0.34 | ['0.83', '0.56']
w2.f3 | x | `really figure` | 4.05 | ['1.78', '2.82']
w2.f4 |   | `‘ em` | 2.77 | ['2.49', '0.47']
w2.f5 | x | `em together` | 3.30 | ['2.30', '1.30']
w2.f6 | x | `movies ,` | 7.05 | ['3.21', '3.93']
w2.f7 |   | `together here` | 1.41 | ['1.18', '1.14']
w2.f8 | x | `two movies` | 6.64 | ['5.87', '0.98']
w2.f9 |   | `how to` | 3.70 | ['-0.96', '4.67']
w2.f10 | x | `‘ em` | 4.53 | ['1.16', '3.50']
w2.f11 |   | `solondz had` | 2.18 | ['1.41', '1.05']
w2.f12 | x | `out how` | 8.27 | ['0.84', '7.47']
w2.f13 | x | `@@UNK@@ ‘` | 3.51 | ['0.61', '3.05']
w2.f14 | x | `@@UNK@@ ‘` | 3.96 | ['0.69', '3.31']
w2.f15 | x | `together here` | 3.96 | ['3.35', '0.88']
w2.f16 | x | `had two` | 2.86 | ['1.80', '1.83']
w2.f17 | x | `two ideas` | 4.03 | ['3.40', '1.25']
w2.f18 | x | `could n't` | 5.24 | ['2.25', '3.11']
w2.f19 | x | `so he` | 4.61 | ['2.24', '2.67']
w3.f0 | x | `so he just` | 6.50 | ['1.76', '3.74', '1.39']
w3.f1 | x | `em together here` | 6.98 | ['2.01', '2.08', '3.26']
w3.f2 | x | `figure out how` | 6.74 | ['3.56', '2.13', '1.14']
w3.f3 |   | `could n't really` | 1.77 | ['1.56', '2.63', '-1.82']
w3.f4 |   | `had two ideas` | 3.28 | ['-0.11', '1.46', '2.28']
w3.f5 | x | `together here .` | 7.55 | ['1.38', '2.18', '4.32']
w3.f6 | x | `figure out how` | 5.62 | ['3.73', '0.23', '1.87']
w3.f7 |   | `for two movies` | 3.75 | ['1.19', '-0.62', '3.68']
w3.f8 | x | `either out ,` | 6.06 | ['-0.57', '4.78', '2.14']
w3.f9 | x | `either out ,` | 6.29 | ['1.54', '1.80', '3.06']
w3.f10 | x | `here . @@PAD@@` | 6.14 | ['4.29', '2.00', '0.00']
w3.f11 | x | `n't really figure` | 8.67 | ['0.77', '4.53', '3.57']
w3.f12 | x | `to flesh either` | 6.01 | ['1.38', '-0.03', '4.78']
w3.f13 |   | `out , so` | 4.26 | ['1.80', '1.92', '0.79']
w3.f14 | x | `so he just` | 6.32 | ['6.10', '0.68', '-0.36']
w3.f15 | x | `so he just` | 5.16 | ['0.29', '3.48', '1.55']
w3.f16 | x | `ideas for two` | 8.02 | ['2.32', '3.80', '2.27']
w3.f17 | x | `could n't really` | 6.28 | ['2.57', '-1.63', '5.49']
w3.f18 | x | `two ideas for` | 7.78 | ['6.20', '1.04', '1.01']
w3.f19 | x | `‘ em together` | 10.28 | ['3.79', '5.79', '0.82']

## Original input: 
``` the @@UNK@@ 2002 @@UNK@@ of the american war for @@UNK@@ , complete with @@UNK@@ of cgi and @@UNK@@ of violence , but not a drop of human blood . ``` 

## Marked input: 
<pre>the @@UNK@@ <span style="background-color: #FFFF00">@</span>2002 <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of the american <span style="background-color: #FFFF00">@</span>war <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>for <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>, complete with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span>cgi <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span>violence <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>but <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>not <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>drop <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>human <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>blood <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `american war` | 4.78 | ['-1.12', '6.27']
w2.f1 | x | `complete with` | 5.29 | ['0.55', '4.87']
w2.f2 |   | `american war` | 0.53 | ['0.68', '0.89']
w2.f3 |   | `american war` | 1.21 | ['0.75', '1.01']
w2.f4 | x | `of cgi` | 5.22 | ['1.04', '4.37']
w2.f5 |   | `of human` | 3.01 | ['0.65', '2.66']
w2.f6 | x | `violence ,` | 4.86 | ['1.02', '3.93']
w2.f7 |   | `of violence` | 1.81 | ['0.11', '2.61']
w2.f8 |   | `complete with` | 3.19 | ['-0.10', '3.50']
w2.f9 |   | `violence ,` | 4.51 | ['4.19', '0.34']
w2.f10 | x | `of human` | 5.06 | ['-0.14', '5.34']
w2.f11 |   | `with @@UNK@@` | 2.33 | ['2.35', '0.25']
w2.f12 | x | `@@UNK@@ 2002` | 5.03 | ['-0.28', '5.35']
w2.f13 | x | `blood .` | 3.84 | ['3.97', '0.01']
w2.f14 |   | `complete with` | 3.02 | ['1.94', '1.12']
w2.f15 | x | `the american` | 5.19 | ['-0.42', '5.88']
w2.f16 | x | `of violence` | 3.03 | ['0.18', '3.60']
w2.f17 | x | `american war` | 3.67 | ['2.25', '2.04']
w2.f18 |   | `and @@UNK@@` | 1.62 | ['3.52', '-1.77']
w2.f19 |   | `of cgi` | 2.69 | ['1.68', '1.31']
w3.f0 | x | `complete with @@UNK@@` | 5.67 | ['3.92', '3.34', '-1.20']
w3.f1 | x | `drop of human` | 5.13 | ['3.80', '-0.85', '2.55']
w3.f2 | x | `, but not` | 7.24 | ['2.60', '0.33', '4.40']
w3.f3 | x | `drop of human` | 2.71 | ['1.76', '-1.38', '2.94']
w3.f4 |   | `@@UNK@@ , complete` | 2.94 | ['0.36', '0.77', '2.17']
w3.f5 | x | `of cgi and` | 5.20 | ['-0.94', '0.66', '5.81']
w3.f6 | x | `violence , but` | 3.99 | ['2.19', '0.38', '1.64']
w3.f7 |   | `drop of human` | 2.52 | ['1.47', '0.18', '1.37']
w3.f8 |   | `of violence ,` | 4.03 | ['1.71', '0.47', '2.14']
w3.f9 | x | `complete with @@UNK@@` | 4.63 | ['2.46', '0.14', '2.13']
w3.f10 | x | `not a drop` | 5.05 | ['0.23', '1.32', '3.65']
w3.f11 | x | `complete with @@UNK@@` | 3.85 | ['3.49', '1.30', '-0.75']
w3.f12 | x | `@@UNK@@ of violence` | 8.27 | ['-0.75', '3.24', '5.91']
w3.f13 | x | `the @@UNK@@ 2002` | 5.80 | ['4.70', '-1.74', '3.09']
w3.f14 | x | `of human blood` | 4.52 | ['-0.37', '1.38', '3.61']
w3.f15 | x | `american war for` | 5.20 | ['2.22', '3.55', '-0.40']
w3.f16 | x | `drop of human` | 5.08 | ['2.51', '-0.73', '3.68']
w3.f17 | x | `, but not` | 7.87 | ['0.73', '2.96', '4.34']
w3.f18 |   | `human blood .` | 3.12 | ['4.82', '-0.28', '-0.95']
w3.f19 | x | `a drop of` | 9.94 | ['3.70', '3.69', '2.66']

## Original input: 
``` watching queen of the damned is like reading a @@UNK@@ paper , with special effects tossed in . ``` 

## Marked input: 
<pre>watching <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>queen <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>damned is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>like <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>reading <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>paper <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>special <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>effects <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>tossed <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>in <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `watching queen` | 2.60 | ['-0.91', '3.89']
w2.f1 | x | `@@PAD@@ watching` | 3.92 | ['0.00', '4.06']
w2.f2 |   | `with special` | 0.29 | ['0.25', '1.09']
w2.f3 | x | `reading a` | 2.34 | ['2.65', '0.24']
w2.f4 | x | `paper ,` | 4.46 | ['2.15', '2.50']
w2.f5 | x | `effects tossed` | 6.97 | ['4.77', '2.50']
w2.f6 | x | `paper ,` | 4.57 | ['0.74', '3.93']
w2.f7 | x | `queen of` | 2.27 | ['3.67', '-0.50']
w2.f8 |   | `reading a` | 1.69 | ['-0.65', '2.56']
w2.f9 | x | `tossed in` | 6.72 | ['4.84', '1.89']
w2.f10 | x | `with special` | 5.94 | ['1.55', '4.52']
w2.f11 | x | `with special` | 4.18 | ['2.35', '2.10']
w2.f12 |   | `tossed in` | 2.99 | ['1.06', '1.97']
w2.f13 | x | `paper ,` | 3.64 | ['1.60', '2.18']
w2.f14 | x | `@@UNK@@ paper` | 9.35 | ['0.69', '8.69']
w2.f15 |   | `watching queen` | 2.68 | ['2.16', '0.79']
w2.f16 | x | `effects tossed` | 3.65 | ['1.41', '3.00']
w2.f17 |   | `watching queen` | 2.00 | ['0.06', '2.56']
w2.f18 |   | `reading a` | 2.95 | ['2.97', '0.10']
w2.f19 |   | `special effects` | 2.58 | ['1.36', '1.53']
w3.f0 | x | `paper , with` | 5.43 | ['7.68', '-0.76', '-1.09']
w3.f1 |   | `@@PAD@@ watching queen` | 2.58 | ['0.00', '2.95', '0.01']
w3.f2 | x | `like reading a` | 4.76 | ['0.27', '2.31', '2.27']
w3.f3 |   | `@@PAD@@ watching queen` | 0.77 | ['0.00', '-0.19', '1.57']
w3.f4 |   | `the damned is` | 2.61 | ['-0.24', '0.74', '2.46']
w3.f5 | x | `with special effects` | 7.30 | ['4.85', '1.73', '1.06']
w3.f6 | x | `special effects tossed` | 3.92 | ['-2.27', '3.61', '2.80']
w3.f7 |   | `@@PAD@@ @@PAD@@ watching` | 3.59 | ['0.00', '0.00', '4.09']
w3.f8 |   | `damned is like` | 4.17 | ['-0.14', '4.71', '-0.11']
w3.f9 | x | `like reading a` | 3.87 | ['1.41', '1.44', '1.13']
w3.f10 | x | `@@PAD@@ watching queen` | 4.69 | ['0.00', '0.62', '4.22']
w3.f11 | x | `with special effects` | 4.29 | ['0.40', '1.66', '2.43']
w3.f12 | x | `@@PAD@@ watching queen` | 7.71 | ['0.00', '0.75', '7.10']
w3.f13 | x | `watching queen of` | 7.74 | ['1.61', '3.68', '2.71']
w3.f14 | x | `damned is like` | 7.84 | ['1.38', '0.90', '5.65']
w3.f15 | x | `, with special` | 5.12 | ['1.52', '3.85', '-0.08']
w3.f16 |   | `effects tossed in` | 2.67 | ['-0.38', '2.99', '0.44']
w3.f17 | x | `effects tossed in` | 5.93 | ['3.98', '2.08', '0.03']
w3.f18 |   | `watching queen of` | 3.04 | ['2.92', '0.84', '-0.25']
w3.f19 | x | `damned is like` | 7.40 | ['1.94', '3.62', '1.96']

## Original input: 
``` one of the best looking and stylish animated movies in quite a while . . . ``` 

## Marked input: 
<pre>one of the <span style="background-color: #FFFF00">@</span>best <span style="background-color: #FFFF00">@</span>looking <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>stylish <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>animated <span style="background-color: #FFFF00">@</span>movies <span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span>quite <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>while <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `animated movies` | 3.29 | ['2.76', '0.90']
w2.f1 | x | `a while` | 7.74 | ['2.95', '4.92']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `quite a` | 2.79 | ['3.11', '0.24']
w2.f4 | x | `a while` | 3.85 | ['2.27', '1.77']
w2.f5 | x | `the best` | 5.04 | ['1.16', '4.18']
w2.f6 |   | `movies in` | 3.73 | ['3.21', '0.62']
w2.f7 |   | `quite a` | 0.79 | ['2.00', '-0.29']
w2.f8 | x | `quite a` | 6.64 | ['4.29', '2.56']
w2.f9 |   | `best looking` | 2.07 | ['-0.07', '2.15']
w2.f10 | x | `a while` | 3.63 | ['1.97', '1.79']
w2.f11 |   | `quite a` | 1.79 | ['3.81', '-1.75']
w2.f12 |   | `quite a` | 0.96 | ['2.27', '-1.27']
w2.f13 | x | `looking and` | 5.48 | ['5.06', '0.57']
w2.f14 | x | `best looking` | 9.08 | ['4.63', '4.49']
w2.f15 |   | `one of` | 2.06 | ['2.69', '-0.35']
w2.f16 | x | `in quite` | 6.90 | ['1.01', '6.65']
w2.f17 | x | `quite a` | 3.81 | ['7.03', '-2.61']
w2.f18 | x | `and stylish` | 6.75 | ['3.52', '3.36']
w2.f19 | x | `and stylish` | 5.53 | ['3.66', '2.17']
w3.f0 |   | `quite a while` | 1.64 | ['2.31', '3.29', '-3.57']
w3.f1 | x | `movies in quite` | 9.74 | ['1.01', '2.27', '6.83']
w3.f2 | x | `in quite a` | 3.72 | ['-1.65', '3.18', '2.27']
w3.f3 |   | `in quite a` | 1.62 | ['1.23', '1.45', '-0.45']
w3.f4 |   | `animated movies in` | 0.15 | ['1.11', '1.55', '-2.15']
w3.f5 | x | `a while .` | 8.48 | ['1.79', '2.70', '4.32']
w3.f6 |   | `a while .` | 2.82 | ['1.76', '2.55', '-1.28']
w3.f7 | x | `stylish animated movies` | 4.94 | ['0.75', '1.01', '3.68']
w3.f8 |   | `and stylish animated` | 1.56 | ['2.47', '-1.42', '0.80']
w3.f9 | x | `quite a while` | 5.58 | ['3.69', '-0.16', '2.16']
w3.f10 |   | `. . @@PAD@@` | 1.94 | ['0.09', '2.00', '0.00']
w3.f11 |   | `in quite a` | 2.41 | ['-1.82', '1.63', '2.78']
w3.f12 |   | `quite a while` | 3.10 | ['3.37', '-0.46', '0.32']
w3.f13 | x | `the best looking` | 9.29 | ['4.70', '4.31', '0.52']
w3.f14 |   | `best looking and` | 2.66 | ['2.15', '1.21', '-0.61']
w3.f15 |   | `@@PAD@@ one of` | 2.95 | ['0.00', '1.11', '2.01']
w3.f16 | x | `of the best` | 8.42 | ['1.87', '0.10', '6.84']
w3.f17 |   | `@@PAD@@ one of` | 2.19 | ['0.00', '0.48', '1.87']
w3.f18 | x | `quite a while` | 3.95 | ['4.49', '-0.07', '-0.01']
w3.f19 | x | `stylish animated movies` | 6.27 | ['0.98', '6.07', '-0.66']

## Original input: 
``` there is truth here ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>there <span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>truth <span style="background-color: #FFFF00">@</span>here</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `here @@PAD@@` | 0.44 | ['0.81', '0.00']
w2.f1 |   | `@@PAD@@ there` | 1.36 | ['0.00', '1.49']
w2.f2 |   | `truth here` | 0.92 | ['1.42', '0.55']
w2.f3 |   | `here @@PAD@@` | 1.12 | ['1.68', '0.00']
w2.f4 |   | `truth here` | 1.90 | ['0.32', '1.77']
w2.f5 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f6 |   | `there is` | 0.48 | ['0.24', '0.33']
w2.f7 |   | `truth here` | 0.93 | ['0.70', '1.14']
w2.f8 |   | `@@PAD@@ there` | 0.96 | ['0.00', '1.17']
w2.f9 |   | `truth here` | 2.60 | ['1.65', '0.97']
w2.f10 |   | `truth here` | 1.07 | ['0.95', '0.26']
w2.f11 |   | `truth here` | 1.80 | ['-0.58', '2.65']
w2.f12 |   | `is truth` | 1.96 | ['-0.59', '2.58']
w2.f13 | x | `truth here` | 3.67 | ['0.97', '2.84']
w2.f14 |   | `truth here` | 2.08 | ['1.87', '0.24']
w2.f15 | x | `is truth` | 4.32 | ['1.15', '3.44']
w2.f16 |   | `there is` | 0.81 | ['1.42', '0.15']
w2.f17 |   | `there is` | 2.66 | ['2.47', '0.80']
w2.f18 |   | `truth here` | 2.80 | ['0.47', '2.44']
w2.f19 |   | `truth here` | 2.41 | ['1.41', '1.30']
w3.f0 | x | `here @@PAD@@ @@PAD@@` | 3.93 | ['4.32', '0.00', '0.00']
w3.f1 | x | `is truth here` | 5.60 | ['1.18', '1.54', '3.26']
w3.f2 |   | `is truth here` | 2.08 | ['-0.81', '1.07', '1.91']
w3.f3 |   | `truth here @@PAD@@` | 0.14 | ['-0.01', '0.75', '0.00']
w3.f4 |   | `@@PAD@@ there is` | 2.86 | ['0.00', '0.75', '2.46']
w3.f5 |   | `truth here @@PAD@@` | 2.92 | ['1.07', '2.18', '0.00']
w3.f6 |   | `@@PAD@@ there is` | 2.36 | ['0.00', '0.93', '1.64']
w3.f7 |   | `truth here @@PAD@@` | 2.57 | ['0.27', '2.80', '0.00']
w3.f8 |   | `there is truth` | 4.03 | ['-0.38', '4.71', '-0.01']
w3.f9 | x | `@@PAD@@ @@PAD@@ there` | 4.23 | ['0.00', '0.00', '4.33']
w3.f10 | x | `here @@PAD@@ @@PAD@@` | 4.14 | ['4.29', '0.00', '0.00']
w3.f11 |   | `here @@PAD@@ @@PAD@@` | 1.77 | ['1.96', '0.00', '0.00']
w3.f12 |   | `@@PAD@@ there is` | 1.47 | ['0.00', '-0.22', '1.82']
w3.f13 | x | `there is truth` | 6.91 | ['1.13', '2.81', '3.22']
w3.f14 |   | `@@PAD@@ there is` | 1.81 | ['0.00', '-0.73', '2.63']
w3.f15 |   | `@@PAD@@ @@PAD@@ there` | 0.29 | ['0.00', '0.00', '0.46']
w3.f16 |   | `there is truth` | 2.86 | ['0.59', '-0.75', '3.40']
w3.f17 |   | `here @@PAD@@ @@PAD@@` | 1.78 | ['1.93', '0.00', '0.00']
w3.f18 |   | `is truth here` | 2.84 | ['-1.94', '3.24', '2.00']
w3.f19 | x | `there is truth` | 3.86 | ['-0.88', '3.62', '1.23']

## Original input: 
``` . . . an hour - and - a - half of inoffensive , unmemorable @@UNK@@ . ``` 

## Marked input: 
<pre>. . . an <span style="background-color: #6698FF">@</span>hour <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>- a - <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>half <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>inoffensive , <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>unmemorable <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `, unmemorable` | 0.36 | ['-1.14', '1.87']
w2.f1 | x | `a -` | 4.56 | ['2.95', '1.75']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `hour -` | 2.52 | ['2.54', '0.54']
w2.f4 | x | `an hour` | 5.33 | ['5.09', '0.43']
w2.f5 | x | `hour -` | 4.20 | ['5.09', '-0.58']
w2.f6 | x | `inoffensive ,` | 4.62 | ['0.79', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `a -` | 2.52 | ['0.88', '1.85']
w2.f9 |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 | x | `inoffensive ,` | 3.05 | ['3.55', '-0.37']
w2.f11 |   | `, unmemorable` | 1.22 | ['-0.67', '2.16']
w2.f12 | x | `an hour` | 5.42 | ['1.03', '4.43']
w2.f13 |   | `half of` | 2.80 | ['2.71', '0.24']
w2.f14 | x | `unmemorable @@UNK@@` | 4.37 | ['4.10', '0.30']
w2.f15 |   | `inoffensive ,` | 2.42 | ['3.00', '-0.31']
w2.f16 |   | `an hour` | 2.35 | ['2.54', '0.57']
w2.f17 |   | `inoffensive ,` | 0.59 | ['1.58', '-0.38']
w2.f18 |   | `and -` | 2.11 | ['3.52', '-1.28']
w2.f19 |   | `of inoffensive` | 2.22 | ['1.68', '0.84']
w3.f0 | x | `a - half` | 4.18 | ['-0.19', '1.13', '3.63']
w3.f1 |   | `. an hour` | 1.06 | ['-0.34', '1.98', '-0.21']
w3.f2 | x | `. an hour` | 4.58 | ['0.04', '1.76', '2.88']
w3.f3 |   | `@@PAD@@ @@PAD@@ .` | 0.00 | ['0.00', '0.00', '-0.75']
w3.f4 |   | `. an hour` | 0.76 | ['-0.66', '0.82', '0.95']
w3.f5 |   | `@@PAD@@ @@PAD@@ .` | 3.99 | ['0.00', '0.00', '4.32']
w3.f6 | x | `inoffensive , unmemorable` | 4.82 | ['1.99', '0.38', '2.66']
w3.f7 |   | `an hour -` | 3.46 | ['2.46', '-0.31', '1.81']
w3.f8 |   | `of inoffensive ,` | 3.29 | ['1.71', '-0.28', '2.14']
w3.f9 |   | `hour - and` | 3.36 | ['1.56', '-0.49', '2.40']
w3.f10 |   | `. . an` | 3.29 | ['0.09', '2.00', '1.34']
w3.f11 |   | `hour - and` | 2.78 | ['1.85', '0.54', '0.58']
w3.f12 |   | `hour - and` | 3.66 | ['-0.17', '2.81', '1.15']
w3.f13 |   | `an hour -` | 2.40 | ['1.41', '0.37', '0.87']
w3.f14 | x | `, unmemorable @@UNK@@` | 3.15 | ['-0.18', '4.79', '-1.37']
w3.f15 |   | `. an hour` | 2.19 | ['0.68', '1.61', '0.06']
w3.f16 | x | `inoffensive , unmemorable` | 9.55 | ['3.51', '3.78', '2.63']
w3.f17 |   | `hour - and` | 3.50 | ['3.52', '0.29', '-0.15']
w3.f18 |   | `of inoffensive ,` | 0.87 | ['-0.21', '0.76', '0.79']
w3.f19 | x | `a - half` | 4.48 | ['3.70', '1.48', '-0.59']

## Original input: 
``` at its best . . . festival in cannes @@UNK@@ with the excitement of the festival in cannes . ``` 

## Marked input: 
<pre>at its <span style="background-color: #FFFF00">@</span>best <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>. <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>. festival in <span style="background-color: #FFFF00">@</span>cannes <span style="background-color: #FFFF00">@</span>@@UNK@@ with <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>excitement <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>festival in cannes .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `festival in` | 5.31 | ['5.76', '-0.08']
w2.f1 | x | `@@UNK@@ with` | 3.86 | ['-0.88', '4.87']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `best .` | 0.66 | ['1.27', '-0.05']
w2.f4 |   | `in cannes` | 2.01 | ['-0.01', '2.21']
w2.f5 |   | `its best` | 1.92 | ['-1.96', '4.18']
w2.f6 | x | `at its` | 4.39 | ['2.94', '1.55']
w2.f7 |   | `at its` | 0.77 | ['1.98', '-0.30']
w2.f8 | x | `@@UNK@@ with` | 3.49 | ['0.21', '3.50']
w2.f9 |   | `at its` | 4.04 | ['4.66', '-0.60']
w2.f10 |   | `@@UNK@@ with` | 0.06 | ['-0.06', '0.25']
w2.f11 |   | `with the` | 2.51 | ['2.35', '0.42']
w2.f12 |   | `@@PAD@@ at` | 3.27 | ['0.00', '3.31']
w2.f13 |   | `excitement of` | 1.70 | ['1.61', '0.24']
w2.f14 | x | `best .` | 4.98 | ['4.63', '0.39']
w2.f15 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f16 |   | `of the` | 0.26 | ['0.18', '0.83']
w2.f17 |   | `@@PAD@@ at` | 0.76 | ['0.00', '1.38']
w2.f18 |   | `best .` | 2.64 | ['2.54', '0.22']
w2.f19 |   | `its best` | 2.34 | ['0.27', '2.36']
w3.f0 |   | `at its best` | 2.88 | ['1.31', '-2.01', '3.97']
w3.f1 | x | `at its best` | 11.56 | ['7.39', '-0.28', '4.83']
w3.f2 |   | `. . festival` | 1.84 | ['0.04', '-1.42', '3.31']
w3.f3 |   | `@@PAD@@ @@PAD@@ at` | 2.05 | ['0.00', '0.00', '2.65']
w3.f4 |   | `at its best` | 2.36 | ['1.13', '0.22', '1.37']
w3.f5 | x | `its best .` | 7.00 | ['1.92', '1.09', '4.32']
w3.f6 |   | `at its best` | 2.13 | ['-0.57', '0.89', '2.03']
w3.f7 |   | `@@PAD@@ at its` | 3.51 | ['0.00', '-0.58', '4.59']
w3.f8 |   | `its best .` | 2.79 | ['1.38', '3.57', '-1.87']
w3.f9 |   | `in cannes @@UNK@@` | 3.36 | ['1.57', '-0.24', '2.13']
w3.f10 |   | `. . festival` | 2.57 | ['0.09', '2.00', '0.62']
w3.f11 |   | `cannes @@UNK@@ with` | 3.53 | ['2.31', '-1.29', '2.70']
w3.f12 |   | `cannes @@UNK@@ with` | 2.88 | ['0.49', '-0.16', '2.68']
w3.f13 | x | `the excitement of` | 8.11 | ['4.70', '0.96', '2.71']
w3.f14 |   | `@@PAD@@ @@PAD@@ at` | 0.93 | ['0.00', '0.00', '1.02']
w3.f15 |   | `@@UNK@@ with the` | 2.38 | ['-0.51', '3.85', '-0.79']
w3.f16 | x | `at its best` | 7.15 | ['-1.52', '2.21', '6.84']
w3.f17 |   | `the excitement of` | 0.98 | ['-1.17', '0.44', '1.87']
w3.f18 |   | `@@UNK@@ with the` | 1.88 | ['-2.55', '2.32', '2.57']
w3.f19 |   | `with the excitement` | 2.00 | ['3.68', '-2.27', '0.71']

## Original input: 
``` this is amusing for about three minutes . ``` 

## Marked input: 
<pre>this is <span style="background-color: #FFFF00">@</span>amusing <span style="background-color: #FFFF00">@</span>for <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>about <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>three <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>minutes <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `amusing for` | 2.48 | ['0.75', '2.10']
w2.f1 |   | `about three` | 2.36 | ['-0.71', '3.21']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `three minutes` | 4.49 | ['0.92', '4.13']
w2.f4 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f5 | x | `amusing for` | 3.75 | ['2.42', '1.63']
w2.f6 |   | `about three` | 3.10 | ['0.72', '2.48']
w2.f7 |   | `three minutes` | 1.31 | ['-0.07', '2.29']
w2.f8 |   | `@@PAD@@ this` | 0.01 | ['0.00', '0.22']
w2.f9 |   | `amusing for` | 2.75 | ['3.34', '-0.57']
w2.f10 |   | `this is` | 0.40 | ['0.62', '-0.08']
w2.f11 | x | `about three` | 2.89 | ['1.20', '1.96']
w2.f12 | x | `about three` | 3.66 | ['-0.92', '4.62']
w2.f13 | x | `amusing for` | 3.54 | ['0.91', '2.78']
w2.f14 |   | `minutes .` | 0.94 | ['0.59', '0.39']
w2.f15 |   | `is amusing` | 2.16 | ['1.15', '1.28']
w2.f16 |   | `three minutes` | 0.81 | ['1.79', '-0.22']
w2.f17 |   | `three minutes` | 3.10 | ['3.86', '-0.14']
w2.f18 |   | `amusing for` | 3.13 | ['2.28', '0.97']
w2.f19 | x | `about three` | 3.35 | ['-0.59', '4.24']
w3.f0 |   | `amusing for about` | 1.67 | ['2.14', '-2.28', '2.20']
w3.f1 |   | `three minutes .` | 2.71 | ['4.79', '0.25', '-1.96']
w3.f2 |   | `for about three` | 2.68 | ['0.26', '1.19', '1.31']
w3.f3 |   | `@@PAD@@ @@PAD@@ this` | 0.00 | ['0.00', '0.00', '-1.76']
w3.f4 |   | `@@PAD@@ this is` | 2.08 | ['0.00', '-0.03', '2.46']
w3.f5 |   | `about three minutes` | 0.23 | ['-0.60', '-0.05', '1.21']
w3.f6 | x | `for about three` | 3.74 | ['1.51', '0.54', '1.90']
w3.f7 | x | `for about three` | 4.52 | ['1.19', '1.02', '2.80']
w3.f8 | x | `this is amusing` | 6.03 | ['-1.03', '4.71', '2.64']
w3.f9 |   | `@@PAD@@ this is` | 0.97 | ['0.00', '0.59', '0.49']
w3.f10 |   | `for about three` | 1.57 | ['-1.62', '3.15', '0.18']
w3.f11 |   | `@@PAD@@ this is` | 1.76 | ['0.00', '0.82', '1.14']
w3.f12 | x | `about three minutes` | 4.30 | ['0.83', '0.56', '3.04']
w3.f13 | x | `this is amusing` | 6.32 | ['3.44', '2.81', '0.33']
w3.f14 |   | `@@PAD@@ this is` | 1.01 | ['0.00', '-1.53', '2.63']
w3.f15 |   | `three minutes .` | 2.38 | ['-0.41', '3.56', '-0.60']
w3.f16 | x | `amusing for about` | 4.61 | ['0.75', '3.80', '0.44']
w3.f17 | x | `three minutes .` | 7.93 | ['2.78', '4.32', '0.98']
w3.f18 |   | `three minutes .` | 1.33 | ['3.79', '-1.05', '-0.95']
w3.f19 | x | `this is amusing` | 4.19 | ['-1.08', '3.62', '1.76']

## Original input: 
``` the gags , and the script , are a mixed bag . ``` 

## Marked input: 
<pre>the <span style="background-color: #6698FF">@</span>gags <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>script <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>are <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>mixed <span style="background-color: #6698FF">@</span>bag <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `a mixed` | 0.68 | ['1.11', '-0.06']
w2.f1 |   | `a mixed` | 2.57 | ['2.95', '-0.24']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `a mixed` | 3.38 | ['-0.30', '4.24']
w2.f4 | x | `gags ,` | 3.65 | ['1.34', '2.50']
w2.f5 |   | `the gags` | 1.02 | ['1.16', '0.16']
w2.f6 | x | `gags ,` | 5.33 | ['1.50', '3.93']
w2.f7 |   | `bag .` | 0.80 | ['1.57', '0.14']
w2.f8 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f9 | x | `script ,` | 6.91 | ['6.59', '0.34']
w2.f10 |   | `, and` | 0.62 | ['-0.72', '1.48']
w2.f11 | x | `mixed bag` | 5.14 | ['3.59', '1.82']
w2.f12 | x | `the gags` | 5.98 | ['0.53', '5.48']
w2.f13 |   | `gags ,` | 3.10 | ['1.07', '2.18']
w2.f14 | x | `gags ,` | 4.61 | ['3.75', '0.89']
w2.f15 |   | `, are` | 1.55 | ['2.19', '-0.37']
w2.f16 |   | `mixed bag` | 1.48 | ['1.25', '0.98']
w2.f17 |   | `bag .` | 3.14 | ['3.29', '0.47']
w2.f18 | x | `and the` | 3.34 | ['3.52', '-0.05']
w2.f19 | x | `and the` | 3.56 | ['3.66', '0.20']
w3.f0 | x | `are a mixed` | 5.70 | ['-0.93', '3.29', '3.73']
w3.f1 |   | `are a mixed` | 2.14 | ['1.91', '-0.71', '1.31']
w3.f2 | x | `and the script` | 5.56 | ['-0.38', '0.94', '5.10']
w3.f3 |   | `@@PAD@@ @@PAD@@ the` | 0.00 | ['0.00', '0.00', '-2.04']
w3.f4 |   | `gags , and` | 0.84 | ['1.52', '0.77', '-1.09']
w3.f5 | x | `gags , and` | 8.31 | ['1.43', '1.40', '5.81']
w3.f6 | x | `@@PAD@@ the gags` | 4.24 | ['0.00', '0.45', '4.00']
w3.f7 |   | `gags , and` | 1.05 | ['0.08', '-0.37', '1.83']
w3.f8 |   | `the gags ,` | 1.61 | ['1.05', '-1.30', '2.14']
w3.f9 |   | `a mixed bag` | 3.16 | ['-2.87', '5.98', '0.15']
w3.f10 | x | `bag . @@PAD@@` | 4.89 | ['3.04', '2.00', '0.00']
w3.f11 |   | `bag . @@PAD@@` | 0.92 | ['2.80', '-1.68', '0.00']
w3.f12 | x | `mixed bag .` | 7.76 | ['4.50', '1.78', '1.61']
w3.f13 | x | `the gags ,` | 5.57 | ['4.70', '1.15', '-0.03']
w3.f14 | x | `a mixed bag` | 4.70 | ['-2.02', '3.84', '2.97']
w3.f15 | x | `the script ,` | 5.89 | ['-0.02', '3.37', '2.70']
w3.f16 |   | `a mixed bag` | 0.54 | ['-0.19', '1.04', '0.07']
w3.f17 | x | `a mixed bag` | 8.17 | ['-1.31', '4.50', '5.13']
w3.f18 |   | `@@PAD@@ @@PAD@@ the` | 2.10 | ['0.00', '0.00', '2.57']
w3.f19 | x | `script , are` | 6.52 | ['0.76', '1.68', '4.20']

## Original input: 
``` superb production values & christian @@UNK@@ 's charisma make up for a derivative plot . ``` 

## Marked input: 
<pre>superb production <span style="background-color: #6698FF">@</span>values <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>& <span style="background-color: #FFFF00">@</span>christian <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>charisma <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>make <span style="background-color: #6698FF">@</span>up <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>for <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>derivative <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>plot <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `& christian` | 4.46 | ['3.18', '1.65']
w2.f1 |   | `charisma make` | 2.98 | ['1.80', '1.31']
w2.f2 |   | `superb production` | 0.48 | ['0.66', '0.86']
w2.f3 |   | `@@PAD@@ superb` | 0.51 | ['0.00', '1.06']
w2.f4 |   | `'s charisma` | 3.55 | ['-0.76', '4.49']
w2.f5 | x | `& christian` | 6.83 | ['6.22', '0.91']
w2.f6 |   | `make up` | 2.37 | ['1.72', '0.75']
w2.f7 |   | `plot .` | 1.78 | ['2.55', '0.14']
w2.f8 | x | `@@UNK@@ 's` | 3.81 | ['0.21', '3.82']
w2.f9 |   | `production values` | 4.41 | ['4.93', '-0.51']
w2.f10 | x | `make up` | 9.25 | ['2.45', '6.94']
w2.f11 | x | `superb production` | 6.03 | ['3.67', '2.63']
w2.f12 |   | `& christian` | 2.45 | ['2.06', '0.43']
w2.f13 | x | `make up` | 3.81 | ['1.73', '2.23']
w2.f14 |   | `production values` | 2.17 | ['2.49', '-0.28']
w2.f15 |   | `superb production` | 3.18 | ['2.41', '1.05']
w2.f16 |   | `charisma make` | 1.82 | ['3.37', '-0.79']
w2.f17 | x | `plot .` | 3.99 | ['4.14', '0.47']
w2.f18 |   | `@@PAD@@ superb` | 1.83 | ['0.00', '1.95']
w2.f19 |   | `charisma make` | 3.05 | ['2.70', '0.64']
w3.f0 |   | `derivative plot .` | 3.44 | ['2.64', '0.82', '0.37']
w3.f1 | x | `values & christian` | 5.08 | ['1.20', '3.69', '0.57']
w3.f2 | x | `a derivative plot` | 5.75 | ['1.87', '2.40', '1.57']
w3.f3 | x | `& christian @@UNK@@` | 3.18 | ['3.47', '0.25', '0.07']
w3.f4 | x | `values & christian` | 3.76 | ['-0.71', '3.70', '1.12']
w3.f5 |   | `@@PAD@@ superb production` | 2.14 | ['0.00', '3.81', '-1.34']
w3.f6 | x | `'s charisma make` | 6.13 | ['3.62', '-0.18', '2.90']
w3.f7 |   | `@@PAD@@ @@PAD@@ superb` | 1.64 | ['0.00', '0.00', '2.14']
w3.f8 | x | `production values &` | 5.62 | ['2.37', '-3.07', '6.61']
w3.f9 |   | `plot . @@PAD@@` | 2.86 | ['2.38', '0.58', '0.00']
w3.f10 |   | `plot . @@PAD@@` | 2.09 | ['0.24', '2.00', '0.00']
w3.f11 | x | `derivative plot .` | 4.98 | ['2.54', '2.71', '-0.08']
w3.f12 |   | `plot . @@PAD@@` | 3.12 | ['3.81', '-0.56', '0.00']
w3.f13 |   | `make up for` | 3.08 | ['1.78', '1.31', '0.23']
w3.f14 | x | `charisma make up` | 5.00 | ['2.00', '3.47', '-0.38']
w3.f15 |   | `for a derivative` | 3.20 | ['0.38', '-0.09', '3.08']
w3.f16 | x | `values & christian` | 5.78 | ['-0.70', '2.65', '4.21']
w3.f17 | x | `up for a` | 5.49 | ['2.46', '5.11', '-1.92']
w3.f18 |   | `make up for` | 2.91 | ['1.07', '1.30', '1.01']
w3.f19 | x | `up for a` | 5.47 | ['3.39', '2.83', '-0.64']

## Original input: 
``` the movie 's @@UNK@@ force still feels like an ugly @@UNK@@ @@UNK@@ in your stomach . but is that @@UNK@@ from dramatic tension or a @@UNK@@ of artistic @@UNK@@ ? ``` 

## Marked input: 
<pre>the movie 's @@UNK@@ force <span style="background-color: #FFFF00">@</span>still <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>feels <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>like <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>an <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>ugly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ in your <span style="background-color: #6698FF">@</span>stomach <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>but <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>that @@UNK@@ from dramatic tension <span style="background-color: #6698FF">@</span>or <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>@@UNK@@ of artistic @@UNK@@ ?</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ force` | 3.11 | ['1.98', '1.50']
w2.f1 |   | `your stomach` | 3.05 | ['1.93', '1.25']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `tension or` | 3.95 | ['3.93', '0.57']
w2.f4 | x | `still feels` | 7.95 | ['8.07', '0.06']
w2.f5 | x | `like an` | 4.00 | ['3.40', '0.91']
w2.f6 | x | `still feels` | 4.97 | ['3.07', '2.00']
w2.f7 | x | `in your` | 2.78 | ['0.14', '3.55']
w2.f8 |   | `movie 's` | 2.07 | ['-1.54', '3.82']
w2.f9 |   | `@@UNK@@ in` | 4.26 | ['2.38', '1.89']
w2.f10 | x | `force still` | 4.23 | ['3.18', '1.18']
w2.f11 | x | `your stomach` | 4.85 | ['1.68', '3.44']
w2.f12 | x | `still feels` | 6.86 | ['1.28', '5.62']
w2.f13 | x | `feels like` | 3.64 | ['0.76', '3.03']
w2.f14 |   | `still feels` | 2.82 | ['-1.10', '3.95']
w2.f15 |   | `from dramatic` | 2.76 | ['1.33', '1.71']
w2.f16 | x | `dramatic tension` | 3.49 | ['-0.14', '4.39']
w2.f17 | x | `dramatic tension` | 4.80 | ['-0.00', '5.42']
w2.f18 |   | `movie 's` | 1.80 | ['0.81', '1.12']
w2.f19 |   | `feels like` | 2.77 | ['1.78', '1.28']
w3.f0 | x | `in your stomach` | 7.71 | ['-0.14', '2.36', '5.88']
w3.f1 |   | `that @@UNK@@ from` | 1.57 | ['-1.39', '-0.73', '4.08']
w3.f2 | x | `dramatic tension or` | 7.23 | ['2.46', '1.56', '3.30']
w3.f3 |   | `still feels like` | 1.96 | ['2.44', '-0.56', '0.68']
w3.f4 | x | `still feels like` | 4.09 | ['1.03', '0.19', '3.23']
w3.f5 |   | `@@UNK@@ from dramatic` | 2.60 | ['0.08', '1.12', '1.73']
w3.f6 | x | `stomach . but` | 4.04 | ['1.54', '1.07', '1.64']
w3.f7 |   | `that @@UNK@@ from` | 4.10 | ['3.01', '-1.81', '3.40']
w3.f8 | x | `@@UNK@@ force still` | 4.37 | ['0.50', '-0.67', '4.83']
w3.f9 | x | `like an ugly` | 7.10 | ['1.41', '3.18', '2.63']
w3.f10 | x | `stomach . but` | 5.43 | ['0.56', '2.00', '3.02']
w3.f11 | x | `force still feels` | 5.82 | ['3.49', '0.35', '2.17']
w3.f12 | x | `still feels like` | 7.53 | ['-0.69', '3.44', '4.91']
w3.f13 |   | `but is that` | 4.09 | ['1.09', '2.81', '0.44']
w3.f14 | x | `still feels like` | 7.92 | ['-0.17', '2.53', '5.65']
w3.f15 | x | `feels like an` | 6.02 | ['2.91', '2.60', '0.67']
w3.f16 |   | `that @@UNK@@ from` | 3.22 | ['1.08', '-0.81', '3.33']
w3.f17 | x | `force still feels` | 5.14 | ['5.02', '1.35', '-1.07']
w3.f18 |   | `@@PAD@@ @@PAD@@ the` | 2.10 | ['0.00', '0.00', '2.57']
w3.f19 | x | `feels like an` | 4.64 | ['-0.84', '3.53', '2.07']

## Original input: 
``` it 's supposed to be a romantic comedy - it suffers from too much @@UNK@@ @@UNK@@ and not enough pretty woman . ``` 

## Marked input: 
<pre>it 's <span style="background-color: #6698FF">@</span>supposed <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>be <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>romantic <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>comedy <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>suffers <span style="background-color: #6698FF">@</span>from <span style="background-color: #6698FF">@</span>too <span style="background-color: #6698FF">@</span>much <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>and not <span style="background-color: #6698FF">@</span>enough <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>pretty <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>woman <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `not enough` | 1.69 | ['-0.06', '2.12']
w2.f1 | x | `comedy -` | 4.02 | ['2.40', '1.75']
w2.f2 |   | `enough pretty` | 0.12 | ['1.07', '0.09']
w2.f3 | x | `from too` | 3.66 | ['0.12', '4.09']
w2.f4 | x | `a romantic` | 7.53 | ['2.27', '5.45']
w2.f5 | x | `much @@UNK@@` | 3.85 | ['4.87', '-0.71']
w2.f6 |   | `suffers from` | 3.39 | ['1.91', '1.58']
w2.f7 |   | `romantic comedy` | 1.32 | ['-0.23', '2.46']
w2.f8 |   | `a romantic` | 3.07 | ['0.88', '2.41']
w2.f9 |   | `suffers from` | 4.12 | ['5.77', '-1.64']
w2.f10 | x | `a romantic` | 5.12 | ['1.97', '3.29']
w2.f11 | x | `too much` | 3.89 | ['3.88', '0.28']
w2.f12 | x | `pretty woman` | 7.11 | ['2.53', '4.62']
w2.f13 |   | `pretty woman` | 2.20 | ['2.33', '0.02']
w2.f14 | x | `it suffers` | 3.81 | ['1.93', '1.91']
w2.f15 | x | `enough pretty` | 3.55 | ['2.11', '1.70']
w2.f16 | x | `'s supposed` | 6.12 | ['-1.72', '8.60']
w2.f17 |   | `and not` | 2.99 | ['1.02', '2.58']
w2.f18 | x | `pretty woman` | 4.50 | ['2.47', '2.16']
w2.f19 | x | `pretty woman` | 7.06 | ['3.81', '3.55']
w3.f0 | x | `it 's supposed` | 4.12 | ['-0.60', '1.91', '3.19']
w3.f1 | x | `enough pretty woman` | 7.28 | ['2.10', '2.16', '3.40']
w3.f2 | x | `- it suffers` | 8.96 | ['2.02', '1.70', '5.33']
w3.f3 |   | `enough pretty woman` | 0.92 | ['-0.33', '-0.50', '2.35']
w3.f4 | x | `enough pretty woman` | 3.65 | ['1.59', '0.16', '2.26']
w3.f5 | x | `a romantic comedy` | 7.31 | ['1.79', '1.50', '4.35']
w3.f6 | x | `and not enough` | 5.38 | ['-0.42', '1.86', '4.15']
w3.f7 |   | `to be a` | 1.65 | ['3.76', '-0.79', '-0.82']
w3.f8 | x | `not enough pretty` | 5.49 | ['0.51', '3.28', '1.99']
w3.f9 | x | `supposed to be` | 8.23 | ['4.73', '0.70', '2.91']
w3.f10 | x | `a romantic comedy` | 3.99 | ['-2.42', '2.28', '4.28']
w3.f11 | x | `'s supposed to` | 6.63 | ['-1.43', '6.19', '2.06']
w3.f12 | x | `suffers from too` | 5.75 | ['0.79', '1.57', '3.52']
w3.f13 |   | `enough pretty woman` | 4.29 | ['0.22', '4.91', '-0.60']
w3.f14 | x | `it 's supposed` | 9.94 | ['0.08', '1.15', '8.80']
w3.f15 |   | `it suffers from` | 3.29 | ['0.62', '0.01', '2.82']
w3.f16 | x | `pretty woman .` | 3.94 | ['4.49', '2.11', '-2.29']
w3.f17 | x | `it 's supposed` | 8.60 | ['1.06', '-0.23', '7.92']
w3.f18 |   | `enough pretty woman` | 1.62 | ['1.43', '0.62', '0.03']
w3.f19 |   | `a romantic comedy` | 3.49 | ['3.70', '-1.47', '1.37']

## Original input: 
``` eccentric enough to @@UNK@@ off @@UNK@@ , caruso 's self - conscious debut is also @@UNK@@ forgettable . ``` 

## Marked input: 
<pre>eccentric <span style="background-color: #FFFF00">@</span>enough <span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>off <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>, caruso 's <span style="background-color: #FFFF00">@</span>self <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>conscious <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>debut <span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>also <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>forgettable .</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `eccentric enough` | 1.78 | ['0.03', '2.12']
w2.f1 |   | `caruso 's` | 3.13 | ['1.69', '1.57']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `@@UNK@@ forgettable` | 1.25 | ['-0.08', '1.89']
w2.f4 |   | `conscious debut` | 1.74 | ['0.58', '1.34']
w2.f5 | x | `eccentric enough` | 4.25 | ['3.92', '0.63']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `- conscious` | 0.29 | ['-1.81', '3.01']
w2.f8 | x | `caruso 's` | 5.96 | ['2.36', '3.82']
w2.f9 | x | `enough to` | 6.85 | ['2.20', '4.67']
w2.f10 |   | `, caruso` | 1.82 | ['-0.72', '2.68']
w2.f11 |   | `eccentric enough` | 1.81 | ['2.68', '-0.59']
w2.f12 |   | `'s self` | 3.27 | ['0.44', '2.86']
w2.f13 | x | `self -` | 3.42 | ['2.37', '1.20']
w2.f14 | x | `@@UNK@@ off` | 5.12 | ['0.69', '4.47']
w2.f15 | x | `@@PAD@@ eccentric` | 5.52 | ['0.00', '5.79']
w2.f16 |   | `eccentric enough` | 0.15 | ['0.45', '0.47']
w2.f17 | x | `- conscious` | 4.31 | ['0.23', '4.70']
w2.f18 |   | `enough to` | 3.03 | ['0.66', '2.50']
w2.f19 |   | `eccentric enough` | 3.06 | ['2.32', '1.05']
w3.f0 | x | `conscious debut is` | 4.75 | ['0.81', '4.20', '0.12']
w3.f1 | x | `caruso 's self` | 8.33 | ['8.20', '-0.93', '1.43']
w3.f2 | x | `'s self -` | 4.30 | ['0.87', '2.98', '0.54']
w3.f3 |   | `@@PAD@@ eccentric enough` | 1.80 | ['0.00', '1.04', '1.36']
w3.f4 |   | `@@PAD@@ eccentric enough` | 3.13 | ['0.00', '0.98', '2.51']
w3.f5 |   | `@@UNK@@ forgettable .` | 4.96 | ['0.08', '0.89', '4.32']
w3.f6 |   | `@@PAD@@ eccentric enough` | 2.90 | ['0.00', '-1.04', '4.15']
w3.f7 |   | `debut is also` | 2.29 | ['2.98', '-1.18', '0.98']
w3.f8 |   | `enough to @@UNK@@` | 2.81 | ['1.75', '1.89', '-0.54']
w3.f9 |   | `@@PAD@@ @@PAD@@ eccentric` | 2.08 | ['0.00', '0.00', '2.19']
w3.f10 | x | `conscious debut is` | 7.12 | ['4.01', '2.23', '1.03']
w3.f11 |   | `- conscious debut` | 3.14 | ['1.42', '-0.70', '2.61']
w3.f12 |   | `self - conscious` | 2.25 | ['-0.51', '2.81', '0.08']
w3.f13 | x | `'s self -` | 5.89 | ['0.09', '5.18', '0.87']
w3.f14 |   | `to @@UNK@@ off` | 2.77 | ['-0.10', '0.79', '2.18']
w3.f15 |   | `@@PAD@@ eccentric enough` | 2.10 | ['0.00', '0.64', '1.63']
w3.f16 | x | `@@PAD@@ eccentric enough` | 7.17 | ['0.00', '2.56', '4.99']
w3.f17 |   | `self - conscious` | 2.64 | ['1.56', '0.29', '0.95']
w3.f18 |   | `eccentric enough to` | 2.14 | ['1.63', '-0.55', '1.52']
w3.f19 | x | `debut is also` | 7.46 | ['1.30', '3.62', '2.65']

## Original input: 
``` while the @@UNK@@ delivered hokum of hart 's war is never fun , it 's still a worthy addition to the growing canon of post - saving private ryan @@UNK@@ to the greatest generation . ``` 

## Marked input: 
<pre>while <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ delivered hokum <span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hart <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>'s <span style="background-color: #FFFF00">@</span>war <span style="background-color: #FFFF00">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>never <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>fun <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>still a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>worthy <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>addition <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the growing <span style="background-color: #FFFF00">@</span>canon <span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span>post <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>saving <span style="background-color: #6698FF">@</span>private <span style="background-color: #6698FF">@</span>ryan <span style="background-color: #6698FF">@</span>@@UNK@@ to <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>greatest <span style="background-color: #FFFF00">@</span>generation <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `'s war` | 5.69 | ['-0.21', '6.27']
w2.f1 | x | `@@PAD@@ while` | 4.79 | ['0.00', '4.92']
w2.f2 |   | `growing canon` | 2.00 | ['1.72', '1.32']
w2.f3 | x | `delivered hokum` | 4.27 | ['0.63', '4.20']
w2.f4 | x | `still a` | 7.87 | ['8.07', '-0.02']
w2.f5 |   | `hokum of` | 2.11 | ['0.65', '1.76']
w2.f6 |   | `fun ,` | 3.75 | ['-0.09', '3.93']
w2.f7 |   | `canon of` | 1.63 | ['3.04', '-0.50']
w2.f8 | x | `still a` | 3.47 | ['1.13', '2.56']
w2.f9 | x | `@@UNK@@ to` | 7.04 | ['2.38', '4.67']
w2.f10 | x | `a worthy` | 6.31 | ['1.97', '4.47']
w2.f11 | x | `delivered hokum` | 7.12 | ['0.98', '6.42']
w2.f12 |   | `to the` | 2.81 | ['1.53', '1.32']
w2.f13 | x | `canon of` | 3.30 | ['3.21', '0.24']
w2.f14 | x | `- saving` | 3.32 | ['-0.18', '3.53']
w2.f15 | x | `the growing` | 3.74 | ['-0.42', '4.42']
w2.f16 | x | `a worthy` | 2.78 | ['-0.39', '3.93']
w2.f17 | x | `worthy addition` | 5.43 | ['3.47', '2.57']
w2.f18 | x | `fun ,` | 4.06 | ['3.29', '0.89']
w2.f19 |   | `of post` | 3.10 | ['1.68', '1.73']
w3.f0 | x | `still a worthy` | 7.26 | ['2.10', '3.29', '2.26']
w3.f1 | x | `is never fun` | 3.78 | ['1.18', '-0.55', '3.53']
w3.f2 | x | `never fun ,` | 5.65 | ['6.11', '-1.70', '1.32']
w3.f3 | x | `a worthy addition` | 3.71 | ['-0.28', '1.03', '3.57']
w3.f4 |   | `saving private ryan` | 3.03 | ['1.28', '1.59', '0.52']
w3.f5 | x | `greatest generation .` | 5.77 | ['1.12', '0.65', '4.32']
w3.f6 | x | `- saving private` | 7.10 | ['0.68', '3.80', '2.82']
w3.f7 | x | `still a worthy` | 4.68 | ['4.62', '0.48', '0.08']
w3.f8 | x | `a worthy addition` | 7.16 | ['0.66', '5.93', '0.86']
w3.f9 | x | `never fun ,` | 5.35 | ['1.13', '1.26', '3.06']
w3.f10 | x | `still a worthy` | 5.07 | ['2.16', '1.32', '1.73']
w3.f11 | x | `war is never` | 6.31 | ['0.49', '-0.19', '6.21']
w3.f12 | x | `post - saving` | 5.68 | ['1.56', '2.81', '1.44']
w3.f13 | x | `the greatest generation` | 6.68 | ['4.70', '0.27', '1.95']
w3.f14 | x | `a worthy addition` | 4.02 | ['-2.02', '2.78', '3.35']
w3.f15 |   | `, it 's` | 3.74 | ['1.52', '2.22', '0.17']
w3.f16 | x | `fun , it` | 11.14 | ['5.88', '3.78', '1.86']
w3.f17 | x | `delivered hokum of` | 7.71 | ['2.79', '3.22', '1.87']
w3.f18 | x | `hokum of hart` | 6.71 | ['4.05', '2.10', '1.04']
w3.f19 | x | `a worthy addition` | 6.23 | ['3.70', '2.79', '-0.14']

## Original input: 
``` solondz creates some effective moments of @@UNK@@ for character and viewer alike . ``` 

## Marked input: 
<pre>solondz <span style="background-color: #FFFF00">@</span>creates <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>some <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>effective <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>moments <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>for <span style="background-color: #FFFF00">@</span>character <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>viewer <span style="background-color: #6698FF">@</span>alike <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `for character` | 6.28 | ['1.57', '5.09']
w2.f1 | x | `viewer alike` | 4.07 | ['2.55', '1.65']
w2.f2 |   | `viewer alike` | 0.54 | ['0.76', '0.83']
w2.f3 |   | `and viewer` | 2.05 | ['0.06', '2.54']
w2.f4 |   | `effective moments` | 1.51 | ['0.88', '0.82']
w2.f5 |   | `creates some` | 1.88 | ['1.86', '0.32']
w2.f6 |   | `effective moments` | 1.47 | ['1.46', '0.11']
w2.f7 | x | `alike .` | 2.13 | ['2.89', '0.14']
w2.f8 | x | `some effective` | 3.38 | ['0.39', '3.20']
w2.f9 |   | `solondz creates` | 1.91 | ['2.93', '-1.00']
w2.f10 |   | `creates some` | 2.04 | ['4.34', '-2.16']
w2.f11 | x | `creates some` | 4.53 | ['0.98', '3.82']
w2.f12 | x | `for character` | 4.75 | ['-0.10', '4.89']
w2.f13 | x | `solondz creates` | 5.05 | ['2.15', '3.05']
w2.f14 | x | `and viewer` | 3.30 | ['0.13', '3.20']
w2.f15 | x | `some effective` | 6.36 | ['-0.19', '6.82']
w2.f16 | x | `viewer alike` | 3.72 | ['-0.35', '4.84']
w2.f17 |   | `creates some` | 2.37 | ['-1.21', '4.19']
w2.f18 | x | `effective moments` | 3.64 | ['3.95', '-0.20']
w2.f19 | x | `creates some` | 4.07 | ['3.69', '0.67']
w3.f0 |   | `some effective moments` | 2.37 | ['-0.28', '1.80', '1.23']
w3.f1 |   | `character and viewer` | 2.01 | ['4.07', '-1.74', '0.06']
w3.f2 |   | `viewer alike .` | 3.18 | ['0.15', '2.27', '0.84']
w3.f3 |   | `alike . @@PAD@@` | 0.48 | ['1.23', '-0.14', '0.00']
w3.f4 |   | `some effective moments` | 2.47 | ['0.52', '1.99', '0.31']
w3.f5 | x | `@@PAD@@ solondz creates` | 6.05 | ['0.00', '1.60', '4.78']
w3.f6 |   | `viewer alike .` | 2.26 | ['2.24', '1.52', '-1.28']
w3.f7 |   | `@@PAD@@ solondz creates` | 2.95 | ['0.00', '2.69', '0.76']
w3.f8 | x | `creates some effective` | 7.85 | ['3.20', '3.55', '1.38']
w3.f9 | x | `alike . @@PAD@@` | 6.67 | ['6.20', '0.58', '0.00']
w3.f10 |   | `@@PAD@@ solondz creates` | 2.90 | ['0.00', '0.50', '2.54']
w3.f11 |   | `for character and` | 2.60 | ['-1.44', '3.65', '0.58']
w3.f12 |   | `character and viewer` | 2.07 | ['1.49', '0.95', '-0.24']
w3.f13 | x | `effective moments of` | 7.04 | ['-0.71', '5.30', '2.71']
w3.f14 | x | `alike . @@PAD@@` | 3.39 | ['4.15', '-0.66', '0.00']
w3.f15 |   | `for character and` | 2.02 | ['0.38', '2.28', '-0.48']
w3.f16 | x | `@@UNK@@ for character` | 5.14 | ['-1.96', '3.80', '3.68']
w3.f17 | x | `creates some effective` | 4.37 | ['0.16', '4.63', '-0.26']
w3.f18 |   | `@@PAD@@ solondz creates` | 0.84 | ['0.00', '0.10', '1.21']
w3.f19 |   | `creates some effective` | 3.83 | ['3.34', '-1.20', '1.80']

## Original input: 
``` it gets the details of its time frame right but it completely misses its emotions . ``` 

## Marked input: 
<pre>it gets the <span style="background-color: #6698FF">@</span>details <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>its <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>time <span style="background-color: #6698FF">@</span>frame <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>right <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>but <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>completely <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>misses <span style="background-color: #6698FF">@</span>its <span style="background-color: #6698FF">@</span>emotions <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `completely misses` | 4.09 | ['1.33', '3.14']
w2.f1 | x | `but it` | 5.95 | ['4.31', '1.78']
w2.f2 |   | `its time` | 0.65 | ['0.27', '1.43']
w2.f3 | x | `completely misses` | 3.67 | ['0.27', '3.96']
w2.f4 |   | `the details` | 2.73 | ['-1.38', '4.31']
w2.f5 |   | `frame right` | 2.07 | ['3.14', '-0.77']
w2.f6 |   | `frame right` | 3.04 | ['2.57', '0.57']
w2.f7 | x | `it completely` | 3.15 | ['-0.01', '4.07']
w2.f8 |   | `@@PAD@@ it` | 1.54 | ['0.00', '1.75']
w2.f9 |   | `details of` | 2.78 | ['1.14', '1.65']
w2.f10 | x | `right but` | 3.18 | ['2.07', '1.25']
w2.f11 | x | `completely misses` | 3.46 | ['0.70', '3.03']
w2.f12 | x | `it completely` | 5.39 | ['-0.01', '5.44']
w2.f13 |   | `frame right` | 2.53 | ['2.11', '0.56']
w2.f14 | x | `time frame` | 3.62 | ['-0.95', '4.60']
w2.f15 |   | `the details` | 1.91 | ['-0.42', '2.60']
w2.f16 |   | `completely misses` | 0.82 | ['0.92', '0.66']
w2.f17 |   | `details of` | 0.91 | ['2.36', '-0.84']
w2.f18 | x | `emotions .` | 5.46 | ['5.36', '0.22']
w2.f19 |   | `its emotions` | 1.35 | ['0.27', '1.38']
w3.f0 | x | `details of its` | 5.00 | ['5.67', '-1.37', '1.08']
w3.f1 |   | `its time frame` | 2.40 | ['0.80', '1.22', '0.76']
w3.f2 | x | `gets the details` | 5.07 | ['-0.78', '0.94', '4.99']
w3.f3 | x | `time frame right` | 3.31 | ['1.81', '1.90', '0.21']
w3.f4 |   | `completely misses its` | 1.84 | ['1.70', '0.51', '-0.00']
w3.f5 | x | `its emotions .` | 7.72 | ['1.92', '1.80', '4.32']
w3.f6 | x | `it completely misses` | 3.78 | ['0.54', '1.53', '1.91']
w3.f7 | x | `time frame right` | 6.01 | ['-0.30', '4.14', '2.67']
w3.f8 |   | `it gets the` | 2.68 | ['2.11', '3.63', '-2.77']
w3.f9 | x | `completely misses its` | 4.85 | ['-0.54', '2.20', '3.30']
w3.f10 |   | `time frame right` | 3.60 | ['-1.26', '2.99', '2.01']
w3.f11 | x | `it completely misses` | 3.72 | ['1.01', '0.11', '2.79']
w3.f12 | x | `the details of` | 5.22 | ['2.43', '2.23', '0.69']
w3.f13 | x | `the details of` | 7.03 | ['4.70', '-0.12', '2.71']
w3.f14 | x | `but it completely` | 5.37 | ['1.72', '-0.67', '4.41']
w3.f15 | x | `time frame right` | 3.99 | ['2.01', '0.20', '1.95']
w3.f16 |   | `of its time` | 2.32 | ['1.87', '2.21', '-1.38']
w3.f17 | x | `misses its emotions` | 4.69 | ['4.23', '-0.26', '0.89']
w3.f18 |   | `of its time` | 2.84 | ['-0.21', '1.12', '2.39']
w3.f19 |   | `its time frame` | 3.78 | ['3.31', '-0.91', '1.50']

## Original input: 
``` the film is really closer to porn than a serious @@UNK@@ of what 's wrong with this increasingly @@UNK@@ aspect of gay culture . ``` 

## Marked input: 
<pre>the film <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>really <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>closer <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span>porn <span style="background-color: #FFFF00">@</span>than <span style="background-color: #FFFF00">@</span>a serious @@UNK@@ of what 's wrong <span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>this <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>increasingly <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>aspect <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>gay culture <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `gay culture` | 4.61 | ['0.13', '4.86']
w2.f1 | x | `wrong with` | 6.84 | ['2.10', '4.87']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `this increasingly` | 2.21 | ['0.36', '2.41']
w2.f4 | x | `closer to` | 6.56 | ['7.20', '-0.45']
w2.f5 | x | `really closer` | 3.54 | ['0.70', '3.14']
w2.f6 |   | `is really` | 2.21 | ['-0.01', '2.32']
w2.f7 |   | `wrong with` | 1.43 | ['2.78', '-0.44']
w2.f8 | x | `wrong with` | 5.88 | ['2.59', '3.50']
w2.f9 |   | `@@UNK@@ of` | 4.02 | ['2.38', '1.65']
w2.f10 | x | `this increasingly` | 4.69 | ['0.62', '4.20']
w2.f11 | x | `@@UNK@@ aspect` | 3.84 | ['-0.97', '5.08']
w2.f12 |   | `with this` | 2.87 | ['0.15', '2.76']
w2.f13 | x | `this increasingly` | 5.02 | ['2.32', '2.85']
w2.f14 |   | `wrong with` | 2.30 | ['1.22', '1.12']
w2.f15 | x | `really closer` | 5.52 | ['1.52', '4.27']
w2.f16 |   | `'s wrong` | 1.87 | ['-1.72', '4.35']
w2.f17 | x | `wrong with` | 3.23 | ['5.95', '-2.11']
w2.f18 | x | `culture .` | 4.90 | ['4.80', '0.22']
w2.f19 |   | `closer to` | 2.39 | ['1.56', '1.12']
w3.f0 | x | `wrong with this` | 6.40 | ['4.79', '3.34', '-1.33']
w3.f1 |   | `closer to porn` | 3.13 | ['-0.20', '0.48', '3.23']
w3.f2 | x | `with this increasingly` | 4.51 | ['0.07', '2.87', '1.66']
w3.f3 |   | `increasingly @@UNK@@ aspect` | 1.40 | ['2.59', '-0.06', '-0.52']
w3.f4 |   | `culture . @@PAD@@` | 3.05 | ['5.67', '-2.26', '0.00']
w3.f5 | x | `with this increasingly` | 7.42 | ['4.85', '-1.02', '3.92']
w3.f6 | x | `'s wrong with` | 4.53 | ['3.62', '3.37', '-2.25']
w3.f7 |   | `closer to porn` | 3.38 | ['2.30', '1.18', '0.39']
w3.f8 | x | `closer to porn` | 7.69 | ['4.87', '1.89', '1.21']
w3.f9 | x | `gay culture .` | 3.83 | ['4.75', '1.46', '-2.28']
w3.f10 | x | `wrong with this` | 4.19 | ['2.02', '1.77', '0.54']
w3.f11 |   | `'s wrong with` | 3.26 | ['-1.43', '2.19', '2.70']
w3.f12 | x | `the film is` | 4.65 | ['2.43', '0.53', '1.82']
w3.f13 |   | `culture . @@PAD@@` | 3.87 | ['4.36', '-0.24', '0.00']
w3.f14 | x | `film is really` | 3.80 | ['0.82', '0.90', '2.17']
w3.f15 |   | `this increasingly @@UNK@@` | 3.08 | ['2.58', '2.72', '-2.05']
w3.f16 | x | `is really closer` | 6.12 | ['1.27', '2.97', '2.26']
w3.f17 | x | `film is really` | 5.00 | ['-2.69', '2.35', '5.49']
w3.f18 | x | `wrong with this` | 4.16 | ['4.49', '2.32', '-2.19']
w3.f19 |   | `a serious @@UNK@@` | 3.69 | ['3.70', '2.13', '-2.02']

## Original input: 
``` there 's much tongue in cheek in the film and there 's no doubt the filmmaker is having fun with it all . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>there <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span>much <span style="background-color: #FFFF00">@</span>tongue <span style="background-color: #FFFF00">@</span>in cheek <span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>film and there <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>no <span style="background-color: #6698FF">@</span>doubt <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>filmmaker <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>having <span style="background-color: #FFFF00">@</span>fun <span style="background-color: #FFFF00">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>all <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `with it` | 4.74 | ['3.44', '1.67']
w2.f1 |   | `fun with` | 3.28 | ['-1.46', '4.87']
w2.f2 |   | `fun with` | 0.01 | ['0.69', '0.36']
w2.f3 |   | `is having` | 1.43 | ['0.28', '1.70']
w2.f4 |   | `the filmmaker` | 3.10 | ['-1.38', '4.67']
w2.f5 | x | `having fun` | 3.54 | ['2.81', '1.03']
w2.f6 | x | `in cheek` | 4.28 | ['1.77', '2.61']
w2.f7 |   | `all .` | 0.21 | ['0.98', '0.14']
w2.f8 | x | `fun with` | 3.97 | ['0.69', '3.50']
w2.f9 |   | `cheek in` | 3.92 | ['2.04', '1.89']
w2.f10 | x | `'s much` | 4.17 | ['2.75', '1.55']
w2.f11 | x | `with it` | 3.36 | ['2.35', '1.28']
w2.f12 |   | `is having` | 2.42 | ['-0.59', '3.04']
w2.f13 |   | `no doubt` | 1.84 | ['2.27', '-0.29']
w2.f14 | x | `'s no` | 4.74 | ['-1.49', '6.27']
w2.f15 | x | `having fun` | 4.80 | ['1.52', '3.55']
w2.f16 |   | `all .` | 1.58 | ['3.88', '-1.53']
w2.f17 |   | `there 's` | 1.79 | ['2.47', '-0.07']
w2.f18 | x | `the filmmaker` | 4.38 | ['-0.23', '4.73']
w2.f19 | x | `and there` | 3.73 | ['3.66', '0.37']
w3.f0 |   | `fun with it` | 3.49 | ['-0.66', '3.34', '1.20']
w3.f1 | x | `is having fun` | 3.73 | ['1.18', '-0.60', '3.53']
w3.f2 |   | `'s much tongue` | 2.21 | ['0.87', '0.08', '1.36']
w3.f3 |   | `with it all` | 2.03 | ['0.04', '-0.33', '2.93']
w3.f4 |   | `is having fun` | 3.03 | ['-1.96', '2.34', '3.01']
w3.f5 | x | `having fun with` | 6.19 | ['0.48', '4.58', '1.46']
w3.f6 |   | `'s much tongue` | 2.84 | ['3.62', '-2.28', '1.71']
w3.f7 | x | `in cheek in` | 4.61 | ['1.23', '2.39', '1.49']
w3.f8 |   | `filmmaker is having` | 4.30 | ['1.61', '4.71', '-1.73']
w3.f9 | x | `@@PAD@@ @@PAD@@ there` | 4.23 | ['0.00', '0.00', '4.33']
w3.f10 |   | `having fun with` | 3.15 | ['1.84', '1.76', '-0.30']
w3.f11 |   | `'s no doubt` | 2.96 | ['-1.43', '2.82', '1.77']
w3.f12 | x | `no doubt the` | 4.63 | ['4.16', '0.77', '-0.17']
w3.f13 | x | `it all .` | 5.88 | ['2.60', '1.08', '2.45']
w3.f14 |   | `there 's no` | 2.61 | ['-0.30', '1.15', '1.85']
w3.f15 | x | `fun with it` | 4.46 | ['0.29', '3.85', '0.49']
w3.f16 | x | `fun with it` | 6.75 | ['5.88', '-0.61', '1.86']
w3.f17 |   | `it all .` | 1.77 | ['1.06', '-0.11', '0.98']
w3.f18 |   | `filmmaker is having` | 2.53 | ['2.17', '0.11', '0.71']
w3.f19 |   | `fun with it` | 2.93 | ['2.59', '-0.57', '1.02']

## Original input: 
``` all these developments and challenges @@UNK@@ santa @@UNK@@ down the plot so heavily that they @@UNK@@ all the film of its energy and needlessly strain credibility . ``` 

## Marked input: 
<pre>all these <span style="background-color: #FFFF00">@</span>developments <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>challenges <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>santa @@UNK@@ down <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>plot so <span style="background-color: #6698FF">@</span>heavily <span style="background-color: #6698FF">@</span>that <span style="background-color: #6698FF">@</span>they <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>all <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>film <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>its <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>energy <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>needlessly <span style="background-color: #FFFF00">@</span>strain <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>credibility <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ down` | 4.34 | ['1.98', '2.74']
w2.f1 | x | `these developments` | 4.51 | ['1.64', '3.00']
w2.f2 |   | `so heavily` | 0.53 | ['0.34', '1.24']
w2.f3 |   | `strain credibility` | 1.63 | ['-0.03', '2.21']
w2.f4 |   | `that they` | 0.97 | ['1.54', '-0.38']
w2.f5 |   | `the film` | 1.83 | ['1.16', '0.98']
w2.f6 |   | `and challenges` | 2.73 | ['-0.03', '2.86']
w2.f7 |   | `plot so` | 1.87 | ['2.55', '0.23']
w2.f8 |   | `energy and` | 2.63 | ['2.50', '0.34']
w2.f9 |   | `@@UNK@@ down` | 3.69 | ['2.38', '1.32']
w2.f10 | x | `energy and` | 3.47 | ['2.13', '1.48']
w2.f11 |   | `santa @@UNK@@` | 2.47 | ['2.49', '0.25']
w2.f12 | x | `needlessly strain` | 4.44 | ['0.04', '4.44']
w2.f13 | x | `heavily that` | 3.41 | ['4.98', '-1.43']
w2.f14 | x | `credibility .` | 4.31 | ['3.96', '0.39']
w2.f15 | x | `its energy` | 4.28 | ['-0.98', '5.53']
w2.f16 | x | `all the` | 3.95 | ['3.88', '0.83']
w2.f17 | x | `these developments` | 4.10 | ['0.84', '3.88']
w2.f18 | x | `and challenges` | 4.26 | ['3.52', '0.86']
w2.f19 | x | `and challenges` | 3.72 | ['3.66', '0.36']
w3.f0 |   | `santa @@UNK@@ down` | 3.67 | ['-0.06', '0.35', '3.76']
w3.f1 |   | `challenges @@UNK@@ santa` | 2.23 | ['0.75', '-0.73', '2.59']
w3.f2 | x | `needlessly strain credibility` | 5.53 | ['0.31', '2.32', '2.98']
w3.f3 | x | `they @@UNK@@ all` | 3.55 | ['1.28', '-0.06', '2.93']
w3.f4 | x | `all these developments` | 4.59 | ['2.01', '2.08', '0.86']
w3.f5 | x | `these developments and` | 7.94 | ['0.11', '2.35', '5.81']
w3.f6 | x | `plot so heavily` | 4.30 | ['3.22', '1.79', '-0.50']
w3.f7 |   | `film of its` | 3.83 | ['-0.44', '0.18', '4.59']
w3.f8 | x | `of its energy` | 6.19 | ['1.71', '0.98', '3.79']
w3.f9 | x | `credibility . @@PAD@@` | 5.35 | ['4.88', '0.58', '0.00']
w3.f10 | x | `of its energy` | 4.70 | ['2.92', '0.99', '0.93']
w3.f11 | x | `so heavily that` | 3.89 | ['2.63', '2.94', '-1.49']
w3.f12 | x | `film of its` | 4.23 | ['0.49', '3.24', '0.62']
w3.f13 | x | `the film of` | 5.77 | ['4.70', '-1.39', '2.71']
w3.f14 | x | `so heavily that` | 5.03 | ['6.10', '0.58', '-1.55']
w3.f15 | x | `strain credibility .` | 5.39 | ['0.31', '5.85', '-0.60']
w3.f16 | x | `of its energy` | 4.03 | ['1.87', '2.21', '0.33']
w3.f17 |   | `down the plot` | 3.46 | ['-0.84', '0.47', '3.99']
w3.f18 | x | `energy and needlessly` | 5.41 | ['4.66', '-0.14', '1.35']
w3.f19 |   | `energy and needlessly` | 2.96 | ['0.39', '1.18', '1.51']

## Original input: 
``` god is great , the movie 's not . ``` 

## Marked input: 
<pre>god <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>great <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>movie <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>not <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f1 |   | `movie 's` | 1.54 | ['0.10', '1.57']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `@@PAD@@ god` | 0.73 | ['0.00', '1.29']
w2.f4 | x | `movie 's` | 3.67 | ['3.31', '0.55']
w2.f5 |   | `the movie` | 0.59 | ['1.16', '-0.26']
w2.f6 | x | `great ,` | 6.61 | ['2.77', '3.93']
w2.f7 |   | `@@PAD@@ god` | 0.44 | ['0.00', '1.34']
w2.f8 |   | `movie 's` | 2.07 | ['-1.54', '3.82']
w2.f9 |   | `@@PAD@@ god` | 1.29 | ['0.00', '1.30']
w2.f10 |   | `is great` | 1.39 | ['-2.88', '4.40']
w2.f11 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f12 |   | `'s not` | 1.76 | ['0.44', '1.35']
w2.f13 | x | `movie 's` | 3.36 | ['3.71', '-0.20']
w2.f14 |   | `@@PAD@@ god` | 2.00 | ['0.00', '2.03']
w2.f15 |   | `great ,` | 0.66 | ['1.24', '-0.31']
w2.f16 |   | `is great` | 0.19 | ['-0.10', '1.05']
w2.f17 |   | `'s not` | 2.06 | ['0.09', '2.58']
w2.f18 |   | `great ,` | 2.61 | ['1.84', '0.89']
w2.f19 |   | `god is` | 1.26 | ['0.87', '0.69']
w3.f0 | x | `movie 's not` | 4.02 | ['1.92', '1.91', '0.57']
w3.f1 |   | `@@PAD@@ @@PAD@@ god` | 0.00 | ['0.00', '0.00', '-2.09']
w3.f2 | x | `, the movie` | 7.38 | ['2.60', '0.94', '3.93']
w3.f3 |   | `@@PAD@@ @@PAD@@ god` | 0.00 | ['0.00', '0.00', '-2.13']
w3.f4 | x | `movie 's not` | 3.74 | ['2.80', '2.08', '-0.77']
w3.f5 | x | `'s not .` | 5.62 | ['0.63', '1.00', '4.32']
w3.f6 | x | `@@PAD@@ god is` | 4.16 | ['0.00', '2.72', '1.64']
w3.f7 |   | `@@PAD@@ god is` | 1.07 | ['0.00', '1.60', '-0.03']
w3.f8 |   | `god is great` | 2.90 | ['-0.55', '4.71', '-0.98']
w3.f9 |   | `is great ,` | 2.36 | ['-1.28', '0.69', '3.06']
w3.f10 | x | `@@PAD@@ god is` | 3.95 | ['0.00', '3.07', '1.03']
w3.f11 |   | `god is great` | 1.61 | ['2.49', '-0.19', '-0.49']
w3.f12 | x | `god is great` | 5.78 | ['1.32', '1.47', '3.12']
w3.f13 |   | `god is great` | 3.35 | ['2.02', '2.81', '-1.23']
w3.f14 | x | `great , the` | 3.56 | ['2.78', '-0.37', '1.24']
w3.f15 |   | `is great ,` | 1.08 | ['-1.83', '0.37', '2.70']
w3.f16 |   | `god is great` | 1.71 | ['-0.12', '-0.75', '2.95']
w3.f17 | x | `great , the` | 5.36 | ['0.92', '3.34', '1.25']
w3.f18 |   | `great , the` | 1.02 | ['2.07', '-3.16', '2.57']
w3.f19 |   | `is great ,` | 3.37 | ['0.33', '2.07', '1.08']

## Original input: 
``` the title , alone , should scare any sane person away . ``` 

## Marked input: 
<pre>the <span style="background-color: #6698FF">@</span>title <span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>alone <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>should <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>scare <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>any <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>sane <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>person <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>away <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `person away` | 2.66 | ['4.33', '-1.30']
w2.f1 | x | `sane person` | 3.90 | ['2.66', '1.37']
w2.f2 |   | `should scare` | 0.57 | ['0.77', '0.84']
w2.f3 | x | `title ,` | 4.27 | ['4.39', '0.44']
w2.f4 | x | `title ,` | 3.90 | ['1.59', '2.50']
w2.f5 |   | `title ,` | 1.25 | ['2.85', '-1.30']
w2.f6 | x | `alone ,` | 4.16 | ['0.33', '3.93']
w2.f7 |   | `should scare` | 1.05 | ['2.95', '-0.99']
w2.f8 |   | `title ,` | 2.17 | ['3.17', '-0.79']
w2.f9 |   | `any sane` | 4.43 | ['2.31', '2.13']
w2.f10 |   | `any sane` | 2.11 | ['-0.47', '2.71']
w2.f11 |   | `any sane` | 2.29 | ['0.98', '1.58']
w2.f12 | x | `the title` | 3.56 | ['0.53', '3.07']
w2.f13 | x | `title ,` | 4.92 | ['2.88', '2.18']
w2.f14 | x | `person away` | 4.95 | ['0.67', '4.32']
w2.f15 |   | `, alone` | 2.86 | ['2.19', '0.94']
w2.f16 |   | `sane person` | 1.26 | ['3.07', '-1.05']
w2.f17 |   | `title ,` | 1.74 | ['2.74', '-0.38']
w2.f18 |   | `alone ,` | 1.76 | ['0.99', '0.89']
w2.f19 |   | `should scare` | 1.24 | ['0.85', '0.69']
w3.f0 | x | `should scare any` | 4.51 | ['1.63', '0.31', '2.96']
w3.f1 | x | `scare any sane` | 6.75 | ['3.93', '0.44', '2.76']
w3.f2 | x | `@@PAD@@ the title` | 10.20 | ['0.00', '0.94', '9.35']
w3.f3 | x | `sane person away` | 3.69 | ['0.75', '2.33', '1.21']
w3.f4 |   | `scare any sane` | 0.53 | ['0.74', '0.10', '0.05']
w3.f5 | x | `sane person away` | 7.25 | ['4.31', '1.18', '2.09']
w3.f6 |   | `away . @@PAD@@` | 3.05 | ['2.19', '1.07', '0.00']
w3.f7 |   | `, alone ,` | 3.52 | ['1.70', '1.13', '1.18']
w3.f8 |   | `the title ,` | 0.46 | ['1.05', '-2.45', '2.14']
w3.f9 | x | `should scare any` | 6.23 | ['1.88', '3.20', '1.25']
w3.f10 | x | `scare any sane` | 4.99 | ['1.77', '-0.43', '3.80']
w3.f11 | x | `@@PAD@@ the title` | 4.00 | ['0.00', '-0.67', '4.86']
w3.f12 |   | `the title ,` | 2.78 | ['2.43', '0.32', '0.16']
w3.f13 | x | `alone , should` | 5.94 | ['0.52', '1.92', '3.75']
w3.f14 | x | `sane person away` | 6.03 | ['4.06', '0.95', '1.11']
w3.f15 | x | `, alone ,` | 5.80 | ['1.52', '1.74', '2.70']
w3.f16 | x | `title , alone` | 3.76 | ['-1.31', '3.78', '1.66']
w3.f17 | x | `@@PAD@@ the title` | 4.41 | ['0.00', '0.47', '4.10']
w3.f18 |   | `@@PAD@@ @@PAD@@ the` | 2.10 | ['0.00', '0.00', '2.57']
w3.f19 | x | `title , alone` | 4.64 | ['0.25', '1.68', '2.82']

## Original input: 
``` i would be shocked if there was actually one correct interpretation , but that should n't make the movie or the discussion any less enjoyable . ``` 

## Marked input: 
<pre>i would <span style="background-color: #6698FF">@</span>be <span style="background-color: #6698FF">@</span>shocked <span style="background-color: #6698FF">@</span>if <span style="background-color: #6698FF">@</span>there <span style="background-color: #6698FF">@</span>was <span style="background-color: #6698FF">@</span>actually <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>one <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>correct <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>interpretation <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>but <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span>should <span style="background-color: #6698FF">@</span>n't <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>make <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>movie or <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>discussion any less <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>enjoyable <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `n't make` | 1.87 | ['1.68', '0.56']
w2.f1 |   | `but that` | 3.43 | ['4.31', '-0.74']
w2.f2 |   | `one correct` | 0.97 | ['0.03', '1.99']
w2.f3 | x | `was actually` | 3.50 | ['1.75', '2.31']
w2.f4 | x | `less enjoyable` | 4.80 | ['2.87', '2.11']
w2.f5 | x | `less enjoyable` | 4.31 | ['-0.08', '4.69']
w2.f6 |   | `would be` | 2.92 | ['2.48', '0.54']
w2.f7 |   | `should n't` | 1.55 | ['2.95', '-0.49']
w2.f8 |   | `correct interpretation` | 1.96 | ['-0.04', '2.22']
w2.f9 |   | `be shocked` | 4.19 | ['3.56', '0.64']
w2.f10 | x | `one correct` | 3.07 | ['0.32', '2.88']
w2.f11 | x | `would be` | 5.17 | ['3.02', '2.42']
w2.f12 |   | `would be` | 2.67 | ['1.70', '1.01']
w2.f13 | x | `movie or` | 3.48 | ['3.71', '-0.08']
w2.f14 | x | `there was` | 3.96 | ['-1.15', '5.14']
w2.f15 |   | `interpretation ,` | 2.57 | ['3.16', '-0.31']
w2.f16 | x | `i would` | 6.16 | ['1.19', '5.74']
w2.f17 | x | `any less` | 3.49 | ['-0.08', '4.18']
w2.f18 |   | `that should` | 3.23 | ['2.33', '1.02']
w2.f19 |   | `correct interpretation` | 1.78 | ['0.12', '1.96']
w3.f0 | x | `less enjoyable .` | 8.50 | ['8.00', '0.52', '0.37']
w3.f1 | x | `correct interpretation ,` | 4.02 | ['6.37', '-0.36', '-1.61']
w3.f2 | x | `but that should` | 4.78 | ['1.07', '1.53', '2.28']
w3.f3 | x | `should n't make` | 3.23 | ['-0.14', '2.63', '1.35']
w3.f4 | x | `any less enjoyable` | 3.92 | ['0.48', '-0.89', '4.69']
w3.f5 | x | `less enjoyable .` | 9.96 | ['1.22', '4.75', '4.32']
w3.f6 | x | `actually one correct` | 4.77 | ['1.92', '-1.28', '4.34']
w3.f7 |   | `should n't make` | 2.92 | ['-0.21', '1.99', '1.64']
w3.f8 |   | `actually one correct` | 3.03 | ['0.32', '-0.43', '3.43']
w3.f9 | x | `shocked if there` | 5.98 | ['2.93', '-1.18', '4.33']
w3.f10 | x | `actually one correct` | 4.63 | ['3.03', '-0.05', '1.80']
w3.f11 | x | `there was actually` | 4.53 | ['0.11', '0.99', '3.62']
w3.f12 | x | `was actually one` | 7.18 | ['3.63', '2.85', '0.84']
w3.f13 | x | `less enjoyable .` | 6.96 | ['1.35', '3.41', '2.45']
w3.f14 | x | `there was actually` | 8.03 | ['-0.30', '3.43', '4.99']
w3.f15 | x | `correct interpretation ,` | 4.58 | ['0.90', '1.14', '2.70']
w3.f16 | x | `any less enjoyable` | 4.72 | ['-0.43', '0.39', '5.13']
w3.f17 |   | `, but that` | 3.74 | ['0.73', '2.96', '0.21']
w3.f18 | x | `was actually one` | 3.45 | ['0.41', '2.51', '1.00']
w3.f19 | x | `actually one correct` | 6.84 | ['1.27', '0.98', '4.70']

## Original input: 
``` makes one thing @@UNK@@ clear . american musical comedy as we know it would n't exist without the @@UNK@@ of yiddish theater , whose jolly , fun - for - @@UNK@@ - sake @@UNK@@ spirit goes to the essence of broadway . ``` 

## Marked input: 
<pre>makes one <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>thing <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>clear <span style="background-color: #6698FF">@</span>. american <span style="background-color: #6698FF">@</span>musical <span style="background-color: #6698FF">@</span>comedy <span style="background-color: #6698FF">@</span>as <span style="background-color: #6698FF">@</span>we <span style="background-color: #6698FF">@</span>know <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>would <span style="background-color: #6698FF">@</span>n't <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>exist <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>without <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>of yiddish theater <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>whose <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>jolly <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>fun <span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span>for <span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span>@@UNK@@ - sake <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>spirit <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>goes <span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>essence <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>broadway <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `n't exist` | 2.97 | ['1.68', '1.66']
w2.f1 | x | `makes one` | 6.60 | ['4.82', '1.91']
w2.f2 |   | `makes one` | 0.00 | ['1.15', '-0.10']
w2.f3 | x | `. american` | 2.49 | ['0.52', '2.52']
w2.f4 |   | `know it` | 3.40 | ['3.22', '0.36']
w2.f5 | x | `we know` | 4.38 | ['4.53', '0.16']
w2.f6 | x | `jolly ,` | 5.17 | ['1.33', '3.93']
w2.f7 |   | `yiddish theater` | 1.52 | ['1.61', '0.82']
w2.f8 |   | `fun -` | 2.33 | ['0.69', '1.85']
w2.f9 | x | `goes to` | 5.47 | ['0.81', '4.67']
w2.f10 |   | `- sake` | 2.73 | ['1.18', '1.68']
w2.f11 | x | `thing @@UNK@@` | 3.28 | ['3.30', '0.25']
w2.f12 | x | `one thing` | 4.10 | ['-1.18', '5.32']
w2.f13 | x | `theater ,` | 6.33 | ['4.30', '2.18']
w2.f14 |   | `theater ,` | 3.00 | ['2.14', '0.89']
w2.f15 | x | `, fun` | 5.46 | ['2.19', '3.55']
w2.f16 | x | `without the` | 3.07 | ['3.00', '0.83']
w2.f17 | x | `makes one` | 8.16 | ['5.31', '3.46']
w2.f18 | x | `we know` | 7.13 | ['4.79', '2.46']
w2.f19 | x | `@@UNK@@ spirit` | 3.48 | ['0.39', '3.38']
w3.f0 |   | `of yiddish theater` | 2.44 | ['-0.27', '1.12', '1.98']
w3.f1 | x | `jolly , fun` | 8.60 | ['4.56', '0.90', '3.53']
w3.f2 | x | `know it would` | 4.07 | ['-0.64', '1.70', '3.09']
w3.f3 | x | `would n't exist` | 3.60 | ['0.84', '2.63', '0.73']
w3.f4 | x | `jolly , fun` | 4.38 | ['0.95', '0.77', '3.01']
w3.f5 |   | `american musical comedy` | 4.16 | ['-0.43', '0.56', '4.35']
w3.f6 | x | `n't exist without` | 7.59 | ['3.72', '0.56', '3.52']
w3.f7 | x | `, fun -` | 4.17 | ['1.70', '1.15', '1.81']
w3.f8 | x | `whose jolly ,` | 6.02 | ['2.17', '2.00', '2.14']
w3.f9 | x | `yiddish theater ,` | 7.08 | ['0.84', '3.29', '3.06']
w3.f10 | x | `american musical comedy` | 5.67 | ['1.13', '0.42', '4.28']
w3.f11 | x | `- sake @@UNK@@` | 4.06 | ['1.42', '3.58', '-0.75']
w3.f12 | x | `comedy as we` | 9.48 | ['-0.80', '4.53', '5.88']
w3.f13 | x | `the essence of` | 5.85 | ['4.70', '-1.30', '2.71']
w3.f14 | x | `it would n't` | 4.63 | ['0.08', '1.02', '3.62']
w3.f15 | x | `yiddish theater ,` | 5.00 | ['-2.95', '5.41', '2.70']
w3.f16 | x | `jolly , fun` | 11.07 | ['5.31', '3.78', '2.35']
w3.f17 | x | `it would n't` | 6.04 | ['1.06', '0.62', '4.52']
w3.f18 | x | `yiddish theater ,` | 3.82 | ['3.04', '0.45', '0.79']
w3.f19 | x | `fun - for` | 4.49 | ['2.59', '1.48', '0.53']

## Original input: 
``` the year 's greatest adventure , and jackson 's limited but enthusiastic adaptation has made @@UNK@@ literal without killing its soul -- a feat any thinking person is bound to appreciate . ``` 

## Marked input: 
<pre>the year <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>greatest <span style="background-color: #FFFF00">@</span>adventure <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>jackson <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>limited <span style="background-color: #FFFF00">@</span>but <span style="background-color: #6698FF">@</span>enthusiastic <span style="background-color: #6698FF">@</span>adaptation <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>has <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>made <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>literal without <span style="background-color: #FFFF00">@</span>killing <span style="background-color: #FFFF00">@</span>its <span style="background-color: #FFFF00">@</span>soul <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>-- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>feat <span style="background-color: #6698FF">@</span>any <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>thinking <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>person <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>bound <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span>appreciate <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `-- a` | 3.28 | ['4.26', '-0.61']
w2.f1 | x | `soul --` | 5.25 | ['5.44', '-0.06']
w2.f2 |   | `has made` | 0.05 | ['0.34', '0.76']
w2.f3 | x | `its soul` | 2.11 | ['-0.44', '3.11']
w2.f4 | x | `soul --` | 3.90 | ['1.46', '2.63']
w2.f5 | x | `bound to` | 6.04 | ['3.96', '2.39']
w2.f6 | x | `soul --` | 5.52 | ['2.80', '2.82']
w2.f7 |   | `enthusiastic adaptation` | 1.88 | ['1.17', '1.61']
w2.f8 | x | `year 's` | 5.65 | ['2.04', '3.82']
w2.f9 |   | `bound to` | 4.57 | ['-0.09', '4.67']
w2.f10 | x | `soul --` | 4.00 | ['0.73', '3.41']
w2.f11 | x | `thinking person` | 6.23 | ['5.34', '1.16']
w2.f12 |   | `adaptation has` | 2.52 | ['2.54', '0.01']
w2.f13 | x | `adaptation has` | 3.48 | ['2.02', '1.61']
w2.f14 | x | `has made` | 3.30 | ['3.08', '0.25']
w2.f15 | x | `is bound` | 5.43 | ['1.15', '4.55']
w2.f16 | x | `any thinking` | 4.81 | ['2.30', '3.27']
w2.f17 | x | `its soul` | 4.56 | ['-0.61', '5.79']
w2.f18 | x | `enthusiastic adaptation` | 3.70 | ['2.24', '1.59']
w2.f19 | x | `and jackson` | 3.45 | ['3.66', '0.09']
w3.f0 |   | `a feat any` | 3.68 | ['-0.19', '1.30', '2.96']
w3.f1 | x | `feat any thinking` | 8.11 | ['4.65', '0.44', '3.40']
w3.f2 |   | `soul -- a` | 2.33 | ['1.09', '-0.95', '2.27']
w3.f3 | x | `literal without killing` | 2.81 | ['2.82', '2.29', '-1.70']
w3.f4 | x | `thinking person is` | 3.58 | ['2.42', '-0.95', '2.46']
w3.f5 | x | `adventure , and` | 7.65 | ['0.77', '1.40', '5.81']
w3.f6 | x | `a feat any` | 5.46 | ['1.76', '3.44', '0.47']
w3.f7 | x | `without killing its` | 5.04 | ['0.83', '0.12', '4.59']
w3.f8 | x | `person is bound` | 8.40 | ['1.15', '4.71', '2.83']
w3.f9 | x | `limited but enthusiastic` | 6.02 | ['1.20', '1.36', '3.58']
w3.f10 | x | `enthusiastic adaptation has` | 5.07 | ['3.84', '0.29', '1.09']
w3.f11 | x | `limited but enthusiastic` | 6.38 | ['4.97', '-0.21', '1.81']
w3.f12 | x | `but enthusiastic adaptation` | 6.27 | ['-0.44', '3.46', '3.38']
w3.f13 | x | `the year 's` | 9.79 | ['4.70', '4.95', '0.39']
w3.f14 | x | `thinking person is` | 8.70 | ['5.21', '0.95', '2.63']
w3.f15 | x | `greatest adventure ,` | 7.52 | ['2.49', '2.49', '2.70']
w3.f16 | x | `killing its soul` | 5.35 | ['0.65', '2.21', '2.87']
w3.f17 |   | `made @@UNK@@ literal` | 3.07 | ['2.30', '1.39', '-0.46']
w3.f18 | x | `enthusiastic adaptation has` | 4.70 | ['-0.85', '4.97', '1.04']
w3.f19 | x | `and jackson 's` | 7.83 | ['3.50', '4.46', '-0.01']

## Original input: 
``` if the idea of the white man @@UNK@@ on foreign @@UNK@@ to show @@UNK@@ @@UNK@@ the true light is @@UNK@@ to you , the simplistic heaven will quite likely be more like hell . ``` 

## Marked input: 
<pre>if the idea <span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>white <span style="background-color: #6698FF">@</span>man @@UNK@@ on foreign @@UNK@@ to <span style="background-color: #6698FF">@</span>show <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>the true light is @@UNK@@ to you , <span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>simplistic <span style="background-color: #6698FF">@</span>heaven <span style="background-color: #6698FF">@</span>will <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>quite <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>likely <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>be <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>more <span style="background-color: #6698FF">@</span>like <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hell <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `true light` | 3.20 | ['6.15', '-2.58']
w2.f1 | x | `heaven will` | 7.46 | ['4.98', '2.61']
w2.f2 |   | `heaven will` | 0.82 | ['1.28', '0.58']
w2.f3 | x | `quite likely` | 4.98 | ['3.11', '2.43']
w2.f4 | x | `you ,` | 4.31 | ['2.00', '2.50']
w2.f5 |   | `foreign @@UNK@@` | 2.71 | ['3.73', '-0.71']
w2.f6 |   | `like hell` | 3.77 | ['2.29', '1.57']
w2.f7 | x | `quite likely` | 2.78 | ['2.00', '1.70']
w2.f8 | x | `quite likely` | 5.03 | ['4.29', '0.95']
w2.f9 | x | `@@UNK@@ to` | 7.04 | ['2.38', '4.67']
w2.f10 | x | `you ,` | 3.65 | ['4.16', '-0.37']
w2.f11 | x | `likely be` | 4.44 | ['2.29', '2.42']
w2.f12 |   | `heaven will` | 2.60 | ['2.53', '0.11']
w2.f13 | x | `more like` | 3.98 | ['1.10', '3.03']
w2.f14 | x | `quite likely` | 3.81 | ['2.46', '1.38']
w2.f15 |   | `to you` | 3.18 | ['-2.54', '5.99']
w2.f16 | x | `will quite` | 4.89 | ['-0.99', '6.65']
w2.f17 | x | `quite likely` | 5.31 | ['7.03', '-1.11']
w2.f18 |   | `hell .` | 2.36 | ['2.26', '0.22']
w2.f19 |   | `simplistic heaven` | 2.95 | ['2.14', '1.11']
w3.f0 | x | `will quite likely` | 3.77 | ['3.37', '1.32', '-0.54']
w3.f1 | x | `heaven will quite` | 5.42 | ['1.51', '-2.53', '6.83']
w3.f2 | x | `, the simplistic` | 6.20 | ['2.60', '0.94', '2.74']
w3.f3 | x | `will quite likely` | 2.90 | ['1.00', '1.45', '1.06']
w3.f4 |   | `@@UNK@@ to you` | 2.89 | ['0.36', '0.44', '2.46']
w3.f5 |   | `@@PAD@@ @@PAD@@ if` | 4.58 | ['0.00', '0.00', '4.91']
w3.f6 | x | `simplistic heaven will` | 3.82 | ['0.49', '2.86', '0.69']
w3.f7 | x | `to show @@UNK@@` | 4.51 | ['3.76', '1.32', '-0.07']
w3.f8 | x | `heaven will quite` | 7.51 | ['6.96', '1.17', '-0.34']
w3.f9 | x | `quite likely be` | 10.27 | ['3.69', '3.78', '2.91']
w3.f10 |   | `of the white` | 3.68 | ['2.92', '-1.03', '1.94']
w3.f11 | x | `heaven will quite` | 4.17 | ['5.96', '0.52', '-2.11']
w3.f12 | x | `the simplistic heaven` | 6.76 | ['2.43', '1.77', '2.69']
w3.f13 | x | `the idea of` | 11.37 | ['4.70', '4.21', '2.71']
w3.f14 | x | `be more like` | 8.11 | ['-2.04', '4.60', '5.65']
w3.f15 | x | `the simplistic heaven` | 5.93 | ['-0.02', '3.89', '2.23']
w3.f16 | x | `heaven will quite` | 3.75 | ['-1.64', '0.00', '5.77']
w3.f17 | x | `idea of the` | 6.41 | ['6.98', '-1.67', '1.25']
w3.f18 |   | `idea of the` | 3.17 | ['-1.03', '2.10', '2.57']
w3.f19 | x | `more like hell` | 4.35 | ['0.01', '3.53', '0.92']

## Original input: 
``` 10 minutes into the film you 'll be white - @@UNK@@ and unable to look away . ``` 

## Marked input: 
<pre>10 <span style="background-color: #6698FF">@</span>minutes <span style="background-color: #6698FF">@</span>into <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>film you 'll <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>be <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>white <span style="background-color: #6698FF">@</span>- @@UNK@@ and unable <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>look <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>away <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@PAD@@ 10` | 2.09 | ['0.00', '2.46']
w2.f1 |   | `you 'll` | 3.26 | ['1.97', '1.43']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `and unable` | 3.87 | ['0.06', '4.36']
w2.f4 |   | `'ll be` | 2.03 | ['2.06', '0.16']
w2.f5 | x | `look away` | 5.28 | ['3.83', '1.76']
w2.f6 |   | `'ll be` | 1.74 | ['1.30', '0.54']
w2.f7 |   | `10 minutes` | 0.91 | ['-0.47', '2.29']
w2.f8 |   | `white -` | 2.70 | ['1.06', '1.85']
w2.f9 |   | `look away` | 4.82 | ['0.83', '4.00']
w2.f10 | x | `you 'll` | 5.19 | ['4.16', '1.17']
w2.f11 |   | `'ll be` | 2.61 | ['0.46', '2.42']
w2.f12 |   | `to look` | 1.34 | ['1.53', '-0.16']
w2.f13 | x | `unable to` | 3.21 | ['4.90', '-1.54']
w2.f14 | x | `look away` | 3.58 | ['-0.70', '4.32']
w2.f15 | x | `look away` | 3.29 | ['2.80', '0.76']
w2.f16 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f17 |   | `you 'll` | 0.89 | ['-0.55', '2.06']
w2.f18 |   | `unable to` | 2.01 | ['-0.36', '2.50']
w2.f19 |   | `look away` | 2.73 | ['2.81', '0.22']
w3.f0 |   | `be white -` | 1.84 | ['0.56', '1.45', '0.22']
w3.f1 |   | `'ll be white` | 2.52 | ['1.42', '1.79', '-0.32']
w3.f2 | x | `10 minutes into` | 3.94 | ['5.51', '-1.71', '0.23']
w3.f3 |   | `film you 'll` | 1.34 | ['0.63', '0.23', '1.08']
w3.f4 |   | `10 minutes into` | 2.11 | ['1.99', '-2.37', '2.85']
w3.f5 | x | `look away .` | 5.40 | ['1.21', '0.20', '4.32']
w3.f6 | x | `@@PAD@@ 10 minutes` | 5.13 | ['0.00', '3.30', '2.03']
w3.f7 |   | `to look away` | 3.57 | ['3.76', '-0.83', '1.13']
w3.f8 |   | `unable to look` | 3.05 | ['-1.34', '1.89', '2.78']
w3.f9 | x | `you 'll be` | 4.01 | ['-0.60', '1.82', '2.91']
w3.f10 |   | `10 minutes into` | 3.12 | ['0.23', '1.81', '1.24']
w3.f11 | x | `and unable to` | 5.34 | ['-1.12', '4.60', '2.06']
w3.f12 | x | `to look away` | 4.85 | ['1.38', '2.33', '1.27']
w3.f13 | x | `to look away` | 6.25 | ['1.07', '1.91', '3.53']
w3.f14 |   | `@@PAD@@ 10 minutes` | 2.69 | ['0.00', '1.92', '0.86']
w3.f15 |   | `unable to look` | 2.98 | ['1.05', '-0.50', '2.60']
w3.f16 |   | `'ll be white` | 0.63 | ['-0.74', '1.31', '0.44']
w3.f17 | x | `10 minutes into` | 5.07 | ['1.05', '4.32', '-0.15']
w3.f18 |   | `minutes into the` | 2.71 | ['-1.64', '2.25', '2.57']
w3.f19 |   | `10 minutes into` | 3.69 | ['0.89', '2.44', '0.47']

## Original input: 
``` the trick when watching godard is to catch the pitch of his @@UNK@@ , @@UNK@@ the pleasure of his sounds and images , and ponder the historical , philosophical , and @@UNK@@ issues that @@UNK@@ with them . ``` 

## Marked input: 
<pre>the trick when <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>watching <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>godard <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>catch <span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>pitch <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>his <span style="background-color: #FFFF00">@</span>@@UNK@@ , @@UNK@@ the pleasure <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>his <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>sounds <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>images <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>ponder <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>historical <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>philosophical <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>issues that @@UNK@@ with <span style="background-color: #FFFF00">@</span>them <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ with` | 2.58 | ['1.98', '0.98']
w2.f1 | x | `watching godard` | 4.75 | ['3.01', '1.88']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `historical ,` | 2.27 | ['2.39', '0.44']
w2.f4 | x | `trick when` | 4.64 | ['2.00', '2.82']
w2.f5 | x | `the historical` | 5.01 | ['1.16', '4.15']
w2.f6 | x | `historical ,` | 6.95 | ['3.12', '3.93']
w2.f7 |   | `trick when` | 1.59 | ['2.04', '0.46']
w2.f8 | x | `@@UNK@@ with` | 3.49 | ['0.21', '3.50']
w2.f9 | x | `historical ,` | 6.33 | ['6.01', '0.34']
w2.f10 | x | `with them` | 3.53 | ['1.55', '2.11']
w2.f11 | x | `watching godard` | 3.29 | ['1.18', '2.38']
w2.f12 |   | `watching godard` | 2.36 | ['0.53', '1.87']
w2.f13 | x | `trick when` | 3.64 | ['2.54', '1.24']
w2.f14 |   | `images ,` | 3.09 | ['2.23', '0.89']
w2.f15 | x | `the pleasure` | 5.39 | ['-0.42', '6.07']
w2.f16 | x | `ponder the` | 3.54 | ['3.47', '0.83']
w2.f17 | x | `trick when` | 6.74 | ['4.26', '3.10']
w2.f18 | x | `and images` | 6.46 | ['3.52', '3.06']
w2.f19 | x | `and ponder` | 5.92 | ['3.66', '2.55']
w3.f0 |   | `his sounds and` | 2.91 | ['0.93', '1.38', '0.99']
w3.f1 | x | `is to catch` | 3.89 | ['1.18', '0.48', '2.61']
w3.f2 | x | `, philosophical ,` | 5.54 | ['2.60', '1.70', '1.32']
w3.f3 |   | `catch the pitch` | 1.68 | ['1.73', '-0.66', '1.21']
w3.f4 | x | `historical , philosophical` | 4.54 | ['3.04', '0.77', '1.09']
w3.f5 | x | `with them .` | 10.03 | ['4.85', '1.18', '4.32']
w3.f6 |   | `with them .` | 3.31 | ['2.33', '2.47', '-1.28']
w3.f7 | x | `trick when watching` | 4.56 | ['-0.95', '1.92', '4.09']
w3.f8 | x | `and images ,` | 9.41 | ['2.47', '5.08', '2.14']
w3.f9 | x | `catch the pitch` | 4.42 | ['2.65', '-0.12', '1.99']
w3.f10 | x | `trick when watching` | 4.13 | ['3.63', '-0.85', '1.49']
w3.f11 | x | `watching godard is` | 4.77 | ['3.34', '0.48', '1.14']
w3.f12 | x | `the pleasure of` | 5.67 | ['2.43', '2.68', '0.69']
w3.f13 | x | `the pitch of` | 8.65 | ['4.70', '1.50', '2.71']
w3.f14 | x | `watching godard is` | 6.97 | ['3.77', '0.66', '2.63']
w3.f15 | x | `when watching godard` | 4.73 | ['1.53', '0.06', '3.30']
w3.f16 | x | `sounds and images` | 5.72 | ['1.02', '-0.30', '5.38']
w3.f17 | x | `philosophical , and` | 7.32 | ['4.29', '3.34', '-0.15']
w3.f18 | x | `pleasure of his` | 5.51 | ['3.19', '2.10', '0.69']
w3.f19 | x | `and images ,` | 9.25 | ['3.50', '4.79', '1.08']

## Original input: 
``` bears is even worse than i imagined a movie ever could be . ``` 

## Marked input: 
<pre>bears <span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>even <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>worse <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>than <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>i <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>imagined <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>movie <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>ever <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>could <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>be <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `even worse` | 2.40 | ['0.28', '2.49']
w2.f1 | x | `a movie` | 3.76 | ['2.95', '0.94']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `even worse` | 2.80 | ['-0.69', '4.05']
w2.f4 | x | `i imagined` | 4.63 | ['3.61', '1.20']
w2.f5 | x | `i imagined` | 3.38 | ['3.97', '-0.29']
w2.f6 |   | `even worse` | 2.82 | ['1.12', '1.79']
w2.f7 |   | `@@PAD@@ bears` | 0.33 | ['0.00', '1.23']
w2.f8 | x | `imagined a` | 4.29 | ['1.94', '2.56']
w2.f9 |   | `bears is` | 4.47 | ['5.75', '-1.27']
w2.f10 | x | `ever could` | 3.76 | ['2.91', '0.99']
w2.f11 | x | `ever could` | 3.10 | ['1.34', '2.03']
w2.f12 |   | `could be` | 3.30 | ['2.33', '1.01']
w2.f13 | x | `bears is` | 4.90 | ['4.55', '0.50']
w2.f14 |   | `is even` | 0.67 | ['-0.15', '0.85']
w2.f15 |   | `movie ever` | 2.91 | ['-1.81', '4.99']
w2.f16 |   | `even worse` | 2.15 | ['1.05', '1.86']
w2.f17 | x | `worse than` | 5.40 | ['3.17', '2.84']
w2.f18 | x | `imagined a` | 3.74 | ['3.77', '0.10']
w2.f19 |   | `imagined a` | 1.28 | ['2.80', '-1.23']
w3.f0 |   | `movie ever could` | 0.97 | ['1.92', '1.05', '-1.61']
w3.f1 |   | `a movie ever` | 2.89 | ['-1.76', '2.75', '2.28']
w3.f2 | x | `worse than i` | 4.51 | ['4.43', '-0.69', '0.86']
w3.f3 |   | `a movie ever` | 0.79 | ['-0.28', '-0.23', '1.90']
w3.f4 | x | `even worse than` | 5.30 | ['3.48', '1.57', '0.61']
w3.f5 |   | `than i imagined` | 4.26 | ['0.81', '2.36', '1.41']
w3.f6 | x | `a movie ever` | 8.17 | ['1.76', '4.49', '2.13']
w3.f7 |   | `@@PAD@@ bears is` | 1.71 | ['0.00', '2.24', '-0.03']
w3.f8 | x | `bears is even` | 6.26 | ['0.88', '4.71', '0.95']
w3.f9 | x | `ever could be` | 5.35 | ['2.39', '0.16', '2.91']
w3.f10 |   | `than i imagined` | 2.58 | ['1.14', '1.44', '0.14']
w3.f11 | x | `is even worse` | 5.00 | ['0.29', '-0.13', '5.04']
w3.f12 |   | `could be .` | 3.05 | ['1.29', '0.29', '1.61']
w3.f13 |   | `i imagined a` | 5.08 | ['2.34', '2.81', '0.18']
w3.f14 | x | `@@PAD@@ bears is` | 7.12 | ['0.00', '4.58', '2.63']
w3.f15 |   | `is even worse` | 2.22 | ['-1.83', '2.57', '1.65']
w3.f16 |   | `even worse than` | 3.37 | ['0.92', '2.58', '0.25']
w3.f17 |   | `even worse than` | 3.30 | ['1.65', '4.37', '-2.57']
w3.f18 | x | `ever could be` | 3.58 | ['3.81', '-0.64', '0.87']
w3.f19 | x | `bears is even` | 5.17 | ['0.82', '3.62', '0.84']

## Original input: 
``` less front - @@UNK@@ and more @@UNK@@ than the two - hour version released here in @@UNK@@ . ``` 

## Marked input: 
<pre>less <span style="background-color: #6698FF">@</span>front <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>more @@UNK@@ than the <span style="background-color: #6698FF">@</span>two <span style="background-color: #6698FF">@</span>- <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hour <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>version <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>released <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>here <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>in <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `version released` | 2.43 | ['1.81', '0.99']
w2.f1 |   | `front -` | 1.98 | ['0.36', '1.75']
w2.f2 |   | `hour version` | 0.58 | ['1.14', '0.49']
w2.f3 | x | `two -` | 3.15 | ['3.17', '0.54']
w2.f4 |   | `hour version` | 3.41 | ['0.07', '3.53']
w2.f5 | x | `hour version` | 7.40 | ['5.09', '2.61']
w2.f6 |   | `less front` | 2.43 | ['1.63', '0.90']
w2.f7 |   | `released here` | 1.42 | ['1.19', '1.14']
w2.f8 | x | `two -` | 7.51 | ['5.87', '1.85']
w2.f9 |   | `version released` | 4.02 | ['2.57', '1.47']
w2.f10 |   | `@@UNK@@ and` | 1.28 | ['-0.06', '1.48']
w2.f11 | x | `released here` | 3.52 | ['1.14', '2.65']
w2.f12 |   | `released here` | 2.85 | ['0.31', '2.58']
w2.f13 | x | `front -` | 5.15 | ['4.10', '1.20']
w2.f14 |   | `front -` | 1.74 | ['1.44', '0.33']
w2.f15 |   | `hour version` | 3.15 | ['1.12', '2.30']
w2.f16 | x | `hour version` | 2.81 | ['2.88', '0.69']
w2.f17 | x | `@@PAD@@ less` | 3.57 | ['0.00', '4.18']
w2.f18 |   | `and more` | 2.56 | ['3.52', '-0.83']
w2.f19 | x | `hour version` | 4.17 | ['0.66', '3.81']
w3.f0 | x | `less front -` | 8.34 | ['8.00', '0.51', '0.22']
w3.f1 | x | `version released here` | 6.29 | ['3.02', '0.39', '3.26']
w3.f2 | x | `@@PAD@@ less front` | 6.44 | ['0.00', '3.93', '2.60']
w3.f3 | x | `- hour version` | 3.50 | ['-0.10', '-0.97', '5.18']
w3.f4 | x | `version released here` | 3.69 | ['2.28', '1.76', '0.01']
w3.f5 |   | `released here in` | 3.93 | ['1.21', '2.18', '0.88']
w3.f6 |   | `than the two` | 3.56 | ['0.50', '0.45', '2.82']
w3.f7 | x | `released here in` | 4.30 | ['0.50', '2.80', '1.49']
w3.f8 |   | `@@UNK@@ and more` | 2.76 | ['0.50', '0.71', '1.84']
w3.f9 | x | `front - @@UNK@@` | 4.66 | ['3.12', '-0.49', '2.13']
w3.f10 | x | `here in @@UNK@@` | 4.36 | ['4.29', '-0.64', '0.86']
w3.f11 |   | `released here in` | 2.63 | ['2.51', '-1.06', '1.38']
w3.f12 | x | `two - hour` | 4.58 | ['2.68', '2.81', '-0.78']
w3.f13 |   | `the two -` | 3.54 | ['4.70', '-1.78', '0.87']
w3.f14 |   | `version released here` | 2.66 | ['0.58', '0.81', '1.37']
w3.f15 | x | `hour version released` | 3.95 | ['1.48', '-0.05', '2.68']
w3.f16 | x | `- hour version` | 4.22 | ['1.48', '0.18', '2.94']
w3.f17 | x | `than the two` | 6.77 | ['2.28', '0.47', '4.17']
w3.f18 | x | `two - hour` | 4.08 | ['6.20', '0.97', '-2.62']
w3.f19 |   | `front - @@UNK@@` | 0.83 | ['1.48', '1.48', '-2.02']

## Original input: 
``` an uplifting , largely bogus story . ``` 

## Marked input: 
<pre>an <span style="background-color: #FFFF00">@</span>uplifting <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>largely <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>bogus <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>story <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `an uplifting` | 3.01 | ['-0.70', '4.08']
w2.f1 |   | `@@PAD@@ an` | 2.40 | ['0.00', '2.54']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `largely bogus` | 3.62 | ['1.02', '3.15']
w2.f4 |   | `an uplifting` | 1.88 | ['5.09', '-3.01']
w2.f5 |   | `an uplifting` | 2.42 | ['3.50', '-0.78']
w2.f6 | x | `uplifting ,` | 5.01 | ['1.18', '3.93']
w2.f7 | x | `largely bogus` | 4.06 | ['1.42', '3.55']
w2.f8 |   | `@@PAD@@ an` | 0.91 | ['0.00', '1.13']
w2.f9 |   | `, largely` | 2.75 | ['0.68', '2.08']
w2.f10 |   | `bogus story` | 0.98 | ['0.28', '0.83']
w2.f11 |   | `bogus story` | 0.93 | ['1.19', '0.00']
w2.f12 | x | `bogus story` | 3.93 | ['3.75', '0.22']
w2.f13 | x | `, largely` | 3.53 | ['-1.15', '4.83']
w2.f14 |   | `@@PAD@@ an` | 2.02 | ['0.00', '2.05']
w2.f15 |   | `an uplifting` | 0.68 | ['0.76', '0.19']
w2.f16 |   | `, largely` | 1.30 | ['-0.98', '3.04']
w2.f17 | x | `largely bogus` | 5.06 | ['2.73', '2.95']
w2.f18 |   | `uplifting ,` | 2.94 | ['2.17', '0.89']
w2.f19 |   | `largely bogus` | 0.34 | ['0.13', '0.51']
w3.f0 |   | `story . @@PAD@@` | 3.52 | ['3.91', '-0.01', '0.00']
w3.f1 | x | `@@PAD@@ an uplifting` | 4.00 | ['0.00', '1.98', '2.40']
w3.f2 | x | `bogus story .` | 5.84 | ['4.31', '0.78', '0.84']
w3.f3 |   | `@@PAD@@ an uplifting` | 0.15 | ['0.00', '-0.13', '0.88']
w3.f4 |   | `@@PAD@@ an uplifting` | 2.07 | ['0.00', '0.82', '1.61']
w3.f5 |   | `bogus story .` | 4.02 | ['0.88', '-0.85', '4.32']
w3.f6 | x | `largely bogus story` | 3.96 | ['-0.21', '3.54', '0.84']
w3.f7 | x | `an uplifting ,` | 5.73 | ['2.46', '2.59', '1.18']
w3.f8 |   | `an uplifting ,` | 4.27 | ['1.44', '0.97', '2.14']
w3.f9 |   | `, largely bogus` | 3.37 | ['-2.20', '4.25', '1.43']
w3.f10 | x | `largely bogus story` | 5.05 | ['0.37', '3.60', '1.22']
w3.f11 | x | `largely bogus story` | 4.78 | ['3.22', '1.09', '0.66']
w3.f12 | x | `, largely bogus` | 5.62 | ['-1.42', '2.97', '4.20']
w3.f13 |   | `an uplifting ,` | 4.64 | ['1.41', '3.51', '-0.03']
w3.f14 | x | `largely bogus story` | 4.61 | ['4.61', '0.92', '-0.83']
w3.f15 |   | `, largely bogus` | 2.14 | ['1.52', '0.29', '0.50']
w3.f16 | x | `uplifting , largely` | 3.99 | ['-0.78', '3.78', '1.37']
w3.f17 | x | `uplifting , largely` | 7.59 | ['-0.75', '3.34', '5.15']
w3.f18 |   | `an uplifting ,` | 2.24 | ['0.67', '1.24', '0.79']
w3.f19 |   | `@@PAD@@ @@PAD@@ an` | 1.95 | ['0.00', '0.00', '2.07']

## Original input: 
``` a cinematic @@UNK@@ @@UNK@@ of impressive potency . ``` 

## Marked input: 
<pre>a cinematic @@UNK@@ @@UNK@@ of <span style="background-color: #FFFF00">@</span>impressive <span style="background-color: #FFFF00">@</span>potency <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `cinematic @@UNK@@` | 1.62 | ['2.79', '-0.79']
w2.f1 | x | `impressive potency` | 4.21 | ['2.48', '1.87']
w2.f2 |   | `of impressive` | 0.20 | ['-0.19', '1.43']
w2.f3 |   | `a cinematic` | 0.49 | ['-0.30', '1.35']
w2.f4 |   | `of impressive` | 1.72 | ['1.04', '0.88']
w2.f5 |   | `of impressive` | 3.18 | ['0.65', '2.83']
w2.f6 |   | `impressive potency` | 1.03 | ['1.79', '-0.66']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 | x | `impressive potency` | 4.42 | ['2.00', '2.63']
w2.f9 |   | `@@UNK@@ of` | 4.02 | ['2.38', '1.65']
w2.f10 | x | `impressive potency` | 4.08 | ['1.85', '2.37']
w2.f11 |   | `cinematic @@UNK@@` | 0.12 | ['0.15', '0.25']
w2.f12 |   | `cinematic @@UNK@@` | 1.40 | ['1.21', '0.22']
w2.f13 |   | `@@PAD@@ a` | 1.30 | ['0.00', '1.45']
w2.f14 | x | `impressive potency` | 5.50 | ['-0.74', '6.27']
w2.f15 |   | `of impressive` | 0.31 | ['-3.18', '3.77']
w2.f16 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f17 |   | `a cinematic` | 0.38 | ['-1.87', '2.86']
w2.f18 |   | `. @@PAD@@` | 0.86 | ['0.99', '0.00']
w2.f19 |   | `of impressive` | 2.47 | ['1.68', '1.09']
w3.f0 |   | `potency . @@PAD@@` | 1.65 | ['2.05', '-0.01', '0.00']
w3.f1 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-2.30']
w3.f2 |   | `@@PAD@@ @@PAD@@ a` | 2.19 | ['0.00', '0.00', '2.27']
w3.f3 |   | `cinematic @@UNK@@ @@UNK@@` | 0.45 | ['1.05', '-0.06', '0.07']
w3.f4 | x | `@@UNK@@ of impressive` | 5.70 | ['0.36', '-0.44', '6.14']
w3.f5 | x | `of impressive potency` | 5.37 | ['-0.94', '4.16', '2.48']
w3.f6 |   | `a cinematic @@UNK@@` | 2.73 | ['1.76', '1.02', '0.15']
w3.f7 |   | `@@PAD@@ a cinematic` | 2.53 | ['0.00', '0.48', '2.55']
w3.f8 |   | `@@UNK@@ of impressive` | 3.42 | ['0.50', '-1.49', '4.70']
w3.f9 |   | `@@PAD@@ @@PAD@@ a` | 1.03 | ['0.00', '0.00', '1.13']
w3.f10 | x | `potency . @@PAD@@` | 4.02 | ['2.17', '2.00', '0.00']
w3.f11 | x | `impressive potency .` | 3.87 | ['1.84', '2.31', '-0.08']
w3.f12 |   | `@@UNK@@ of impressive` | 0.41 | ['-0.75', '3.24', '-1.95']
w3.f13 |   | `impressive potency .` | 1.94 | ['1.57', '-1.82', '2.45']
w3.f14 |   | `cinematic @@UNK@@ @@UNK@@` | 2.17 | ['2.84', '0.79', '-1.37']
w3.f15 |   | `impressive potency .` | 1.97 | ['-0.28', '3.02', '-0.60']
w3.f16 |   | `of impressive potency` | 2.66 | ['1.87', '-0.85', '2.01']
w3.f17 |   | `impressive potency .` | 1.97 | ['0.99', '0.16', '0.98']
w3.f18 | x | `impressive potency .` | 3.96 | ['4.40', '0.98', '-0.95']
w3.f19 |   | `@@UNK@@ of impressive` | 2.79 | ['-0.26', '-1.61', '4.77']

## Original input: 
``` while it would be easy to give crush the new title of two weddings and a funeral , it 's a far more thoughtful film than any slice of hugh grant whimsy . ``` 

## Marked input: 
<pre>while it <span style="background-color: #6698FF">@</span>would <span style="background-color: #6698FF">@</span>be <span style="background-color: #6698FF">@</span>easy <span style="background-color: #6698FF">@</span>to <span style="background-color: #FFFF00">@</span>give <span style="background-color: #FFFF00">@</span>crush <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>new title <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>two <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>weddings <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>funeral <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>it <span style="background-color: #FFFF00">@</span>'s a <span style="background-color: #6698FF">@</span>far <span style="background-color: #6698FF">@</span>more <span style="background-color: #6698FF">@</span>thoughtful <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>film <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>than <span style="background-color: #FFFF00">@</span>any slice <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hugh <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>grant whimsy <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `more thoughtful` | 4.32 | ['-1.58', '6.27']
w2.f1 | x | `a funeral` | 6.91 | ['2.95', '4.10']
w2.f2 |   | `give crush` | 0.91 | ['1.18', '0.78']
w2.f3 | x | `give crush` | 3.79 | ['0.28', '4.06']
w2.f4 | x | `funeral ,` | 4.27 | ['1.96', '2.50']
w2.f5 | x | `title of` | 4.31 | ['2.85', '1.76']
w2.f6 | x | `new title` | 5.26 | ['1.61', '3.75']
w2.f7 |   | `of hugh` | 1.67 | ['0.11', '2.47']
w2.f8 | x | `two weddings` | 6.54 | ['5.87', '0.88']
w2.f9 |   | `easy to` | 4.30 | ['-0.36', '4.67']
w2.f10 |   | `'s a` | 2.81 | ['2.75', '0.20']
w2.f11 | x | `would be` | 5.17 | ['3.02', '2.42']
w2.f12 | x | `new title` | 3.92 | ['0.89', '3.07']
w2.f13 | x | `new title` | 6.11 | ['2.15', '4.11']
w2.f14 |   | `new title` | 1.77 | ['1.71', '0.09']
w2.f15 |   | `thoughtful film` | 3.05 | ['1.44', '1.88']
w2.f16 | x | `new title` | 2.80 | ['1.08', '2.48']
w2.f17 | x | `give crush` | 3.29 | ['2.69', '1.22']
w2.f18 | x | `two weddings` | 6.51 | ['2.10', '4.54']
w2.f19 | x | `grant whimsy` | 4.62 | ['2.31', '2.60']
w3.f0 | x | `'s a far` | 4.06 | ['-1.14', '3.29', '2.30']
w3.f1 | x | `title of two` | 6.03 | ['3.45', '-0.85', '3.80']
w3.f2 | x | `while it would` | 8.73 | ['4.03', '1.70', '3.09']
w3.f3 |   | `easy to give` | 1.70 | ['2.54', '-1.32', '1.07']
w3.f4 | x | `more thoughtful film` | 3.52 | ['0.65', '1.13', '2.09']
w3.f5 | x | `two weddings and` | 7.00 | ['-0.55', '2.07', '5.81']
w3.f6 | x | `far more thoughtful` | 5.23 | ['2.80', '2.50', '0.13']
w3.f7 | x | `easy to give` | 5.66 | ['-0.02', '1.18', '5.00']
w3.f8 | x | `of two weddings` | 7.55 | ['1.71', '3.46', '2.66']
w3.f9 |   | `would be easy` | 3.57 | ['3.25', '-2.01', '2.44']
w3.f10 | x | `far more thoughtful` | 6.94 | ['2.20', '3.50', '1.40']
w3.f11 | x | `a far more` | 5.76 | ['-0.77', '3.80', '2.92']
w3.f12 | x | `two weddings and` | 4.67 | ['2.68', '0.97', '1.15']
w3.f13 | x | `grant whimsy .` | 5.29 | ['4.34', '-1.25', '2.45']
w3.f14 |   | `than any slice` | 2.69 | ['1.81', '0.80', '0.17']
w3.f15 | x | `any slice of` | 6.91 | ['2.46', '2.61', '2.01']
w3.f16 | x | `easy to give` | 5.61 | ['1.97', '-0.49', '4.51']
w3.f17 | x | `title of two` | 5.11 | ['2.77', '-1.67', '4.17']
w3.f18 | x | `two weddings and` | 6.42 | ['6.20', '2.81', '-2.13']
w3.f19 | x | `any slice of` | 8.08 | ['1.43', '4.10', '2.66']

## Original input: 
``` the only young people who possibly will enjoy it are @@UNK@@ . . . who might be @@UNK@@ by the movie 's quick movements and sounds . ``` 

## Marked input: 
<pre>the <span style="background-color: #6698FF">@</span>only <span style="background-color: #6698FF">@</span>young <span style="background-color: #6698FF">@</span>people <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>who <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>possibly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>will <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>enjoy <span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>are <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>. who might be @@UNK@@ by the movie 's <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>quick <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>movements <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>sounds <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `possibly will` | 3.70 | ['1.10', '2.98']
w2.f1 | x | `possibly will` | 6.86 | ['4.38', '2.61']
w2.f2 |   | `who possibly` | 0.12 | ['0.42', '0.74']
w2.f3 |   | `young people` | 0.97 | ['0.76', '0.77']
w2.f4 | x | `movie 's` | 3.67 | ['3.31', '0.55']
w2.f5 |   | `. who` | 1.97 | ['0.67', '1.60']
w2.f6 |   | `will enjoy` | 3.47 | ['2.71', '0.86']
w2.f7 |   | `only young` | 1.25 | ['1.26', '0.90']
w2.f8 |   | `possibly will` | 2.08 | ['3.11', '-0.82']
w2.f9 |   | `'s quick` | 4.12 | ['0.84', '3.30']
w2.f10 |   | `young people` | 2.03 | ['0.87', '1.30']
w2.f11 |   | `movements and` | 2.07 | ['2.07', '0.27']
w2.f12 |   | `@@UNK@@ by` | 3.39 | ['-0.28', '3.71']
w2.f13 | x | `only young` | 5.98 | ['6.80', '-0.67']
w2.f14 | x | `the only` | 5.99 | ['0.10', '5.93']
w2.f15 |   | `only young` | 2.96 | ['2.27', '0.96']
w2.f16 |   | `young people` | 1.83 | ['0.32', '2.28']
w2.f17 |   | `who possibly` | 2.62 | ['-0.41', '3.64']
w2.f18 | x | `will enjoy` | 4.66 | ['1.88', '2.91']
w2.f19 |   | `only young` | 2.72 | ['-0.01', '3.02']
w3.f0 | x | `movie 's quick` | 6.03 | ['1.92', '1.91', '2.59']
w3.f1 | x | `who possibly will` | 7.55 | ['2.59', '1.64', '3.70']
w3.f2 | x | `enjoy it are` | 4.71 | ['3.22', '1.70', '-0.12']
w3.f3 |   | `possibly will enjoy` | 1.62 | ['1.39', '-1.18', '2.01']
w3.f4 | x | `possibly will enjoy` | 4.01 | ['0.81', '2.26', '1.30']
w3.f5 |   | `will enjoy it` | 4.45 | ['0.93', '3.45', '0.40']
w3.f6 | x | `'s quick movements` | 8.28 | ['3.62', '2.74', '2.13']
w3.f7 |   | `who possibly will` | 3.27 | ['1.01', '1.47', '1.29']
w3.f8 | x | `enjoy it are` | 4.68 | ['3.02', '0.83', '1.11']
w3.f9 | x | `quick movements and` | 6.28 | ['2.69', '1.30', '2.40']
w3.f10 | x | `people who possibly` | 5.86 | ['3.67', '2.31', '0.03']
w3.f11 | x | `young people who` | 6.02 | ['1.90', '4.18', '0.14']
w3.f12 | x | `only young people` | 5.22 | ['-0.16', '3.59', '1.92']
w3.f13 |   | `the only young` | 4.87 | ['4.70', '-0.19', '0.61']
w3.f14 | x | `@@PAD@@ the only` | 5.29 | ['0.00', '-0.32', '5.70']
w3.f15 | x | `the only young` | 4.27 | ['-0.02', '1.19', '3.27']
w3.f16 | x | `young people who` | 4.34 | ['2.14', '1.05', '1.53']
w3.f17 | x | `are @@UNK@@ .` | 4.88 | ['2.67', '1.39', '0.98']
w3.f18 | x | `people who possibly` | 4.29 | ['1.01', '2.93', '0.82']
w3.f19 | x | `enjoy it are` | 4.32 | ['0.89', '-0.66', '4.20']

## Original input: 
``` . . . the good and different idea [ of middle - aged romance ] is not handled well and , except for the fine star performances , there is little else to recommend " never again . " ``` 

## Marked input: 
<pre>. . . the good <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>different <span style="background-color: #FFFF00">@</span>idea <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>[ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>middle <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>aged <span style="background-color: #6698FF">@</span>romance <span style="background-color: #6698FF">@</span>] <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>not <span style="background-color: #6698FF">@</span>handled well and , except for <span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>fine <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>star <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>performances <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>there <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>little else to <span style="background-color: #6698FF">@</span>recommend <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>" <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>never <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>again <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>"</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `" never` | 4.79 | ['2.79', '2.37']
w2.f1 | x | `fine star` | 3.85 | ['1.39', '2.59']
w2.f2 |   | `recommend "` | 0.36 | ['-0.05', '1.46']
w2.f3 | x | `different idea` | 3.27 | ['-0.25', '4.08']
w2.f4 | x | `recommend "` | 3.61 | ['-0.24', '4.04']
w2.f5 | x | `except for` | 3.48 | ['2.15', '1.63']
w2.f6 |   | `and ,` | 3.81 | ['-0.03', '3.93']
w2.f7 |   | `idea [` | 1.58 | ['0.28', '2.21']
w2.f8 |   | `" never` | 2.39 | ['0.25', '2.35']
w2.f9 |   | `romance ]` | 3.58 | ['4.72', '-1.13']
w2.f10 | x | `star performances` | 8.29 | ['1.84', '6.58']
w2.f11 | x | `different idea` | 2.96 | ['-0.17', '3.41']
w2.f12 | x | `idea [` | 3.62 | ['1.62', '2.04']
w2.f13 |   | `except for` | 2.55 | ['-0.08', '2.78']
w2.f14 | x | `again .` | 5.62 | ['5.26', '0.39']
w2.f15 | x | `recommend "` | 5.96 | ['2.78', '3.45']
w2.f16 | x | `recommend "` | 2.82 | ['1.25', '2.33']
w2.f17 | x | `different idea` | 5.96 | ['2.14', '4.44']
w2.f18 | x | `and different` | 5.40 | ['3.52', '2.01']
w2.f19 | x | `and different` | 5.62 | ['3.66', '2.26']
w3.f0 | x | `idea [ of` | 9.68 | ['4.66', '5.16', '0.24']
w3.f1 | x | `performances , there` | 5.50 | ['5.96', '0.90', '-0.98']
w3.f2 | x | `never again .` | 8.16 | ['6.11', '1.29', '0.84']
w3.f3 |   | `fine star performances` | 0.93 | ['0.67', '-0.73', '1.60']
w3.f4 | x | `recommend " never` | 6.68 | ['2.05', '1.15', '3.84']
w3.f5 | x | `the good and` | 7.46 | ['-0.36', '2.33', '5.81']
w3.f6 | x | `for the fine` | 6.27 | ['1.51', '0.45', '4.52']
w3.f7 | x | `to recommend "` | 4.62 | ['3.76', '2.37', '-1.01']
w3.f8 | x | `the fine star` | 6.85 | ['1.05', '6.83', '-0.75']
w3.f9 | x | `performances , there` | 6.11 | ['3.20', '-1.33', '4.33']
w3.f10 | x | `else to recommend` | 5.49 | ['3.35', '1.69', '0.61']
w3.f11 | x | `recommend " never` | 6.81 | ['0.83', '-0.04', '6.21']
w3.f12 | x | `middle - aged` | 7.96 | ['3.28', '2.81', '1.99']
w3.f13 | x | `the good and` | 6.51 | ['4.70', '3.04', '-0.98']
w3.f14 | x | `romance ] is` | 3.52 | ['-0.23', '1.21', '2.63']
w3.f15 | x | `" never again` | 7.21 | ['2.76', '2.25', '2.37']
w3.f16 | x | `different idea [` | 4.37 | ['2.91', '0.58', '1.25']
w3.f17 | x | `idea [ of` | 10.34 | ['6.98', '1.66', '1.87']
w3.f18 | x | `" never again` | 4.06 | ['-0.14', '2.30', '2.37']
w3.f19 | x | `star performances ,` | 8.26 | ['-0.60', '7.89', '1.08']

## Original input: 
``` k-19 exploits our substantial collective fear of nuclear holocaust to generate cheap hollywood tension . ``` 

## Marked input: 
<pre>k-19 <span style="background-color: #6698FF">@</span>exploits <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>our <span style="background-color: #FFFF00">@</span>substantial <span style="background-color: #FFFF00">@</span>collective <span style="background-color: #FFFF00">@</span>fear <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>nuclear <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>holocaust <span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>generate <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>cheap <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hollywood <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>tension <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `exploits our` | 6.45 | ['2.56', '4.26']
w2.f1 | x | `our substantial` | 8.46 | ['6.66', '1.94']
w2.f2 |   | `substantial collective` | 0.47 | ['0.17', '1.35']
w2.f3 | x | `generate cheap` | 3.94 | ['2.64', '1.86']
w2.f4 | x | `cheap hollywood` | 5.49 | ['3.03', '2.65']
w2.f5 |   | `holocaust to` | 2.59 | ['0.50', '2.39']
w2.f6 |   | `of nuclear` | 2.95 | ['-0.05', '3.10']
w2.f7 | x | `generate cheap` | 3.35 | ['1.58', '2.67']
w2.f8 |   | `cheap hollywood` | 3.20 | ['1.59', '1.82']
w2.f9 |   | `holocaust to` | 4.12 | ['-0.54', '4.67']
w2.f10 | x | `nuclear holocaust` | 6.34 | ['-1.39', '7.87']
w2.f11 | x | `collective fear` | 6.55 | ['1.26', '5.56']
w2.f12 |   | `collective fear` | 2.00 | ['0.48', '1.56']
w2.f13 |   | `fear of` | 1.33 | ['1.24', '0.24']
w2.f14 | x | `generate cheap` | 6.63 | ['3.74', '2.92']
w2.f15 | x | `cheap hollywood` | 5.35 | ['1.72', '3.90']
w2.f16 |   | `to generate` | 2.64 | ['-1.25', '4.66']
w2.f17 | x | `@@PAD@@ k-19` | 4.66 | ['0.00', '5.27']
w2.f18 | x | `holocaust to` | 3.92 | ['1.55', '2.50']
w2.f19 | x | `of nuclear` | 4.86 | ['1.68', '3.48']
w3.f0 | x | `to generate cheap` | 6.00 | ['-0.93', '4.36', '2.96']
w3.f1 | x | `nuclear holocaust to` | 5.14 | ['5.80', '2.36', '-2.64']
w3.f2 | x | `hollywood tension .` | 6.51 | ['4.19', '1.56', '0.84']
w3.f3 |   | `of nuclear holocaust` | 1.75 | ['-1.29', '1.22', '2.42']
w3.f4 |   | `holocaust to generate` | 2.95 | ['3.64', '0.44', '-0.76']
w3.f5 | x | `k-19 exploits our` | 5.84 | ['0.44', '2.72', '3.01']
w3.f6 | x | `collective fear of` | 3.83 | ['0.59', '4.24', '-0.79']
w3.f7 |   | `to generate cheap` | 3.86 | ['3.76', '0.26', '0.33']
w3.f8 | x | `generate cheap hollywood` | 7.51 | ['2.38', '2.79', '2.62']
w3.f9 |   | `holocaust to generate` | 2.87 | ['1.87', '0.70', '0.41']
w3.f10 | x | `holocaust to generate` | 4.92 | ['0.29', '1.69', '3.09']
w3.f11 | x | `generate cheap hollywood` | 6.59 | ['3.18', '2.79', '0.81']
w3.f12 | x | `holocaust to generate` | 5.34 | ['-1.08', '1.37', '5.17']
w3.f13 |   | `our substantial collective` | 4.57 | ['0.06', '1.06', '3.69']
w3.f14 |   | `generate cheap hollywood` | 2.41 | ['1.62', '3.71', '-2.83']
w3.f15 |   | `substantial collective fear` | 3.74 | ['2.55', '0.14', '1.21']
w3.f16 | x | `of nuclear holocaust` | 6.42 | ['1.87', '1.52', '3.41']
w3.f17 | x | `cheap hollywood tension` | 6.13 | ['3.90', '0.49', '1.89']
w3.f18 | x | `fear of nuclear` | 5.22 | ['2.22', '2.10', '1.37']
w3.f19 | x | `collective fear of` | 4.10 | ['0.28', '1.27', '2.66']

## Original input: 
``` @@UNK@@ creates a world that 's at once surreal and @@UNK@@ familiar ; absurd , yet @@UNK@@ sad . ``` 

## Marked input: 
<pre>@@UNK@@ creates <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>world <span style="background-color: #FFFF00">@</span>that <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>at <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>once <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>surreal <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>familiar ; <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>absurd <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>yet <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>sad .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `surreal and` | 7.46 | ['9.32', '-1.48']
w2.f1 |   | `; absurd` | 3.56 | ['0.56', '3.13']
w2.f2 |   | `; absurd` | 0.40 | ['0.27', '1.17']
w2.f3 |   | `familiar ;` | 1.55 | ['2.14', '-0.04']
w2.f4 | x | `absurd ,` | 5.09 | ['2.78', '2.50']
w2.f5 |   | `world that` | 1.71 | ['0.70', '1.31']
w2.f6 | x | `at once` | 4.84 | ['2.94', '1.99']
w2.f7 |   | `at once` | 0.95 | ['1.98', '-0.12']
w2.f8 | x | `that 's` | 4.30 | ['0.70', '3.82']
w2.f9 |   | `@@UNK@@ sad` | 3.55 | ['2.38', '1.18']
w2.f10 | x | `a world` | 8.94 | ['1.97', '7.11']
w2.f11 |   | `a world` | 2.30 | ['0.43', '2.14']
w2.f12 | x | `'s at` | 3.72 | ['0.44', '3.31']
w2.f13 | x | `@@UNK@@ creates` | 3.51 | ['0.61', '3.05']
w2.f14 | x | `; absurd` | 5.05 | ['1.00', '4.09']
w2.f15 |   | `, yet` | 3.22 | ['2.19', '1.30']
w2.f16 | x | `once surreal` | 3.09 | ['1.07', '2.78']
w2.f17 |   | `once surreal` | 3.09 | ['1.62', '2.09']
w2.f18 | x | `familiar ;` | 4.10 | ['2.34', '1.88']
w2.f19 |   | `familiar ;` | 2.34 | ['1.49', '1.15']
w3.f0 |   | `that 's at` | 2.52 | ['-1.27', '1.91', '2.26']
w3.f1 | x | `at once surreal` | 6.04 | ['7.39', '0.67', '-1.63']
w3.f2 |   | `, yet @@UNK@@` | 3.35 | ['2.60', '1.15', '-0.31']
w3.f3 | x | `that 's at` | 3.95 | ['2.19', '-0.29', '2.65']
w3.f4 | x | `that 's at` | 4.01 | ['0.40', '2.08', '1.89']
w3.f5 |   | `once surreal and` | 4.85 | ['-1.09', '0.45', '5.81']
w3.f6 | x | `'s at once` | 7.04 | ['3.62', '1.79', '1.84']
w3.f7 | x | `that 's at` | 4.78 | ['3.01', '-0.11', '2.38']
w3.f8 |   | `that 's at` | 3.19 | ['3.58', '0.26', '-0.37']
w3.f9 | x | `; absurd ,` | 4.72 | ['-1.06', '2.82', '3.06']
w3.f10 |   | `absurd , yet` | 2.07 | ['1.35', '-0.41', '1.27']
w3.f11 |   | `absurd , yet` | 2.93 | ['4.38', '-1.36', '0.10']
w3.f12 |   | `; absurd ,` | 3.78 | ['-0.93', '4.69', '0.16']
w3.f13 |   | `'s at once` | 2.50 | ['0.09', '0.91', '1.75']
w3.f14 |   | `that 's at` | 1.63 | ['-0.45', '1.15', '1.02']
w3.f15 | x | `familiar ; absurd` | 4.31 | ['0.58', '1.35', '2.54']
w3.f16 |   | `creates a world` | 2.22 | ['1.58', '0.35', '0.66']
w3.f17 | x | `absurd , yet` | 7.03 | ['2.25', '3.34', '1.59']
w3.f18 |   | `at once surreal` | 1.71 | ['0.02', '0.61', '1.55']
w3.f19 | x | `a world that` | 5.17 | ['3.70', '3.16', '-1.56']

## Original input: 
``` the cast is phenomenal , especially the women . ``` 

## Marked input: 
<pre>the cast is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>phenomenal <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span>especially the women <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `cast is` | 0.32 | ['1.47', '-0.78']
w2.f1 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `cast is` | 2.83 | ['2.79', '0.59']
w2.f4 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f5 |   | `the cast` | 2.95 | ['1.16', '2.09']
w2.f6 |   | `phenomenal ,` | 3.20 | ['-0.63', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `cast is` | 1.51 | ['2.28', '-0.56']
w2.f9 |   | `the women` | 1.11 | ['-0.44', '1.56']
w2.f10 |   | `is phenomenal` | 0.98 | ['-2.88', '4.00']
w2.f11 |   | `especially the` | 2.09 | ['1.94', '0.42']
w2.f12 |   | `especially the` | 1.77 | ['0.49', '1.32']
w2.f13 |   | `phenomenal ,` | 0.72 | ['-1.32', '2.18']
w2.f14 |   | `the women` | 1.65 | ['0.10', '1.58']
w2.f15 |   | `the cast` | 2.97 | ['-0.42', '3.66']
w2.f16 |   | `cast is` | 1.04 | ['1.66', '0.15']
w2.f17 |   | `cast is` | 1.66 | ['1.47', '0.80']
w2.f18 |   | `women .` | 2.05 | ['1.95', '0.22']
w2.f19 |   | `is phenomenal` | 1.03 | ['0.37', '0.96']
w3.f0 |   | `phenomenal , especially` | 1.69 | ['-0.34', '-0.76', '3.18']
w3.f1 |   | `@@PAD@@ the cast` | 2.22 | ['0.00', '-0.57', '3.17']
w3.f2 |   | `@@PAD@@ @@PAD@@ the` | 0.00 | ['0.00', '0.00', '-1.91']
w3.f3 |   | `@@PAD@@ the cast` | 0.53 | ['0.00', '-0.66', '1.79']
w3.f4 |   | `the cast is` | 1.69 | ['-0.24', '-0.18', '2.46']
w3.f5 |   | `phenomenal , especially` | 4.02 | ['1.07', '1.40', '1.88']
w3.f6 |   | `@@PAD@@ the cast` | 2.13 | ['0.00', '0.45', '1.89']
w3.f7 |   | `phenomenal , especially` | 1.08 | ['0.64', '-0.37', '1.31']
w3.f8 |   | `cast is phenomenal` | 2.64 | ['-1.22', '4.71', '-0.56']
w3.f9 |   | `cast is phenomenal` | 1.31 | ['1.29', '0.12', '0.00']
w3.f10 | x | `women . @@PAD@@` | 4.20 | ['2.34', '2.00', '0.00']
w3.f11 |   | `cast is phenomenal` | 2.55 | ['0.97', '-0.19', '1.96']
w3.f12 | x | `the women .` | 5.61 | ['2.43', '1.70', '1.61']
w3.f13 | x | `the women .` | 5.86 | ['4.70', '-1.03', '2.45']
w3.f14 |   | `the cast is` | 2.25 | ['-1.08', '0.80', '2.63']
w3.f15 |   | `is phenomenal ,` | 2.18 | ['-1.83', '1.47', '2.70']
w3.f16 |   | `phenomenal , especially` | 2.68 | ['0.34', '3.78', '-1.06']
w3.f17 |   | `, especially the` | 2.51 | ['0.73', '0.69', '1.25']
w3.f18 |   | `@@PAD@@ @@PAD@@ the` | 2.10 | ['0.00', '0.00', '2.57']
w3.f19 | x | `cast is phenomenal` | 4.11 | ['0.43', '3.62', '0.18']

## Original input: 
``` happily for mr . @@UNK@@ -- though @@UNK@@ for his subjects -- the @@UNK@@ hand of the @@UNK@@ wrote a script that no human screenwriter could have hoped to match . ``` 

## Marked input: 
<pre>happily for <span style="background-color: #FFFF00">@</span>mr <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>@@UNK@@ -- though <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>for his subjects -- <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>hand <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>the @@UNK@@ wrote <span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>script <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>no <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>human <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>screenwriter <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>could <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>have <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hoped <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>match <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ wrote` | 5.02 | ['1.98', '3.42']
w2.f1 | x | `human screenwriter` | 5.79 | ['5.09', '0.83']
w2.f2 |   | `that no` | 0.28 | ['0.13', '1.20']
w2.f3 | x | `could have` | 2.48 | ['-0.74', '3.78']
w2.f4 | x | `a script` | 4.01 | ['2.27', '1.93']
w2.f5 | x | `no human` | 3.47 | ['1.12', '2.66']
w2.f6 |   | `subjects --` | 3.61 | ['0.89', '2.82']
w2.f7 |   | `hand of` | 1.14 | ['2.54', '-0.50']
w2.f8 | x | `a script` | 3.85 | ['0.88', '3.18']
w2.f9 | x | `script that` | 7.66 | ['6.59', '1.09']
w2.f10 | x | `subjects --` | 4.92 | ['1.65', '3.41']
w2.f11 |   | `hand of` | 2.54 | ['1.87', '0.95']
w2.f12 | x | `could have` | 4.48 | ['2.33', '2.18']
w2.f13 | x | `screenwriter could` | 3.29 | ['0.80', '2.64']
w2.f14 | x | `that no` | 7.08 | ['0.85', '6.27']
w2.f15 | x | `-- though` | 7.79 | ['4.88', '3.18']
w2.f16 |   | `@@UNK@@ hand` | 1.74 | ['-0.75', '3.25']
w2.f17 | x | `could have` | 3.32 | ['3.51', '0.43']
w2.f18 |   | `hoped to` | 3.15 | ['0.78', '2.50']
w2.f19 |   | `@@UNK@@ hand` | 2.95 | ['0.39', '2.85']
w3.f0 | x | `screenwriter could have` | 6.09 | ['4.64', '2.38', '-0.54']
w3.f1 |   | `@@PAD@@ @@PAD@@ happily` | 2.58 | ['0.00', '0.00', '2.96']
w3.f2 | x | `wrote a script` | 5.11 | ['0.98', '-0.88', '5.10']
w3.f3 | x | `that no human` | 4.03 | ['2.19', '-0.49', '2.94']
w3.f4 |   | `human screenwriter could` | 2.66 | ['1.41', '0.37', '1.24']
w3.f5 |   | `no human screenwriter` | 3.69 | ['0.71', '4.28', '-0.97']
w3.f6 |   | `mr . @@UNK@@` | 2.55 | ['1.53', '1.07', '0.15']
w3.f7 | x | `to match .` | 4.97 | ['3.76', '1.53', '0.18']
w3.f8 | x | `that no human` | 6.01 | ['3.58', '-0.44', '3.15']
w3.f9 | x | `screenwriter could have` | 6.52 | ['5.07', '0.16', '1.40']
w3.f10 | x | `no human screenwriter` | 4.86 | ['2.04', '-0.62', '3.59']
w3.f11 | x | `wrote a script` | 4.37 | ['1.73', '0.22', '2.62']
w3.f12 | x | `the @@UNK@@ hand` | 7.97 | ['2.43', '-0.16', '5.83']
w3.f13 |   | `for his subjects` | 3.93 | ['0.33', '0.62', '3.22']
w3.f14 | x | `the @@UNK@@ hand` | 3.34 | ['-1.08', '0.79', '3.73']
w3.f15 |   | `subjects -- the` | 2.73 | ['0.84', '2.85', '-0.79']
w3.f16 | x | `that no human` | 5.90 | ['1.08', '1.53', '3.68']
w3.f17 | x | `could have hoped` | 9.39 | ['2.57', '3.75', '3.23']
w3.f18 | x | `human screenwriter could` | 4.11 | ['4.82', '-2.63', '2.39']
w3.f19 | x | `happily for mr` | 4.16 | ['-0.33', '2.83', '1.77']

## Original input: 
``` this version moves beyond the original 's nostalgia for the @@UNK@@ film experiences of @@UNK@@ to a deeper @@UNK@@ of cinema 's @@UNK@@ to stand in for true , lived experience . ``` 

## Marked input: 
<pre>this <span style="background-color: #FFFF00">@</span>version <span style="background-color: #FFFF00">@</span>moves <span style="background-color: #FFFF00">@</span>beyond <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>original <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>nostalgia <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>for <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>film experiences of <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>deeper <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>cinema <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>@@UNK@@ to stand <span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span>for <span style="background-color: #FFFF00">@</span>true <span style="background-color: #FFFF00">@</span>, lived experience <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `version moves` | 5.34 | ['1.81', '3.90']
w2.f1 | x | `original 's` | 3.78 | ['2.35', '1.57']
w2.f2 |   | `stand in` | 0.09 | ['1.01', '0.12']
w2.f3 |   | `experience .` | 1.93 | ['2.54', '-0.05']
w2.f4 | x | `a deeper` | 3.78 | ['2.27', '1.70']
w2.f5 | x | `this version` | 5.15 | ['2.84', '2.61']
w2.f6 |   | `true ,` | 3.33 | ['-0.51', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 | x | `original 's` | 4.28 | ['0.68', '3.82']
w2.f9 | x | `@@UNK@@ to` | 7.04 | ['2.38', '4.67']
w2.f10 | x | `a deeper` | 5.87 | ['1.97', '4.04']
w2.f11 | x | `experiences of` | 3.07 | ['2.40', '0.95']
w2.f12 | x | `moves beyond` | 6.24 | ['1.00', '5.28']
w2.f13 |   | `@@PAD@@ this` | 2.85 | ['0.00', '3.00']
w2.f14 |   | `nostalgia for` | 1.92 | ['2.25', '-0.30']
w2.f15 | x | `of cinema` | 8.78 | ['-3.18', '12.24']
w2.f16 | x | `moves beyond` | 2.92 | ['-0.38', '4.05']
w2.f17 | x | `'s nostalgia` | 3.92 | ['0.09', '4.45']
w2.f18 | x | `a deeper` | 3.26 | ['0.76', '2.62']
w2.f19 | x | `this version` | 5.09 | ['1.58', '3.81']
w3.f0 | x | `original 's nostalgia` | 8.10 | ['5.05', '1.91', '1.52']
w3.f1 | x | `@@PAD@@ this version` | 3.84 | ['0.00', '-0.45', '4.67']
w3.f2 | x | `moves beyond the` | 6.33 | ['4.93', '3.41', '-1.91']
w3.f3 | x | `@@PAD@@ this version` | 4.37 | ['0.00', '-0.20', '5.18']
w3.f4 | x | `original 's nostalgia` | 3.88 | ['1.32', '2.08', '0.85']
w3.f5 | x | `lived experience .` | 5.86 | ['0.66', '1.20', '4.32']
w3.f6 | x | `'s nostalgia for` | 5.41 | ['3.62', '1.30', '0.71']
w3.f7 | x | `to stand in` | 5.19 | ['3.76', '0.43', '1.49']
w3.f8 | x | `a deeper @@UNK@@` | 5.21 | ['0.66', '5.38', '-0.54']
w3.f9 |   | `of cinema 's` | 2.66 | ['-1.50', '3.13', '1.14']
w3.f10 |   | `of cinema 's` | 3.33 | ['2.92', '1.36', '-0.80']
w3.f11 | x | `original 's nostalgia` | 4.83 | ['4.34', '0.46', '0.22']
w3.f12 |   | `version moves beyond` | 3.58 | ['2.89', '-1.11', '1.93']
w3.f13 |   | `the original 's` | 4.11 | ['4.70', '-0.73', '0.39']
w3.f14 | x | `original 's nostalgia` | 4.25 | ['1.34', '1.15', '1.85']
w3.f15 |   | `for true ,` | 3.34 | ['0.38', '0.42', '2.70']
w3.f16 | x | `@@PAD@@ this version` | 3.87 | ['0.00', '1.31', '2.94']
w3.f17 | x | `nostalgia for the` | 6.98 | ['0.77', '5.11', '1.25']
w3.f18 | x | `original 's nostalgia` | 3.54 | ['2.13', '0.79', '1.08']
w3.f19 | x | `stand in for` | 3.98 | ['2.34', '1.23', '0.53']

## Original input: 
``` does n't really add up to much . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>does <span style="background-color: #6698FF">@</span>n't <span style="background-color: #6698FF">@</span>really <span style="background-color: #6698FF">@</span>add <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>up <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>much <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@PAD@@ does` | 3.34 | ['0.00', '3.71']
w2.f1 |   | `add up` | 2.96 | ['0.21', '2.88']
w2.f2 |   | `add up` | 1.52 | ['0.98', '1.59']
w2.f3 | x | `really add` | 4.82 | ['1.78', '3.60']
w2.f4 |   | `much .` | 1.57 | ['1.79', '-0.03']
w2.f5 |   | `much .` | 2.16 | ['4.87', '-2.41']
w2.f6 |   | `n't really` | 0.89 | ['-1.33', '2.32']
w2.f7 |   | `add up` | 1.71 | ['1.59', '1.03']
w2.f8 |   | `n't really` | 0.64 | ['0.91', '-0.05']
w2.f9 | x | `up to` | 5.77 | ['1.12', '4.67']
w2.f10 | x | `add up` | 7.04 | ['0.24', '6.94']
w2.f11 | x | `add up` | 4.14 | ['1.84', '2.58']
w2.f12 |   | `add up` | 1.45 | ['1.05', '0.44']
w2.f13 |   | `n't really` | 2.60 | ['1.45', '1.30']
w2.f14 |   | `does n't` | 1.84 | ['-0.44', '2.31']
w2.f15 | x | `really add` | 4.79 | ['1.52', '3.55']
w2.f16 | x | `@@PAD@@ does` | 2.84 | ['0.00', '3.60']
w2.f17 |   | `really add` | 2.91 | ['2.18', '1.35']
w2.f18 |   | `up to` | 2.58 | ['0.21', '2.50']
w2.f19 |   | `up to` | 1.53 | ['0.71', '1.12']
w3.f0 |   | `up to much` | 3.34 | ['5.35', '-1.42', '-0.20']
w3.f1 |   | `really add up` | 2.05 | ['-0.90', '1.18', '2.15']
w3.f2 |   | `add up to` | 2.27 | ['1.05', '2.68', '-1.37']
w3.f3 |   | `@@PAD@@ does n't` | 1.37 | ['0.00', '1.99', '-0.01']
w3.f4 |   | `really add up` | 2.89 | ['-0.50', '1.68', '2.06']
w3.f5 |   | `to much .` | 2.96 | ['0.53', '-1.57', '4.32']
w3.f6 | x | `n't really add` | 4.93 | ['3.72', '0.93', '0.49']
w3.f7 |   | `to much .` | 2.11 | ['3.76', '-1.33', '0.18']
w3.f8 |   | `up to much` | 1.27 | ['0.36', '1.89', '-0.69']
w3.f9 |   | `n't really add` | 3.28 | ['2.93', '0.12', '0.33']
w3.f10 | x | `really add up` | 12.35 | ['4.32', '3.66', '4.51']
w3.f11 | x | `add up to` | 7.42 | ['4.43', '1.12', '2.06']
w3.f12 | x | `really add up` | 5.30 | ['3.69', '0.77', '0.96']
w3.f13 |   | `to much .` | 1.07 | ['1.07', '-2.20', '2.45']
w3.f14 | x | `@@PAD@@ @@PAD@@ does` | 3.62 | ['0.00', '0.00', '3.71']
w3.f15 | x | `really add up` | 5.62 | ['1.90', '3.99', '-0.11']
w3.f16 |   | `does n't really` | 0.69 | ['-0.23', '2.52', '-1.22']
w3.f17 | x | `@@PAD@@ does n't` | 7.06 | ['0.00', '2.70', '4.52']
w3.f18 |   | `add up to` | 2.36 | ['0.01', '1.30', '1.52']
w3.f19 | x | `up to much` | 6.15 | ['3.39', '0.71', '2.16']

## Original input: 
``` director david @@UNK@@ gives dahmer a @@UNK@@ that the @@UNK@@ never game his victims . ``` 

## Marked input: 
<pre>director david @@UNK@@ gives <span style="background-color: #FFFF00">@</span>dahmer <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>that <span style="background-color: #6698FF">@</span>the @@UNK@@ never game <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>his <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>victims <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `never game` | 4.29 | ['4.09', '0.58']
w2.f1 |   | `@@PAD@@ director` | 2.08 | ['0.00', '2.21']
w2.f2 |   | `gives dahmer` | 0.01 | ['0.50', '0.56']
w2.f3 |   | `@@UNK@@ never` | 1.73 | ['-0.08', '2.36']
w2.f4 |   | `his victims` | 2.71 | ['0.33', '2.57']
w2.f5 |   | `director david` | 1.08 | ['0.32', '1.06']
w2.f6 |   | `director david` | 1.88 | ['1.58', '0.39']
w2.f7 |   | `gives dahmer` | 1.47 | ['2.38', '0.00']
w2.f8 |   | `@@UNK@@ never` | 2.34 | ['0.21', '2.35']
w2.f9 |   | `@@UNK@@ gives` | 3.46 | ['2.38', '1.09']
w2.f10 | x | `gives dahmer` | 4.20 | ['1.74', '2.59']
w2.f11 |   | `gives dahmer` | 2.11 | ['1.78', '0.60']
w2.f12 | x | `gives dahmer` | 3.69 | ['1.85', '1.88']
w2.f13 | x | `gives dahmer` | 3.19 | ['-0.01', '3.35']
w2.f14 |   | `david @@UNK@@` | 1.87 | ['1.60', '0.30']
w2.f15 | x | `@@UNK@@ gives` | 4.07 | ['-1.59', '5.93']
w2.f16 |   | `director david` | 2.41 | ['0.53', '2.64']
w2.f17 |   | `his victims` | 3.03 | ['-0.01', '3.65']
w2.f18 |   | `director david` | 2.73 | ['3.48', '-0.62']
w2.f19 | x | `his victims` | 3.65 | ['1.37', '2.58']
w3.f0 |   | `dahmer a @@UNK@@` | 2.63 | ['0.93', '3.29', '-1.20']
w3.f1 |   | `@@PAD@@ @@PAD@@ director` | 0.18 | ['0.00', '0.00', '0.56']
w3.f2 | x | `never game his` | 8.44 | ['6.11', '1.69', '0.73']
w3.f3 |   | `that the @@UNK@@` | 0.99 | ['2.19', '-0.66', '0.07']
w3.f4 | x | `game his victims` | 4.89 | ['1.39', '-0.28', '4.14']
w3.f5 | x | `his victims .` | 10.76 | ['1.53', '5.23', '4.32']
w3.f6 |   | `@@PAD@@ director david` | 1.84 | ['0.00', '0.07', '1.98']
w3.f7 |   | `his victims .` | 1.81 | ['1.44', '0.69', '0.18']
w3.f8 |   | `game his victims` | 2.93 | ['2.89', '-0.07', '0.39']
w3.f9 | x | `dahmer a @@UNK@@` | 4.09 | ['2.22', '-0.16', '2.13']
w3.f10 |   | `victims . @@PAD@@` | 3.32 | ['1.47', '2.00', '0.00']
w3.f11 | x | `never game his` | 5.02 | ['3.52', '0.83', '0.86']
w3.f12 | x | `game his victims` | 5.34 | ['3.56', '1.37', '0.54']
w3.f13 |   | `the @@UNK@@ never` | 3.82 | ['4.70', '-1.74', '1.11']
w3.f14 |   | `game his victims` | 2.60 | ['-1.79', '-1.83', '6.31']
w3.f15 |   | `game his victims` | 1.22 | ['-0.68', '-0.35', '2.41']
w3.f16 |   | `game his victims` | 0.42 | ['-1.00', '1.12', '0.67']
w3.f17 |   | `@@UNK@@ gives dahmer` | 0.32 | ['-2.59', '0.76', '2.31']
w3.f18 |   | `never game his` | 2.88 | ['1.32', '1.34', '0.69']
w3.f19 |   | `director david @@UNK@@` | 1.30 | ['1.47', '1.97', '-2.02']

## Original input: 
``` watching war @@UNK@@ , you come to believe that nachtwey @@UNK@@ the wars he shows and @@UNK@@ with the victims he reveals . ``` 

## Marked input: 
<pre>watching <span style="background-color: #FFFF00">@</span>war <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>, you <span style="background-color: #FFFF00">@</span>come <span style="background-color: #FFFF00">@</span>to believe that <span style="background-color: #FFFF00">@</span>nachtwey <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span>wars <span style="background-color: #FFFF00">@</span>he <span style="background-color: #FFFF00">@</span>shows <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>with the <span style="background-color: #6698FF">@</span>victims <span style="background-color: #6698FF">@</span>he <span style="background-color: #6698FF">@</span>reveals <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `watching war` | 4.99 | ['-0.91', '6.27']
w2.f1 | x | `@@PAD@@ watching` | 3.92 | ['0.00', '4.06']
w2.f2 |   | `watching war` | 0.32 | ['0.47', '0.89']
w2.f3 |   | `victims he` | 0.67 | ['1.24', '-0.02']
w2.f4 |   | `watching war` | 1.38 | ['0.77', '0.80']
w2.f5 | x | `the wars` | 5.07 | ['1.16', '4.21']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 | x | `wars he` | 4.28 | ['1.51', '2.98']
w2.f9 |   | `come to` | 2.98 | ['-1.67', '4.67']
w2.f10 |   | `shows and` | 2.96 | ['1.62', '1.48']
w2.f11 |   | `believe that` | 2.54 | ['2.86', '-0.06']
w2.f12 | x | `that nachtwey` | 3.43 | ['1.55', '1.92']
w2.f13 |   | `@@UNK@@ ,` | 2.64 | ['0.61', '2.18']
w2.f14 |   | `@@UNK@@ with` | 1.77 | ['0.69', '1.12']
w2.f15 | x | `, you` | 7.91 | ['2.19', '5.99']
w2.f16 |   | `victims he` | 0.78 | ['1.55', '-0.01']
w2.f17 |   | `watching war` | 1.48 | ['0.06', '2.04']
w2.f18 |   | `to believe` | 3.07 | ['0.12', '3.07']
w2.f19 |   | `wars he` | 2.96 | ['0.59', '2.67']
w3.f0 | x | `victims he reveals` | 6.40 | ['2.74', '3.74', '0.31']
w3.f1 | x | `believe that nachtwey` | 4.19 | ['2.42', '0.66', '1.49']
w3.f2 | x | `victims he reveals` | 4.63 | ['0.52', '2.89', '1.31']
w3.f3 |   | `that nachtwey @@UNK@@` | 2.17 | ['2.19', '0.53', '0.07']
w3.f4 |   | `@@UNK@@ , you` | 3.23 | ['0.36', '0.77', '2.46']
w3.f5 | x | `he shows and` | 7.52 | ['0.38', '1.65', '5.81']
w3.f6 |   | `with the victims` | 3.01 | ['2.33', '0.45', '0.44']
w3.f7 |   | `@@PAD@@ @@PAD@@ watching` | 3.59 | ['0.00', '0.00', '4.09']
w3.f8 | x | `that nachtwey @@UNK@@` | 5.09 | ['3.58', '2.33', '-0.54']
w3.f9 | x | `he shows and` | 5.60 | ['2.19', '1.11', '2.40']
w3.f10 |   | `reveals . @@PAD@@` | 3.19 | ['1.34', '2.00', '0.00']
w3.f11 | x | `victims he reveals` | 4.84 | ['2.60', '1.70', '0.72']
w3.f12 | x | `he reveals .` | 5.47 | ['2.80', '1.19', '1.61']
w3.f13 |   | `wars he shows` | 5.14 | ['2.55', '-0.54', '3.37']
w3.f14 | x | `with the victims` | 4.88 | ['-1.02', '-0.32', '6.31']
w3.f15 |   | `@@UNK@@ with the` | 2.38 | ['-0.51', '3.85', '-0.79']
w3.f16 | x | `believe that nachtwey` | 6.68 | ['2.50', '2.04', '2.52']
w3.f17 |   | `watching war @@UNK@@` | 2.22 | ['1.34', '2.85', '-1.81']
w3.f18 |   | `you come to` | 2.94 | ['0.51', '1.38', '1.52']
w3.f19 |   | `@@UNK@@ , you` | 3.56 | ['-0.26', '1.68', '2.24']

## Original input: 
``` beautifully crafted and @@UNK@@ unsettling . . . @@UNK@@ the atmosphere of the crime expertly . ``` 

## Marked input: 
<pre><span style="background-color: #FFFF00">@</span>beautifully <span style="background-color: #FFFF00">@</span>crafted <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>unsettling <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>. @@UNK@@ the atmosphere <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>crime <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>expertly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ unsettling` | 2.64 | ['1.98', '1.04']
w2.f1 | x | `crime expertly` | 5.32 | ['0.99', '4.46']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `crime expertly` | 1.11 | ['0.60', '1.07']
w2.f4 |   | `unsettling .` | 0.99 | ['1.21', '-0.03']
w2.f5 |   | `the crime` | 1.59 | ['1.16', '0.74']
w2.f6 |   | `beautifully crafted` | 1.70 | ['2.87', '-1.07']
w2.f7 |   | `expertly .` | 0.10 | ['0.86', '0.14']
w2.f8 |   | `@@PAD@@ beautifully` | 2.16 | ['0.00', '2.37']
w2.f9 |   | `atmosphere of` | 3.53 | ['1.89', '1.65']
w2.f10 | x | `@@PAD@@ beautifully` | 9.80 | ['0.00', '9.94']
w2.f11 |   | `atmosphere of` | 1.58 | ['0.90', '0.95']
w2.f12 |   | `the atmosphere` | 2.00 | ['0.53', '1.50']
w2.f13 | x | `unsettling .` | 4.51 | ['4.65', '0.01']
w2.f14 |   | `the crime` | 1.38 | ['0.10', '1.31']
w2.f15 |   | `beautifully crafted` | 2.51 | ['0.64', '2.15']
w2.f16 |   | `atmosphere of` | 1.39 | ['2.49', '-0.34']
w2.f17 |   | `crime expertly` | 2.12 | ['0.40', '2.34']
w2.f18 |   | `unsettling .` | 2.82 | ['2.72', '0.22']
w2.f19 |   | `@@PAD@@ beautifully` | 1.89 | ['0.00', '2.19']
w3.f0 |   | `expertly . @@PAD@@` | 2.89 | ['3.29', '-0.01', '0.00']
w3.f1 |   | `beautifully crafted and` | 3.35 | ['4.55', '-0.65', '-0.17']
w3.f2 | x | `crime expertly .` | 4.33 | ['3.20', '0.38', '0.84']
w3.f3 |   | `@@PAD@@ @@PAD@@ beautifully` | 2.18 | ['0.00', '0.00', '2.78']
w3.f4 | x | `@@PAD@@ @@PAD@@ beautifully` | 4.03 | ['0.00', '0.00', '4.39']
w3.f5 | x | `beautifully crafted and` | 5.39 | ['0.59', '-0.68', '5.81']
w3.f6 |   | `@@UNK@@ the atmosphere` | 2.22 | ['-0.28', '0.45', '2.26']
w3.f7 |   | `beautifully crafted and` | 2.81 | ['0.86', '0.62', '1.83']
w3.f8 | x | `and @@UNK@@ unsettling` | 8.45 | ['2.47', '-0.27', '6.53']
w3.f9 |   | `. . @@UNK@@` | 3.28 | ['0.67', '0.58', '2.13']
w3.f10 |   | `. . @@UNK@@` | 2.80 | ['0.09', '2.00', '0.86']
w3.f11 |   | `expertly . @@PAD@@` | 0.80 | ['2.67', '-1.68', '0.00']
w3.f12 | x | `the crime expertly` | 4.78 | ['2.43', '1.75', '0.74']
w3.f13 | x | `the atmosphere of` | 8.32 | ['4.70', '1.17', '2.71']
w3.f14 | x | `the crime expertly` | 3.46 | ['-1.08', '3.15', '1.49']
w3.f15 |   | `beautifully crafted and` | 3.29 | ['1.49', '2.44', '-0.48']
w3.f16 |   | `@@PAD@@ @@PAD@@ beautifully` | 0.73 | ['0.00', '0.00', '1.10']
w3.f17 |   | `crime expertly .` | 2.88 | ['1.05', '1.01', '0.98']
w3.f18 | x | `atmosphere of the` | 3.34 | ['-0.86', '2.10', '2.57']
w3.f19 |   | `@@PAD@@ beautifully crafted` | 2.99 | ['0.00', '2.50', '0.61']

## Original input: 
``` the movie ends with @@UNK@@ in which most of the characters forget their lines and just utter ' @@UNK@@ , ' which is better than most of the writing in the movie . ``` 

## Marked input: 
<pre>the <span style="background-color: #6698FF">@</span>movie <span style="background-color: #6698FF">@</span>ends <span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>in which <span style="background-color: #6698FF">@</span>most <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>the characters <span style="background-color: #FFFF00">@</span>forget <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>their <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>lines <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>just <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>utter <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>' <span style="background-color: #6698FF">@</span>@@UNK@@ , ' which <span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>better <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>than <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>most <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span>the writing <span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>movie .</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `their lines` | 5.48 | ['4.53', '1.32']
w2.f1 |   | `in which` | 1.65 | ['-1.00', '2.78']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `just utter` | 1.29 | ['1.31', '0.54']
w2.f4 |   | `most of` | 3.51 | ['4.24', '-0.55']
w2.f5 |   | `forget their` | 0.71 | ['0.74', '0.28']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `characters forget` | 1.52 | ['0.60', '1.83']
w2.f8 |   | `' which` | 2.04 | ['0.95', '1.30']
w2.f9 | x | `' which` | 5.82 | ['2.80', '3.04']
w2.f10 | x | `which most` | 5.33 | ['0.69', '4.77']
w2.f11 |   | `characters forget` | 2.53 | ['0.57', '2.22']
w2.f12 |   | `' @@UNK@@` | 2.38 | ['2.20', '0.22']
w2.f13 | x | `movie ends` | 5.23 | ['3.71', '1.66']
w2.f14 | x | `in which` | 5.13 | ['-0.13', '5.29']
w2.f15 | x | `the characters` | 3.34 | ['-0.42', '4.03']
w2.f16 |   | `forget their` | 2.66 | ['1.84', '1.58']
w2.f17 | x | `just utter` | 4.77 | ['2.70', '2.68']
w2.f18 | x | `forget their` | 5.51 | ['-0.35', '5.98']
w2.f19 | x | `and just` | 3.86 | ['3.66', '0.50']
w3.f0 |   | `their lines and` | 3.67 | ['-0.23', '3.30', '0.99']
w3.f1 | x | `forget their lines` | 3.96 | ['2.35', '2.95', '-0.97']
w3.f2 | x | `@@PAD@@ the movie` | 4.78 | ['0.00', '0.94', '3.93']
w3.f3 |   | `@@PAD@@ @@PAD@@ the` | 0.00 | ['0.00', '0.00', '-2.04']
w3.f4 |   | `characters forget their` | 2.75 | ['2.01', '0.38', '0.72']
w3.f5 | x | `their lines and` | 5.72 | ['0.32', '-0.08', '5.81']
w3.f6 | x | `characters forget their` | 4.86 | ['1.82', '2.83', '0.43']
w3.f7 | x | `their lines and` | 5.93 | ['3.48', '1.11', '1.83']
w3.f8 | x | `which is better` | 5.49 | ['0.19', '4.71', '0.88']
w3.f9 | x | `their lines and` | 4.39 | ['1.77', '0.33', '2.40']
w3.f10 | x | `which is better` | 4.91 | ['2.23', '0.69', '2.14']
w3.f11 |   | `' which is` | 2.72 | ['0.98', '0.80', '1.14']
w3.f12 | x | `movie ends with` | 5.29 | ['0.15', '2.59', '2.68']
w3.f13 | x | `the writing in` | 6.32 | ['4.70', '1.34', '0.53']
w3.f14 | x | `' which is` | 6.53 | ['1.53', '2.47', '2.63']
w3.f15 |   | `ends with @@UNK@@` | 1.88 | ['0.25', '3.85', '-2.05']
w3.f16 | x | `is better than` | 4.69 | ['1.27', '3.55', '0.25']
w3.f17 | x | `better than most` | 5.60 | ['0.97', '-0.54', '5.32']
w3.f18 |   | `of the characters` | 2.95 | ['-0.21', '-0.59', '4.21']
w3.f19 | x | `which is better` | 7.41 | ['1.98', '3.62', '1.92']

## Original input: 
``` a by - the - numbers patient / @@UNK@@ pic that covers all the usual ground ``` 

## Marked input: 
<pre>a by - the - <span style="background-color: #6698FF">@</span>numbers <span style="background-color: #6698FF">@</span>patient <span style="background-color: #6698FF">@</span>/ <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>pic that <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>covers <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>all <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>usual <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>ground</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `ground @@PAD@@` | 2.89 | ['3.27', '0.00']
w2.f1 | x | `usual ground` | 4.76 | ['2.20', '2.69']
w2.f2 |   | `usual ground` | 0.69 | ['1.88', '-0.15']
w2.f3 |   | `- numbers` | 1.27 | ['0.84', '0.98']
w2.f4 | x | `that covers` | 5.04 | ['1.54', '3.68']
w2.f5 | x | `the usual` | 5.88 | ['1.16', '5.02']
w2.f6 |   | `patient /` | 2.42 | ['1.66', '0.86']
w2.f7 |   | `covers all` | 0.57 | ['2.28', '-0.80']
w2.f8 |   | `usual ground` | 2.63 | ['1.90', '0.94']
w2.f9 |   | `covers all` | 4.67 | ['3.73', '0.95']
w2.f10 |   | `pic that` | 2.90 | ['2.36', '0.67']
w2.f11 |   | `the usual` | 1.57 | ['-1.49', '3.33']
w2.f12 | x | `usual ground` | 3.99 | ['-0.50', '4.53']
w2.f13 | x | `numbers patient` | 5.37 | ['1.99', '3.53']
w2.f14 | x | `- numbers` | 7.57 | ['-0.18', '7.79']
w2.f15 |   | `the usual` | 2.96 | ['-0.42', '3.64']
w2.f16 | x | `all the` | 3.95 | ['3.88', '0.83']
w2.f17 |   | `covers all` | 2.29 | ['1.65', '1.26']
w2.f18 |   | `that covers` | 3.19 | ['2.33', '0.98']
w2.f19 | x | `usual ground` | 4.66 | ['4.02', '0.94']
w3.f0 | x | `numbers patient /` | 7.55 | ['3.57', '4.17', '0.20']
w3.f1 | x | `all the usual` | 9.21 | ['-1.74', '-0.57', '11.90']
w3.f2 |   | `- the -` | 3.41 | ['2.02', '0.94', '0.54']
w3.f3 | x | `that covers all` | 5.67 | ['2.19', '1.16', '2.93']
w3.f4 | x | `usual ground @@PAD@@` | 3.57 | ['2.46', '1.47', '0.00']
w3.f5 |   | `that covers all` | 1.84 | ['1.79', '2.46', '-2.08']
w3.f6 |   | `covers all the` | 3.40 | ['5.32', '-0.55', '-1.16']
w3.f7 |   | `that covers all` | 3.12 | ['3.01', '-0.07', '0.68']
w3.f8 | x | `pic that covers` | 4.61 | ['1.86', '2.35', '0.69']
w3.f9 | x | `pic that covers` | 4.91 | ['2.06', '1.05', '1.90']
w3.f10 |   | `pic that covers` | 1.75 | ['3.09', '-0.63', '-0.56']
w3.f11 | x | `pic that covers` | 7.18 | ['4.96', '0.56', '1.86']
w3.f12 | x | `the - numbers` | 6.49 | ['2.43', '2.81', '1.37']
w3.f13 |   | `ground @@PAD@@ @@PAD@@` | 2.43 | ['2.67', '0.00', '0.00']
w3.f14 | x | `covers all the` | 5.43 | ['2.27', '2.00', '1.24']
w3.f15 |   | `/ @@UNK@@ pic` | 1.48 | ['2.14', '-1.69', '1.19']
w3.f16 | x | `all the usual` | 8.25 | ['1.41', '0.10', '7.11']
w3.f17 |   | `all the usual` | 3.50 | ['-0.00', '0.47', '3.19']
w3.f18 | x | `usual ground @@PAD@@` | 4.27 | ['6.76', '-2.02', '0.00']
w3.f19 | x | `pic that covers` | 4.87 | ['2.92', '0.63', '1.43']

## Original input: 
``` . . . del @@UNK@@ maintains a dark mood that makes the film seem like something to endure instead of enjoy . ``` 

## Marked input: 
<pre>. . . del <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>maintains <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>dark <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>mood <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>makes <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>film <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>seem <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>like <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>something <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>endure <span style="background-color: #6698FF">@</span>instead <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>enjoy <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `a dark` | 3.60 | ['1.11', '2.86']
w2.f1 |   | `maintains a` | 2.86 | ['2.01', '0.98']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `maintains a` | 1.67 | ['1.99', '0.24']
w2.f4 | x | `dark mood` | 5.01 | ['0.72', '4.47']
w2.f5 | x | `like something` | 6.23 | ['3.40', '3.14']
w2.f6 |   | `dark mood` | 2.48 | ['0.22', '2.36']
w2.f7 | x | `film seem` | 2.45 | ['0.28', '3.08']
w2.f8 | x | `maintains a` | 6.00 | ['3.66', '2.56']
w2.f9 | x | `something to` | 7.65 | ['2.99', '4.67']
w2.f10 | x | `dark mood` | 5.30 | ['1.19', '4.24']
w2.f11 |   | `instead of` | 2.04 | ['1.36', '0.95']
w2.f12 | x | `like something` | 3.98 | ['-1.80', '5.82']
w2.f13 | x | `seem like` | 4.20 | ['1.32', '3.03']
w2.f14 | x | `film seem` | 4.49 | ['0.32', '4.20']
w2.f15 |   | `seem like` | 2.18 | ['2.93', '-0.48']
w2.f16 |   | `endure instead` | 1.90 | ['-0.59', '3.25']
w2.f17 | x | `makes the` | 4.43 | ['5.31', '-0.27']
w2.f18 |   | `something to` | 2.96 | ['0.58', '2.50']
w2.f19 | x | `of enjoy` | 5.22 | ['1.68', '3.84']
w3.f0 | x | `maintains a dark` | 5.18 | ['0.64', '3.29', '1.64']
w3.f1 | x | `mood that makes` | 6.50 | ['3.71', '0.66', '2.50']
w3.f2 | x | `a dark mood` | 3.67 | ['1.87', '1.37', '0.52']
w3.f3 |   | `del @@UNK@@ maintains` | 2.11 | ['1.45', '-0.06', '1.32']
w3.f4 |   | `maintains a dark` | 3.08 | ['1.71', '0.29', '1.44']
w3.f5 | x | `of enjoy .` | 6.51 | ['-0.94', '3.45', '4.32']
w3.f6 |   | `to endure instead` | 2.27 | ['-0.82', '2.13', '1.17']
w3.f7 |   | `enjoy . @@PAD@@` | 2.65 | ['3.42', '-0.27', '0.00']
w3.f8 | x | `dark mood that` | 5.66 | ['3.91', '2.91', '-0.87']
w3.f9 | x | `. del @@UNK@@` | 4.73 | ['0.67', '2.03', '2.13']
w3.f10 |   | `. . del` | 2.97 | ['0.09', '2.00', '1.03']
w3.f11 |   | `instead of enjoy` | 1.05 | ['2.50', '-2.01', '0.76']
w3.f12 | x | `instead of enjoy` | 5.31 | ['2.66', '3.24', '-0.47']
w3.f13 | x | `dark mood that` | 7.73 | ['1.46', '6.07', '0.44']
w3.f14 | x | `film seem like` | 6.87 | ['0.82', '0.49', '5.65']
w3.f15 |   | `seem like something` | 2.95 | ['-0.25', '2.60', '0.77']
w3.f16 | x | `mood that makes` | 8.87 | ['4.94', '2.04', '2.26']
w3.f17 | x | `endure instead of` | 4.42 | ['1.51', '1.21', '1.87']
w3.f18 | x | `makes the film` | 4.66 | ['4.92', '-0.59', '0.80']
w3.f19 | x | `seem like something` | 4.50 | ['-0.37', '3.53', '1.46']

## Original input: 
``` aimed squarely at the least demanding of demographic groups : very small children who will be @@UNK@@ simply to spend more time with familiar cartoon characters . ``` 

## Marked input: 
<pre><span style="background-color: #FFFF00">@</span>aimed <span style="background-color: #FFFF00">@</span>squarely <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>at <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>least <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>demanding <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>demographic <span style="background-color: #6698FF">@</span>groups <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>: <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>very <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>small <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>children <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>who <span style="background-color: #6698FF">@</span>will <span style="background-color: #6698FF">@</span>be @@UNK@@ simply <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>spend <span style="background-color: #6698FF">@</span>more <span style="background-color: #6698FF">@</span>time <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>familiar <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>cartoon <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>characters <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `very small` | 7.38 | ['4.99', '2.77']
w2.f1 | x | `time with` | 5.36 | ['0.62', '4.87']
w2.f2 |   | `aimed squarely` | 1.68 | ['0.74', '1.99']
w2.f3 | x | `cartoon characters` | 4.35 | ['2.26', '2.64']
w2.f4 | x | `with familiar` | 5.74 | ['1.51', '4.42']
w2.f5 | x | `familiar cartoon` | 5.09 | ['3.17', '2.22']
w2.f6 |   | `groups :` | 3.35 | ['0.95', '2.50']
w2.f7 |   | `cartoon characters` | 1.62 | ['2.19', '0.34']
w2.f8 |   | `very small` | 3.07 | ['0.89', '2.39']
w2.f9 | x | `aimed squarely` | 5.45 | ['4.68', '0.79']
w2.f10 | x | `with familiar` | 3.80 | ['1.55', '2.38']
w2.f11 | x | `familiar cartoon` | 3.15 | ['0.77', '2.66']
w2.f12 | x | `@@UNK@@ simply` | 3.55 | ['-0.28', '3.87']
w2.f13 | x | `aimed squarely` | 3.81 | ['1.68', '2.28']
w2.f14 | x | `squarely at` | 4.15 | ['1.19', '2.99']
w2.f15 | x | `demographic groups` | 7.65 | ['2.97', '4.96']
w2.f16 | x | `familiar cartoon` | 6.20 | ['2.24', '4.72']
w2.f17 | x | `cartoon characters` | 6.98 | ['5.40', '2.20']
w2.f18 | x | `groups :` | 3.70 | ['-0.06', '3.89']
w2.f19 | x | `cartoon characters` | 3.43 | ['2.61', '1.12']
w3.f0 | x | `aimed squarely at` | 6.09 | ['2.42', '1.79', '2.26']
w3.f1 | x | `at the least` | 6.67 | ['7.39', '-0.57', '0.23']
w3.f2 | x | `to spend more` | 7.13 | ['0.63', '1.90', '4.68']
w3.f3 | x | `@@PAD@@ aimed squarely` | 2.53 | ['0.00', '1.46', '1.67']
w3.f4 |   | `groups : very` | 2.69 | ['1.42', '0.64', '0.99']
w3.f5 | x | `more time with` | 6.48 | ['0.77', '4.58', '1.46']
w3.f6 | x | `: very small` | 4.10 | ['0.18', '1.59', '2.54']
w3.f7 |   | `simply to spend` | 3.10 | ['0.79', '1.18', '1.63']
w3.f8 | x | `@@PAD@@ aimed squarely` | 6.72 | ['0.00', '6.18', '0.83']
w3.f9 | x | `very small children` | 6.19 | ['4.11', '0.51', '1.68']
w3.f10 | x | `of demographic groups` | 4.24 | ['2.92', '0.72', '0.74']
w3.f11 | x | `familiar cartoon characters` | 4.80 | ['3.96', '0.63', '0.41']
w3.f12 | x | `small children who` | 4.09 | ['0.83', '-0.21', '3.60']
w3.f13 | x | `the least demanding` | 5.53 | ['4.70', '2.13', '-1.05']
w3.f14 | x | `squarely at the` | 3.89 | ['2.89', '-0.15', '1.24']
w3.f15 | x | `time with familiar` | 7.65 | ['2.01', '3.85', '1.96']
w3.f16 | x | `@@PAD@@ @@PAD@@ aimed` | 5.46 | ['0.00', '0.00', '5.84']
w3.f17 | x | `cartoon characters .` | 7.38 | ['6.11', '0.45', '0.98']
w3.f18 | x | `@@PAD@@ aimed squarely` | 5.15 | ['0.00', '5.22', '0.40']
w3.f19 | x | `@@PAD@@ aimed squarely` | 4.84 | ['0.00', '5.46', '-0.51']

## Original input: 
``` the band performances @@UNK@@ in drumline are red hot . . . [ but ] from a mere story point of view , the film 's ice cold . ``` 

## Marked input: 
<pre>the band <span style="background-color: #FFFF00">@</span>performances <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span>drumline <span style="background-color: #FFFF00">@</span>are red hot <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>. [ but <span style="background-color: #6698FF">@</span>] <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>from <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span>mere <span style="background-color: #6698FF">@</span>story <span style="background-color: #6698FF">@</span>point <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>view <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>film <span style="background-color: #6698FF">@</span>'s ice <span style="background-color: #6698FF">@</span>cold <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `but ]` | 6.92 | ['0.91', '6.38']
w2.f1 | x | `but ]` | 4.90 | ['4.31', '0.72']
w2.f2 |   | `band performances` | 0.71 | ['1.03', '0.72']
w2.f3 | x | `[ but` | 2.31 | ['1.34', '1.53']
w2.f4 |   | `ice cold` | 3.45 | ['3.65', '-0.00']
w2.f5 | x | `the band` | 3.48 | ['1.16', '2.63']
w2.f6 |   | `in drumline` | 2.98 | ['1.77', '1.32']
w2.f7 | x | `cold .` | 2.87 | ['3.64', '0.14']
w2.f8 | x | `band performances` | 3.51 | ['3.06', '0.66']
w2.f9 |   | `story point` | 4.77 | ['0.41', '4.37']
w2.f10 | x | `band performances` | 10.19 | ['3.75', '6.58']
w2.f11 | x | `ice cold` | 2.88 | ['-2.40', '5.55']
w2.f12 |   | `drumline are` | 3.15 | ['0.61', '2.57']
w2.f13 | x | `view ,` | 4.96 | ['2.93', '2.18']
w2.f14 | x | `band performances` | 4.42 | ['3.25', '1.21']
w2.f15 | x | `the band` | 7.15 | ['-0.42', '7.84']
w2.f16 | x | `story point` | 3.54 | ['1.28', '3.02']
w2.f17 | x | `cold .` | 4.00 | ['4.15', '0.47']
w2.f18 |   | `ice cold` | 1.61 | ['-0.49', '2.21']
w2.f19 | x | `of view` | 3.66 | ['1.68', '2.28']
w3.f0 | x | `from a mere` | 6.87 | ['2.47', '3.29', '1.50']
w3.f1 | x | `performances @@UNK@@ in` | 6.27 | ['5.96', '-0.73', '1.42']
w3.f2 | x | `ice cold .` | 5.59 | ['2.07', '2.77', '0.84']
w3.f3 |   | `band performances @@UNK@@` | 1.99 | ['3.26', '-0.74', '0.07']
w3.f4 |   | `the band performances` | 3.44 | ['-0.24', '2.21', '1.82']
w3.f5 | x | `red hot .` | 5.09 | ['1.32', '-0.23', '4.32']
w3.f6 | x | `'s ice cold` | 5.92 | ['3.62', '3.00', '-0.49']
w3.f7 |   | `but ] from` | 3.35 | ['0.57', '-0.12', '3.40']
w3.f8 |   | `from a mere` | 4.19 | ['5.16', '-2.09', '1.40']
w3.f9 | x | `cold . @@PAD@@` | 5.33 | ['4.85', '0.58', '0.00']
w3.f10 | x | `cold . @@PAD@@` | 3.97 | ['2.11', '2.00', '0.00']
w3.f11 | x | `from a mere` | 6.34 | ['4.70', '0.22', '1.62']
w3.f12 |   | `red hot .` | 2.90 | ['1.72', '-0.30', '1.61']
w3.f13 | x | `the band performances` | 7.04 | ['4.70', '0.55', '2.04']
w3.f14 | x | `[ but ]` | 7.70 | ['3.25', '3.83', '0.71']
w3.f15 | x | `mere story point` | 4.68 | ['4.23', '-1.57', '2.19']
w3.f16 | x | `band performances @@UNK@@` | 4.52 | ['4.82', '3.60', '-3.52']
w3.f17 | x | `view , the` | 5.77 | ['1.33', '3.34', '1.25']
w3.f18 | x | `band performances @@UNK@@` | 6.59 | ['6.65', '0.63', '-0.23']
w3.f19 | x | `story point of` | 6.02 | ['1.76', '1.71', '2.66']

## Original input: 
``` while hoffman 's performance is great , the subject matter goes nowhere . ``` 

## Marked input: 
<pre>while <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>hoffman <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>performance <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>great , <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>subject <span style="background-color: #6698FF">@</span>matter <span style="background-color: #6698FF">@</span>goes <span style="background-color: #6698FF">@</span>nowhere <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `matter goes` | 3.59 | ['3.56', '0.40']
w2.f1 | x | `@@PAD@@ while` | 4.79 | ['0.00', '4.92']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `goes nowhere` | 2.65 | ['1.10', '2.11']
w2.f4 |   | `subject matter` | 3.26 | ['3.31', '0.14']
w2.f5 | x | `while hoffman` | 5.42 | ['2.41', '3.32']
w2.f6 | x | `great ,` | 6.61 | ['2.77', '3.93']
w2.f7 | x | `while hoffman` | 2.32 | ['0.16', '3.07']
w2.f8 | x | `hoffman 's` | 7.56 | ['3.95', '3.82']
w2.f9 |   | `hoffman 's` | 2.00 | ['3.06', '-1.05']
w2.f10 |   | `'s performance` | 2.84 | ['2.75', '0.22']
w2.f11 |   | `hoffman 's` | 0.60 | ['2.02', '-1.15']
w2.f12 |   | `while hoffman` | 3.28 | ['0.86', '2.46']
w2.f13 |   | `great ,` | 1.33 | ['-0.71', '2.18']
w2.f14 |   | `@@PAD@@ while` | 1.06 | ['0.00', '1.10']
w2.f15 | x | `'s performance` | 6.79 | ['1.82', '5.25']
w2.f16 | x | `while hoffman` | 5.78 | ['1.50', '5.04']
w2.f17 |   | `hoffman 's` | 2.80 | ['3.48', '-0.07']
w2.f18 |   | `hoffman 's` | 2.77 | ['1.78', '1.12']
w2.f19 |   | `performance is` | 2.41 | ['2.02', '0.69']
w3.f0 | x | `subject matter goes` | 6.25 | ['-0.70', '2.10', '5.25']
w3.f1 | x | `hoffman 's performance` | 4.11 | ['4.27', '-0.93', '1.15']
w3.f2 | x | `while hoffman 's` | 4.83 | ['4.03', '0.78', '0.11']
w3.f3 | x | `while hoffman 's` | 4.03 | ['1.73', '2.59', '0.31']
w3.f4 | x | `hoffman 's performance` | 4.70 | ['0.33', '2.08', '2.65']
w3.f5 |   | `'s performance is` | 4.74 | ['0.63', '4.50', '-0.05']
w3.f6 |   | `'s performance is` | 3.53 | ['3.62', '-1.52', '1.64']
w3.f7 |   | `hoffman 's performance` | 1.40 | ['0.70', '-0.11', '1.32']
w3.f8 |   | `performance is great` | 3.24 | ['-0.21', '4.71', '-0.98']
w3.f9 |   | `is great ,` | 2.36 | ['-1.28', '0.69', '3.06']
w3.f10 | x | `@@PAD@@ while hoffman` | 4.12 | ['0.00', '2.58', '1.69']
w3.f11 |   | `subject matter goes` | 3.62 | ['0.58', '-0.29', '3.53']
w3.f12 | x | `goes nowhere .` | 5.59 | ['1.55', '2.56', '1.61']
w3.f13 |   | `performance is great` | 3.04 | ['1.70', '2.81', '-1.23']
w3.f14 | x | `great , the` | 3.56 | ['2.78', '-0.37', '1.24']
w3.f15 |   | `nowhere . @@PAD@@` | 3.44 | ['4.13', '-0.52', '0.00']
w3.f16 |   | `performance is great` | 3.51 | ['1.68', '-0.75', '2.95']
w3.f17 | x | `great , the` | 5.36 | ['0.92', '3.34', '1.25']
w3.f18 |   | `while hoffman 's` | 2.60 | ['-0.30', '3.04', '0.32']
w3.f19 |   | `is great ,` | 3.37 | ['0.33', '2.07', '1.08']

## Original input: 
``` that zhang would make such a @@UNK@@ cute film -- with a blind @@UNK@@ at its center , no less -- @@UNK@@ where his ambitions have @@UNK@@ . ``` 

## Marked input: 
<pre>that zhang <span style="background-color: #FFFF00">@</span>would <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>make <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>such <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>cute <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>film <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>-- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>with <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>blind <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>at <span style="background-color: #6698FF">@</span>its <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>center <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span>no <span style="background-color: #6698FF">@</span>less <span style="background-color: #6698FF">@</span>-- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>where his ambitions have <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `-- with` | 4.87 | ['4.26', '0.98']
w2.f1 | x | `-- with` | 3.97 | ['-0.77', '4.87']
w2.f2 |   | `a blind` | 0.22 | ['0.10', '1.16']
w2.f3 | x | `ambitions have` | 6.35 | ['3.13', '3.78']
w2.f4 | x | `less --` | 5.31 | ['2.87', '2.63']
w2.f5 |   | `less --` | 1.48 | ['-0.08', '1.87']
w2.f6 | x | `at its` | 4.39 | ['2.94', '1.55']
w2.f7 |   | `at its` | 0.77 | ['1.98', '-0.30']
w2.f8 | x | `-- with` | 3.43 | ['0.15', '3.50']
w2.f9 |   | `@@UNK@@ at` | 4.57 | ['2.38', '2.20']
w2.f10 |   | `film --` | 2.93 | ['-0.35', '3.41']
w2.f11 | x | `a blind` | 6.15 | ['0.43', '5.99']
w2.f12 | x | `would make` | 4.72 | ['1.70', '3.06']
w2.f13 | x | `center ,` | 7.36 | ['5.32', '2.18']
w2.f14 | x | `, no` | 4.15 | ['-2.09', '6.27']
w2.f15 | x | `-- with` | 4.67 | ['4.88', '0.06']
w2.f16 | x | `zhang would` | 3.88 | ['-1.09', '5.74']
w2.f17 | x | `make such` | 5.72 | ['1.49', '4.84']
w2.f18 |   | `make such` | 3.06 | ['1.13', '2.05']
w2.f19 |   | `zhang would` | 2.26 | ['1.68', '0.88']
w3.f0 | x | `blind @@UNK@@ at` | 8.13 | ['5.91', '0.35', '2.26']
w3.f1 | x | `with a blind` | 3.87 | ['-1.34', '-0.71', '6.29']
w3.f2 | x | `, no less` | 7.59 | ['2.60', '2.06', '3.02']
w3.f3 |   | `that zhang would` | 1.93 | ['2.19', '-0.33', '0.68']
w3.f4 | x | `@@UNK@@ cute film` | 3.51 | ['0.36', '1.42', '2.09']
w3.f5 | x | `with a blind` | 5.55 | ['4.85', '-1.91', '2.94']
w3.f6 | x | `zhang would make` | 5.08 | ['-0.49', '2.89', '2.90']
w3.f7 |   | `cute film --` | 2.40 | ['-1.34', '2.52', '1.72']
w3.f8 | x | `that zhang would` | 5.32 | ['3.58', '1.13', '0.90']
w3.f9 | x | `ambitions have @@UNK@@` | 4.33 | ['3.48', '-1.18', '2.13']
w3.f10 | x | `@@UNK@@ cute film` | 4.84 | ['0.33', '2.29', '2.36']
w3.f11 | x | `such a @@UNK@@` | 3.95 | ['4.68', '0.22', '-0.75']
w3.f12 |   | `, no less` | 3.21 | ['-1.42', '3.58', '1.17']
w3.f13 |   | `make such a` | 3.93 | ['1.78', '2.23', '0.18']
w3.f14 | x | `, no less` | 6.22 | ['-0.18', '4.41', '2.07']
w3.f15 |   | `-- with a` | 3.72 | ['1.21', '3.85', '-1.17']
w3.f16 |   | `at its center` | 1.71 | ['-1.52', '2.21', '1.40']
w3.f17 |   | `blind @@UNK@@ at` | 3.53 | ['2.62', '1.39', '-0.33']
w3.f18 |   | `-- with a` | 1.61 | ['0.12', '2.32', '-0.37']
w3.f19 |   | `a @@UNK@@ cute` | 3.09 | ['3.70', '-2.39', '1.90']

## Original input: 
``` the film grows on you . and how . ``` 

## Marked input: 
<pre>the film grows on <span style="background-color: #FFFF00">@</span>you <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span>how <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `on you` | 4.75 | ['3.79', '1.33']
w2.f1 |   | `on you` | 1.26 | ['0.32', '1.07']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f4 |   | `you .` | 1.78 | ['2.00', '-0.03']
w2.f5 |   | `the film` | 1.83 | ['1.16', '0.98']
w2.f6 |   | `grows on` | 0.26 | ['0.02', '0.33']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 | x | `on you` | 3.34 | ['-0.59', '4.14']
w2.f9 |   | `you .` | 1.00 | ['0.55', '0.46']
w2.f10 |   | `you .` | 2.86 | ['4.16', '-1.16']
w2.f11 |   | `@@PAD@@ the` | 0.15 | ['0.00', '0.42']
w2.f12 | x | `and how` | 7.61 | ['0.18', '7.47']
w2.f13 |   | `and how` | 2.31 | ['-0.53', '3.00']
w2.f14 | x | `on you` | 3.61 | ['2.12', '1.52']
w2.f15 |   | `on you` | 2.96 | ['-2.77', '5.99']
w2.f16 |   | `grows on` | 0.48 | ['-0.30', '1.55']
w2.f17 |   | `and how` | 0.53 | ['1.02', '0.12']
w2.f18 |   | `and how` | 2.46 | ['3.52', '-0.94']
w2.f19 | x | `and how` | 6.47 | ['3.66', '3.11']
w3.f0 |   | `on you .` | 1.43 | ['-0.15', '1.60', '0.37']
w3.f1 |   | `@@PAD@@ @@PAD@@ the` | 0.00 | ['0.00', '0.00', '-5.12']
w3.f2 |   | `and how .` | 2.32 | ['-0.38', '1.95', '0.84']
w3.f3 |   | `film grows on` | 1.23 | ['0.63', '0.63', '0.57']
w3.f4 | x | `grows on you` | 5.47 | ['1.15', '2.22', '2.46']
w3.f5 |   | `on you .` | 4.05 | ['-0.84', '0.90', '4.32']
w3.f6 | x | `you . and` | 4.34 | ['2.54', '1.07', '0.95']
w3.f7 |   | `the film grows` | 2.43 | ['-1.23', '2.52', '1.63']
w3.f8 |   | `film grows on` | 2.26 | ['-0.14', '2.54', '0.15']
w3.f9 |   | `you . and` | 2.27 | ['-0.60', '0.58', '2.40']
w3.f10 | x | `you . and` | 4.85 | ['3.27', '2.00', '-0.27']
w3.f11 |   | `on you .` | 1.50 | ['-1.83', '3.60', '-0.08']
w3.f12 |   | `on you .` | 2.22 | ['-0.10', '0.84', '1.61']
w3.f13 |   | `how . @@PAD@@` | 3.31 | ['3.80', '-0.24', '0.00']
w3.f14 |   | `. and how` | 1.94 | ['-1.71', '1.09', '2.66']
w3.f15 |   | `on you .` | 1.42 | ['0.05', '2.14', '-0.60']
w3.f16 |   | `@@PAD@@ @@PAD@@ the` | 0.00 | ['0.00', '0.00', '-2.84']
w3.f17 | x | `and how .` | 4.40 | ['-1.40', '4.98', '0.98']
w3.f18 |   | `@@PAD@@ @@PAD@@ the` | 2.10 | ['0.00', '0.00', '2.57']
w3.f19 | x | `grows on you` | 4.60 | ['1.17', '1.30', '2.24']

## Original input: 
``` a trashy , exploitative , thoroughly unpleasant experience . ``` 

## Marked input: 
<pre>a trashy <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>exploitative <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>thoroughly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>unpleasant <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>experience <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `a trashy` | 3.13 | ['1.11', '2.39']
w2.f1 | x | `a trashy` | 4.25 | ['2.95', '1.44']
w2.f2 |   | `thoroughly unpleasant` | 0.65 | ['0.37', '1.32']
w2.f3 | x | `thoroughly unpleasant` | 3.74 | ['0.99', '3.31']
w2.f4 | x | `trashy ,` | 9.28 | ['6.97', '2.50']
w2.f5 |   | `, thoroughly` | 2.52 | ['1.09', '1.73']
w2.f6 | x | `trashy ,` | 7.52 | ['3.68', '3.93']
w2.f7 | x | `unpleasant experience` | 2.28 | ['3.55', '-0.35']
w2.f8 |   | `@@PAD@@ a` | 2.34 | ['0.00', '2.56']
w2.f9 |   | `thoroughly unpleasant` | 4.16 | ['4.03', '0.14']
w2.f10 |   | `a trashy` | 2.33 | ['1.97', '0.50']
w2.f11 | x | `, exploitative` | 3.13 | ['-0.67', '4.06']
w2.f12 |   | `thoroughly unpleasant` | 2.49 | ['1.49', '1.04']
w2.f13 | x | `trashy ,` | 5.15 | ['3.12', '2.18']
w2.f14 | x | `thoroughly unpleasant` | 4.18 | ['1.22', '2.99']
w2.f15 | x | `unpleasant experience` | 5.26 | ['1.04', '4.49']
w2.f16 | x | `, exploitative` | 4.26 | ['-0.98', '6.01']
w2.f17 | x | `experience .` | 3.56 | ['3.71', '0.47']
w2.f18 |   | `trashy ,` | 0.91 | ['0.14', '0.89']
w2.f19 |   | `unpleasant experience` | 2.41 | ['0.34', '2.37']
w3.f0 | x | `thoroughly unpleasant experience` | 4.17 | ['4.84', '0.81', '-1.09']
w3.f1 | x | `, thoroughly unpleasant` | 3.74 | ['1.74', '0.93', '1.45']
w3.f2 | x | `, exploitative ,` | 8.55 | ['2.60', '4.71', '1.32']
w3.f3 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.45']
w3.f4 |   | `@@PAD@@ a trashy` | 2.10 | ['0.00', '0.29', '2.17']
w3.f5 |   | `unpleasant experience .` | 4.71 | ['-0.48', '1.20', '4.32']
w3.f6 | x | `thoroughly unpleasant experience` | 4.02 | ['1.52', '1.48', '1.23']
w3.f7 | x | `thoroughly unpleasant experience` | 4.37 | ['1.40', '1.33', '2.13']
w3.f8 |   | `, exploitative ,` | 0.03 | ['-2.16', '0.33', '2.14']
w3.f9 |   | `trashy , exploitative` | 2.55 | ['2.37', '-1.33', '1.61']
w3.f10 | x | `trashy , exploitative` | 5.34 | ['1.94', '-0.41', '3.96']
w3.f11 | x | `thoroughly unpleasant experience` | 9.66 | ['1.10', '5.01', '3.74']
w3.f12 | x | `unpleasant experience .` | 6.57 | ['4.43', '0.66', '1.61']
w3.f13 |   | `unpleasant experience .` | 1.71 | ['-0.21', '-0.28', '2.45']
w3.f14 |   | `trashy , exploitative` | 2.77 | ['-1.12', '-0.37', '4.35']
w3.f15 | x | `thoroughly unpleasant experience` | 7.02 | ['1.18', '3.49', '2.51']
w3.f16 | x | `exploitative , thoroughly` | 7.85 | ['-0.22', '3.78', '4.67']
w3.f17 | x | `trashy , exploitative` | 6.27 | ['-0.19', '3.34', '3.28']
w3.f18 |   | `a trashy ,` | 1.04 | ['-1.48', '2.20', '0.79']
w3.f19 | x | `a trashy ,` | 4.18 | ['3.70', '-0.48', '1.08']

## Original input: 
``` kept @@UNK@@ largely by a @@UNK@@ @@UNK@@ ensemble . ``` 

## Marked input: 
<pre>kept <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>largely <span style="background-color: #6698FF">@</span>by <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>@@UNK@@ @@UNK@@ ensemble .</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ largely` | 1.60 | ['1.98', '-0.00']
w2.f1 |   | `a @@UNK@@` | 1.57 | ['2.95', '-1.25']
w2.f2 |   | `@@PAD@@ kept` | 0.09 | ['0.00', '1.14']
w2.f3 |   | `kept @@UNK@@` | 0.65 | ['1.94', '-0.73']
w2.f4 |   | `@@PAD@@ kept` | 0.49 | ['0.00', '0.68']
w2.f5 |   | `. @@PAD@@` | 0.37 | ['0.67', '0.00']
w2.f6 |   | `@@PAD@@ kept` | 0.79 | ['0.00', '0.89']
w2.f7 |   | `kept @@UNK@@` | 0.62 | ['2.60', '-1.08']
w2.f8 |   | `kept @@UNK@@` | 0.50 | ['1.42', '-0.71']
w2.f9 |   | `@@UNK@@ largely` | 4.45 | ['2.38', '2.08']
w2.f10 |   | `@@UNK@@ ensemble` | 0.81 | ['-0.06', '1.00']
w2.f11 |   | `@@PAD@@ kept` | 2.64 | ['0.00', '2.91']
w2.f12 | x | `largely by` | 3.64 | ['-0.02', '3.71']
w2.f13 | x | `@@UNK@@ largely` | 5.29 | ['0.61', '4.83']
w2.f14 | x | `kept @@UNK@@` | 3.32 | ['3.05', '0.30']
w2.f15 |   | `@@PAD@@ kept` | 0.69 | ['0.00', '0.96']
w2.f16 |   | `@@UNK@@ largely` | 1.53 | ['-0.75', '3.04']
w2.f17 | x | `@@PAD@@ kept` | 5.38 | ['0.00', '6.00']
w2.f18 |   | `. @@PAD@@` | 0.86 | ['0.99', '0.00']
w2.f19 |   | `@@UNK@@ largely` | 1.34 | ['0.39', '1.24']
w3.f0 |   | `@@PAD@@ @@PAD@@ kept` | 2.11 | ['0.00', '0.00', '2.50']
w3.f1 |   | `kept @@UNK@@ largely` | 3.20 | ['4.02', '-0.73', '0.30']
w3.f2 |   | `@@PAD@@ kept @@UNK@@` | 2.40 | ['0.00', '2.81', '-0.31']
w3.f3 |   | `@@PAD@@ @@PAD@@ kept` | 2.02 | ['0.00', '0.00', '2.62']
w3.f4 |   | `@@UNK@@ @@UNK@@ ensemble` | 1.20 | ['0.36', '-0.29', '1.49']
w3.f5 |   | `@@UNK@@ ensemble .` | 3.66 | ['0.08', '-0.41', '4.32']
w3.f6 |   | `kept @@UNK@@ largely` | 1.10 | ['3.31', '-1.80', '-0.20']
w3.f7 |   | `largely by a` | 1.53 | ['1.57', '1.28', '-0.82']
w3.f8 |   | `@@UNK@@ @@UNK@@ ensemble` | 1.44 | ['0.50', '-0.27', '1.49']
w3.f9 |   | `@@UNK@@ largely by` | 2.68 | ['-1.38', '4.25', '-0.08']
w3.f10 |   | `kept @@UNK@@ largely` | 2.69 | ['1.71', '-2.56', '3.69']
w3.f11 |   | `largely by a` | 3.20 | ['3.22', '-2.61', '2.78']
w3.f12 | x | `kept @@UNK@@ largely` | 5.96 | ['5.30', '-0.16', '0.95']
w3.f13 |   | `@@UNK@@ ensemble .` | 3.11 | ['-0.04', '0.95', '2.45']
w3.f14 | x | `kept @@UNK@@ largely` | 4.88 | ['-0.19', '0.79', '4.38']
w3.f15 |   | `. @@PAD@@ @@PAD@@` | 0.52 | ['0.68', '0.00', '0.00']
w3.f16 |   | `@@PAD@@ @@PAD@@ kept` | 2.26 | ['0.00', '0.00', '2.64']
w3.f17 | x | `kept @@UNK@@ largely` | 5.59 | ['-0.80', '1.39', '5.15']
w3.f18 |   | `@@PAD@@ @@PAD@@ kept` | 1.67 | ['0.00', '0.00', '2.14']
w3.f19 |   | `@@UNK@@ ensemble .` | 1.41 | ['-0.26', '4.16', '-2.38']

## Original input: 
``` the warm presence of zhao @@UNK@@ makes the preposterous lying hero into something more than he reasonably should be . ``` 

## Marked input: 
<pre>the <span style="background-color: #FFFF00">@</span>warm <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>presence <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>zhao <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>makes <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>preposterous <span style="background-color: #6698FF">@</span>lying <span style="background-color: #6698FF">@</span>hero <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>into <span style="background-color: #FFFF00">@</span>something <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>more <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>than <span style="background-color: #6698FF">@</span>he <span style="background-color: #6698FF">@</span>reasonably <span style="background-color: #6698FF">@</span>should <span style="background-color: #6698FF">@</span>be <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `lying hero` | 5.48 | ['4.63', '1.22']
w2.f1 |   | `into something` | 2.51 | ['0.53', '2.11']
w2.f2 |   | `should be` | 0.78 | ['0.77', '1.05']
w2.f3 |   | `something more` | 1.82 | ['0.21', '2.17']
w2.f4 |   | `reasonably should` | 1.89 | ['1.17', '0.92']
w2.f5 | x | `the warm` | 6.21 | ['1.16', '5.36']
w2.f6 |   | `preposterous lying` | 2.59 | ['2.83', '-0.15']
w2.f7 |   | `should be` | 1.18 | ['2.95', '-0.86']
w2.f8 |   | `hero into` | 2.65 | ['2.73', '0.13']
w2.f9 | x | `preposterous lying` | 5.22 | ['4.81', '0.43']
w2.f10 |   | `warm presence` | 2.20 | ['2.83', '-0.50']
w2.f11 |   | `more than` | 1.98 | ['2.11', '0.14']
w2.f12 |   | `into something` | 3.36 | ['-2.41', '5.82']
w2.f13 |   | `preposterous lying` | 2.71 | ['0.72', '2.14']
w2.f14 |   | `he reasonably` | 2.43 | ['1.93', '0.53']
w2.f15 | x | `the warm` | 5.27 | ['-0.42', '5.96']
w2.f16 | x | `reasonably should` | 3.38 | ['1.65', '2.49']
w2.f17 | x | `makes the` | 4.43 | ['5.31', '-0.27']
w2.f18 |   | `hero into` | 1.92 | ['-0.08', '2.12']
w2.f19 |   | `than he` | 2.92 | ['0.55', '2.67']
w3.f0 | x | `than he reasonably` | 4.88 | ['1.46', '3.74', '0.07']
w3.f1 | x | `zhao @@UNK@@ makes` | 3.98 | ['2.59', '-0.73', '2.50']
w3.f2 | x | `into something more` | 4.98 | ['1.98', '-1.59', '4.68']
w3.f3 |   | `zhao @@UNK@@ makes` | 2.16 | ['1.61', '-0.06', '1.21']
w3.f4 | x | `lying hero into` | 3.52 | ['-0.39', '1.42', '2.85']
w3.f5 |   | `preposterous lying hero` | 4.07 | ['3.86', '1.30', '-0.76']
w3.f6 |   | `hero into something` | 1.56 | ['1.85', '-1.61', '1.53']
w3.f7 |   | `of zhao @@UNK@@` | 2.76 | ['0.84', '2.49', '-0.07']
w3.f8 | x | `the warm presence` | 5.33 | ['1.05', '2.62', '1.94']
w3.f9 | x | `makes the preposterous` | 4.41 | ['2.89', '-0.12', '1.74']
w3.f10 | x | `the warm presence` | 4.17 | ['-1.27', '2.15', '3.44']
w3.f11 | x | `presence of zhao` | 4.18 | ['5.41', '-2.01', '0.97']
w3.f12 | x | `he reasonably should` | 5.22 | ['2.80', '1.08', '1.47']
w3.f13 | x | `warm presence of` | 8.23 | ['3.27', '2.50', '2.71']
w3.f14 |   | `presence of zhao` | 2.05 | ['5.22', '-2.13', '-0.95']
w3.f15 | x | `he reasonably should` | 5.60 | ['1.06', '-0.26', '4.97']
w3.f16 | x | `@@PAD@@ the warm` | 6.76 | ['0.00', '0.10', '7.04']
w3.f17 |   | `reasonably should be` | 3.18 | ['4.56', '-2.15', '0.92']
w3.f18 | x | `hero into something` | 3.86 | ['2.84', '2.25', '-0.77']
w3.f19 | x | `warm presence of` | 6.99 | ['5.01', '-0.57', '2.66']

## Original input: 
``` [ " take care of my cat " ] is an honestly nice little film that takes us on an examination of young adult life in urban south korea through the hearts and minds of the five @@UNK@@ . ``` 

## Marked input: 
<pre>[ <span style="background-color: #6698FF">@</span>" <span style="background-color: #6698FF">@</span>take <span style="background-color: #6698FF">@</span>care <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>my <span style="background-color: #6698FF">@</span>cat <span style="background-color: #6698FF">@</span>" <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>] <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>an <span style="background-color: #FFFF00">@</span>honestly <span style="background-color: #6698FF">@</span>nice <span style="background-color: #6698FF">@</span>little <span style="background-color: #6698FF">@</span>film that takes <span style="background-color: #FFFF00">@</span>us <span style="background-color: #FFFF00">@</span>on <span style="background-color: #FFFF00">@</span>an <span style="background-color: #6698FF">@</span>examination <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>young <span style="background-color: #6698FF">@</span>adult <span style="background-color: #FFFF00">@</span>life <span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span>urban <span style="background-color: #FFFF00">@</span>south <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>korea <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>through <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hearts <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>minds <span style="background-color: #FFFF00">@</span>of the five @@UNK@@ .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `" ]` | 8.80 | ['2.79', '6.38']
w2.f1 |   | `" take` | 3.22 | ['-2.50', '5.85']
w2.f2 |   | `take care` | 1.13 | ['0.63', '1.55']
w2.f3 | x | `urban south` | 3.40 | ['2.52', '1.44']
w2.f4 | x | `take care` | 6.70 | ['5.42', '1.46']
w2.f5 | x | `in urban` | 7.19 | ['0.92', '6.57']
w2.f6 | x | `cat "` | 4.78 | ['1.85', '3.03']
w2.f7 | x | `an examination` | 3.26 | ['0.98', '3.19']
w2.f8 | x | `south korea` | 6.75 | ['3.55', '3.41']
w2.f9 |   | `takes us` | 4.47 | ['4.17', '0.32']
w2.f10 | x | `urban south` | 8.31 | ['2.60', '5.84']
w2.f11 | x | `care of` | 5.34 | ['4.67', '0.95']
w2.f12 | x | `[ "` | 3.74 | ['1.83', '1.95']
w2.f13 |   | `minds of` | 2.27 | ['2.18', '0.24']
w2.f14 | x | `on an` | 4.13 | ['2.12', '2.05']
w2.f15 | x | `south korea` | 10.89 | ['2.32', '8.84']
w2.f16 | x | `cat "` | 3.54 | ['1.98', '2.33']
w2.f17 | x | `@@PAD@@ [` | 5.03 | ['0.00', '5.65']
w2.f18 | x | `young adult` | 3.28 | ['-0.19', '3.60']
w2.f19 | x | `young adult` | 4.60 | ['1.78', '3.12']
w3.f0 | x | `[ " take` | 6.69 | ['1.99', '0.73', '4.36']
w3.f1 | x | `urban south korea` | 7.20 | ['1.40', '-0.66', '6.85']
w3.f2 | x | `through the hearts` | 3.73 | ['4.51', '0.94', '-1.63']
w3.f3 | x | `that takes us` | 4.97 | ['2.19', '1.03', '2.35']
w3.f4 | x | `" ] is` | 5.17 | ['0.32', '2.75', '2.46']
w3.f5 | x | `the hearts and` | 6.93 | ['-0.36', '1.81', '5.81']
w3.f6 | x | `an honestly nice` | 5.08 | ['1.58', '2.67', '1.04']
w3.f7 | x | `life in urban` | 5.86 | ['1.28', '0.70', '4.38']
w3.f8 | x | `urban south korea` | 9.86 | ['5.34', '1.24', '3.56']
w3.f9 | x | `south korea through` | 5.18 | ['0.33', '2.37', '2.58']
w3.f10 | x | `of my cat` | 8.16 | ['2.92', '5.19', '0.19']
w3.f11 | x | `south korea through` | 7.05 | ['4.37', '-1.57', '4.44']
w3.f12 | x | `on an examination` | 6.44 | ['-0.10', '1.18', '5.48']
w3.f13 | x | `urban south korea` | 9.10 | ['-0.13', '4.33', '5.16']
w3.f14 | x | `[ " take` | 5.10 | ['3.25', '0.47', '1.47']
w3.f15 | x | `take care of` | 7.52 | ['0.63', '5.05', '2.01']
w3.f16 | x | `life in urban` | 9.91 | ['1.73', '1.85', '6.70']
w3.f17 | x | `an examination of` | 7.02 | ['3.05', '2.26', '1.87']
w3.f18 | x | `korea through the` | 7.71 | ['3.40', '2.21', '2.57']
w3.f19 | x | `south korea through` | 9.65 | ['5.47', '4.20', '0.09']

## Original input: 
``` if you have n't seen the film @@UNK@@ , you may be surprised at the variety of tones in spielberg 's work . much of it is funny , but there are also some startling , @@UNK@@ moments . . . ``` 

## Marked input: 
<pre>if you have <span style="background-color: #6698FF">@</span>n't <span style="background-color: #6698FF">@</span>seen <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>film @@UNK@@ , you <span style="background-color: #FFFF00">@</span>may <span style="background-color: #FFFF00">@</span>be <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>surprised <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>at <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span>variety <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>tones <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>spielberg <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>work <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>much <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span>it <span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span>funny <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>but there <span style="background-color: #FFFF00">@</span>are <span style="background-color: #FFFF00">@</span>also <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>some <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>startling <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>moments . . .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `n't seen` | 7.88 | ['1.68', '6.57']
w2.f1 | x | `some startling` | 6.17 | ['0.55', '5.75']
w2.f2 |   | `may be` | 0.27 | ['0.26', '1.05']
w2.f3 | x | `you have` | 3.64 | ['0.42', '3.78']
w2.f4 | x | `you may` | 5.21 | ['2.00', '3.41']
w2.f5 | x | `spielberg 's` | 7.62 | ['7.67', '0.26']
w2.f6 | x | `startling ,` | 9.68 | ['5.84', '3.93']
w2.f7 |   | `at the` | 0.88 | ['1.98', '-0.19']
w2.f8 | x | `spielberg 's` | 5.41 | ['1.80', '3.82']
w2.f9 | x | `be surprised` | 5.14 | ['3.56', '1.60']
w2.f10 | x | `you may` | 5.45 | ['4.16', '1.42']
w2.f11 | x | `may be` | 4.51 | ['2.36', '2.42']
w2.f12 | x | `tones in` | 3.97 | ['2.04', '1.97']
w2.f13 |   | `@@UNK@@ ,` | 2.64 | ['0.61', '2.18']
w2.f14 |   | `surprised at` | 3.04 | ['0.08', '2.99']
w2.f15 | x | `, you` | 7.91 | ['2.19', '5.99']
w2.f16 |   | `of tones` | 2.48 | ['0.18', '3.06']
w2.f17 | x | `also some` | 5.73 | ['2.16', '4.19']
w2.f18 | x | `startling ,` | 4.21 | ['3.44', '0.89']
w2.f19 | x | `surprised at` | 4.83 | ['3.42', '1.70']
w3.f0 |   | `tones in spielberg` | 1.20 | ['1.30', '1.29', '-1.00']
w3.f1 | x | `at the variety` | 7.87 | ['7.39', '-0.57', '1.43']
w3.f2 |   | `there are also` | 3.32 | ['1.89', '0.35', '1.17']
w3.f3 | x | `also some startling` | 2.61 | ['0.73', '0.43', '2.05']
w3.f4 | x | `but there are` | 5.32 | ['1.41', '0.75', '3.51']
w3.f5 | x | `'s work .` | 7.31 | ['0.63', '2.69', '4.32']
w3.f6 |   | `but there are` | 2.79 | ['1.54', '0.93', '0.53']
w3.f7 | x | `be surprised at` | 4.60 | ['0.84', '1.87', '2.38']
w3.f8 | x | `it is funny` | 7.53 | ['2.11', '4.71', '1.00']
w3.f9 | x | `in spielberg 's` | 3.92 | ['1.57', '1.32', '1.14']
w3.f10 |   | `of it is` | 3.26 | ['2.92', '-0.54', '1.03']
w3.f11 | x | `you have n't` | 4.64 | ['1.07', '2.99', '0.77']
w3.f12 | x | `the variety of` | 6.70 | ['2.43', '3.71', '0.69']
w3.f13 | x | `the variety of` | 8.63 | ['4.70', '1.48', '2.71']
w3.f14 | x | `are also some` | 3.91 | ['1.83', '-2.01', '4.18']
w3.f15 | x | `. much of` | 6.12 | ['0.68', '3.59', '2.01']
w3.f16 | x | `also some startling` | 8.00 | ['1.23', '0.84', '6.30']
w3.f17 | x | `you have n't` | 4.95 | ['-3.16', '3.75', '4.52']
w3.f18 | x | `surprised at the` | 7.40 | ['3.90', '1.39', '2.57']
w3.f19 | x | `it is funny` | 5.70 | ['-1.26', '3.62', '3.45']

## Original input: 
``` rock solid family fun out of the @@UNK@@ , extremely imaginative through out , but @@UNK@@ in the middle ``` 

## Marked input: 
<pre>rock <span style="background-color: #6698FF">@</span>solid <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>family <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>fun <span style="background-color: #FFFF00">@</span>out <span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>, extremely <span style="background-color: #6698FF">@</span>imaginative <span style="background-color: #6698FF">@</span>through <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>out <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>but <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ in the <span style="background-color: #6698FF">@</span>middle</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `imaginative through` | 8.87 | ['1.99', '7.25']
w2.f1 | x | `imaginative through` | 4.21 | ['1.33', '3.02']
w2.f2 |   | `solid family` | 0.05 | ['0.99', '0.11']
w2.f3 |   | `rock solid` | 1.96 | ['0.46', '2.06']
w2.f4 | x | `rock solid` | 7.87 | ['4.58', '3.48']
w2.f5 | x | `rock solid` | 3.38 | ['0.52', '3.17']
w2.f6 | x | `out ,` | 4.59 | ['0.75', '3.93']
w2.f7 | x | `rock solid` | 2.25 | ['1.19', '1.97']
w2.f8 | x | `rock solid` | 5.01 | ['1.28', '3.94']
w2.f9 |   | `@@UNK@@ in` | 4.26 | ['2.38', '1.89']
w2.f10 | x | `solid family` | 5.55 | ['3.49', '2.19']
w2.f11 | x | `@@PAD@@ rock` | 3.28 | ['0.00', '3.56']
w2.f12 |   | `but @@UNK@@` | 1.82 | ['1.63', '0.22']
w2.f13 |   | `@@UNK@@ ,` | 2.64 | ['0.61', '2.18']
w2.f14 |   | `out ,` | 2.86 | ['2.01', '0.89']
w2.f15 | x | `rock solid` | 9.01 | ['1.31', '7.97']
w2.f16 |   | `extremely imaginative` | 1.38 | ['1.83', '0.32']
w2.f17 | x | `extremely imaginative` | 4.25 | ['3.19', '1.67']
w2.f18 | x | `family fun` | 5.81 | ['5.05', '0.88']
w2.f19 | x | `family fun` | 3.99 | ['1.57', '2.72']
w3.f0 |   | `rock solid family` | 2.44 | ['2.49', '1.07', '-0.72']
w3.f1 |   | `fun out of` | 2.98 | ['3.19', '0.31', '-0.14']
w3.f2 | x | `through out ,` | 7.88 | ['4.51', '2.13', '1.32']
w3.f3 |   | `rock solid family` | 2.35 | ['0.63', '0.39', '1.93']
w3.f4 | x | `family fun out` | 3.90 | ['2.64', '0.51', '1.11']
w3.f5 |   | `extremely imaginative through` | 4.57 | ['-0.43', '5.54', '-0.22']
w3.f6 |   | `, extremely imaginative` | 2.09 | ['-1.13', '1.83', '1.59']
w3.f7 |   | `rock solid family` | 4.12 | ['0.24', '2.78', '1.60']
w3.f8 | x | `through out ,` | 6.79 | ['0.15', '4.78', '2.14']
w3.f9 |   | `extremely imaginative through` | 3.17 | ['0.87', '-0.18', '2.58']
w3.f10 | x | `extremely imaginative through` | 5.57 | ['3.96', '1.37', '0.38']
w3.f11 | x | `extremely imaginative through` | 6.30 | ['1.71', '0.35', '4.44']
w3.f12 | x | `out of the` | 5.95 | ['3.00', '3.24', '-0.17']
w3.f13 |   | `fun out of` | 4.67 | ['-1.84', '4.06', '2.71']
w3.f14 | x | `, extremely imaginative` | 3.75 | ['-0.18', '3.16', '0.86']
w3.f15 |   | `@@PAD@@ rock solid` | 3.33 | ['0.00', '1.17', '2.33']
w3.f16 | x | `solid family fun` | 6.90 | ['6.76', '-1.83', '2.35']
w3.f17 | x | `in the middle` | 4.82 | ['-1.11', '0.47', '5.62']
w3.f18 | x | `solid family fun` | 4.03 | ['2.00', '0.43', '2.06']
w3.f19 | x | `family fun out` | 5.33 | ['6.05', '1.11', '-1.71']

## Original input: 
``` it 's endlessly inventive , consistently intelligent and @@UNK@@ @@UNK@@ . ``` 

## Marked input: 
<pre>it 's endlessly <span style="background-color: #FFFF00">@</span>inventive <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>consistently <span style="background-color: #FFFF00">@</span>intelligent <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@PAD@@ it` | 1.30 | ['0.00', '1.67']
w2.f1 |   | `'s endlessly` | 2.74 | ['-0.75', '3.63']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f4 | x | `consistently intelligent` | 4.40 | ['2.09', '2.50']
w2.f5 | x | `endlessly inventive` | 6.07 | ['2.26', '4.12']
w2.f6 |   | `inventive ,` | 3.93 | ['0.09', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 | x | `'s endlessly` | 6.51 | ['2.75', '3.89']
w2.f11 |   | `intelligent and` | 1.39 | ['1.40', '0.27']
w2.f12 |   | `@@PAD@@ it` | 0.92 | ['0.00', '0.96']
w2.f13 |   | `inventive ,` | 2.21 | ['0.18', '2.18']
w2.f14 |   | `@@UNK@@ .` | 1.04 | ['0.69', '0.39']
w2.f15 | x | `endlessly inventive` | 6.70 | ['3.02', '3.95']
w2.f16 |   | `endlessly inventive` | 0.65 | ['1.60', '-0.19']
w2.f17 |   | `endlessly inventive` | 0.15 | ['0.29', '0.48']
w2.f18 |   | `consistently intelligent` | 2.26 | ['0.94', '1.44']
w2.f19 |   | `endlessly inventive` | 1.80 | ['0.17', '1.93']
w3.f0 |   | `endlessly inventive ,` | 1.32 | ['4.41', '-1.30', '-1.39']
w3.f1 |   | `, consistently intelligent` | 3.72 | ['1.74', '3.02', '-0.66']
w3.f2 |   | `@@PAD@@ it 's` | 1.72 | ['0.00', '1.70', '0.11']
w3.f3 |   | `, consistently intelligent` | 0.78 | ['-0.33', '1.40', '0.32']
w3.f4 |   | `it 's endlessly` | 2.61 | ['-0.70', '2.08', '1.59']
w3.f5 | x | `consistently intelligent and` | 7.40 | ['-0.55', '2.47', '5.81']
w3.f6 |   | `'s endlessly inventive` | 3.00 | ['3.62', '-0.95', '0.53']
w3.f7 | x | `endlessly inventive ,` | 4.52 | ['1.92', '1.91', '1.18']
w3.f8 |   | `it 's endlessly` | 3.67 | ['2.11', '0.26', '1.59']
w3.f9 | x | `consistently intelligent and` | 4.13 | ['0.92', '0.92', '2.40']
w3.f10 |   | `consistently intelligent and` | 3.23 | ['1.36', '2.29', '-0.27']
w3.f11 |   | `@@PAD@@ it 's` | 1.99 | ['0.00', '0.91', '1.27']
w3.f12 |   | `inventive , consistently` | 1.04 | ['0.15', '-0.15', '1.17']
w3.f13 | x | `'s endlessly inventive` | 6.62 | ['0.09', '3.83', '2.95']
w3.f14 |   | `, consistently intelligent` | 0.26 | ['-0.18', '0.74', '-0.21']
w3.f15 |   | `@@PAD@@ it 's` | 2.22 | ['0.00', '2.22', '0.17']
w3.f16 | x | `inventive , consistently` | 9.88 | ['6.77', '3.78', '-0.30']
w3.f17 |   | `inventive , consistently` | 0.10 | ['-2.88', '3.34', '-0.20']
w3.f18 | x | `endlessly inventive ,` | 6.41 | ['4.79', '1.29', '0.79']
w3.f19 | x | `intelligent and @@UNK@@` | 3.96 | ['4.92', '1.18', '-2.02']

## Original input: 
``` it 's leaden and predictable , and laughs are lacking . ``` 

## Marked input: 
<pre>it 's leaden <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>predictable <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>laughs <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>are <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>lacking <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `laughs are` | 1.98 | ['0.66', '1.69']
w2.f1 |   | `it 's` | 1.94 | ['0.50', '1.57']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `and predictable` | 0.28 | ['0.06', '0.77']
w2.f4 | x | `predictable ,` | 5.16 | ['2.84', '2.50']
w2.f5 |   | `. @@PAD@@` | 0.37 | ['0.67', '0.00']
w2.f6 |   | `predictable ,` | 2.09 | ['-1.75', '3.93']
w2.f7 |   | `leaden and` | 1.67 | ['2.49', '0.09']
w2.f8 |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 |   | `and laughs` | 3.76 | ['-0.02', '3.80']
w2.f10 |   | `predictable ,` | 0.99 | ['1.50', '-0.37']
w2.f11 |   | `and predictable` | 2.40 | ['0.34', '2.33']
w2.f12 | x | `'s leaden` | 4.91 | ['0.44', '4.51']
w2.f13 | x | `are lacking` | 3.57 | ['0.53', '3.19']
w2.f14 |   | `leaden and` | 3.03 | ['3.05', '0.01']
w2.f15 |   | `predictable ,` | 1.20 | ['1.78', '-0.31']
w2.f16 |   | `'s leaden` | 2.32 | ['-1.72', '4.80']
w2.f17 |   | `laughs are` | 2.27 | ['2.21', '0.68']
w2.f18 | x | `and laughs` | 6.79 | ['3.52', '3.40']
w2.f19 | x | `and laughs` | 5.10 | ['3.66', '1.74']
w3.f0 | x | `leaden and predictable` | 5.44 | ['4.69', '-1.09', '2.22']
w3.f1 |   | `predictable , and` | 1.24 | ['0.89', '0.90', '-0.17']
w3.f2 | x | `'s leaden and` | 7.43 | ['0.87', '6.18', '0.47']
w3.f3 |   | `@@PAD@@ @@PAD@@ it` | 0.00 | ['0.00', '0.00', '-2.43']
w3.f4 | x | `and laughs are` | 4.44 | ['-0.23', '1.51', '3.51']
w3.f5 | x | `predictable , and` | 5.76 | ['-1.13', '1.40', '5.81']
w3.f6 |   | `'s leaden and` | 2.78 | ['3.62', '-1.58', '0.95']
w3.f7 |   | `predictable , and` | 2.99 | ['2.02', '-0.37', '1.83']
w3.f8 | x | `and predictable ,` | 5.70 | ['2.47', '1.37', '2.14']
w3.f9 | x | `laughs are lacking` | 10.13 | ['6.47', '1.41', '2.36']
w3.f10 |   | `and laughs are` | 2.79 | ['-1.89', '1.05', '3.78']
w3.f11 |   | `@@PAD@@ it 's` | 1.99 | ['0.00', '0.91', '1.27']
w3.f12 | x | `laughs are lacking` | 4.50 | ['0.60', '2.18', '1.85']
w3.f13 |   | `predictable , and` | 3.55 | ['2.86', '1.92', '-0.98']
w3.f14 | x | `leaden and predictable` | 3.42 | ['2.12', '1.09', '0.30']
w3.f15 | x | `leaden and predictable` | 4.04 | ['2.10', '-1.32', '3.43']
w3.f16 |   | `@@PAD@@ @@PAD@@ it` | 1.48 | ['0.00', '0.00', '1.86']
w3.f17 | x | `predictable , and` | 8.13 | ['5.09', '3.34', '-0.15']
w3.f18 |   | `laughs are lacking` | 0.65 | ['3.66', '-0.28', '-2.27']
w3.f19 | x | `and laughs are` | 9.06 | ['3.50', '1.48', '4.20']

## Original input: 
``` if you open yourself up to mr . reggio 's theory of this imagery as the movie 's set . . . it can @@UNK@@ an almost visceral sense of @@UNK@@ and change . ``` 

## Marked input: 
<pre>if you <span style="background-color: #FFFF00">@</span>open <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>yourself <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>up <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>mr <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>. <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>reggio <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>theory <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>this <span style="background-color: #6698FF">@</span>imagery <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>as <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>movie <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>set <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #6698FF">@</span>. . it can @@UNK@@ an almost <span style="background-color: #FFFF00">@</span>visceral <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>sense <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of @@UNK@@ and change <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ an` | 2.01 | ['1.98', '0.41']
w2.f1 | x | `. reggio` | 4.70 | ['-0.03', '4.86']
w2.f2 |   | `yourself up` | 0.98 | ['0.44', '1.59']
w2.f3 |   | `you open` | 1.54 | ['0.42', '1.68']
w2.f4 | x | `movie 's` | 3.67 | ['3.31', '0.55']
w2.f5 | x | `this imagery` | 4.01 | ['2.84', '1.47']
w2.f6 |   | `visceral sense` | 1.69 | ['-0.93', '2.72']
w2.f7 | x | `almost visceral` | 2.63 | ['1.02', '2.51']
w2.f8 | x | `this imagery` | 3.50 | ['0.76', '2.96']
w2.f9 | x | `up to` | 5.77 | ['1.12', '4.67']
w2.f10 | x | `yourself up` | 6.64 | ['-0.16', '6.94']
w2.f11 |   | `yourself up` | 2.46 | ['0.15', '2.58']
w2.f12 | x | `'s set` | 5.25 | ['0.44', '4.84']
w2.f13 | x | `movie 's` | 3.36 | ['3.71', '-0.20']
w2.f14 |   | `@@UNK@@ an` | 2.71 | ['0.69', '2.05']
w2.f15 | x | `if you` | 5.81 | ['0.09', '5.99']
w2.f16 | x | `almost visceral` | 4.40 | ['1.88', '3.28']
w2.f17 | x | `almost visceral` | 5.76 | ['2.41', '3.97']
w2.f18 | x | `and change` | 4.00 | ['3.52', '0.61']
w2.f19 |   | `. reggio` | 2.68 | ['0.47', '2.51']
w3.f0 | x | `reggio 's theory` | 6.01 | ['-2.06', '1.91', '6.55']
w3.f1 |   | `up to mr` | 1.40 | ['1.84', '0.48', '-0.54']
w3.f2 | x | `as the movie` | 4.94 | ['0.16', '0.94', '3.93']
w3.f3 | x | `open yourself up` | 2.44 | ['1.37', '0.87', '0.80']
w3.f4 |   | `movie 's set` | 3.43 | ['2.80', '2.08', '-1.08']
w3.f5 |   | `to mr .` | 4.60 | ['0.53', '0.08', '4.32']
w3.f6 | x | `you open yourself` | 6.19 | ['2.54', '1.33', '2.53']
w3.f7 |   | `to mr .` | 2.96 | ['3.76', '-0.48', '0.18']
w3.f8 |   | `an almost visceral` | 2.95 | ['1.44', '1.38', '0.41']
w3.f9 |   | `set . .` | 3.05 | ['4.85', '0.58', '-2.28']
w3.f10 | x | `mr . reggio` | 4.56 | ['1.06', '2.00', '1.64']
w3.f11 |   | `almost visceral sense` | 3.62 | ['4.40', '-0.10', '-0.49']
w3.f12 | x | `theory of this` | 5.13 | ['4.37', '3.24', '-2.35']
w3.f13 |   | `set . .` | 4.32 | ['2.36', '-0.24', '2.45']
w3.f14 | x | `reggio 's theory` | 3.40 | ['0.73', '1.15', '1.61']
w3.f15 | x | `this imagery as` | 5.38 | ['2.58', '1.94', '1.03']
w3.f16 |   | `of this imagery` | 2.24 | ['1.87', '1.31', '-0.56']
w3.f17 | x | `up to mr` | 5.91 | ['2.46', '1.66', '1.95']
w3.f18 | x | `an almost visceral` | 3.58 | ['0.67', '-0.32', '3.70']
w3.f19 | x | `up to mr` | 5.76 | ['3.39', '0.71', '1.77']

## Original input: 
``` director claude chabrol has become the master of innuendo . it is not what you see , it is what you think you see . ``` 

## Marked input: 
<pre>director claude <span style="background-color: #FFFF00">@</span>chabrol <span style="background-color: #FFFF00">@</span>has <span style="background-color: #FFFF00">@</span>become <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>master <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>innuendo <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>it <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>not <span style="background-color: #6698FF">@</span>what <span style="background-color: #6698FF">@</span>you see , it is what you <span style="background-color: #FFFF00">@</span>think <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>you <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>see <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `claude chabrol` | 8.35 | ['4.41', '4.31']
w2.f1 |   | `@@PAD@@ director` | 2.08 | ['0.00', '2.21']
w2.f2 |   | `you see` | 0.24 | ['0.78', '0.51']
w2.f3 |   | `innuendo .` | 2.02 | ['2.63', '-0.05']
w2.f4 |   | `you see` | 2.29 | ['2.00', '0.48']
w2.f5 | x | `what you` | 3.90 | ['2.99', '1.22']
w2.f6 |   | `director claude` | 3.11 | ['1.58', '1.62']
w2.f7 | x | `innuendo .` | 3.29 | ['4.06', '0.14']
w2.f8 | x | `think you` | 4.08 | ['0.16', '4.14']
w2.f9 | x | `innuendo .` | 5.58 | ['5.13', '0.46']
w2.f10 | x | `you think` | 4.47 | ['4.16', '0.45']
w2.f11 | x | `of innuendo` | 4.44 | ['-0.32', '5.04']
w2.f12 |   | `director claude` | 2.89 | ['1.31', '1.62']
w2.f13 | x | `master of` | 4.19 | ['4.11', '0.24']
w2.f14 | x | `think you` | 4.24 | ['2.74', '1.52']
w2.f15 | x | `what you` | 8.27 | ['2.55', '5.99']
w2.f16 |   | `of innuendo` | 2.49 | ['0.18', '3.07']
w2.f17 | x | `innuendo .` | 3.28 | ['3.43', '0.47']
w2.f18 | x | `director claude` | 4.66 | ['3.48', '1.31']
w2.f19 |   | `you see` | 3.15 | ['0.48', '2.96']
w3.f0 | x | `master of innuendo` | 4.68 | ['1.20', '-1.37', '5.23']
w3.f1 |   | `become the master` | 2.94 | ['2.18', '-0.57', '1.71']
w3.f2 | x | `master of innuendo` | 4.38 | ['1.43', '-0.92', '3.96']
w3.f3 |   | `director claude chabrol` | 0.64 | ['-0.46', '0.10', '1.61']
w3.f4 | x | `director claude chabrol` | 5.02 | ['1.07', '2.60', '1.71']
w3.f5 |   | `is what you` | 4.51 | ['0.80', '3.49', '0.54']
w3.f6 | x | `you think you` | 3.72 | ['2.54', '-0.35', '1.75']
w3.f7 |   | `director claude chabrol` | 2.10 | ['-0.27', '1.09', '1.78']
w3.f8 | x | `think you see` | 7.25 | ['6.24', '-1.35', '2.65']
w3.f9 |   | `innuendo . it` | 2.79 | ['2.39', '0.58', '-0.07']
w3.f10 |   | `innuendo . it` | 3.23 | ['3.01', '2.00', '-1.64']
w3.f11 |   | `you see ,` | 2.61 | ['1.07', '1.54', '0.19']
w3.f12 | x | `it is not` | 5.13 | ['0.79', '1.47', '3.00']
w3.f13 | x | `become the master` | 7.13 | ['4.78', '-1.14', '3.74']
w3.f14 |   | `it is what` | 2.99 | ['0.08', '0.90', '2.11']
w3.f15 | x | `think you see` | 4.58 | ['1.27', '2.14', '1.34']
w3.f16 | x | `think you see` | 4.97 | ['1.74', '0.70', '2.91']
w3.f17 | x | `it is not` | 7.60 | ['1.06', '2.35', '4.34']
w3.f18 |   | `claude chabrol has` | 2.59 | ['1.23', '0.78', '1.04']
w3.f19 | x | `chabrol has become` | 4.23 | ['1.85', '2.09', '0.41']

## Original input: 
``` though it runs @@UNK@@ minutes , safe conduct is anything but @@UNK@@ . it 's packed to @@UNK@@ with incident , and with scores of characters , some fictional , some from history . ``` 

## Marked input: 
<pre>though it <span style="background-color: #6698FF">@</span>runs <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>minutes <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>safe <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>conduct <span style="background-color: #FFFF00">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>anything <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>but <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>. it 's <span style="background-color: #FFFF00">@</span>packed <span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>with <span style="background-color: #FFFF00">@</span>incident <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span>with scores <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>characters <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>some <span style="background-color: #6698FF">@</span>fictional <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>some <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>from <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>history <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `with scores` | 4.17 | ['3.44', '1.10']
w2.f1 | x | `@@UNK@@ with` | 3.86 | ['-0.88', '4.87']
w2.f2 |   | `, safe` | 0.11 | ['-0.83', '1.99']
w2.f3 | x | `@@UNK@@ minutes` | 3.50 | ['-0.08', '4.13']
w2.f4 | x | `safe conduct` | 10.51 | ['6.01', '4.69']
w2.f5 | x | `scores of` | 3.58 | ['2.13', '1.76']
w2.f6 | x | `with incident` | 5.63 | ['1.15', '4.58']
w2.f7 |   | `anything but` | 1.31 | ['1.71', '0.51']
w2.f8 | x | `@@UNK@@ with` | 3.49 | ['0.21', '3.50']
w2.f9 | x | `packed to` | 8.51 | ['3.85', '4.67']
w2.f10 | x | `'s packed` | 7.14 | ['2.75', '4.52']
w2.f11 | x | `anything but` | 4.58 | ['2.48', '2.37']
w2.f12 |   | `some fictional` | 2.77 | ['0.68', '2.13']
w2.f13 |   | `minutes ,` | 2.36 | ['0.32', '2.18']
w2.f14 | x | `incident ,` | 3.75 | ['2.90', '0.89']
w2.f15 | x | `'s packed` | 6.30 | ['1.82', '4.76']
w2.f16 | x | `is anything` | 3.33 | ['-0.10', '4.19']
w2.f17 |   | `'s packed` | 2.45 | ['0.09', '2.98']
w2.f18 | x | `with incident` | 5.27 | ['1.75', '3.63']
w2.f19 |   | `from history` | 3.13 | ['1.58', '1.84']
w3.f0 | x | `characters , some` | 3.93 | ['3.25', '-0.76', '1.83']
w3.f1 | x | `some from history` | 6.11 | ['1.19', '-0.77', '6.07']
w3.f2 | x | `though it runs` | 3.69 | ['0.39', '1.70', '1.69']
w3.f3 | x | `it 's packed` | 3.12 | ['-0.74', '-0.29', '4.76']
w3.f4 |   | `it 's packed` | 3.39 | ['-0.70', '2.08', '2.38']
w3.f5 | x | `safe conduct is` | 5.91 | ['3.76', '2.54', '-0.05']
w3.f6 | x | `characters , some` | 4.55 | ['1.82', '0.38', '2.56']
w3.f7 | x | `, some from` | 4.66 | ['1.70', '0.05', '3.40']
w3.f8 | x | `conduct is anything` | 7.45 | ['3.40', '4.71', '-0.38']
w3.f9 |   | `packed to @@UNK@@` | 3.44 | ['0.72', '0.70', '2.13']
w3.f10 | x | `is anything but` | 4.03 | ['-0.61', '1.78', '3.02']
w3.f11 | x | `conduct is anything` | 6.67 | ['1.92', '-0.19', '5.13']
w3.f12 |   | `characters , some` | 3.95 | ['0.52', '-0.15', '3.71']
w3.f13 | x | `some from history` | 5.39 | ['4.29', '-0.19', '1.53']
w3.f14 | x | `, some from` | 5.51 | ['-0.18', '3.18', '2.60']
w3.f15 | x | `@@UNK@@ minutes ,` | 5.59 | ['-0.51', '3.56', '2.70']
w3.f16 | x | `, safe conduct` | 5.05 | ['-0.14', '2.87', '2.69']
w3.f17 | x | `, some fictional` | 6.18 | ['0.73', '4.63', '0.97']
w3.f18 | x | `scores of characters` | 8.60 | ['2.76', '2.10', '4.21']
w3.f19 | x | `conduct is anything` | 6.46 | ['1.15', '3.62', '1.80']

## Original input: 
``` an instance of an old dog not only learning but @@UNK@@ a remarkable new trick . ``` 

## Marked input: 
<pre>an instance <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>an <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>old <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>dog <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>not <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>only <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>learning <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>but <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>remarkable <span style="background-color: #FFFF00">@</span>new <span style="background-color: #FFFF00">@</span>trick <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `old dog` | 2.50 | ['1.05', '1.83']
w2.f1 | x | `a remarkable` | 8.09 | ['2.95', '5.27']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `trick .` | 1.30 | ['1.91', '-0.05']
w2.f4 | x | `an old` | 8.29 | ['5.09', '3.39']
w2.f5 | x | `an instance` | 6.11 | ['3.50', '2.91']
w2.f6 |   | `new trick` | 1.51 | ['1.61', '-0.01']
w2.f7 |   | `dog not` | 1.55 | ['0.88', '1.58']
w2.f8 | x | `a remarkable` | 3.45 | ['0.88', '2.79']
w2.f9 |   | `instance of` | 2.86 | ['1.22', '1.65']
w2.f10 | x | `remarkable new` | 3.54 | ['4.84', '-1.17']
w2.f11 |   | `new trick` | 1.20 | ['0.05', '1.42']
w2.f12 |   | `but @@UNK@@` | 1.82 | ['1.63', '0.22']
w2.f13 | x | `only learning` | 5.76 | ['6.80', '-0.89']
w2.f14 | x | `not only` | 4.23 | ['-1.66', '5.93']
w2.f15 | x | `an instance` | 3.40 | ['0.76', '2.91']
w2.f16 |   | `old dog` | 1.96 | ['-1.04', '3.76']
w2.f17 | x | `trick .` | 4.11 | ['4.26', '0.47']
w2.f18 |   | `a remarkable` | 2.52 | ['0.76', '1.88']
w2.f19 | x | `remarkable new` | 3.63 | ['3.80', '0.13']
w3.f0 |   | `an old dog` | 2.01 | ['0.61', '0.05', '1.75']
w3.f1 |   | `@@PAD@@ an instance` | 3.39 | ['0.00', '1.98', '1.79']
w3.f2 | x | `old dog not` | 8.57 | ['2.89', '1.37', '4.40']
w3.f3 | x | `not only learning` | 2.57 | ['-0.65', '2.83', '1.00']
w3.f4 | x | `an old dog` | 3.94 | ['1.31', '1.01', '1.98']
w3.f5 |   | `an old dog` | 4.18 | ['0.97', '2.58', '0.95']
w3.f6 | x | `an old dog` | 6.11 | ['1.58', '0.94', '3.80']
w3.f7 |   | `an old dog` | 4.01 | ['2.46', '3.43', '-1.37']
w3.f8 | x | `a remarkable new` | 4.66 | ['0.66', '1.70', '2.59']
w3.f9 | x | `learning but @@UNK@@` | 4.05 | ['0.67', '1.36', '2.13']
w3.f10 | x | `trick . @@PAD@@` | 5.49 | ['3.63', '2.00', '0.00']
w3.f11 |   | `an old dog` | 3.54 | ['-0.26', '0.42', '3.58']
w3.f12 | x | `old dog not` | 5.33 | ['-0.72', '3.18', '3.00']
w3.f13 |   | `an instance of` | 3.41 | ['1.41', '-0.45', '2.71']
w3.f14 | x | `learning but @@UNK@@` | 4.12 | ['1.74', '3.83', '-1.37']
w3.f15 |   | `old dog not` | 2.23 | ['-0.15', '2.89', '-0.35']
w3.f16 |   | `@@PAD@@ an instance` | 2.48 | ['0.00', '0.18', '2.68']
w3.f17 | x | `an instance of` | 4.80 | ['3.05', '0.04', '1.87']
w3.f18 | x | `of an old` | 3.92 | ['-0.21', '0.28', '4.31']
w3.f19 | x | `remarkable new trick` | 5.08 | ['4.31', '0.45', '0.44']

## Original input: 
``` an overly melodramatic but somewhat insightful french coming - of - age film . . . ``` 

## Marked input: 
<pre>an <span style="background-color: #6698FF">@</span>overly <span style="background-color: #6698FF">@</span>melodramatic <span style="background-color: #6698FF">@</span>but <span style="background-color: #6698FF">@</span>somewhat <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>insightful <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>french <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>coming <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span>age film <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `french coming` | 4.86 | ['6.06', '-0.82']
w2.f1 | x | `somewhat insightful` | 7.14 | ['1.27', '6.00']
w2.f2 |   | `age film` | 0.27 | ['0.49', '0.83']
w2.f3 |   | `melodramatic but` | 1.76 | ['0.79', '1.53']
w2.f4 | x | `insightful french` | 8.52 | ['5.09', '3.63']
w2.f5 | x | `french coming` | 3.79 | ['2.29', '1.80']
w2.f6 |   | `insightful french` | 2.30 | ['0.15', '2.24']
w2.f7 |   | `an overly` | 1.58 | ['0.98', '1.51']
w2.f8 |   | `coming -` | 2.47 | ['0.84', '1.85']
w2.f9 |   | `coming -` | 2.90 | ['2.45', '0.46']
w2.f10 | x | `insightful french` | 6.10 | ['2.40', '3.83']
w2.f11 | x | `melodramatic but` | 3.16 | ['1.06', '2.37']
w2.f12 |   | `but somewhat` | 2.43 | ['1.63', '0.83']
w2.f13 |   | `an overly` | 2.12 | ['1.17', '1.10']
w2.f14 | x | `french coming` | 8.38 | ['2.43', '5.99']
w2.f15 | x | `but somewhat` | 5.01 | ['2.02', '3.26']
w2.f16 | x | `insightful french` | 3.17 | ['-0.95', '4.88']
w2.f17 | x | `insightful french` | 4.10 | ['3.31', '1.40']
w2.f18 |   | `age film` | 1.69 | ['0.86', '0.95']
w2.f19 | x | `somewhat insightful` | 4.20 | ['3.98', '0.52']
w3.f0 | x | `an overly melodramatic` | 8.54 | ['0.61', '3.25', '5.08']
w3.f1 | x | `somewhat insightful french` | 4.47 | ['1.17', '3.48', '0.21']
w3.f2 | x | `@@PAD@@ an overly` | 4.95 | ['0.00', '1.76', '3.28']
w3.f3 | x | `insightful french coming` | 3.02 | ['2.00', '0.61', '1.01']
w3.f4 |   | `insightful french coming` | 1.15 | ['0.68', '0.79', '0.04']
w3.f5 | x | `insightful french coming` | 6.17 | ['-0.13', '2.46', '4.16']
w3.f6 |   | `overly melodramatic but` | 2.52 | ['2.14', '-1.04', '1.64']
w3.f7 | x | `age film .` | 4.67 | ['2.47', '2.52', '0.18']
w3.f8 | x | `somewhat insightful french` | 8.32 | ['3.75', '1.66', '3.19']
w3.f9 | x | `melodramatic but somewhat` | 4.30 | ['2.83', '1.36', '0.22']
w3.f10 | x | `overly melodramatic but` | 9.31 | ['5.26', '1.18', '3.02']
w3.f11 | x | `an overly melodramatic` | 4.43 | ['-0.26', '2.68', '2.20']
w3.f12 |   | `an overly melodramatic` | 3.92 | ['-0.83', '3.96', '0.91']
w3.f13 |   | `but somewhat insightful` | 4.85 | ['1.09', '2.90', '1.11']
w3.f14 | x | `an overly melodramatic` | 5.46 | ['1.08', '3.78', '0.69']
w3.f15 |   | `coming - of` | 2.93 | ['1.45', '-0.37', '2.01']
w3.f16 |   | `insightful french coming` | 2.66 | ['0.15', '0.35', '2.54']
w3.f17 | x | `melodramatic but somewhat` | 4.84 | ['2.20', '2.96', '-0.17']
w3.f18 | x | `french coming -` | 3.64 | ['4.86', '0.68', '-1.43']
w3.f19 | x | `coming - of` | 9.50 | ['5.47', '1.48', '2.66']

## Original input: 
``` the film is a very good viewing alternative for young women . ``` 

## Marked input: 
<pre>the film <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>very <span style="background-color: #FFFF00">@</span>good <span style="background-color: #FFFF00">@</span>viewing <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>alternative <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>for <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>young <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>women <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `for young` | 2.12 | ['1.57', '0.93']
w2.f1 |   | `young women` | 2.40 | ['0.93', '1.60']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `very good` | 0.12 | ['2.65', '-1.97']
w2.f4 | x | `for young` | 4.09 | ['0.66', '3.62']
w2.f5 |   | `the film` | 1.83 | ['1.16', '0.98']
w2.f6 |   | `women .` | 1.47 | ['2.94', '-1.38']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `viewing alternative` | 1.58 | ['0.48', '1.31']
w2.f9 |   | `a very` | 2.36 | ['-0.54', '2.91']
w2.f10 |   | `a very` | 2.30 | ['1.97', '0.47']
w2.f11 |   | `viewing alternative` | 2.66 | ['0.34', '2.59']
w2.f12 |   | `viewing alternative` | 1.48 | ['1.04', '0.47']
w2.f13 | x | `alternative for` | 4.50 | ['1.87', '2.78']
w2.f14 |   | `good viewing` | 2.17 | ['0.44', '1.77']
w2.f15 |   | `the film` | 1.19 | ['-0.42', '1.88']
w2.f16 |   | `good viewing` | 2.35 | ['2.10', '1.02']
w2.f17 |   | `viewing alternative` | 0.18 | ['0.60', '0.20']
w2.f18 | x | `a very` | 5.53 | ['0.76', '4.89']
w2.f19 | x | `a very` | 3.67 | ['0.99', '2.97']
w3.f0 |   | `young women .` | 3.05 | ['3.95', '-0.88', '0.37']
w3.f1 |   | `women . @@PAD@@` | 1.93 | ['2.66', '-0.35', '0.00']
w3.f2 | x | `good viewing alternative` | 3.76 | ['-1.12', '2.39', '2.58']
w3.f3 | x | `a very good` | 3.07 | ['-0.28', '1.66', '2.29']
w3.f4 | x | `for young women` | 3.50 | ['1.21', '0.87', '1.78']
w3.f5 |   | `good viewing alternative` | 2.52 | ['0.93', '1.49', '0.43']
w3.f6 |   | `a very good` | 3.14 | ['1.76', '1.59', '-0.00']
w3.f7 |   | `for young women` | 2.46 | ['1.19', '0.94', '0.82']
w3.f8 |   | `film is a` | 3.83 | ['-0.14', '4.71', '-0.46']
w3.f9 | x | `good viewing alternative` | 4.06 | ['0.16', '4.06', '-0.05']
w3.f10 | x | `women . @@PAD@@` | 4.20 | ['2.34', '2.00', '0.00']
w3.f11 |   | `is a very` | 1.54 | ['0.29', '0.22', '1.23']
w3.f12 | x | `the film is` | 4.65 | ['2.43', '0.53', '1.82']
w3.f13 |   | `film is a` | 3.16 | ['0.42', '2.81', '0.18']
w3.f14 |   | `good viewing alternative` | 2.44 | ['1.47', '-0.16', '1.22']
w3.f15 |   | `a very good` | 1.72 | ['-2.48', '4.81', '-0.44']
w3.f16 |   | `alternative for young` | 1.30 | ['-2.36', '3.80', '0.24']
w3.f17 | x | `alternative for young` | 8.39 | ['0.99', '5.11', '2.44']
w3.f18 | x | `very good viewing` | 3.76 | ['1.40', '0.40', '2.43']
w3.f19 | x | `alternative for young` | 4.72 | ['0.30', '2.83', '1.70']

## Original input: 
``` true to its title , it @@UNK@@ audiences in a series of relentlessly nasty situations that we would pay a considerable @@UNK@@ not to be looking at . ``` 

## Marked input: 
<pre>true to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>its <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>title <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>it <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>audiences <span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>series <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>relentlessly nasty <span style="background-color: #6698FF">@</span>situations <span style="background-color: #6698FF">@</span>that <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>we <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>would <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>pay <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>considerable <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>not <span style="background-color: #FFFF00">@</span>to be looking <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>at <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `true to` | 5.33 | ['6.15', '-0.45']
w2.f1 | x | `would pay` | 4.35 | ['0.82', '3.67']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `title ,` | 4.27 | ['4.39', '0.44']
w2.f4 | x | `title ,` | 3.90 | ['1.59', '2.50']
w2.f5 |   | `we would` | 3.07 | ['4.53', '-1.15']
w2.f6 | x | `its title` | 4.23 | ['0.58', '3.75']
w2.f7 | x | `nasty situations` | 2.81 | ['2.19', '1.53']
w2.f8 | x | `a considerable` | 3.73 | ['0.88', '3.06']
w2.f9 | x | `be looking` | 5.70 | ['3.56', '2.15']
w2.f10 |   | `a series` | 2.55 | ['1.97', '0.72']
w2.f11 | x | `nasty situations` | 8.08 | ['6.38', '1.97']
w2.f12 | x | `nasty situations` | 6.28 | ['3.38', '2.93']
w2.f13 | x | `looking at` | 6.10 | ['5.06', '1.19']
w2.f14 | x | `nasty situations` | 5.13 | ['5.17', '-0.01']
w2.f15 |   | `a considerable` | 3.25 | ['-2.48', '6.00']
w2.f16 | x | `relentlessly nasty` | 5.08 | ['3.22', '2.63']
w2.f17 |   | `situations that` | 1.97 | ['4.96', '-2.38']
w2.f18 | x | `that we` | 3.54 | ['2.33', '1.33']
w2.f19 |   | `not to` | 1.42 | ['0.59', '1.12']
w3.f0 | x | `in a series` | 4.41 | ['-0.14', '3.29', '1.65']
w3.f1 | x | `at . @@PAD@@` | 6.66 | ['7.39', '-0.35', '0.00']
w3.f2 | x | `its title ,` | 5.70 | ['1.61', '2.85', '1.32']
w3.f3 | x | `be looking at` | 3.23 | ['-0.20', '1.39', '2.65']
w3.f4 |   | `@@PAD@@ @@PAD@@ true` | 1.83 | ['0.00', '0.00', '2.19']
w3.f5 | x | `situations that we` | 5.07 | ['-0.34', '-0.14', '5.88']
w3.f6 | x | `@@UNK@@ audiences in` | 4.32 | ['-0.28', '4.67', '0.14']
w3.f7 | x | `true to its` | 5.04 | ['-0.22', '1.18', '4.59']
w3.f8 |   | `that we would` | 3.06 | ['3.58', '-1.13', '0.90']
w3.f9 | x | `true to its` | 5.71 | ['1.81', '0.70', '3.30']
w3.f10 |   | `at . @@PAD@@` | 2.36 | ['0.51', '2.00', '0.00']
w3.f11 |   | `nasty situations that` | 2.63 | ['1.39', '2.92', '-1.49']
w3.f12 | x | `situations that we` | 11.91 | ['6.04', '0.13', '5.88']
w3.f13 |   | `a series of` | 4.78 | ['-2.81', '5.12', '2.71']
w3.f14 |   | `series of relentlessly` | 1.06 | ['-0.06', '-2.13', '3.34']
w3.f15 |   | `true to its` | 3.02 | ['3.52', '-0.50', '0.17']
w3.f16 | x | `title , it` | 3.95 | ['-1.31', '3.78', '1.86']
w3.f17 | x | `relentlessly nasty situations` | 7.10 | ['3.99', '-1.28', '4.55']
w3.f18 |   | `@@PAD@@ true to` | 1.80 | ['0.00', '0.75', '1.52']
w3.f19 | x | `a considerable @@UNK@@` | 5.32 | ['3.70', '3.75', '-2.02']

## Original input: 
``` a @@UNK@@ whose pieces do not fit . some are fascinating and others are not , and in the end , it is almost a good movie . ``` 

## Marked input: 
<pre>a @@UNK@@ whose pieces <span style="background-color: #FFFF00">@</span>do <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>not <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>fit <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>some <span style="background-color: #6698FF">@</span>are <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>fascinating <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>others <span style="background-color: #FFFF00">@</span>are <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>not <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>and in the end , <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>it <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span>almost <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>good <span style="background-color: #FFFF00">@</span>movie <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `others are` | 2.91 | ['1.59', '1.69']
w2.f1 | x | `are fascinating` | 5.31 | ['0.74', '4.70']
w2.f2 |   | `is almost` | 0.11 | ['-0.22', '1.37']
w2.f3 |   | `. some` | 1.40 | ['0.52', '1.43']
w2.f4 |   | `movie .` | 3.09 | ['3.31', '-0.03']
w2.f5 |   | `pieces do` | 2.47 | ['3.46', '-0.68']
w2.f6 |   | `end ,` | 3.46 | ['-0.37', '3.93']
w2.f7 |   | `do not` | 1.98 | ['1.31', '1.58']
w2.f8 | x | `almost a` | 3.37 | ['1.03', '2.56']
w2.f9 |   | `@@UNK@@ whose` | 3.91 | ['2.38', '1.54']
w2.f10 | x | `a good` | 4.90 | ['1.97', '3.06']
w2.f11 | x | `. some` | 3.04 | ['-0.51', '3.82']
w2.f12 |   | `some are` | 3.21 | ['0.68', '2.57']
w2.f13 | x | `end ,` | 5.70 | ['3.66', '2.18']
w2.f14 |   | `good movie` | 1.06 | ['0.44', '0.66']
w2.f15 |   | `is almost` | 3.13 | ['1.15', '2.25']
w2.f16 | x | `pieces do` | 3.40 | ['1.56', '2.60']
w2.f17 | x | `do not` | 3.73 | ['1.76', '2.58']
w2.f18 | x | `and others` | 4.19 | ['3.52', '0.79']
w2.f19 | x | `a good` | 4.54 | ['0.99', '3.85']
w3.f0 |   | `do not fit` | 3.35 | ['2.17', '-0.63', '2.20']
w3.f1 |   | `some are fascinating` | 2.89 | ['1.19', '-1.91', '3.99']
w3.f2 | x | `pieces do not` | 7.22 | ['1.50', '1.41', '4.40']
w3.f3 |   | `in the end` | 0.93 | ['1.23', '-0.66', '0.97']
w3.f4 |   | `@@UNK@@ whose pieces` | 3.06 | ['0.36', '2.65', '0.42']
w3.f5 | x | `are fascinating and` | 7.55 | ['0.98', '1.08', '5.81']
w3.f6 | x | `do not fit` | 4.94 | ['1.05', '1.86', '2.24']
w3.f7 |   | `the end ,` | 1.21 | ['-1.23', '1.75', '1.18']
w3.f8 | x | `it is almost` | 5.98 | ['2.11', '4.71', '-0.55']
w3.f9 |   | `in the end` | 2.73 | ['1.57', '-0.12', '1.39']
w3.f10 | x | `. some are` | 5.37 | ['0.09', '1.64', '3.78']
w3.f11 |   | `almost a good` | 3.54 | ['4.40', '0.22', '-0.88']
w3.f12 | x | `fit . some` | 5.11 | ['2.09', '-0.56', '3.71']
w3.f13 | x | `some are fascinating` | 8.34 | ['4.29', '2.28', '2.01']
w3.f14 | x | `fit . some` | 4.76 | ['1.33', '-0.66', '4.18']
w3.f15 |   | `the end ,` | 3.29 | ['-0.02', '0.78', '2.70']
w3.f16 | x | `end , it` | 4.11 | ['-1.15', '3.78', '1.86']
w3.f17 | x | `others are not` | 6.96 | ['1.24', '1.54', '4.34']
w3.f18 | x | `whose pieces do` | 4.32 | ['0.63', '1.71', '2.45']
w3.f19 | x | `and others are` | 8.66 | ['3.50', '1.08', '4.20']

## Original input: 
``` when a film is created @@UNK@@ because it 's a @@UNK@@ product , soulless and ugly movies like this are the result . let your silly childhood nostalgia @@UNK@@ @@UNK@@ . ``` 

## Marked input: 
<pre>when a film is <span style="background-color: #FFFF00">@</span>created <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>because <span style="background-color: #FFFF00">@</span>it <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>a @@UNK@@ <span style="background-color: #6698FF">@</span>product <span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>soulless <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>ugly <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>movies <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>like <span style="background-color: #FFFF00">@</span>this <span style="background-color: #FFFF00">@</span>are <span style="background-color: #FFFF00">@</span>the result <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>let <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>your <span style="background-color: #6698FF">@</span>silly <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>childhood <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>nostalgia <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ .</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `because it` | 4.86 | ['3.57', '1.67']
w2.f1 |   | `a film` | 2.24 | ['2.95', '-0.58']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `@@UNK@@ product` | 4.42 | ['-0.08', '5.05']
w2.f4 | x | `product ,` | 4.51 | ['2.19', '2.50']
w2.f5 | x | `like this` | 3.94 | ['3.40', '0.85']
w2.f6 | x | `because it` | 4.10 | ['3.79', '0.41']
w2.f7 | x | `let your` | 3.71 | ['1.07', '3.55']
w2.f8 | x | `created @@UNK@@` | 3.70 | ['4.62', '-0.71']
w2.f9 |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 |   | `'s a` | 2.81 | ['2.75', '0.20']
w2.f11 | x | `your silly` | 3.26 | ['1.68', '1.85']
w2.f12 | x | `. let` | 6.84 | ['-0.60', '7.48']
w2.f13 | x | `soulless and` | 4.57 | ['4.15', '0.57']
w2.f14 | x | `@@UNK@@ product` | 4.15 | ['0.69', '3.49']
w2.f15 | x | `is created` | 5.97 | ['1.15', '5.09']
w2.f16 | x | `childhood nostalgia` | 4.97 | ['1.12', '4.61']
w2.f17 | x | `childhood nostalgia` | 6.42 | ['2.58', '4.45']
w2.f18 | x | `and ugly` | 4.85 | ['3.52', '1.46']
w2.f19 | x | `and ugly` | 3.62 | ['3.66', '0.26']
w3.f0 | x | `product , soulless` | 5.42 | ['4.70', '-0.76', '1.87']
w3.f1 |   | `created @@UNK@@ because` | 3.07 | ['5.23', '-0.73', '-1.06']
w3.f2 | x | `. let your` | 4.46 | ['0.04', '4.13', '0.38']
w3.f3 | x | `created @@UNK@@ because` | 3.55 | ['2.75', '-0.06', '1.46']
w3.f4 |   | `ugly movies like` | 2.46 | ['-1.96', '1.55', '3.23']
w3.f5 |   | `let your silly` | 3.37 | ['-1.12', '0.73', '4.09']
w3.f6 | x | `a @@UNK@@ product` | 4.26 | ['1.76', '-1.80', '4.51']
w3.f7 | x | `, soulless and` | 4.44 | ['1.70', '1.40', '1.83']
w3.f8 | x | `film is created` | 9.69 | ['-0.14', '4.71', '5.41']
w3.f9 | x | `, soulless and` | 7.62 | ['-2.20', '7.53', '2.40']
w3.f10 | x | `product , soulless` | 6.34 | ['3.59', '-0.41', '3.30']
w3.f11 | x | `product , soulless` | 4.20 | ['3.36', '-1.36', '2.39']
w3.f12 | x | `let your silly` | 6.09 | ['2.64', '0.75', '2.83']
w3.f13 | x | `the result .` | 5.72 | ['4.70', '-1.17', '2.45']
w3.f14 | x | `soulless and ugly` | 4.82 | ['2.10', '1.09', '1.73']
w3.f15 | x | `@@UNK@@ product ,` | 6.66 | ['-0.51', '4.64', '2.70']
w3.f16 |   | `film is created` | 2.34 | ['-1.17', '-0.75', '4.63']
w3.f17 | x | `let your silly` | 5.83 | ['1.65', '-0.86', '5.19']
w3.f18 | x | `your silly childhood` | 5.34 | ['2.20', '0.95', '2.66']
w3.f19 | x | `movies like this` | 7.53 | ['1.76', '3.53', '2.36']

## Original input: 
``` @@UNK@@ 's @@UNK@@ could have used some @@UNK@@ , adult @@UNK@@ . ``` 

## Marked input: 
<pre>@@UNK@@ 's <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>could have <span style="background-color: #6698FF">@</span>used <span style="background-color: #6698FF">@</span>some <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>, adult @@UNK@@ .</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ 's` | 2.28 | ['1.98', '0.68']
w2.f1 |   | `@@UNK@@ 's` | 0.55 | ['-0.88', '1.57']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `could have` | 2.48 | ['-0.74', '3.78']
w2.f4 |   | `@@UNK@@ ,` | 1.12 | ['-1.19', '2.50']
w2.f5 |   | `used some` | 2.72 | ['2.70', '0.32']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 | x | `@@UNK@@ 's` | 3.81 | ['0.21', '3.82']
w2.f9 |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 |   | `have used` | 1.87 | ['0.00', '2.00']
w2.f11 | x | `used some` | 3.31 | ['-0.24', '3.82']
w2.f12 | x | `could have` | 4.48 | ['2.33', '2.18']
w2.f13 |   | `@@UNK@@ could` | 3.10 | ['0.61', '2.64']
w2.f14 |   | `@@UNK@@ ,` | 1.54 | ['0.69', '0.89']
w2.f15 |   | `have used` | 0.86 | ['1.21', '-0.08']
w2.f16 |   | `used some` | 1.30 | ['-0.25', '2.31']
w2.f17 | x | `used some` | 4.36 | ['0.78', '4.19']
w2.f18 |   | `, adult` | 1.94 | ['-1.54', '3.60']
w2.f19 |   | `, adult` | 2.12 | ['-0.70', '3.12']
w3.f0 |   | `have used some` | 1.31 | ['-0.13', '0.01', '1.83']
w3.f1 |   | `could have used` | 2.55 | ['2.18', '1.97', '-1.22']
w3.f2 |   | `used some @@UNK@@` | 2.40 | ['1.91', '0.89', '-0.31']
w3.f3 |   | `@@PAD@@ @@PAD@@ @@UNK@@` | 0.00 | ['0.00', '0.00', '0.07']
w3.f4 |   | `@@UNK@@ , adult` | 0.56 | ['0.36', '0.77', '-0.21']
w3.f5 |   | `@@UNK@@ , adult` | 0.44 | ['0.08', '1.40', '-0.71']
w3.f6 | x | `have used some` | 4.72 | ['0.69', '1.67', '2.56']
w3.f7 |   | `, adult @@UNK@@` | 0.14 | ['1.70', '-0.99', '-0.07']
w3.f8 |   | `@@UNK@@ could have` | 4.25 | ['0.50', '1.91', '2.12']
w3.f9 |   | `@@PAD@@ @@PAD@@ @@UNK@@` | 2.03 | ['0.00', '0.00', '2.13']
w3.f10 |   | `used some @@UNK@@` | 3.64 | ['1.28', '1.64', '0.86']
w3.f11 | x | `could have used` | 4.21 | ['1.00', '2.99', '0.41']
w3.f12 | x | `have used some` | 4.83 | ['-0.39', '1.63', '3.71']
w3.f13 |   | `some @@UNK@@ ,` | 2.27 | ['4.29', '-1.74', '-0.03']
w3.f14 |   | `used some @@UNK@@` | 1.96 | ['0.23', '3.18', '-1.37']
w3.f15 |   | `could have used` | 1.16 | ['0.49', '-0.33', '1.17']
w3.f16 |   | `'s @@UNK@@ could` | 1.53 | ['2.11', '-0.81', '0.61']
w3.f17 | x | `could have used` | 6.20 | ['2.57', '3.75', '0.04']
w3.f18 |   | `some @@UNK@@ ,` | 0.44 | ['0.56', '-0.45', '0.79']
w3.f19 |   | `@@UNK@@ , adult` | 1.12 | ['-0.26', '1.68', '-0.19']

## Original input: 
``` this time mr . burns is trying something in the martin scorsese street - @@UNK@@ @@UNK@@ , but his self - regarding sentimentality @@UNK@@ him up again . ``` 

## Marked input: 
<pre>this time <span style="background-color: #FFFF00">@</span>mr <span style="background-color: #FFFF00">@</span>. burns <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>trying <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>something <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>the martin <span style="background-color: #6698FF">@</span>scorsese <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>street <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>- <span style="background-color: #FFFF00">@</span>@@UNK@@ @@UNK@@ , but his <span style="background-color: #FFFF00">@</span>self <span style="background-color: #FFFF00">@</span>- regarding <span style="background-color: #6698FF">@</span>sentimentality <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>him <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>up <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>again <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `time mr` | 2.80 | ['1.50', '1.68']
w2.f1 | x | `but his` | 4.15 | ['4.31', '-0.03']
w2.f2 |   | `him up` | 0.85 | ['0.30', '1.59']
w2.f3 | x | `is trying` | 2.52 | ['0.28', '2.79']
w2.f4 | x | `up again` | 3.74 | ['0.08', '3.85']
w2.f5 | x | `burns is` | 3.51 | ['4.78', '-0.97']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `him up` | 0.81 | ['0.69', '1.03']
w2.f8 |   | `street -` | 2.77 | ['1.13', '1.85']
w2.f9 | x | `@@UNK@@ him` | 5.57 | ['2.38', '3.20']
w2.f10 | x | `him up` | 7.56 | ['0.76', '6.94']
w2.f11 |   | `time mr` | 2.60 | ['2.35', '0.52']
w2.f12 | x | `trying something` | 7.19 | ['1.41', '5.82']
w2.f13 | x | `. burns` | 5.15 | ['0.44', '4.86']
w2.f14 | x | `again .` | 5.62 | ['5.26', '0.39']
w2.f15 | x | `this time` | 3.97 | ['3.03', '1.21']
w2.f16 | x | `regarding sentimentality` | 3.08 | ['1.46', '2.38']
w2.f17 |   | `sentimentality @@UNK@@` | 1.54 | ['3.25', '-1.09']
w2.f18 | x | `. burns` | 5.01 | ['0.99', '4.15']
w2.f19 |   | `@@UNK@@ him` | 3.09 | ['0.39', '2.99']
w3.f0 | x | `up again .` | 6.66 | ['5.35', '1.33', '0.37']
w3.f1 |   | `scorsese street -` | 2.91 | ['2.37', '-0.73', '1.66']
w3.f2 | x | `- regarding sentimentality` | 5.54 | ['2.02', '-0.31', '3.92']
w3.f3 |   | `. burns is` | 0.74 | ['-1.15', '3.50', '-1.00']
w3.f4 | x | `@@UNK@@ him up` | 3.75 | ['0.36', '1.69', '2.06']
w3.f5 | x | `up again .` | 6.45 | ['1.50', '0.96', '4.32']
w3.f6 |   | `is trying something` | 3.18 | ['-0.04', '1.89', '1.53']
w3.f7 |   | `up again .` | 2.15 | ['-0.07', '2.54', '0.18']
w3.f8 | x | `burns is trying` | 5.45 | ['-0.16', '4.71', '1.19']
w3.f9 | x | `the martin scorsese` | 3.79 | ['-3.85', '5.23', '2.52']
w3.f10 |   | `- regarding sentimentality` | 3.62 | ['-0.37', '1.86', '2.28']
w3.f11 | x | `. burns is` | 3.85 | ['-0.15', '3.05', '1.14']
w3.f12 |   | `the martin scorsese` | 3.85 | ['2.43', '0.31', '1.24']
w3.f13 |   | `up again .` | 5.01 | ['-2.44', '5.25', '2.45']
w3.f14 |   | `mr . burns` | 2.44 | ['-1.67', '-0.66', '4.87']
w3.f15 | x | `him up again` | 5.72 | ['3.04', '0.47', '2.37']
w3.f16 |   | `. burns is` | 1.93 | ['-0.12', '3.73', '-1.30']
w3.f17 | x | `sentimentality @@UNK@@ him` | 6.88 | ['3.80', '1.39', '1.86']
w3.f18 |   | `@@PAD@@ this time` | 1.39 | ['0.00', '-0.54', '2.39']
w3.f19 | x | `martin scorsese street` | 4.74 | ['-0.57', '2.71', '2.71']

## Original input: 
``` though there are entertaining and audacious moments , the movie 's wildly @@UNK@@ tone and an extremely flat lead performance do little to @@UNK@@ this filmmaker 's flailing reputation . ``` 

## Marked input: 
<pre>though there <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>are <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>entertaining <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>audacious <span style="background-color: #FFFF00">@</span>moments <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>movie <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span>wildly <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>tone and an <span style="background-color: #6698FF">@</span>extremely <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>flat <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>lead <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>performance <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>do <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>little <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>@@UNK@@ this filmmaker <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>flailing <span style="background-color: #FFFF00">@</span>reputation <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `flat lead` | 3.32 | ['-0.70', '4.40']
w2.f1 | x | `flailing reputation` | 6.03 | ['4.77', '1.39']
w2.f2 |   | `performance do` | 0.68 | ['0.96', '0.77']
w2.f3 | x | `flat lead` | 2.98 | ['1.55', '1.99']
w2.f4 | x | `an extremely` | 6.27 | ['5.09', '1.37']
w2.f5 | x | `this filmmaker` | 4.72 | ['2.84', '2.18']
w2.f6 |   | `moments ,` | 2.41 | ['-1.42', '3.93']
w2.f7 | x | `flat lead` | 3.82 | ['2.43', '2.30']
w2.f8 | x | `lead performance` | 5.18 | ['3.26', '2.14']
w2.f9 |   | `@@UNK@@ tone` | 4.74 | ['2.38', '2.38']
w2.f10 | x | `an extremely` | 4.54 | ['1.91', '2.76']
w2.f11 | x | `extremely flat` | 8.51 | ['2.04', '6.74']
w2.f12 | x | `do little` | 3.92 | ['0.96', '2.99']
w2.f13 | x | `lead performance` | 4.21 | ['3.29', '1.06']
w2.f14 | x | `flat lead` | 4.35 | ['3.69', '0.69']
w2.f15 | x | `lead performance` | 6.55 | ['1.58', '5.25']
w2.f16 | x | `extremely flat` | 8.73 | ['1.83', '7.67']
w2.f17 | x | `flailing reputation` | 6.41 | ['4.34', '2.69']
w2.f18 | x | `this filmmaker` | 4.77 | ['0.16', '4.73']
w2.f19 | x | `this filmmaker` | 4.50 | ['1.58', '3.23']
w3.f0 |   | `flailing reputation .` | 3.40 | ['4.70', '-1.28', '0.37']
w3.f1 | x | `are entertaining and` | 3.84 | ['1.91', '2.47', '-0.17']
w3.f2 | x | `, the movie` | 7.38 | ['2.60', '0.94', '3.93']
w3.f3 |   | `@@UNK@@ this filmmaker` | 0.73 | ['-1.16', '-0.20', '2.69']
w3.f4 | x | `flat lead performance` | 6.25 | ['1.63', '2.33', '2.65']
w3.f5 | x | `flailing reputation .` | 7.38 | ['0.55', '2.83', '4.32']
w3.f6 | x | `an extremely flat` | 8.05 | ['1.58', '1.83', '4.85']
w3.f7 |   | `this filmmaker 's` | 2.02 | ['-0.63', '3.24', '-0.10']
w3.f8 |   | `and audacious moments` | 4.18 | ['2.47', '1.06', '0.93']
w3.f9 | x | `and an extremely` | 4.12 | ['-2.57', '3.18', '3.63']
w3.f10 | x | `though there are` | 6.03 | ['0.73', '1.67', '3.78']
w3.f11 | x | `movie 's wildly` | 5.13 | ['-0.17', '0.46', '5.03']
w3.f12 | x | `lead performance do` | 4.18 | ['2.13', '0.20', '1.98']
w3.f13 | x | `audacious moments ,` | 5.82 | ['0.80', '5.30', '-0.03']
w3.f14 | x | `an extremely flat` | 10.26 | ['1.08', '3.16', '6.11']
w3.f15 |   | `performance do little` | 2.51 | ['2.48', '-0.20', '0.39']
w3.f16 | x | `entertaining and audacious` | 8.60 | ['4.76', '-0.30', '4.53']
w3.f17 | x | `moments , the` | 6.70 | ['2.26', '3.34', '1.25']
w3.f18 | x | `filmmaker 's flailing` | 5.19 | ['2.17', '0.79', '2.70']
w3.f19 | x | `though there are` | 4.67 | ['2.26', '-1.66', '4.20']

## Original input: 
``` as a hybrid teen thriller and murder mystery , murder by numbers fits the profile too closely . ``` 

## Marked input: 
<pre>as a <span style="background-color: #6698FF">@</span>hybrid <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>teen <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>thriller <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>murder <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>mystery <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span>murder <span style="background-color: #6698FF">@</span>by <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>numbers <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>fits <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span>profile <span style="background-color: #FFFF00">@</span>too <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>closely <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `too closely` | 3.29 | ['-0.57', '4.24']
w2.f1 |   | `thriller and` | 1.74 | ['2.36', '-0.48']
w2.f2 |   | `murder mystery` | 0.06 | ['0.46', '0.65']
w2.f3 | x | `profile too` | 2.44 | ['-1.09', '4.09']
w2.f4 | x | `a hybrid` | 5.46 | ['2.27', '3.38']
w2.f5 | x | `fits the` | 3.91 | ['4.45', '-0.23']
w2.f6 |   | `hybrid teen` | 3.93 | ['1.43', '2.59']
w2.f7 | x | `teen thriller` | 2.86 | ['2.25', '1.52']
w2.f8 | x | `hybrid teen` | 4.18 | ['1.98', '2.41']
w2.f9 |   | `by numbers` | 3.40 | ['0.85', '2.56']
w2.f10 | x | `the profile` | 6.73 | ['-1.39', '8.25']
w2.f11 | x | `too closely` | 4.98 | ['3.88', '1.37']
w2.f12 | x | `murder by` | 5.81 | ['2.14', '3.71']
w2.f13 | x | `thriller and` | 3.31 | ['2.89', '0.57']
w2.f14 | x | `by numbers` | 8.53 | ['0.78', '7.79']
w2.f15 | x | `numbers fits` | 3.67 | ['2.82', '1.13']
w2.f16 | x | `too closely` | 4.18 | ['2.26', '2.68']
w2.f17 | x | `hybrid teen` | 3.47 | ['3.40', '0.69']
w2.f18 | x | `and murder` | 4.91 | ['3.52', '1.52']
w2.f19 | x | `and murder` | 4.78 | ['3.66', '1.41']
w3.f0 | x | `as a hybrid` | 5.05 | ['-2.34', '3.29', '4.49']
w3.f1 | x | `hybrid teen thriller` | 4.52 | ['2.52', '1.10', '1.27']
w3.f2 | x | `a hybrid teen` | 4.10 | ['1.87', '1.86', '0.46']
w3.f3 |   | `profile too closely` | 0.57 | ['1.02', '-0.10', '0.25']
w3.f4 |   | `too closely .` | 3.26 | ['3.10', '1.04', '-0.52']
w3.f5 | x | `teen thriller and` | 7.69 | ['0.97', '1.24', '5.81']
w3.f6 | x | `teen thriller and` | 4.43 | ['1.38', '2.32', '0.95']
w3.f7 | x | `murder by numbers` | 4.83 | ['1.09', '1.28', '2.97']
w3.f8 |   | `murder mystery ,` | 3.09 | ['1.71', '-0.47', '2.14']
w3.f9 | x | `teen thriller and` | 4.32 | ['1.17', '0.85', '2.40']
w3.f10 | x | `closely . @@PAD@@` | 4.14 | ['2.28', '2.00', '0.00']
w3.f11 | x | `murder mystery ,` | 6.91 | ['4.15', '2.76', '0.19']
w3.f12 | x | `mystery , murder` | 6.81 | ['3.73', '-0.15', '3.36']
w3.f13 | x | `the profile too` | 5.93 | ['4.70', '4.20', '-2.72']
w3.f14 | x | `murder by numbers` | 9.79 | ['4.58', '2.00', '3.30']
w3.f15 | x | `murder mystery ,` | 4.73 | ['1.28', '0.92', '2.70']
w3.f16 | x | `fits the profile` | 6.29 | ['1.61', '0.10', '4.96']
w3.f17 | x | `murder by numbers` | 4.43 | ['2.11', '1.35', '1.13']
w3.f18 | x | `fits the profile` | 3.55 | ['2.82', '-0.59', '1.78']
w3.f19 | x | `a hybrid teen` | 9.18 | ['3.70', '2.08', '3.52']

## Original input: 
``` every potential twist is telegraphed well in advance , every performance @@UNK@@ muted ; the movie itself seems to have been made under the influence of @@UNK@@ . ``` 

## Marked input: 
<pre>every potential <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>twist <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>telegraphed <span style="background-color: #6698FF">@</span>well <span style="background-color: #6698FF">@</span>in advance , <span style="background-color: #6698FF">@</span>every <span style="background-color: #6698FF">@</span>performance @@UNK@@ muted <span style="background-color: #FFFF00">@</span>; <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>movie <span style="background-color: #6698FF">@</span>itself <span style="background-color: #6698FF">@</span>seems <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>have <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>been <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>made <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>under <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span>influence <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `have been` | 5.66 | ['0.65', '5.38']
w2.f1 |   | `muted ;` | 2.55 | ['0.96', '1.71']
w2.f2 |   | `itself seems` | 0.59 | ['0.72', '0.91']
w2.f3 | x | `advance ,` | 2.50 | ['2.62', '0.44']
w2.f4 |   | `influence of` | 3.30 | ['4.03', '-0.55']
w2.f5 | x | `seems to` | 5.47 | ['3.39', '2.39']
w2.f6 |   | `advance ,` | 3.20 | ['-0.63', '3.93']
w2.f7 |   | `been made` | 1.67 | ['0.80', '1.78']
w2.f8 |   | `muted ;` | 1.85 | ['0.52', '1.54']
w2.f9 | x | `advance ,` | 5.32 | ['5.00', '0.34']
w2.f10 |   | `made under` | 2.92 | ['-0.01', '3.06']
w2.f11 | x | `influence of` | 4.05 | ['3.38', '0.95']
w2.f12 | x | `is telegraphed` | 4.38 | ['-0.59', '5.00']
w2.f13 | x | `advance ,` | 4.43 | ['2.40', '2.18']
w2.f14 | x | `potential twist` | 4.43 | ['3.22', '1.24']
w2.f15 | x | `the influence` | 4.05 | ['-0.42', '4.73']
w2.f16 | x | `every potential` | 3.89 | ['2.04', '2.62']
w2.f17 | x | `have been` | 4.66 | ['2.06', '3.21']
w2.f18 | x | `seems to` | 3.58 | ['1.21', '2.50']
w2.f19 |   | `telegraphed well` | 3.04 | ['1.65', '1.69']
w3.f0 |   | `itself seems to` | 3.36 | ['1.59', '3.49', '-1.33']
w3.f1 | x | `every potential twist` | 4.90 | ['0.15', '1.79', '3.33']
w3.f2 | x | `; the movie` | 4.04 | ['-0.74', '0.94', '3.93']
w3.f3 |   | `movie itself seems` | 1.29 | ['-0.45', '0.76', '1.59']
w3.f4 |   | `movie itself seems` | 1.61 | ['2.80', '0.55', '-1.37']
w3.f5 |   | `every performance @@UNK@@` | 2.39 | ['-0.85', '4.50', '-0.93']
w3.f6 |   | `the movie itself` | 3.54 | ['-0.32', '4.49', '-0.43']
w3.f7 |   | `in advance ,` | 3.33 | ['1.23', '1.41', '1.18']
w3.f8 | x | `under the influence` | 4.96 | ['1.20', '-1.07', '5.12']
w3.f9 | x | `itself seems to` | 6.88 | ['3.03', '4.34', '-0.38']
w3.f10 | x | `have been made` | 4.36 | ['2.81', '2.71', '-1.00']
w3.f11 | x | `to have been` | 5.48 | ['-1.19', '2.99', '3.87']
w3.f12 |   | `potential twist is` | 3.88 | ['2.35', '-0.16', '1.82']
w3.f13 |   | `the movie itself` | 3.86 | ['4.70', '-1.93', '1.33']
w3.f14 | x | `to have been` | 4.89 | ['-0.10', '1.57', '3.51']
w3.f15 | x | `itself seems to` | 5.75 | ['5.08', '1.42', '-0.59']
w3.f16 | x | `been made under` | 4.84 | ['-0.06', '1.58', '3.70']
w3.f17 | x | `seems to have` | 5.34 | ['4.91', '1.66', '-1.07']
w3.f18 | x | `influence of @@UNK@@` | 4.88 | ['3.47', '2.10', '-0.23']
w3.f19 | x | `@@UNK@@ muted ;` | 4.35 | ['-0.26', '2.81', '1.91']

## Original input: 
``` this film is full of @@UNK@@ . @@UNK@@ . but like most @@UNK@@ , it seems to lack substance . ``` 

## Marked input: 
<pre>this <span style="background-color: #FFFF00">@</span>film <span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>full <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>@@UNK@@ . but <span style="background-color: #6698FF">@</span>like <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>most <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ , it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>seems <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>lack <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>substance <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `, it` | 0.15 | ['-1.14', '1.67']
w2.f1 |   | `but like` | 3.16 | ['4.31', '-1.01']
w2.f2 |   | `it seems` | 0.37 | ['0.50', '0.91']
w2.f3 | x | `lack substance` | 2.13 | ['1.24', '1.45']
w2.f4 |   | `lack substance` | 2.30 | ['1.67', '0.83']
w2.f5 | x | `seems to` | 5.47 | ['3.39', '2.39']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `lack substance` | 1.24 | ['1.53', '0.62']
w2.f8 |   | `this film` | 1.16 | ['0.76', '0.61']
w2.f9 |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 | x | `but like` | 3.09 | ['0.75', '2.47']
w2.f11 |   | `it seems` | 2.00 | ['0.00', '2.27']
w2.f12 |   | `@@PAD@@ this` | 2.72 | ['0.00', '2.76']
w2.f13 |   | `@@PAD@@ this` | 2.85 | ['0.00', '3.00']
w2.f14 |   | `to lack` | 1.55 | ['-2.35', '3.93']
w2.f15 | x | `it seems` | 5.16 | ['1.16', '4.27']
w2.f16 |   | `is full` | 1.89 | ['-0.10', '2.76']
w2.f17 |   | `seems to` | 2.35 | ['3.94', '-0.97']
w2.f18 | x | `seems to` | 3.58 | ['1.21', '2.50']
w2.f19 |   | `seems to` | 1.32 | ['0.50', '1.12']
w3.f0 |   | `seems to lack` | 3.10 | ['4.55', '-1.42', '0.36']
w3.f1 | x | `, it seems` | 5.94 | ['1.74', '-0.10', '4.67']
w3.f2 | x | `, it seems` | 4.70 | ['2.60', '1.70', '0.49']
w3.f3 |   | `, it seems` | 0.32 | ['-0.33', '-0.33', '1.59']
w3.f4 |   | `. but like` | 2.52 | ['-0.66', '0.31', '3.23']
w3.f5 |   | `lack substance .` | 4.02 | ['0.03', '-0.01', '4.32']
w3.f6 |   | `@@UNK@@ . but` | 2.22 | ['-0.28', '1.07', '1.64']
w3.f7 | x | `to lack substance` | 5.56 | ['3.76', '1.53', '0.77']
w3.f8 | x | `film is full` | 5.93 | ['-0.14', '4.71', '1.64']
w3.f9 |   | `. but like` | 3.27 | ['0.67', '1.36', '1.35']
w3.f10 | x | `lack substance .` | 6.59 | ['6.78', '2.23', '-2.27']
w3.f11 | x | `to lack substance` | 4.33 | ['-1.19', '3.94', '1.78']
w3.f12 | x | `lack substance .` | 6.54 | ['3.14', '1.92', '1.61']
w3.f13 | x | `film is full` | 6.33 | ['0.42', '2.81', '3.35']
w3.f14 | x | `. but like` | 7.68 | ['-1.71', '3.83', '5.65']
w3.f15 | x | `, it seems` | 4.33 | ['1.52', '2.22', '0.76']
w3.f16 |   | `@@UNK@@ , it` | 3.30 | ['-1.96', '3.78', '1.86']
w3.f17 | x | `seems to lack` | 9.54 | ['4.91', '1.66', '3.12']
w3.f18 | x | `full of @@UNK@@` | 5.73 | ['4.32', '2.10', '-0.23']
w3.f19 | x | `@@PAD@@ this film` | 4.16 | ['0.00', '0.77', '3.51']

## Original input: 
``` having had the good sense to cast actors who are , generally speaking , @@UNK@@ by the movie - going public , @@UNK@@ then gets terrific performances from them all . ``` 

## Marked input: 
<pre>having had <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>good <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>sense <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>cast <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>actors <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>who <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>are <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>generally <span style="background-color: #6698FF">@</span>speaking <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>by the movie - going public <span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>then <span style="background-color: #6698FF">@</span>gets <span style="background-color: #6698FF">@</span>terrific <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>performances <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>from <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>them <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>all <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `cast actors` | 5.69 | ['1.47', '4.59']
w2.f1 | x | `gets terrific` | 5.97 | ['4.15', '1.95']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `going public` | 3.16 | ['1.40', '2.32']
w2.f4 | x | `public ,` | 3.81 | ['1.50', '2.50']
w2.f5 | x | `having had` | 4.33 | ['2.81', '1.82']
w2.f6 | x | `speaking ,` | 4.43 | ['0.59', '3.93']
w2.f7 | x | `gets terrific` | 2.16 | ['2.03', '1.04']
w2.f8 | x | `gets terrific` | 3.69 | ['2.41', '1.49']
w2.f9 |   | `sense to` | 3.69 | ['-0.97', '4.67']
w2.f10 | x | `gets terrific` | 7.79 | ['2.93', '4.99']
w2.f11 |   | `then gets` | 2.48 | ['1.91', '0.84']
w2.f12 | x | `who are` | 4.05 | ['1.52', '2.57']
w2.f13 | x | `then gets` | 5.11 | ['7.25', '-1.99']
w2.f14 | x | `going public` | 3.76 | ['2.04', '1.76']
w2.f15 | x | `terrific performances` | 3.40 | ['3.15', '0.52']
w2.f16 |   | `had the` | 1.87 | ['1.80', '0.83']
w2.f17 | x | `cast actors` | 5.51 | ['1.47', '4.66']
w2.f18 |   | `actors who` | 2.23 | ['0.76', '1.59']
w2.f19 | x | `performances from` | 3.52 | ['2.63', '1.19']
w3.f0 | x | `gets terrific performances` | 6.64 | ['1.99', '-0.96', '6.00']
w3.f1 | x | `terrific performances from` | 6.75 | ['2.93', '0.12', '4.08']
w3.f2 | x | `, @@UNK@@ then` | 7.89 | ['2.60', '-0.65', '6.02']
w3.f3 | x | `gets terrific performances` | 2.49 | ['-0.09', '1.59', '1.60']
w3.f4 | x | `actors who are` | 5.23 | ['1.46', '0.61', '3.51']
w3.f5 | x | `them all .` | 5.24 | ['1.47', '-0.22', '4.32']
w3.f6 | x | `@@UNK@@ then gets` | 4.55 | ['-0.28', '1.54', '3.49']
w3.f7 | x | `to cast actors` | 4.89 | ['3.76', '0.69', '0.93']
w3.f8 | x | `gets terrific performances` | 6.62 | ['1.55', '3.49', '1.87']
w3.f9 | x | `generally speaking ,` | 5.38 | ['1.03', '1.41', '3.06']
w3.f10 | x | `sense to cast` | 5.27 | ['0.63', '1.69', '3.10']
w3.f11 | x | `, generally speaking` | 4.24 | ['-1.39', '0.84', '4.98']
w3.f12 | x | `the good sense` | 5.35 | ['2.43', '-1.34', '4.39']
w3.f13 | x | `the good sense` | 6.42 | ['4.70', '3.04', '-1.08']
w3.f14 | x | `terrific performances from` | 3.28 | ['0.42', '0.36', '2.60']
w3.f15 | x | `going public ,` | 5.71 | ['1.20', '1.97', '2.70']
w3.f16 | x | `terrific performances from` | 5.46 | ['-1.09', '3.60', '3.33']
w3.f17 | x | `are , generally` | 6.32 | ['2.67', '3.34', '0.46']
w3.f18 | x | `cast actors who` | 5.52 | ['2.33', '1.74', '1.91']
w3.f19 | x | `gets terrific performances` | 11.00 | ['1.90', '7.12', '2.10']

## Original input: 
``` a @@UNK@@ thoughtful minor classic , the work of a genuine and @@UNK@@ artist . ``` 

## Marked input: 
<pre>a @@UNK@@ thoughtful <span style="background-color: #FFFF00">@</span>minor <span style="background-color: #FFFF00">@</span>classic <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>work <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>genuine <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>artist .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ thoughtful` | 7.88 | ['1.98', '6.27']
w2.f1 |   | `a genuine` | 2.95 | ['2.95', '0.13']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `minor classic` | 1.49 | ['1.39', '0.65']
w2.f4 |   | `artist .` | 2.75 | ['2.97', '-0.03']
w2.f5 | x | `thoughtful minor` | 4.30 | ['-0.93', '5.54']
w2.f6 |   | `minor classic` | 3.31 | ['2.48', '0.92']
w2.f7 |   | `@@UNK@@ thoughtful` | 0.36 | ['-0.69', '1.96']
w2.f8 |   | `@@PAD@@ a` | 2.34 | ['0.00', '2.56']
w2.f9 |   | `@@UNK@@ artist` | 2.67 | ['2.38', '0.31']
w2.f10 |   | `thoughtful minor` | 2.66 | ['2.99', '-0.19']
w2.f11 |   | `work of` | 2.68 | ['2.00', '0.95']
w2.f12 |   | `minor classic` | 2.74 | ['1.90', '0.87']
w2.f13 | x | `minor classic` | 3.21 | ['2.92', '0.43']
w2.f14 |   | `classic ,` | 2.12 | ['1.27', '0.89']
w2.f15 |   | `@@UNK@@ artist` | 3.04 | ['-1.59', '4.90']
w2.f16 |   | `@@UNK@@ thoughtful` | 0.43 | ['-0.75', '1.94']
w2.f17 |   | `artist .` | 1.00 | ['1.15', '0.47']
w2.f18 |   | `minor classic` | 2.72 | ['1.04', '1.80']
w2.f19 |   | `a genuine` | 2.00 | ['0.99', '1.31']
w3.f0 |   | `a genuine and` | 2.06 | ['-0.19', '1.65', '0.99']
w3.f1 |   | `and @@UNK@@ artist` | 2.41 | ['-2.71', '-0.73', '6.24']
w3.f2 | x | `a genuine and` | 4.44 | ['1.87', '2.18', '0.47']
w3.f3 | x | `thoughtful minor classic` | 4.33 | ['3.36', '0.31', '1.26']
w3.f4 |   | `thoughtful minor classic` | 2.95 | ['3.64', '-0.25', '-0.08']
w3.f5 | x | `a genuine and` | 11.21 | ['1.79', '3.94', '5.81']
w3.f6 |   | `a genuine and` | 3.01 | ['1.76', '0.52', '0.95']
w3.f7 |   | `minor classic ,` | 3.74 | ['1.58', '1.47', '1.18']
w3.f8 | x | `@@UNK@@ thoughtful minor` | 5.84 | ['0.50', '4.52', '1.11']
w3.f9 | x | `minor classic ,` | 3.69 | ['1.66', '-0.92', '3.06']
w3.f10 | x | `of a genuine` | 5.35 | ['2.92', '1.32', '1.26']
w3.f11 |   | `@@PAD@@ @@PAD@@ a` | 2.59 | ['0.00', '0.00', '2.78']
w3.f12 |   | `the work of` | 3.20 | ['2.43', '0.21', '0.69']
w3.f13 | x | `the work of` | 7.88 | ['4.70', '0.73', '2.71']
w3.f14 |   | `classic , the` | 2.80 | ['2.02', '-0.37', '1.24']
w3.f15 |   | `minor classic ,` | 3.37 | ['0.46', '0.37', '2.70']
w3.f16 | x | `of a genuine` | 4.43 | ['1.87', '0.35', '2.58']
w3.f17 | x | `classic , the` | 7.83 | ['3.39', '3.34', '1.25']
w3.f18 | x | `thoughtful minor classic` | 3.41 | ['3.05', '0.70', '0.13']
w3.f19 |   | `@@UNK@@ thoughtful minor` | 3.28 | ['-0.26', '2.08', '1.57']

## Original input: 
``` moore 's complex and important film is also , believe it or not , immensely entertaining , a david and @@UNK@@ story that 's still very much playing itself out . ``` 

## Marked input: 
<pre>moore 's <span style="background-color: #FFFF00">@</span>complex <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>important <span style="background-color: #FFFF00">@</span>film <span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>also , <span style="background-color: #FFFF00">@</span>believe <span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span>or <span style="background-color: #6698FF">@</span>not <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>immensely <span style="background-color: #FFFF00">@</span>entertaining <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>david <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>story that 's <span style="background-color: #FFFF00">@</span>still <span style="background-color: #FFFF00">@</span>very <span style="background-color: #FFFF00">@</span>much <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>playing <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>itself <span style="background-color: #6698FF">@</span>out .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `very much` | 6.10 | ['4.99', '1.49']
w2.f1 |   | `believe it` | 2.63 | ['0.98', '1.78']
w2.f2 |   | `@@PAD@@ moore` | 0.22 | ['0.00', '1.27']
w2.f3 | x | `very much` | 2.23 | ['2.65', '0.14']
w2.f4 | x | `still very` | 8.96 | ['8.07', '1.07']
w2.f5 | x | `entertaining ,` | 3.79 | ['5.39', '-1.30']
w2.f6 | x | `also ,` | 5.39 | ['1.55', '3.93']
w2.f7 |   | `or not` | 1.70 | ['1.02', '1.58']
w2.f8 | x | `moore 's` | 5.46 | ['1.85', '3.82']
w2.f9 |   | `playing itself` | 4.64 | ['0.31', '4.35']
w2.f10 | x | `'s complex` | 4.99 | ['2.75', '2.38']
w2.f11 | x | `believe it` | 3.87 | ['2.86', '1.28']
w2.f12 |   | `believe it` | 2.25 | ['1.33', '0.96']
w2.f13 |   | `also ,` | 2.29 | ['0.26', '2.18']
w2.f14 |   | `playing itself` | 2.97 | ['0.85', '2.15']
w2.f15 | x | `, immensely` | 8.09 | ['2.19', '6.17']
w2.f16 |   | `itself out` | 2.55 | ['2.62', '0.69']
w2.f17 |   | `or not` | 1.87 | ['-0.09', '2.58']
w2.f18 | x | `still very` | 5.21 | ['0.45', '4.89']
w2.f19 | x | `and important` | 5.44 | ['3.66', '2.08']
w3.f0 |   | `itself out .` | 3.71 | ['1.59', '2.14', '0.37']
w3.f1 | x | `complex and important` | 7.05 | ['2.78', '-1.74', '6.39']
w3.f2 | x | `it or not` | 5.78 | ['-0.61', '2.08', '4.40']
w3.f3 | x | `still very much` | 3.71 | ['2.44', '1.66', '0.20']
w3.f4 | x | `moore 's complex` | 3.56 | ['-0.94', '2.08', '2.78']
w3.f5 | x | `a david and` | 10.56 | ['1.79', '3.29', '5.81']
w3.f6 |   | `still very much` | 3.19 | ['0.98', '1.59', '0.83']
w3.f7 |   | `, immensely entertaining` | 2.73 | ['1.70', '3.13', '-1.61']
w3.f8 | x | `that 's still` | 8.39 | ['3.58', '0.26', '4.83']
w3.f9 | x | `immensely entertaining ,` | 4.71 | ['1.51', '0.25', '3.06']
w3.f10 |   | `@@PAD@@ moore 's` | 2.50 | ['0.00', '3.44', '-0.80']
w3.f11 |   | `@@PAD@@ moore 's` | 3.03 | ['0.00', '1.95', '1.27']
w3.f12 | x | `it or not` | 4.39 | ['0.79', '0.73', '3.00']
w3.f13 |   | `itself out .` | 4.79 | ['-1.47', '4.06', '2.45']
w3.f14 |   | `very much playing` | 1.38 | ['1.65', '-0.74', '0.57']
w3.f15 | x | `very much playing` | 6.03 | ['2.73', '3.59', '-0.12']
w3.f16 | x | `entertaining , a` | 6.04 | ['4.76', '3.78', '-2.12']
w3.f17 | x | `it or not` | 5.97 | ['1.06', '0.73', '4.34']
w3.f18 | x | `immensely entertaining ,` | 3.80 | ['1.38', '2.09', '0.79']
w3.f19 | x | `and important film` | 8.23 | ['3.50', '1.34', '3.51']

## Original input: 
``` i wonder what the reaction of @@UNK@@ will be to this supposedly @@UNK@@ presentation . ``` 

## Marked input: 
<pre>i wonder <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>what <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>reaction <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>will <span style="background-color: #FFFF00">@</span>be <span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span>this <span style="background-color: #6698FF">@</span>supposedly <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>presentation <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ will` | 4.58 | ['1.98', '2.98']
w2.f1 |   | `@@UNK@@ will` | 1.60 | ['-0.88', '2.61']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `this supposedly` | 2.14 | ['0.36', '2.34']
w2.f4 | x | `i wonder` | 4.10 | ['3.61', '0.68']
w2.f5 |   | `what the` | 2.45 | ['2.99', '-0.23']
w2.f6 |   | `will be` | 3.15 | ['2.71', '0.54']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `@@UNK@@ presentation` | 1.19 | ['0.21', '1.19']
w2.f9 | x | `be to` | 8.22 | ['3.56', '4.67']
w2.f10 |   | `wonder what` | 2.32 | ['0.01', '2.44']
w2.f11 |   | `supposedly @@UNK@@` | 1.48 | ['1.51', '0.25']
w2.f12 | x | `to this` | 4.25 | ['1.53', '2.76']
w2.f13 | x | `presentation .` | 4.65 | ['4.78', '0.01']
w2.f14 |   | `@@UNK@@ presentation` | 2.54 | ['0.69', '1.89']
w2.f15 |   | `this supposedly` | 3.18 | ['3.03', '0.43']
w2.f16 |   | `what the` | 0.11 | ['0.04', '0.83']
w2.f17 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f18 |   | `i wonder` | 2.73 | ['1.52', '1.34']
w2.f19 |   | `be to` | 0.82 | ['-0.00', '1.12']
w3.f0 |   | `supposedly @@UNK@@ presentation` | 2.92 | ['-0.39', '0.35', '3.35']
w3.f1 |   | `i wonder what` | 0.30 | ['-1.92', '2.09', '0.51']
w3.f2 | x | `to this supposedly` | 3.79 | ['0.63', '2.87', '0.38']
w3.f3 |   | `@@PAD@@ @@PAD@@ i` | 0.00 | ['0.00', '0.00', '0.26']
w3.f4 |   | `i wonder what` | 1.46 | ['-0.95', '0.76', '2.01']
w3.f5 | x | `@@UNK@@ presentation .` | 5.43 | ['0.08', '1.36', '4.32']
w3.f6 |   | `i wonder what` | 2.33 | ['-0.07', '2.20', '0.41']
w3.f7 |   | `to this supposedly` | 2.90 | ['3.76', '0.43', '-0.79']
w3.f8 |   | `be to this` | 3.80 | ['1.23', '1.89', '0.96']
w3.f9 |   | `this supposedly @@UNK@@` | 1.68 | ['-0.87', '0.52', '2.13']
w3.f10 |   | `presentation . @@PAD@@` | 3.08 | ['1.23', '2.00', '0.00']
w3.f11 |   | `@@PAD@@ i wonder` | 3.48 | ['0.00', '1.26', '2.41']
w3.f12 | x | `the reaction of` | 4.94 | ['2.43', '1.95', '0.69']
w3.f13 |   | `the reaction of` | 4.98 | ['4.70', '-2.17', '2.71']
w3.f14 | x | `i wonder what` | 4.13 | ['-3.37', '5.48', '2.11']
w3.f15 |   | `this supposedly @@UNK@@` | 2.60 | ['2.58', '2.24', '-2.05']
w3.f16 |   | `to this supposedly` | 2.73 | ['1.59', '1.31', '0.21']
w3.f17 |   | `supposedly @@UNK@@ presentation` | 3.75 | ['-1.55', '1.39', '4.06']
w3.f18 |   | `@@UNK@@ presentation .` | 0.12 | ['-2.55', '4.09', '-0.95']
w3.f19 |   | `be to this` | 1.50 | ['-1.46', '0.71', '2.36']

## Original input: 
``` you would be better off @@UNK@@ in the worthy @@UNK@@ recording that serves as the soundtrack , or the home video of the @@UNK@@ @@UNK@@ - @@UNK@@ production . ``` 

## Marked input: 
<pre>you <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>would <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>be <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>better <span style="background-color: #6698FF">@</span>off <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>in the worthy <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>recording <span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>serves <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>as <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>soundtrack <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>or <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the home video <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ @@UNK@@ - @@UNK@@ production .</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ recording` | 2.46 | ['1.98', '0.85']
w2.f1 |   | `home video` | 1.92 | ['-1.31', '3.36']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `better off` | 1.32 | ['0.15', '1.73']
w2.f4 | x | `soundtrack ,` | 4.11 | ['1.80', '2.50']
w2.f5 | x | `video of` | 4.08 | ['2.62', '1.76']
w2.f6 |   | `would be` | 2.92 | ['2.48', '0.54']
w2.f7 |   | `better off` | 1.48 | ['0.78', '1.60']
w2.f8 | x | `@@PAD@@ you` | 3.93 | ['0.00', '4.14']
w2.f9 | x | `be better` | 5.88 | ['3.56', '2.34']
w2.f10 | x | `you would` | 4.09 | ['4.16', '0.06']
w2.f11 | x | `would be` | 5.17 | ['3.02', '2.42']
w2.f12 | x | `home video` | 4.94 | ['-0.28', '5.25']
w2.f13 | x | `better off` | 4.74 | ['2.23', '2.65']
w2.f14 | x | `better off` | 7.31 | ['2.88', '4.47']
w2.f15 | x | `@@PAD@@ you` | 5.72 | ['0.00', '5.99']
w2.f16 | x | `you would` | 4.12 | ['-0.85', '5.74']
w2.f17 |   | `the worthy` | 2.01 | ['-2.64', '5.27']
w2.f18 |   | `that serves` | 2.45 | ['2.33', '0.24']
w2.f19 |   | `video of` | 2.04 | ['2.92', '-0.58']
w3.f0 | x | `@@PAD@@ you would` | 4.95 | ['0.00', '1.60', '3.74']
w3.f1 |   | `recording that serves` | 2.51 | ['1.38', '0.66', '0.85']
w3.f2 | x | `as the soundtrack` | 5.20 | ['0.16', '0.94', '4.19']
w3.f3 | x | `recording that serves` | 2.66 | ['1.81', '-0.85', '2.30']
w3.f4 |   | `@@PAD@@ @@PAD@@ you` | 2.10 | ['0.00', '0.00', '2.46']
w3.f5 |   | `soundtrack , or` | 1.57 | ['0.91', '1.40', '-0.41']
w3.f6 | x | `you would be` | 5.54 | ['2.54', '2.89', '0.32']
w3.f7 | x | `recording that serves` | 4.96 | ['2.01', '-0.01', '3.46']
w3.f8 | x | `the worthy @@UNK@@` | 6.16 | ['1.05', '5.93', '-0.54']
w3.f9 | x | `recording that serves` | 3.84 | ['0.74', '1.05', '2.16']
w3.f10 |   | `production . @@PAD@@` | 3.71 | ['1.85', '2.00', '0.00']
w3.f11 |   | `@@PAD@@ you would` | 3.55 | ['0.00', '3.60', '0.14']
w3.f12 | x | `the soundtrack ,` | 5.02 | ['2.43', '2.56', '0.16']
w3.f13 |   | `home video of` | 4.40 | ['2.08', '-0.14', '2.71']
w3.f14 |   | `, or the` | 1.89 | ['-0.18', '0.92', '1.24']
w3.f15 |   | `would be better` | 3.17 | ['1.45', '-0.82', '2.71']
w3.f16 | x | `recording that serves` | 6.77 | ['3.88', '2.04', '1.23']
w3.f17 |   | `soundtrack , or` | 3.02 | ['0.35', '3.34', '-0.51']
w3.f18 | x | `serves as the` | 3.78 | ['-0.22', '1.90', '2.57']
w3.f19 |   | `you would be` | 2.71 | ['1.24', '1.65', '-0.06']

## Original input: 
``` [ @@UNK@@ i suffered and @@UNK@@ on the hard ground of @@UNK@@ @@UNK@@ , i 'd want something a bit more complex than we were soldiers to be remembered by . ``` 

## Marked input: 
<pre>[ <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>i <span style="background-color: #6698FF">@</span>suffered <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>on the hard <span style="background-color: #6698FF">@</span>ground <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ , i 'd want something <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>bit <span style="background-color: #6698FF">@</span>more <span style="background-color: #6698FF">@</span>complex <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>than <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>we <span style="background-color: #FFFF00">@</span>were <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>soldiers <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>be <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>remembered <span style="background-color: #FFFF00">@</span>by <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `i suffered` | 2.45 | ['-0.23', '3.06']
w2.f1 |   | `hard ground` | 3.08 | ['0.53', '2.69']
w2.f2 |   | `were soldiers` | 0.42 | ['0.25', '1.22']
w2.f3 |   | `we were` | 1.90 | ['0.37', '2.09']
w2.f4 | x | `i suffered` | 4.56 | ['3.61', '1.14']
w2.f5 | x | `we were` | 4.86 | ['4.53', '0.63']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `@@PAD@@ [` | 1.30 | ['0.00', '2.21']
w2.f8 |   | `something a` | 2.02 | ['-0.33', '2.56']
w2.f9 | x | `soldiers to` | 6.25 | ['1.59', '4.67']
w2.f10 | x | `suffered and` | 3.41 | ['2.07', '1.48']
w2.f11 | x | `were soldiers` | 3.56 | ['3.01', '0.83']
w2.f12 | x | `want something` | 4.98 | ['-0.80', '5.82']
w2.f13 | x | `remembered by` | 3.45 | ['0.13', '3.48']
w2.f14 | x | `[ @@UNK@@` | 4.05 | ['3.78', '0.30']
w2.f15 |   | `were soldiers` | 1.66 | ['2.25', '-0.32']
w2.f16 |   | `i 'd` | 1.44 | ['1.19', '1.01']
w2.f17 | x | `@@PAD@@ [` | 5.03 | ['0.00', '5.65']
w2.f18 | x | `we were` | 5.50 | ['4.79', '0.83']
w2.f19 | x | `were soldiers` | 4.06 | ['1.47', '2.89']
w3.f0 |   | `@@PAD@@ [ @@UNK@@` | 3.57 | ['0.00', '5.16', '-1.20']
w3.f1 | x | `more complex than` | 5.23 | ['4.72', '0.11', '0.78']
w3.f2 | x | `a bit more` | 5.93 | ['1.87', '-0.54', '4.68']
w3.f3 |   | `we were soldiers` | 0.30 | ['0.42', '-0.32', '0.81']
w3.f4 | x | `we were soldiers` | 5.75 | ['1.03', '1.05', '4.03']
w3.f5 | x | `i suffered and` | 6.70 | ['0.80', '0.42', '5.81']
w3.f6 | x | `the hard ground` | 3.73 | ['-0.32', '2.49', '1.76']
w3.f7 | x | `be remembered by` | 4.69 | ['0.84', '3.04', '1.30']
w3.f8 |   | `bit more complex` | 2.98 | ['0.63', '-0.18', '2.82']
w3.f9 | x | `we were soldiers` | 6.52 | ['-0.56', '7.01', '0.18']
w3.f10 |   | `than we were` | 3.60 | ['1.14', '1.58', '1.02']
w3.f11 |   | `'d want something` | 1.97 | ['1.38', '4.27', '-3.49']
w3.f12 | x | `remembered by .` | 4.73 | ['-0.01', '3.26', '1.61']
w3.f13 |   | `we were soldiers` | 4.03 | ['2.64', '2.57', '-0.94']
w3.f14 | x | `bit more complex` | 4.91 | ['1.15', '4.60', '-0.75']
w3.f15 | x | `hard ground of` | 4.18 | ['2.04', '0.30', '2.01']
w3.f16 | x | `to be remembered` | 5.54 | ['1.59', '1.31', '3.02']
w3.f17 | x | `hard ground of` | 6.65 | ['2.01', '2.93', '1.87']
w3.f18 |   | `we were soldiers` | 2.97 | ['0.00', '2.40', '1.03']
w3.f19 |   | `a bit more` | 3.61 | ['3.70', '0.39', '-0.36']

## Original input: 
``` every now and again , a movie comes along to remind us of how very bad a motion picture can truly be . frank @@UNK@@ c . i . is that movie ! ``` 

## Marked input: 
<pre>every <span style="background-color: #6698FF">@</span>now <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>again <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>movie <span style="background-color: #6698FF">@</span>comes <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>along <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>remind <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>us <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>how <span style="background-color: #6698FF">@</span>very <span style="background-color: #6698FF">@</span>bad <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>motion <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>picture <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>can <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>truly <span style="background-color: #6698FF">@</span>be <span style="background-color: #6698FF">@</span>. frank @@UNK@@ c <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>i <span style="background-color: #FFFF00">@</span>. is that movie !</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `very bad` | 1.64 | ['4.99', '-2.97']
w2.f1 | x | `a motion` | 5.51 | ['2.95', '2.69']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `very bad` | 3.49 | ['2.65', '1.40']
w2.f4 | x | `movie comes` | 4.90 | ['3.31', '1.78']
w2.f5 |   | `a motion` | 2.23 | ['0.71', '1.83']
w2.f6 |   | `@@UNK@@ c` | 3.05 | ['0.07', '3.08']
w2.f7 | x | `every now` | 2.34 | ['0.05', '3.20']
w2.f8 |   | `bad a` | 1.57 | ['-0.77', '2.56']
w2.f9 | x | `along to` | 7.05 | ['2.39', '4.67']
w2.f10 | x | `comes along` | 4.65 | ['0.52', '4.26']
w2.f11 | x | `can truly` | 5.54 | ['0.88', '4.93']
w2.f12 | x | `of how` | 6.61 | ['-0.82', '7.47']
w2.f13 | x | `very bad` | 4.34 | ['0.86', '3.62']
w2.f14 | x | `again ,` | 6.12 | ['5.26', '0.89']
w2.f15 |   | `remind us` | 3.16 | ['1.59', '1.84']
w2.f16 | x | `very bad` | 5.49 | ['1.70', '4.56']
w2.f17 |   | `remind us` | 2.29 | ['0.07', '2.84']
w2.f18 | x | `and again` | 5.49 | ['3.52', '2.10']
w2.f19 | x | `and again` | 5.86 | ['3.66', '2.49']
w3.f0 | x | `bad a motion` | 7.50 | ['2.31', '3.29', '2.29']
w3.f1 | x | `to remind us` | 4.85 | ['-0.45', '0.74', '4.94']
w3.f2 | x | `, a movie` | 5.57 | ['2.60', '-0.88', '3.93']
w3.f3 |   | `c . i` | 1.66 | ['2.15', '-0.14', '0.26']
w3.f4 | x | `movie ! @@PAD@@` | 3.68 | ['2.80', '1.24', '0.00']
w3.f5 | x | `@@UNK@@ c .` | 7.75 | ['0.08', '3.68', '4.32']
w3.f6 | x | `a movie comes` | 8.34 | ['1.76', '4.49', '2.30']
w3.f7 | x | `every now and` | 4.22 | ['-0.21', '3.09', '1.83']
w3.f8 |   | `and again ,` | 4.13 | ['2.47', '-0.20', '2.14']
w3.f9 | x | `very bad a` | 11.40 | ['4.11', '6.27', '1.13']
w3.f10 | x | `bad a motion` | 5.22 | ['2.70', '1.32', '1.36']
w3.f11 | x | `bad a motion` | 6.37 | ['5.12', '0.22', '1.22']
w3.f12 | x | `@@PAD@@ every now` | 4.59 | ['0.00', '1.38', '3.34']
w3.f13 |   | `remind us of` | 4.50 | ['0.45', '1.59', '2.71']
w3.f14 |   | `of how very` | 1.96 | ['-0.37', '0.96', '1.47']
w3.f15 | x | `how very bad` | 4.32 | ['-1.66', '4.81', '1.33']
w3.f16 |   | `is that movie` | 2.18 | ['1.27', '2.04', '-0.75']
w3.f17 | x | `picture can truly` | 7.38 | ['3.05', '0.09', '4.39']
w3.f18 |   | `comes along to` | 3.17 | ['1.37', '0.75', '1.52']
w3.f19 | x | `a motion picture` | 7.66 | ['3.70', '6.55', '-2.48']

## Original input: 
``` paid in full is so stale , in fact , that its most vibrant scene is one that uses @@UNK@@ from brian de palma 's @@UNK@@ . that 's a @@UNK@@ . ``` 

## Marked input: 
<pre>paid in full is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>so <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>stale <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>fact <span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span>that <span style="background-color: #FFFF00">@</span>its <span style="background-color: #FFFF00">@</span>most <span style="background-color: #FFFF00">@</span>vibrant <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>scene <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>one <span style="background-color: #FFFF00">@</span>that uses @@UNK@@ <span style="background-color: #FFFF00">@</span>from <span style="background-color: #FFFF00">@</span>brian <span style="background-color: #FFFF00">@</span>de <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>palma <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>. that 's a @@UNK@@ .</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `vibrant scene` | 4.30 | ['0.56', '4.11']
w2.f1 | x | `vibrant scene` | 6.13 | ['4.68', '1.59']
w2.f2 |   | `from brian` | 0.43 | ['0.61', '0.87']
w2.f3 |   | `stale ,` | 2.04 | ['2.16', '0.44']
w2.f4 |   | `fact ,` | 3.05 | ['0.74', '2.50']
w2.f5 |   | `brian de` | 3.14 | ['0.84', '2.60']
w2.f6 | x | `fact ,` | 4.95 | ['1.12', '3.93']
w2.f7 | x | `so stale` | 3.96 | ['1.25', '3.62']
w2.f8 | x | `palma 's` | 4.93 | ['1.32', '3.82']
w2.f9 |   | `so stale` | 4.24 | ['3.80', '0.45']
w2.f10 | x | `from brian` | 4.39 | ['0.27', '4.25']
w2.f11 | x | `vibrant scene` | 6.34 | ['3.21', '3.40']
w2.f12 | x | `so stale` | 6.44 | ['2.41', '4.07']
w2.f13 | x | `stale ,` | 6.01 | ['3.98', '2.18']
w2.f14 |   | `that its` | 2.50 | ['0.85', '1.69']
w2.f15 | x | `most vibrant` | 4.12 | ['-2.94', '7.34']
w2.f16 | x | `brian de` | 3.21 | ['3.09', '0.88']
w2.f17 | x | `so stale` | 3.57 | ['1.08', '3.10']
w2.f18 | x | `that its` | 3.78 | ['2.33', '1.57']
w2.f19 |   | `brian de` | 2.41 | ['-0.22', '2.94']
w3.f0 | x | `most vibrant scene` | 5.76 | ['4.37', '-1.24', '3.03']
w3.f1 | x | `uses @@UNK@@ from` | 4.99 | ['2.03', '-0.73', '4.08']
w3.f2 |   | `, that its` | 3.30 | ['2.60', '1.53', '-0.74']
w3.f3 | x | `brian de palma` | 3.53 | ['1.48', '1.50', '1.16']
w3.f4 | x | `vibrant scene is` | 4.13 | ['1.05', '0.98', '2.46']
w3.f5 |   | `its most vibrant` | 3.92 | ['1.92', '2.81', '-0.48']
w3.f6 |   | `fact , that` | 2.67 | ['1.31', '0.38', '1.19']
w3.f7 | x | `, that its` | 5.78 | ['1.70', '-0.01', '4.59']
w3.f8 | x | `brian de palma` | 5.14 | ['-0.32', '5.66', '0.09']
w3.f9 | x | `so stale ,` | 6.04 | ['1.68', '1.41', '3.06']
w3.f10 | x | `full is so` | 6.11 | ['2.91', '0.69', '2.66']
w3.f11 | x | `brian de palma` | 6.52 | ['2.84', '1.45', '2.42']
w3.f12 | x | `most vibrant scene` | 6.08 | ['-0.39', '0.94', '5.66']
w3.f13 |   | `scene is one` | 5.02 | ['2.35', '2.81', '0.10']
w3.f14 | x | `so stale ,` | 4.54 | ['6.10', '1.29', '-2.75']
w3.f15 |   | `most vibrant scene` | 3.60 | ['1.66', '0.46', '1.64']
w3.f16 | x | `that its most` | 4.60 | ['1.08', '2.21', '1.69']
w3.f17 | x | `stale , in` | 6.14 | ['2.93', '3.34', '0.03']
w3.f18 | x | `full is so` | 4.35 | ['4.32', '0.11', '0.38']
w3.f19 | x | `its most vibrant` | 6.61 | ['3.31', '-1.75', '5.16']

## Original input: 
``` with dickens ' words and writer - director @@UNK@@ mcgrath 's even - @@UNK@@ direction , a @@UNK@@ good yarn is told . ``` 

## Marked input: 
<pre>with dickens <span style="background-color: #6698FF">@</span>' <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>words <span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>writer <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>director @@UNK@@ <span style="background-color: #FFFF00">@</span>mcgrath <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>even <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>direction , <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>@@UNK@@ good <span style="background-color: #FFFF00">@</span>yarn <span style="background-color: #FFFF00">@</span>is told <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `with dickens` | 3.54 | ['3.44', '0.48']
w2.f1 | x | `mcgrath 's` | 7.00 | ['5.57', '1.57']
w2.f2 |   | `mcgrath 's` | 0.42 | ['1.96', '-0.50']
w2.f3 | x | `and writer` | 2.79 | ['0.06', '3.29']
w2.f4 | x | `' words` | 5.76 | ['1.10', '4.86']
w2.f5 |   | `mcgrath 's` | 2.68 | ['2.73', '0.26']
w2.f6 | x | `direction ,` | 5.78 | ['1.95', '3.93']
w2.f7 |   | `dickens '` | 0.72 | ['0.51', '1.12']
w2.f8 | x | `mcgrath 's` | 7.19 | ['3.58', '3.82']
w2.f9 |   | `told .` | 3.91 | ['3.47', '0.46']
w2.f10 | x | `'s even` | 4.15 | ['2.75', '1.53']
w2.f11 | x | `with dickens` | 3.79 | ['2.35', '1.71']
w2.f12 |   | `direction ,` | 1.61 | ['1.68', '-0.03']
w2.f13 | x | `told .` | 4.08 | ['4.22', '0.01']
w2.f14 |   | `is told` | 2.41 | ['-0.15', '2.59']
w2.f15 | x | `@@UNK@@ mcgrath` | 9.15 | ['-1.59', '11.01']
w2.f16 |   | `good yarn` | 1.95 | ['2.10', '0.61']
w2.f17 |   | `and writer` | 2.70 | ['1.02', '2.30']
w2.f18 | x | `' words` | 7.15 | ['2.45', '4.82']
w2.f19 | x | `@@UNK@@ good` | 3.95 | ['0.39', '3.85']
w3.f0 |   | `' words and` | 2.33 | ['1.32', '0.41', '0.99']
w3.f1 | x | `mcgrath 's even` | 5.38 | ['7.05', '-0.93', '-0.36']
w3.f2 |   | `direction , a` | 2.80 | ['3.41', '-2.80', '2.27']
w3.f3 | x | `mcgrath 's even` | 2.44 | ['2.64', '-0.29', '0.70']
w3.f4 | x | `dickens ' words` | 4.95 | ['2.01', '0.21', '3.08']
w3.f5 | x | `' words and` | 12.36 | ['1.09', '5.78', '5.81']
w3.f6 | x | `'s even -` | 5.10 | ['3.62', '2.23', '-0.54']
w3.f7 |   | `, a @@UNK@@` | 1.61 | ['1.70', '0.48', '-0.07']
w3.f8 | x | `director @@UNK@@ mcgrath` | 4.83 | ['1.27', '-0.27', '4.11']
w3.f9 |   | `with dickens '` | 3.29 | ['-0.55', '-1.28', '5.23']
w3.f10 |   | `@@UNK@@ mcgrath 's` | 3.06 | ['0.33', '3.68', '-0.80']
w3.f11 |   | `direction , a` | 2.74 | ['1.51', '-1.36', '2.78']
w3.f12 |   | `- @@UNK@@ direction` | 3.51 | ['-2.29', '-0.16', '6.09']
w3.f13 | x | `is told .` | 5.32 | ['1.15', '1.97', '2.45']
w3.f14 | x | `words and writer` | 4.14 | ['-1.68', '1.09', '4.82']
w3.f15 |   | `@@PAD@@ with dickens` | 3.26 | ['0.00', '3.85', '-0.42']
w3.f16 | x | `director @@UNK@@ mcgrath` | 5.54 | ['0.72', '-0.81', '6.01']
w3.f17 |   | `direction , a` | 1.69 | ['0.43', '3.34', '-1.92']
w3.f18 | x | `mcgrath 's even` | 7.70 | ['7.02', '0.79', '0.36']
w3.f19 | x | `director @@UNK@@ mcgrath` | 4.86 | ['1.47', '-2.39', '5.91']

## Original input: 
``` i 'd give real money to see the @@UNK@@ of chicago torn apart by @@UNK@@ . ``` 

## Marked input: 
<pre>i 'd give <span style="background-color: #FFFF00">@</span>real <span style="background-color: #FFFF00">@</span>money <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span>see <span style="background-color: #6698FF">@</span>the @@UNK@@ <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>chicago <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>torn <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>apart <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>by <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `torn apart` | 1.66 | ['1.14', '0.89']
w2.f1 | x | `torn apart` | 6.85 | ['4.54', '2.44']
w2.f2 |   | `torn apart` | 1.77 | ['1.25', '1.57']
w2.f3 |   | `give real` | 1.95 | ['0.28', '2.23']
w2.f4 |   | `i 'd` | 3.21 | ['3.61', '-0.21']
w2.f5 |   | `i 'd` | 2.42 | ['3.97', '-1.25']
w2.f6 |   | `torn apart` | 2.39 | ['0.97', '1.51']
w2.f7 |   | `give real` | 1.28 | ['-0.47', '2.66']
w2.f8 |   | `real money` | 1.87 | ['0.40', '1.68']
w2.f9 |   | `@@UNK@@ of` | 4.02 | ['2.38', '1.65']
w2.f10 |   | `'d give` | 0.87 | ['-0.51', '1.52']
w2.f11 | x | `chicago torn` | 3.30 | ['1.49', '2.08']
w2.f12 | x | `apart by` | 3.78 | ['0.11', '3.71']
w2.f13 | x | `apart by` | 5.39 | ['2.06', '3.48']
w2.f14 |   | `of chicago` | 2.39 | ['0.02', '2.41']
w2.f15 |   | `of chicago` | 0.77 | ['-3.18', '4.23']
w2.f16 |   | `see the` | 1.87 | ['1.80', '0.83']
w2.f17 |   | `see the` | 1.42 | ['2.30', '-0.27']
w2.f18 | x | `give real` | 3.41 | ['2.89', '0.65']
w2.f19 | x | `of chicago` | 3.97 | ['1.68', '2.59']
w3.f0 |   | `@@PAD@@ i 'd` | 2.75 | ['0.00', '-0.05', '3.20']
w3.f1 |   | `money to see` | 2.92 | ['-1.93', '0.48', '4.76']
w3.f2 |   | `see the @@UNK@@` | 1.51 | ['0.97', '0.94', '-0.31']
w3.f3 |   | `give real money` | 2.13 | ['1.13', '0.77', '0.83']
w3.f4 |   | `chicago torn apart` | 3.00 | ['0.11', '3.15', '0.09']
w3.f5 |   | `@@PAD@@ i 'd` | 3.22 | ['0.00', '2.36', '1.18']
w3.f6 | x | `torn apart by` | 5.19 | ['0.27', '2.79', '2.35']
w3.f7 | x | `torn apart by` | 6.38 | ['1.21', '4.37', '1.30']
w3.f8 | x | `'d give real` | 4.56 | ['-0.11', '1.45', '3.50']
w3.f9 |   | `see the @@UNK@@` | 3.38 | ['1.47', '-0.12', '2.13']
w3.f10 | x | `of chicago torn` | 9.56 | ['2.92', '2.01', '4.77']
w3.f11 | x | `real money to` | 3.79 | ['0.81', '1.12', '2.06']
w3.f12 |   | `@@UNK@@ of chicago` | 3.38 | ['-0.75', '3.24', '1.02']
w3.f13 | x | `the @@UNK@@ of` | 5.41 | ['4.70', '-1.74', '2.71']
w3.f14 |   | `torn apart by` | 1.89 | ['1.79', '-2.39', '2.59']
w3.f15 | x | `torn apart by` | 4.71 | ['3.67', '1.27', '-0.07']
w3.f16 |   | `of chicago torn` | 3.38 | ['1.87', '0.09', '1.80']
w3.f17 |   | `the @@UNK@@ of` | 1.92 | ['-1.17', '1.39', '1.87']
w3.f18 | x | `chicago torn apart` | 4.75 | ['1.32', '3.11', '0.78']
w3.f19 | x | `chicago torn apart` | 6.17 | ['5.13', '-0.27', '1.42']

## Original input: 
``` the kind of trifle that date nights were @@UNK@@ for . ``` 

## Marked input: 
<pre>the kind <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>trifle <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>that <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>date <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>nights <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>were <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>for <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ for` | 3.71 | ['1.98', '2.10']
w2.f1 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `nights were` | 2.09 | ['0.55', '2.09']
w2.f4 |   | `that date` | 1.50 | ['1.54', '0.15']
w2.f5 |   | `kind of` | 2.25 | ['0.80', '1.76']
w2.f6 |   | `nights were` | 2.87 | ['2.89', '0.08']
w2.f7 |   | `of trifle` | 1.09 | ['0.11', '1.89']
w2.f8 |   | `kind of` | 1.08 | ['2.28', '-0.99']
w2.f9 |   | `kind of` | 2.12 | ['0.48', '1.65']
w2.f10 |   | `the kind` | 1.56 | ['-1.39', '3.09']
w2.f11 | x | `were @@UNK@@` | 2.98 | ['3.01', '0.25']
w2.f12 |   | `were @@UNK@@` | 2.49 | ['2.30', '0.22']
w2.f13 | x | `nights were` | 3.65 | ['1.31', '2.49']
w2.f14 |   | `the kind` | 1.08 | ['0.10', '1.01']
w2.f15 |   | `that date` | 2.22 | ['-0.23', '2.72']
w2.f16 |   | `@@PAD@@ the` | 0.07 | ['0.00', '0.83']
w2.f17 |   | `of trifle` | 2.51 | ['-1.87', '5.00']
w2.f18 | x | `that date` | 3.40 | ['2.33', '1.19']
w2.f19 |   | `of trifle` | 2.62 | ['1.68', '1.24']
w3.f0 | x | `nights were @@UNK@@` | 4.55 | ['2.56', '3.58', '-1.20']
w3.f1 |   | `trifle that date` | 2.61 | ['1.97', '0.66', '0.35']
w3.f2 | x | `trifle that date` | 5.31 | ['3.82', '1.53', '0.05']
w3.f3 |   | `that date nights` | 1.68 | ['2.19', '-0.71', '0.81']
w3.f4 |   | `kind of trifle` | 0.04 | ['-0.35', '-0.44', '1.19']
w3.f5 |   | `@@UNK@@ for .` | 2.60 | ['0.08', '-1.47', '4.32']
w3.f6 |   | `of trifle that` | 2.89 | ['-0.15', '2.05', '1.19']
w3.f7 | x | `that date nights` | 4.17 | ['3.01', '1.43', '0.22']
w3.f8 |   | `that date nights` | 3.89 | ['3.58', '-1.81', '2.40']
w3.f9 | x | `nights were @@UNK@@` | 9.03 | ['-0.00', '7.01', '2.13']
w3.f10 | x | `of trifle that` | 4.53 | ['2.92', '2.16', '-0.41']
w3.f11 |   | `trifle that date` | 1.88 | ['1.38', '0.56', '0.14']
w3.f12 | x | `kind of trifle` | 7.11 | ['-0.04', '3.24', '4.03']
w3.f13 | x | `the kind of` | 5.48 | ['4.70', '-1.67', '2.71']
w3.f14 | x | `were @@UNK@@ for` | 5.34 | ['3.54', '0.79', '1.11']
w3.f15 |   | `the kind of` | 2.53 | ['-0.02', '0.71', '2.01']
w3.f16 |   | `that date nights` | 2.99 | ['1.08', '2.79', '-0.49']
w3.f17 |   | `@@UNK@@ for .` | 3.34 | ['-2.59', '5.11', '0.98']
w3.f18 | x | `kind of trifle` | 5.04 | ['3.20', '2.10', '0.21']
w3.f19 |   | `date nights were` | 1.17 | ['0.04', '0.92', '0.33']

## Original input: 
``` an exceptionally dreary and overwrought bit of work , every bit as @@UNK@@ as @@UNK@@ 's the @@UNK@@ of @@UNK@@ from @@UNK@@ . ``` 

## Marked input: 
<pre>an <span style="background-color: #FFFF00">@</span>exceptionally <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>dreary <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>overwrought <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>bit <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>work <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>every <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>bit <span style="background-color: #6698FF">@</span>as <span style="background-color: #6698FF">@</span>@@UNK@@ as @@UNK@@ 's <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>from <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `exceptionally dreary` | 4.27 | ['1.38', '3.26']
w2.f1 | x | `exceptionally dreary` | 6.37 | ['3.11', '3.39']
w2.f2 |   | `exceptionally dreary` | 1.59 | ['0.79', '1.84']
w2.f3 |   | `and overwrought` | 1.90 | ['0.06', '2.40']
w2.f4 | x | `work ,` | 3.61 | ['1.30', '2.50']
w2.f5 | x | `an exceptionally` | 6.61 | ['3.50', '3.41']
w2.f6 |   | `work ,` | 3.16 | ['-0.68', '3.93']
w2.f7 | x | `dreary and` | 4.22 | ['5.04', '0.09']
w2.f8 | x | `@@UNK@@ 's` | 3.81 | ['0.21', '3.82']
w2.f9 |   | `@@UNK@@ of` | 4.02 | ['2.38', '1.65']
w2.f10 | x | `an exceptionally` | 3.42 | ['1.91', '1.65']
w2.f11 | x | `dreary and` | 6.30 | ['6.31', '0.27']
w2.f12 |   | `and overwrought` | 2.64 | ['0.18', '2.49']
w2.f13 | x | `dreary and` | 3.58 | ['3.15', '0.57']
w2.f14 | x | `dreary and` | 3.87 | ['3.89', '0.01']
w2.f15 |   | `, every` | 1.26 | ['2.19', '-0.66']
w2.f16 | x | `dreary and` | 3.08 | ['5.11', '-1.27']
w2.f17 |   | `overwrought bit` | 1.43 | ['1.08', '0.97']
w2.f18 |   | `an exceptionally` | 1.66 | ['-0.46', '2.24']
w2.f19 |   | `and overwrought` | 2.38 | ['3.66', '-0.98']
w3.f0 | x | `dreary and overwrought` | 7.70 | ['3.40', '-1.09', '5.78']
w3.f1 | x | `@@PAD@@ an exceptionally` | 5.58 | ['0.00', '1.98', '3.97']
w3.f2 | x | `, every bit` | 4.81 | ['2.60', '1.14', '1.15']
w3.f3 | x | `an exceptionally dreary` | 3.58 | ['0.82', '0.33', '3.04']
w3.f4 |   | `@@PAD@@ an exceptionally` | 2.28 | ['0.00', '0.82', '1.82']
w3.f5 |   | `exceptionally dreary and` | 4.26 | ['0.91', '-2.13', '5.81']
w3.f6 | x | `an exceptionally dreary` | 5.06 | ['1.58', '0.48', '3.21']
w3.f7 |   | `an exceptionally dreary` | 3.95 | ['2.46', '0.81', '1.18']
w3.f8 | x | `of work ,` | 4.60 | ['1.71', '1.03', '2.14']
w3.f9 | x | `exceptionally dreary and` | 7.25 | ['1.63', '3.33', '2.40']
w3.f10 |   | `an exceptionally dreary` | 3.72 | ['-0.44', '0.47', '3.84']
w3.f11 |   | `dreary and overwrought` | 3.15 | ['6.53', '-1.20', '-1.99']
w3.f12 |   | `overwrought bit of` | 3.77 | ['5.70', '-2.49', '0.69']
w3.f13 | x | `the @@UNK@@ of` | 5.41 | ['4.70', '-1.74', '2.71']
w3.f14 |   | `of @@UNK@@ from` | 2.92 | ['-0.37', '0.79', '2.60']
w3.f15 |   | `, every bit` | 2.78 | ['1.52', '1.34', '0.08']
w3.f16 | x | `of @@UNK@@ from` | 4.01 | ['1.87', '-0.81', '3.33']
w3.f17 | x | `overwrought bit of` | 5.83 | ['5.63', '-1.51', '1.87']
w3.f18 | x | `exceptionally dreary and` | 4.07 | ['4.75', '1.92', '-2.13']
w3.f19 | x | `an exceptionally dreary` | 4.12 | ['-1.58', '3.49', '2.32']

## Original input: 
``` rarely has sex on screen been so aggressively anti - erotic . ``` 

## Marked input: 
<pre>rarely <span style="background-color: #FFFF00">@</span>has <span style="background-color: #FFFF00">@</span>sex <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>on <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>screen <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>been <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>so <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>aggressively <span style="background-color: #6698FF">@</span>anti <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>erotic <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `screen been` | 7.16 | ['2.16', '5.38']
w2.f1 |   | `been so` | 2.07 | ['-0.55', '2.76']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `screen been` | 2.44 | ['0.65', '2.35']
w2.f4 |   | `erotic .` | 1.34 | ['1.56', '-0.03']
w2.f5 |   | `sex on` | 0.54 | ['1.88', '-1.03']
w2.f6 |   | `aggressively anti` | 2.63 | ['1.63', '1.10']
w2.f7 |   | `screen been` | 0.90 | ['1.75', '0.06']
w2.f8 | x | `screen been` | 4.72 | ['4.11', '0.83']
w2.f9 | x | `so aggressively` | 5.37 | ['3.80', '1.59']
w2.f10 |   | `- erotic` | 2.30 | ['1.18', '1.25']
w2.f11 | x | `sex on` | 3.26 | ['1.83', '1.71']
w2.f12 |   | `screen been` | 1.49 | ['-0.51', '2.04']
w2.f13 |   | `rarely has` | 2.63 | ['1.17', '1.61']
w2.f14 |   | `- erotic` | 2.65 | ['-0.18', '2.86']
w2.f15 | x | `has sex` | 6.00 | ['1.71', '4.56']
w2.f16 |   | `been so` | 1.28 | ['1.27', '0.77']
w2.f17 | x | `screen been` | 5.21 | ['2.61', '3.21']
w2.f18 |   | `sex on` | 2.03 | ['1.22', '0.93']
w2.f19 |   | `has sex` | 2.49 | ['1.03', '1.76']
w3.f0 | x | `has sex on` | 4.63 | ['1.40', '0.84', '2.79']
w3.f1 |   | `been so aggressively` | 1.96 | ['1.71', '-0.01', '0.63']
w3.f2 |   | `aggressively anti -` | 2.23 | ['1.90', '-0.13', '0.54']
w3.f3 |   | `sex on screen` | 2.28 | ['1.55', '0.33', '1.01']
w3.f4 | x | `sex on screen` | 4.41 | ['1.41', '2.22', '1.14']
w3.f5 | x | `- erotic .` | 5.78 | ['0.99', '0.80', '4.32']
w3.f6 | x | `aggressively anti -` | 4.23 | ['4.21', '0.78', '-0.54']
w3.f7 |   | `aggressively anti -` | 3.23 | ['1.55', '0.37', '1.81']
w3.f8 | x | `rarely has sex` | 6.42 | ['1.37', '3.82', '1.51']
w3.f9 | x | `screen been so` | 8.03 | ['5.65', '1.27', '1.22']
w3.f10 | x | `screen been so` | 6.31 | ['1.09', '2.71', '2.66']
w3.f11 | x | `on screen been` | 5.69 | ['-1.83', '3.84', '3.87']
w3.f12 | x | `been so aggressively` | 8.87 | ['-0.66', '0.60', '9.06']
w3.f13 |   | `rarely has sex` | 5.26 | ['0.53', '4.26', '0.71']
w3.f14 | x | `so aggressively anti` | 11.82 | ['6.10', '0.31', '5.51']
w3.f15 |   | `screen been so` | 2.13 | ['-0.50', '0.90', '1.89']
w3.f16 |   | `rarely has sex` | 1.59 | ['1.68', '-2.89', '3.17']
w3.f17 |   | `so aggressively anti` | 3.72 | ['0.04', '2.36', '1.48']
w3.f18 | x | `@@PAD@@ rarely has` | 4.03 | ['0.00', '3.46', '1.04']
w3.f19 | x | `sex on screen` | 4.02 | ['0.70', '1.30', '2.14']

## Original input: 
``` the second coming of harry potter is a film far superior to its predecessor . a movie that successfully @@UNK@@ a best selling novel into a @@UNK@@ that @@UNK@@ that you avoid the @@UNK@@ sized @@UNK@@ . ``` 

## Marked input: 
<pre>the second <span style="background-color: #FFFF00">@</span>coming <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>harry <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>potter <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>film <span style="background-color: #6698FF">@</span>far superior <span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span>its <span style="background-color: #FFFF00">@</span>predecessor <span style="background-color: #FFFF00">@</span>. <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>movie <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>successfully <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span>best <span style="background-color: #FFFF00">@</span>selling <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>novel <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>into <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ that @@UNK@@ that you <span style="background-color: #FFFF00">@</span>avoid <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>sized <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `far superior` | 3.45 | ['1.18', '2.64']
w2.f1 | x | `a movie` | 3.76 | ['2.95', '0.94']
w2.f2 |   | `best selling` | 0.79 | ['0.76', '1.08']
w2.f3 | x | `selling novel` | 3.61 | ['1.94', '2.23']
w2.f4 | x | `you avoid` | 4.43 | ['2.00', '2.62']
w2.f5 | x | `far superior` | 4.88 | ['3.32', '1.87']
w2.f6 |   | `movie that` | 2.60 | ['1.65', '1.05']
w2.f7 | x | `novel into` | 2.47 | ['2.43', '0.95']
w2.f8 | x | `that you` | 4.62 | ['0.70', '4.14']
w2.f9 |   | `coming of` | 4.09 | ['2.45', '1.65']
w2.f10 |   | `novel into` | 2.57 | ['2.23', '0.48']
w2.f11 | x | `best selling` | 6.42 | ['1.09', '5.59']
w2.f12 |   | `that successfully` | 3.34 | ['1.55', '1.82']
w2.f13 | x | `novel into` | 3.97 | ['3.50', '0.62']
w2.f14 | x | `second coming` | 6.64 | ['0.69', '5.99']
w2.f15 | x | `that you` | 5.49 | ['-0.23', '5.99']
w2.f16 | x | `best selling` | 3.91 | ['0.67', '4.01']
w2.f17 | x | `harry potter` | 4.14 | ['0.93', '3.83']
w2.f18 | x | `novel into` | 4.37 | ['2.37', '2.12']
w2.f19 |   | `a best` | 3.06 | ['0.99', '2.36']
w3.f0 | x | `of harry potter` | 7.10 | ['-0.27', '2.88', '4.89']
w3.f1 | x | `best selling novel` | 4.75 | ['0.93', '0.12', '4.08']
w3.f2 | x | `movie that successfully` | 3.70 | ['2.41', '1.53', '-0.14']
w3.f3 |   | `that successfully @@UNK@@` | 1.93 | ['2.19', '0.28', '0.07']
w3.f4 |   | `harry potter is` | 2.64 | ['-0.31', '0.85', '2.46']
w3.f5 | x | `the second coming` | 5.92 | ['-0.36', '2.45', '4.16']
w3.f6 | x | `a movie that` | 7.23 | ['1.76', '4.49', '1.19']
w3.f7 | x | `superior to its` | 5.02 | ['-0.25', '1.18', '4.59']
w3.f8 | x | `of harry potter` | 6.09 | ['1.71', '1.91', '2.76']
w3.f9 | x | `predecessor . a` | 5.12 | ['3.51', '0.58', '1.13']
w3.f10 | x | `of harry potter` | 10.88 | ['2.92', '5.06', '3.05']
w3.f11 | x | `selling novel into` | 8.20 | ['4.44', '2.58', '1.37']
w3.f12 | x | `the @@UNK@@ sized` | 6.45 | ['2.43', '-0.16', '4.31']
w3.f13 | x | `the second coming` | 6.69 | ['4.70', '2.65', '-0.41']
w3.f14 | x | `best selling novel` | 5.90 | ['2.15', '4.46', '-0.61']
w3.f15 |   | `second coming of` | 3.46 | ['-0.15', '1.77', '2.01']
w3.f16 | x | `@@UNK@@ a best` | 4.85 | ['-1.96', '0.35', '6.84']
w3.f17 | x | `potter is a` | 5.08 | ['4.81', '2.35', '-1.92']
w3.f18 | x | `coming of harry` | 3.67 | ['1.43', '2.10', '0.61']
w3.f19 | x | `coming of harry` | 4.14 | ['5.47', '-1.61', '0.39']

## Original input: 
``` summer 's far too fleeting to @@UNK@@ on @@UNK@@ like this . ``` 

## Marked input: 
<pre>summer <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>far <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>too <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>fleeting <span style="background-color: #6698FF">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>on <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>like <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>this <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `summer 's` | 5.76 | ['5.45', '0.68']
w2.f1 | x | `@@PAD@@ summer` | 6.93 | ['0.00', '7.07']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `far too` | 4.17 | ['0.64', '4.09']
w2.f4 |   | `@@PAD@@ summer` | 2.80 | ['0.00', '2.99']
w2.f5 | x | `like this` | 3.94 | ['3.40', '0.85']
w2.f6 |   | `like this` | 2.56 | ['2.29', '0.37']
w2.f7 |   | `far too` | 0.56 | ['-0.36', '1.83']
w2.f8 | x | `summer 's` | 3.89 | ['0.28', '3.82']
w2.f9 |   | `fleeting to` | 3.62 | ['-1.04', '4.67']
w2.f10 |   | `@@PAD@@ summer` | 2.67 | ['0.00', '2.81']
w2.f11 | x | `too fleeting` | 5.35 | ['3.88', '1.74']
w2.f12 |   | `to @@UNK@@` | 1.72 | ['1.53', '0.22']
w2.f13 | x | `@@UNK@@ like` | 3.49 | ['0.61', '3.03']
w2.f14 |   | `on @@UNK@@` | 2.39 | ['2.12', '0.30']
w2.f15 | x | `summer 's` | 3.61 | ['4.52', '-0.64']
w2.f16 |   | `too fleeting` | 2.11 | ['2.26', '0.61']
w2.f17 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f18 |   | `fleeting to` | 2.91 | ['0.54', '2.50']
w2.f19 |   | `fleeting to` | 3.01 | ['2.18', '1.12']
w3.f0 |   | `summer 's far` | 1.85 | ['-1.98', '1.91', '2.30']
w3.f1 |   | `@@PAD@@ @@PAD@@ summer` | 2.06 | ['0.00', '0.00', '2.44']
w3.f2 | x | `like this .` | 3.89 | ['0.27', '2.87', '0.84']
w3.f3 |   | `@@PAD@@ @@PAD@@ summer` | 1.30 | ['0.00', '0.00', '1.90']
w3.f4 | x | `summer 's far` | 8.43 | ['3.90', '2.08', '2.82']
w3.f5 |   | `'s far too` | 2.68 | ['0.63', '1.54', '0.85']
w3.f6 | x | `far too fleeting` | 8.40 | ['2.80', '4.25', '1.56']
w3.f7 |   | `to @@UNK@@ on` | 2.01 | ['3.76', '-1.81', '0.55']
w3.f8 | x | `fleeting to @@UNK@@` | 5.06 | ['3.99', '1.89', '-0.54']
w3.f9 | x | `far too fleeting` | 3.99 | ['0.96', '2.90', '0.24']
w3.f10 | x | `far too fleeting` | 5.62 | ['2.20', '3.11', '0.46']
w3.f11 | x | `'s far too` | 5.96 | ['-1.43', '3.80', '3.78']
w3.f12 | x | `on @@UNK@@ like` | 4.52 | ['-0.10', '-0.16', '4.91']
w3.f13 |   | `like this .` | 4.70 | ['0.87', '1.63', '2.45']
w3.f14 | x | `on @@UNK@@ like` | 5.81 | ['-0.53', '0.79', '5.65']
w3.f15 | x | `far too fleeting` | 7.34 | ['2.79', '3.12', '1.59']
w3.f16 |   | `'s far too` | 1.22 | ['2.11', '1.42', '-1.94']
w3.f17 |   | `far too fleeting` | 2.19 | ['1.06', '2.80', '-1.52']
w3.f18 | x | `summer 's far` | 4.71 | ['3.70', '0.79', '0.68']
w3.f19 | x | `@@UNK@@ like this` | 5.52 | ['-0.26', '3.53', '2.36']

## Original input: 
``` @@UNK@@ is a grating , mannered onscreen presence , which is especially unfortunate in light of the fine work done by most of the rest of her cast . ``` 

## Marked input: 
<pre>@@UNK@@ is a grating <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>mannered <span style="background-color: #6698FF">@</span>onscreen <span style="background-color: #6698FF">@</span>presence <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>which <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #6698FF">@</span>especially <span style="background-color: #6698FF">@</span>unfortunate <span style="background-color: #6698FF">@</span>in <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>light <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>fine <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>work <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>done <span style="background-color: #FFFF00">@</span>by <span style="background-color: #6698FF">@</span>most <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the rest of her <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>cast <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `the fine` | 2.99 | ['-1.87', '5.23']
w2.f1 |   | `work done` | 2.22 | ['1.82', '0.53']
w2.f2 |   | `a grating` | 0.13 | ['0.10', '1.07']
w2.f3 | x | `cast .` | 2.19 | ['2.79', '-0.05']
w2.f4 | x | `presence ,` | 4.87 | ['2.55', '2.50']
w2.f5 | x | `light of` | 3.34 | ['1.88', '1.76']
w2.f6 | x | `presence ,` | 4.33 | ['0.50', '3.93']
w2.f7 |   | `unfortunate in` | 1.38 | ['3.21', '-0.92']
w2.f8 |   | `fine work` | 3.07 | ['2.33', '0.96']
w2.f9 | x | `especially unfortunate` | 5.05 | ['0.93', '4.13']
w2.f10 | x | `by most` | 4.02 | ['-0.62', '4.77']
w2.f11 | x | `a grating` | 6.95 | ['0.43', '6.79']
w2.f12 | x | `unfortunate in` | 4.66 | ['2.73', '1.97']
w2.f13 | x | `by most` | 3.49 | ['1.21', '2.42']
w2.f14 | x | `done by` | 3.97 | ['1.89', '2.12']
w2.f15 | x | `fine work` | 5.19 | ['2.22', '3.24']
w2.f16 |   | `mannered onscreen` | 2.35 | ['1.61', '1.50']
w2.f17 | x | `grating ,` | 4.97 | ['5.97', '-0.38']
w2.f18 |   | `presence ,` | 2.21 | ['1.44', '0.89']
w2.f19 |   | `her cast` | 3.06 | ['1.68', '1.68']
w3.f0 | x | `grating , mannered` | 5.79 | ['6.05', '-0.76', '0.89']
w3.f1 |   | `of her cast` | 3.66 | ['-3.20', '4.07', '3.17']
w3.f2 | x | `a grating ,` | 6.75 | ['1.87', '3.64', '1.32']
w3.f3 |   | `fine work done` | 1.97 | ['0.67', '0.34', '1.57']
w3.f4 |   | `@@PAD@@ @@UNK@@ is` | 1.82 | ['0.00', '-0.29', '2.46']
w3.f5 |   | `in light of` | 2.74 | ['0.52', '3.02', '-0.47']
w3.f6 | x | `of the fine` | 4.61 | ['-0.15', '0.45', '4.52']
w3.f7 | x | `unfortunate in light` | 4.28 | ['2.77', '0.70', '1.30']
w3.f8 | x | `the fine work` | 9.91 | ['1.05', '6.83', '2.32']
w3.f9 | x | `onscreen presence ,` | 5.74 | ['-0.32', '3.11', '3.06']
w3.f10 | x | `of her cast` | 6.06 | ['2.92', '0.18', '3.10']
w3.f11 | x | `presence , which` | 4.09 | ['5.41', '-1.36', '0.24']
w3.f12 | x | `is especially unfortunate` | 5.98 | ['0.69', '-0.83', '6.25']
w3.f13 | x | `the fine work` | 7.38 | ['4.70', '2.44', '0.49']
w3.f14 | x | `presence , which` | 6.46 | ['5.22', '-0.37', '1.70']
w3.f15 | x | `onscreen presence ,` | 4.73 | ['1.07', '1.12', '2.70']
w3.f16 | x | `of her cast` | 4.89 | ['1.87', '0.98', '2.41']
w3.f17 | x | `presence , which` | 8.70 | ['5.03', '3.34', '0.49']
w3.f18 | x | `light of the` | 5.50 | ['1.30', '2.10', '2.57']
w3.f19 | x | `in light of` | 4.67 | ['-1.65', '3.77', '2.66']

## Original input: 
``` @@UNK@@ along , @@UNK@@ the twisted humor and eye - @@UNK@@ visuals that have made @@UNK@@ . . . a cult hero . ``` 

## Marked input: 
<pre>@@UNK@@ along <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>the twisted <span style="background-color: #FFFF00">@</span>humor <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>eye <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>- <span style="background-color: #FFFF00">@</span>@@UNK@@ visuals that <span style="background-color: #FFFF00">@</span>have <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>made <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>. a cult <span style="background-color: #FFFF00">@</span>hero <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `cult hero` | 4.08 | ['3.24', '1.22']
w2.f1 | x | `a cult` | 7.22 | ['2.95', '4.41']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `that have` | 2.43 | ['-0.79', '3.78']
w2.f4 | x | `visuals that` | 3.70 | ['4.92', '-1.03']
w2.f5 | x | `the twisted` | 3.26 | ['1.16', '2.41']
w2.f6 | x | `along ,` | 6.60 | ['2.77', '3.93']
w2.f7 |   | `have made` | 0.38 | ['-0.49', '1.78']
w2.f8 |   | `twisted humor` | 2.52 | ['2.81', '-0.07']
w2.f9 | x | `cult hero` | 5.24 | ['3.55', '1.70']
w2.f10 | x | `@@UNK@@ along` | 4.06 | ['-0.06', '4.26']
w2.f11 |   | `humor and` | 1.69 | ['1.69', '0.27']
w2.f12 | x | `that have` | 3.70 | ['1.55', '2.18']
w2.f13 |   | `that have` | 1.93 | ['0.66', '1.42']
w2.f14 | x | `humor and` | 4.62 | ['4.64', '0.01']
w2.f15 |   | `twisted humor` | 1.96 | ['1.30', '0.93']
w2.f16 |   | `humor and` | 0.79 | ['2.82', '-1.27']
w2.f17 |   | `hero .` | 0.79 | ['0.94', '0.47']
w2.f18 |   | `visuals that` | 2.48 | ['2.55', '0.06']
w2.f19 | x | `and eye` | 4.84 | ['3.66', '1.47']
w3.f0 |   | `made @@UNK@@ .` | 3.14 | ['2.80', '0.35', '0.37']
w3.f1 |   | `twisted humor and` | 0.72 | ['1.31', '-0.04', '-0.17']
w3.f2 | x | `twisted humor and` | 5.11 | ['2.61', '2.11', '0.47']
w3.f3 |   | `the twisted humor` | 2.13 | ['-1.52', '1.44', '2.82']
w3.f4 |   | `. a cult` | 3.26 | ['-0.66', '0.29', '3.99']
w3.f5 | x | `a cult hero` | 5.53 | ['1.79', '4.83', '-0.76']
w3.f6 |   | `@@UNK@@ the twisted` | 3.17 | ['-0.28', '0.45', '3.21']
w3.f7 |   | `humor and eye` | 3.73 | ['2.49', '-2.95', '4.69']
w3.f8 | x | `humor and eye` | 7.30 | ['6.56', '0.71', '0.32']
w3.f9 | x | `twisted humor and` | 5.22 | ['-0.12', '3.05', '2.40']
w3.f10 | x | `have made @@UNK@@` | 4.22 | ['2.81', '0.70', '0.86']
w3.f11 |   | `that have made` | 1.49 | ['-1.63', '2.99', '0.32']
w3.f12 |   | `humor and eye` | 2.99 | ['3.52', '0.95', '-1.35']
w3.f13 | x | `the twisted humor` | 9.14 | ['4.70', '4.30', '0.39']
w3.f14 | x | `cult hero .` | 4.31 | ['0.71', '4.33', '-0.64']
w3.f15 |   | `@@UNK@@ along ,` | 3.35 | ['-0.51', '1.32', '2.70']
w3.f16 | x | `humor and eye` | 5.41 | ['0.69', '-0.30', '5.40']
w3.f17 | x | `made @@UNK@@ .` | 4.51 | ['2.30', '1.39', '0.98']
w3.f18 |   | `twisted humor and` | 2.98 | ['3.19', '2.38', '-2.13']
w3.f19 |   | `@@UNK@@ along ,` | 3.67 | ['-0.26', '2.96', '1.08']

## Original input: 
``` you never know where changing lanes is going to take you but it 's a @@UNK@@ of a ride . @@UNK@@ l . jackson is one of the best actors there is . ``` 

## Marked input: 
<pre>you <span style="background-color: #6698FF">@</span>never <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>know <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>where <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>changing <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>lanes <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>going <span style="background-color: #6698FF">@</span>to take <span style="background-color: #6698FF">@</span>you <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>but <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>a @@UNK@@ of a <span style="background-color: #FFFF00">@</span>ride <span style="background-color: #FFFF00">@</span>. <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>l <span style="background-color: #6698FF">@</span>. jackson <span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>one <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>best <span style="background-color: #FFFF00">@</span>actors <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>there <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>is .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `you never` | 3.92 | ['1.93', '2.37']
w2.f1 | x | `but it` | 5.95 | ['4.31', '1.78']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `. jackson` | 2.36 | ['0.52', '2.39']
w2.f4 | x | `take you` | 5.42 | ['5.42', '0.19']
w2.f5 | x | `the best` | 5.04 | ['1.16', '4.18']
w2.f6 |   | `is going` | 1.76 | ['-0.01', '1.87']
w2.f7 |   | `take you` | 1.52 | ['1.67', '0.76']
w2.f8 | x | `you never` | 4.46 | ['2.33', '2.35']
w2.f9 |   | `going to` | 4.46 | ['-0.20', '4.67']
w2.f10 | x | `you never` | 6.92 | ['4.16', '2.89']
w2.f11 | x | `you but` | 3.93 | ['1.83', '2.37']
w2.f12 |   | `to take` | 3.25 | ['1.53', '1.75']
w2.f13 |   | `of a` | 1.64 | ['0.35', '1.45']
w2.f14 | x | `best actors` | 4.52 | ['4.63', '-0.07']
w2.f15 | x | `take you` | 9.16 | ['3.44', '5.99']
w2.f16 |   | `know where` | 1.29 | ['2.18', '-0.12']
w2.f17 |   | `where changing` | 2.93 | ['0.63', '2.91']
w2.f18 | x | `a ride` | 5.79 | ['0.76', '5.15']
w2.f19 | x | `best actors` | 4.81 | ['2.44', '2.67']
w3.f0 | x | `where changing lanes` | 5.88 | ['2.16', '2.90', '1.21']
w3.f1 | x | `never know where` | 9.44 | ['1.72', '4.87', '3.24']
w3.f2 | x | `never know where` | 3.76 | ['6.11', '-2.45', '0.19']
w3.f3 |   | `take you but` | 2.12 | ['1.81', '0.23', '0.68']
w3.f4 | x | `where changing lanes` | 4.59 | ['1.54', '-0.45', '3.86']
w3.f5 | x | `a ride .` | 7.15 | ['1.79', '1.37', '4.32']
w3.f6 | x | `never know where` | 5.65 | ['0.98', '5.23', '-0.35']
w3.f7 | x | `of a ride` | 5.12 | ['0.84', '0.48', '4.30']
w3.f8 | x | `jackson is one` | 7.00 | ['3.68', '4.71', '-1.10']
w3.f9 | x | `ride . @@UNK@@` | 4.32 | ['1.72', '0.58', '2.13']
w3.f10 | x | `take you but` | 6.71 | ['2.83', '1.01', '3.02']
w3.f11 | x | `@@PAD@@ you never` | 9.62 | ['0.00', '3.60', '6.21']
w3.f12 | x | `to take you` | 4.50 | ['1.38', '2.49', '0.76']
w3.f13 | x | `the best actors` | 6.81 | ['4.70', '4.31', '-1.95']
w3.f14 | x | `changing lanes is` | 4.55 | ['0.96', '1.05', '2.63']
w3.f15 |   | `you never know` | 3.11 | ['-1.55', '2.25', '2.58']
w3.f16 | x | `of the best` | 8.42 | ['1.87', '0.10', '6.84']
w3.f17 |   | `. jackson is` | 2.58 | ['-1.75', '4.51', '-0.02']
w3.f18 | x | `one of the` | 3.48 | ['-0.72', '2.10', '2.57']
w3.f19 | x | `you never know` | 6.65 | ['1.24', '3.22', '2.30']

## Original input: 
``` if you 're looking for an intelligent movie in which you can release your @@UNK@@ up anger , enough is just the ticket you need . ``` 

## Marked input: 
<pre>if you 're looking for <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>an <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>intelligent <span style="background-color: #FFFF00">@</span>movie <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>which <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>you <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>can <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>release <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>your <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>up <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>anger <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>enough <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span>just the ticket <span style="background-color: #FFFF00">@</span>you <span style="background-color: #FFFF00">@</span>need <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `ticket you` | 4.58 | ['3.62', '1.33']
w2.f1 | x | `you can` | 4.18 | ['1.97', '2.35']
w2.f2 |   | `intelligent movie` | 0.06 | ['1.27', '-0.16']
w2.f3 | x | `up anger` | 2.35 | ['1.18', '1.73']
w2.f4 | x | `an intelligent` | 7.40 | ['5.09', '2.50']
w2.f5 |   | `, enough` | 1.42 | ['1.09', '0.63']
w2.f6 |   | `anger ,` | 2.57 | ['-1.26', '3.93']
w2.f7 | x | `release your` | 3.95 | ['1.31', '3.55']
w2.f8 | x | `ticket you` | 5.03 | ['1.10', '4.14']
w2.f9 |   | `in which` | 3.18 | ['0.15', '3.04']
w2.f10 | x | `@@UNK@@ up` | 6.74 | ['-0.06', '6.94']
w2.f11 | x | `you can` | 3.73 | ['1.83', '2.17']
w2.f12 | x | `movie in` | 3.46 | ['1.52', '1.97']
w2.f13 | x | `looking for` | 7.69 | ['5.06', '2.78']
w2.f14 | x | `in which` | 5.13 | ['-0.13', '5.29']
w2.f15 | x | `ticket you` | 9.09 | ['3.36', '5.99']
w2.f16 |   | `which you` | 1.56 | ['2.59', '-0.26']
w2.f17 | x | `release your` | 5.91 | ['2.85', '3.67']
w2.f18 |   | `you can` | 0.88 | ['-0.74', '1.75']
w2.f19 |   | `you 're` | 2.58 | ['0.48', '2.40']
w3.f0 | x | `release your @@UNK@@` | 5.85 | ['5.08', '2.36', '-1.20']
w3.f1 | x | `intelligent movie in` | 4.22 | ['0.43', '2.75', '1.42']
w3.f2 |   | `intelligent movie in` | 2.46 | ['1.19', '1.21', '0.16']
w3.f3 |   | `release your @@UNK@@` | 1.16 | ['0.50', '1.20', '0.07']
w3.f4 | x | `which you can` | 4.11 | ['1.97', '0.38', '2.12']
w3.f5 |   | `which you can` | 4.96 | ['2.11', '0.90', '2.28']
w3.f6 | x | `intelligent movie in` | 6.56 | ['2.15', '4.49', '0.14']
w3.f7 |   | `intelligent movie in` | 2.59 | ['-0.97', '2.56', '1.49']
w3.f8 |   | `enough is just` | 3.10 | ['1.75', '4.71', '-3.07']
w3.f9 | x | `up anger ,` | 4.41 | ['2.28', '-0.82', '3.06']
w3.f10 | x | `your @@UNK@@ up` | 6.28 | ['4.47', '-2.56', '4.51']
w3.f11 | x | `which you can` | 4.85 | ['-0.30', '3.60', '1.74']
w3.f12 | x | `which you can` | 5.67 | ['1.60', '0.84', '3.36']
w3.f13 | x | `the ticket you` | 7.36 | ['4.70', '1.81', '1.10']
w3.f14 |   | `'re looking for` | 2.41 | ['0.18', '1.21', '1.11']
w3.f15 | x | `up anger ,` | 5.50 | ['3.07', '-0.10', '2.70']
w3.f16 | x | `anger , enough` | 9.50 | ['1.11', '3.78', '4.99']
w3.f17 |   | `up anger ,` | 3.58 | ['2.46', '2.33', '-1.05']
w3.f18 |   | `ticket you need` | 3.17 | ['3.73', '1.20', '-1.30']
w3.f19 | x | `looking for an` | 5.47 | ['0.68', '2.83', '2.07']

## Original input: 
``` a fun family movie that 's @@UNK@@ for all ages -- a movie that will make you laugh , cry and realize , ' it 's never too late to believe in your dreams . ' ``` 

## Marked input: 
<pre>a fun <span style="background-color: #FFFF00">@</span>family <span style="background-color: #FFFF00">@</span>movie that <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>for <span style="background-color: #6698FF">@</span>all <span style="background-color: #6698FF">@</span>ages <span style="background-color: #FFFF00">@</span>-- <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>movie <span style="background-color: #FFFF00">@</span>that <span style="background-color: #FFFF00">@</span>will make <span style="background-color: #FFFF00">@</span>you <span style="background-color: #FFFF00">@</span>laugh <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span>cry <span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>realize <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>' it 's <span style="background-color: #6698FF">@</span>never <span style="background-color: #6698FF">@</span>too <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>late <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>believe <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>your <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>dreams <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>'</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `never too` | 6.82 | ['4.09', '3.11']
w2.f1 | x | `a movie` | 3.76 | ['2.95', '0.94']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `never too` | 3.51 | ['-0.02', '4.09']
w2.f4 | x | `a fun` | 6.15 | ['2.27', '4.07']
w2.f5 | x | `ages --` | 4.98 | ['3.42', '1.87']
w2.f6 |   | `laugh ,` | 3.06 | ['-0.78', '3.93']
w2.f7 | x | `in your` | 2.78 | ['0.14', '3.55']
w2.f8 | x | `make you` | 5.39 | ['1.47', '4.14']
w2.f9 | x | `late to` | 5.07 | ['0.42', '4.67']
w2.f10 | x | `ages --` | 7.35 | ['4.08', '3.41']
w2.f11 | x | `too late` | 5.79 | ['3.88', '2.18']
w2.f12 |   | `believe in` | 3.26 | ['1.33', '1.97']
w2.f13 | x | `@@UNK@@ for` | 3.24 | ['0.61', '2.78']
w2.f14 |   | `cry and` | 2.78 | ['2.80', '0.01']
w2.f15 | x | `make you` | 6.58 | ['0.86', '5.99']
w2.f16 | x | `too late` | 5.53 | ['2.26', '4.03']
w2.f17 | x | `in your` | 3.60 | ['0.54', '3.67']
w2.f18 | x | `and realize` | 5.82 | ['3.52', '2.43']
w2.f19 | x | `and realize` | 4.92 | ['3.66', '1.56']
w3.f0 | x | `laugh , cry` | 9.36 | ['-0.24', '-0.76', '10.75']
w3.f1 | x | `late to believe` | 9.46 | ['6.36', '0.48', '3.00']
w3.f2 | x | `movie that 's` | 3.95 | ['2.41', '1.53', '0.11']
w3.f3 |   | `@@UNK@@ for all` | 2.14 | ['-1.16', '0.98', '2.93']
w3.f4 | x | `will make you` | 5.48 | ['1.67', '1.70', '2.46']
w3.f5 | x | `to believe in` | 7.04 | ['0.53', '5.96', '0.88']
w3.f6 | x | `laugh , cry` | 7.46 | ['3.54', '0.38', '3.75']
w3.f7 | x | `to believe in` | 4.90 | ['3.76', '0.14', '1.49']
w3.f8 | x | `cry and realize` | 5.86 | ['0.88', '0.71', '4.56']
w3.f9 | x | `dreams . '` | 6.75 | ['1.05', '0.58', '5.23']
w3.f10 | x | `dreams . '` | 5.17 | ['3.57', '2.00', '-0.26']
w3.f11 | x | `it 's never` | 7.49 | ['1.01', '0.46', '6.21']
w3.f12 | x | `too late to` | 4.16 | ['4.03', '0.17', '0.10']
w3.f13 |   | `that will make` | 4.26 | ['2.51', '0.86', '1.13']
w3.f14 | x | `never too late` | 7.46 | ['0.09', '3.69', '3.77']
w3.f15 |   | `never too late` | 3.50 | ['-1.28', '3.12', '1.82']
w3.f16 | x | `all ages --` | 5.20 | ['1.41', '2.05', '2.10']
w3.f17 | x | `late to believe` | 5.11 | ['4.09', '1.66', '-0.49']
w3.f18 |   | `in your dreams` | 2.81 | ['-0.32', '1.86', '1.73']
w3.f19 | x | `cry and realize` | 5.16 | ['2.13', '1.18', '1.97']

## Original input: 
``` there 's nothing provocative about this film save for the ways in which it @@UNK@@ avoids provoking thought . ``` 

## Marked input: 
<pre>there 's <span style="background-color: #6698FF">@</span>nothing <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>provocative <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>about <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>this <span style="background-color: #FFFF00">@</span>film <span style="background-color: #FFFF00">@</span>save <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>for <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>ways <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>in <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>which <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>it <span style="background-color: #6698FF">@</span>@@UNK@@ avoids <span style="background-color: #FFFF00">@</span>provoking <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>thought <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ avoids` | 5.60 | ['1.98', '3.99']
w2.f1 | x | `@@UNK@@ avoids` | 6.59 | ['-0.88', '7.60']
w2.f2 |   | `film save` | 0.40 | ['-0.53', '1.98']
w2.f3 |   | `save for` | 1.56 | ['3.47', '-1.35']
w2.f4 |   | `provoking thought` | 2.53 | ['5.02', '-2.30']
w2.f5 | x | `this film` | 3.51 | ['2.84', '0.98']
w2.f6 |   | `nothing provocative` | 2.55 | ['0.58', '2.07']
w2.f7 |   | `save for` | 1.13 | ['3.65', '-1.61']
w2.f8 |   | `there 's` | 2.88 | ['-0.72', '3.82']
w2.f9 |   | `in which` | 3.18 | ['0.15', '3.04']
w2.f10 | x | `'s nothing` | 3.35 | ['2.75', '0.73']
w2.f11 |   | `provoking thought` | 1.22 | ['1.73', '-0.24']
w2.f12 | x | `'s nothing` | 8.36 | ['0.44', '7.96']
w2.f13 | x | `nothing provocative` | 6.85 | ['3.82', '3.18']
w2.f14 | x | `in which` | 5.13 | ['-0.13', '5.29']
w2.f15 | x | `this film` | 4.63 | ['3.03', '1.88']
w2.f16 | x | `film save` | 2.78 | ['0.91', '2.63']
w2.f17 | x | `avoids provoking` | 3.25 | ['3.36', '0.51']
w2.f18 |   | `avoids provoking` | 2.88 | ['3.41', '-0.41']
w2.f19 |   | `provocative about` | 2.57 | ['2.98', '-0.12']
w3.f0 |   | `this film save` | 2.46 | ['-1.03', '0.84', '3.04']
w3.f1 | x | `nothing provocative about` | 10.24 | ['6.02', '1.88', '2.72']
w3.f2 |   | `'s nothing provocative` | 3.37 | ['0.87', '2.01', '0.58']
w3.f3 | x | `avoids provoking thought` | 2.54 | ['3.22', '-0.82', '0.75']
w3.f4 |   | `for the ways` | 3.15 | ['1.21', '-2.22', '4.53']
w3.f5 |   | `provoking thought .` | 3.89 | ['1.37', '-1.47', '4.32']
w3.f6 | x | `for the ways` | 4.74 | ['1.51', '0.45', '2.99']
w3.f7 |   | `in which it` | 2.49 | ['1.23', '1.49', '0.27']
w3.f8 | x | `avoids provoking thought` | 6.99 | ['1.02', '3.17', '3.09']
w3.f9 | x | `film save for` | 4.66 | ['-0.53', '4.19', '1.11']
w3.f10 |   | `which it @@UNK@@` | 2.41 | ['2.23', '-0.54', '0.86']
w3.f11 |   | `ways in which` | 1.81 | ['2.38', '-0.61', '0.24']
w3.f12 |   | `film save for` | 3.79 | ['0.49', '2.47', '0.96']
w3.f13 | x | `the ways in` | 8.58 | ['4.70', '3.60', '0.53']
w3.f14 | x | `there 's nothing` | 4.63 | ['-0.30', '1.15', '3.87']
w3.f15 | x | `film save for` | 4.00 | ['-1.48', '6.05', '-0.40']
w3.f16 | x | `'s nothing provocative` | 6.73 | ['2.11', '1.22', '3.78']
w3.f17 | x | `save for the` | 6.50 | ['0.29', '5.11', '1.25']
w3.f18 |   | `@@PAD@@ @@PAD@@ there` | 0.00 | ['0.00', '0.00', '0.13']
w3.f19 | x | `avoids provoking thought` | 4.51 | ['3.41', '0.25', '0.97']

## Original input: 
``` @@UNK@@ 's structure and pacing are @@UNK@@ slack . ``` 

## Marked input: 
<pre>@@UNK@@ 's <span style="background-color: #FFFF00">@</span>structure <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>pacing <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>are <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>slack <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `pacing are` | 3.81 | ['2.49', '1.69']
w2.f1 |   | `@@UNK@@ 's` | 0.55 | ['-0.88', '1.57']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `'s structure` | 0.81 | ['-1.68', '3.05']
w2.f4 |   | `slack .` | 0.49 | ['0.70', '-0.03']
w2.f5 |   | `pacing are` | 0.41 | ['1.74', '-1.03']
w2.f6 |   | `'s structure` | 2.26 | ['1.03', '1.33']
w2.f7 |   | `@@UNK@@ slack` | 0.09 | ['-0.69', '1.69']
w2.f8 | x | `@@UNK@@ 's` | 3.81 | ['0.21', '3.82']
w2.f9 |   | `pacing are` | 3.20 | ['1.27', '1.94']
w2.f10 | x | `'s structure` | 3.47 | ['2.75', '0.85']
w2.f11 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f12 | x | `and pacing` | 4.81 | ['0.18', '4.66']
w2.f13 | x | `pacing are` | 3.53 | ['1.47', '2.20']
w2.f14 | x | `@@UNK@@ slack` | 4.80 | ['0.69', '4.14']
w2.f15 |   | `'s structure` | 3.08 | ['1.82', '1.53']
w2.f16 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f17 |   | `and pacing` | 2.72 | ['1.02', '2.31']
w2.f18 | x | `and pacing` | 3.50 | ['3.52', '0.10']
w2.f19 |   | `and pacing` | 2.98 | ['3.66', '-0.39']
w3.f0 |   | `structure and pacing` | 3.20 | ['3.18', '-1.09', '1.51']
w3.f1 |   | `are @@UNK@@ slack` | 0.45 | ['1.91', '-0.73', '-0.35']
w3.f2 |   | `'s structure and` | 3.04 | ['0.87', '1.79', '0.47']
w3.f3 |   | `@@PAD@@ @@PAD@@ @@UNK@@` | 0.00 | ['0.00', '0.00', '0.07']
w3.f4 |   | `@@UNK@@ 's structure` | 2.95 | ['0.36', '2.08', '0.88']
w3.f5 | x | `'s structure and` | 6.21 | ['0.63', '0.10', '5.81']
w3.f6 | x | `'s structure and` | 6.07 | ['3.62', '1.72', '0.95']
w3.f7 |   | `'s structure and` | 2.95 | ['-0.31', '1.92', '1.83']
w3.f8 |   | `and pacing are` | 3.33 | ['2.47', '0.03', '1.11']
w3.f9 |   | `@@PAD@@ @@PAD@@ @@UNK@@` | 2.03 | ['0.00', '0.00', '2.13']
w3.f10 | x | `slack . @@PAD@@` | 3.98 | ['2.12', '2.00', '0.00']
w3.f11 |   | `structure and pacing` | 3.68 | ['3.17', '-1.20', '1.90']
w3.f12 |   | `'s structure and` | 3.29 | ['-0.70', '2.98', '1.15']
w3.f13 |   | `@@UNK@@ slack .` | 5.19 | ['-0.04', '3.03', '2.45']
w3.f14 | x | `structure and pacing` | 4.13 | ['2.98', '1.09', '0.16']
w3.f15 |   | `slack . @@PAD@@` | 0.67 | ['1.36', '-0.52', '0.00']
w3.f16 |   | `'s structure and` | 0.92 | ['2.11', '1.88', '-2.69']
w3.f17 | x | `are @@UNK@@ slack` | 4.96 | ['2.67', '1.39', '1.06']
w3.f18 |   | `@@PAD@@ @@PAD@@ @@UNK@@` | 0.00 | ['0.00', '0.00', '-0.23']
w3.f19 | x | `and pacing are` | 7.46 | ['3.50', '-0.12', '4.20']

## Original input: 
``` the movie is hardly a masterpiece , but it does mark ms . bullock 's best work in some time . ``` 

## Marked input: 
<pre>the <span style="background-color: #6698FF">@</span>movie <span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hardly <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>masterpiece <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span>but <span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>does <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>mark <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>ms <span style="background-color: #FFFF00">@</span>. <span style="background-color: #6698FF">@</span>bullock <span style="background-color: #6698FF">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>best <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>work <span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>some <span style="background-color: #6698FF">@</span>time <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `does mark` | 7.42 | ['1.01', '6.79']
w2.f1 | x | `but it` | 5.95 | ['4.31', '1.78']
w2.f2 |   | `best work` | 0.59 | ['0.76', '0.88']
w2.f3 | x | `hardly a` | 2.80 | ['3.11', '0.24']
w2.f4 | x | `masterpiece ,` | 5.57 | ['3.26', '2.50']
w2.f5 | x | `bullock 's` | 5.04 | ['5.09', '0.26']
w2.f6 | x | `masterpiece ,` | 8.38 | ['4.55', '3.93']
w2.f7 |   | `does mark` | 1.67 | ['1.64', '0.94']
w2.f8 | x | `hardly a` | 5.33 | ['2.98', '2.56']
w2.f9 |   | `a masterpiece` | 1.67 | ['-0.54', '2.22']
w2.f10 | x | `a masterpiece` | 4.63 | ['1.97', '2.80']
w2.f11 | x | `it does` | 3.36 | ['0.00', '3.63']
w2.f12 | x | `is hardly` | 5.32 | ['-0.59', '5.94']
w2.f13 | x | `hardly a` | 4.07 | ['2.77', '1.45']
w2.f14 | x | `best work` | 5.93 | ['4.63', '1.34']
w2.f15 |   | `mark ms` | 1.83 | ['1.17', '0.94']
w2.f16 |   | `in some` | 2.56 | ['1.01', '2.31']
w2.f17 | x | `in some` | 4.12 | ['0.54', '4.19']
w2.f18 | x | `hardly a` | 4.21 | ['4.24', '0.10']
w2.f19 | x | `a masterpiece` | 4.57 | ['0.99', '3.88']
w3.f0 | x | `movie is hardly` | 3.85 | ['1.92', '2.08', '0.24']
w3.f1 |   | `best work in` | 3.01 | ['0.93', '1.03', '1.42']
w3.f2 | x | `@@PAD@@ the movie` | 4.78 | ['0.00', '0.94', '3.93']
w3.f3 |   | `it does mark` | 2.22 | ['-0.74', '1.99', '1.58']
w3.f4 | x | `hardly a masterpiece` | 5.07 | ['1.95', '0.29', '3.20']
w3.f5 | x | `some time .` | 8.46 | ['-0.11', '4.58', '4.32']
w3.f6 | x | `the movie is` | 5.60 | ['-0.32', '4.49', '1.64']
w3.f7 |   | `a masterpiece ,` | 3.44 | ['-0.02', '2.78', '1.18']
w3.f8 | x | `movie is hardly` | 5.21 | ['-0.93', '4.71', '1.71']
w3.f9 | x | `. bullock 's` | 4.75 | ['0.67', '3.04', '1.14']
w3.f10 | x | `ms . bullock` | 5.04 | ['0.91', '2.00', '2.27']
w3.f11 | x | `is hardly a` | 5.27 | ['0.29', '2.39', '2.78']
w3.f12 |   | `bullock 's best` | 2.80 | ['2.98', '-0.83', '0.77']
w3.f13 | x | `some time .` | 7.91 | ['4.29', '1.42', '2.45']
w3.f14 | x | `but it does` | 4.67 | ['1.72', '-0.67', '3.71']
w3.f15 |   | `. bullock 's` | 2.92 | ['0.68', '2.23', '0.17']
w3.f16 | x | `hardly a masterpiece` | 4.98 | ['1.40', '0.35', '3.60']
w3.f17 |   | `does mark ms` | 3.76 | ['-0.64', '1.64', '2.92']
w3.f18 |   | `mark ms .` | 3.08 | ['1.48', '3.02', '-0.95']
w3.f19 | x | `a masterpiece ,` | 10.48 | ['3.70', '5.82', '1.08']

## Original input: 
``` @@UNK@@ 's @@UNK@@ from little screen to big is far less painful than his opening scene encounter with an over - @@UNK@@ @@UNK@@ . ``` 

## Marked input: 
<pre>@@UNK@@ 's @@UNK@@ from little <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>screen <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>big <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>far <span style="background-color: #6698FF">@</span>less <span style="background-color: #6698FF">@</span>painful <span style="background-color: #6698FF">@</span>than <span style="background-color: #6698FF">@</span>his <span style="background-color: #6698FF">@</span>opening <span style="background-color: #FFFF00">@</span>scene <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>encounter <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>an <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>over <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>@@UNK@@ .</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `with an` | 3.48 | ['3.44', '0.41']
w2.f1 | x | `encounter with` | 4.68 | ['-0.06', '4.87']
w2.f2 |   | `from little` | 0.47 | ['0.61', '0.90']
w2.f3 | x | `is far` | 3.12 | ['0.28', '3.39']
w2.f4 | x | `an over` | 6.48 | ['5.09', '1.58']
w2.f5 | x | `an over` | 6.01 | ['3.50', '2.81']
w2.f6 |   | `@@UNK@@ from` | 1.55 | ['0.07', '1.58']
w2.f7 |   | `little screen` | 1.54 | ['1.59', '0.85']
w2.f8 | x | `encounter with` | 4.58 | ['1.29', '3.50']
w2.f9 | x | `screen to` | 5.40 | ['0.74', '4.67']
w2.f10 |   | `his opening` | 1.67 | ['0.58', '1.23']
w2.f11 | x | `opening scene` | 3.99 | ['0.86', '3.40']
w2.f12 | x | `less painful` | 5.17 | ['-0.90', '6.11']
w2.f13 | x | `less painful` | 4.87 | ['1.87', '3.15']
w2.f14 | x | `an over` | 4.28 | ['-0.05', '4.37']
w2.f15 |   | `scene encounter` | 1.87 | ['1.40', '0.74']
w2.f16 | x | `little screen` | 3.07 | ['1.14', '2.68']
w2.f17 | x | `little screen` | 5.94 | ['1.63', '4.93']
w2.f18 |   | `with an` | 2.39 | ['1.75', '0.75']
w2.f19 |   | `his opening` | 1.33 | ['1.37', '0.26']
w3.f0 | x | `less painful than` | 10.15 | ['8.00', '0.80', '1.74']
w3.f1 | x | `screen to big` | 4.26 | ['2.73', '0.48', '1.43']
w3.f2 | x | `far less painful` | 5.59 | ['1.95', '3.93', '-0.21']
w3.f3 |   | `opening scene encounter` | 1.44 | ['0.55', '1.34', '0.15']
w3.f4 |   | `little screen to` | 1.84 | ['-0.32', '3.29', '-0.77']
w3.f5 |   | `with an over` | 2.78 | ['4.85', '-0.83', '-0.91']
w3.f6 | x | `screen to big` | 7.23 | ['3.44', '0.76', '3.23']
w3.f7 | x | `an over -` | 7.21 | ['2.46', '3.44', '1.81']
w3.f8 | x | `from little screen` | 9.53 | ['5.16', '0.32', '4.34']
w3.f9 | x | `screen to big` | 5.60 | ['5.65', '0.70', '-0.64']
w3.f10 | x | `encounter with an` | 4.34 | ['1.37', '1.77', '1.34']
w3.f11 | x | `from little screen` | 6.08 | ['4.70', '1.10', '0.48']
w3.f12 | x | `scene encounter with` | 6.25 | ['3.11', '0.59', '2.68']
w3.f13 |   | `from little screen` | 4.79 | ['1.33', '1.16', '2.54']
w3.f14 | x | `from little screen` | 4.50 | ['2.08', '-0.52', '3.03']
w3.f15 |   | `encounter with an` | 3.73 | ['-0.62', '3.85', '0.67']
w3.f16 | x | `his opening scene` | 5.31 | ['0.62', '3.29', '1.78']
w3.f17 | x | `little screen to` | 4.28 | ['2.61', '2.08', '-0.25']
w3.f18 |   | `with an over` | 2.29 | ['0.27', '0.28', '2.20']
w3.f19 | x | `with an over` | 3.91 | ['3.68', '-2.19', '2.53']

## Original input: 
``` by turns fanciful , grisly and engagingly @@UNK@@ . ``` 

## Marked input: 
<pre>by <span style="background-color: #6698FF">@</span>turns <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>fanciful <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>grisly <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>engagingly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f1 |   | `and engagingly` | 1.73 | ['-1.18', '3.04']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `, grisly` | 1.34 | ['-2.07', '3.97']
w2.f4 |   | `fanciful ,` | 1.97 | ['-0.34', '2.50']
w2.f5 |   | `engagingly @@UNK@@` | 0.59 | ['1.61', '-0.71']
w2.f6 |   | `fanciful ,` | 2.28 | ['-1.55', '3.93']
w2.f7 |   | `grisly and` | 0.81 | ['1.63', '0.09']
w2.f8 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f9 |   | `turns fanciful` | 3.15 | ['2.71', '0.44']
w2.f10 |   | `grisly and` | 0.46 | ['-0.88', '1.48']
w2.f11 | x | `, grisly` | 2.89 | ['-0.67', '3.83']
w2.f12 | x | `by turns` | 3.76 | ['-1.10', '4.90']
w2.f13 | x | `by turns` | 4.05 | ['1.21', '2.99']
w2.f14 |   | `by turns` | 2.89 | ['0.78', '2.14']
w2.f15 | x | `, grisly` | 4.59 | ['2.19', '2.67']
w2.f16 |   | `grisly and` | 0.67 | ['2.70', '-1.27']
w2.f17 |   | `turns fanciful` | 0.44 | ['-0.90', '1.95']
w2.f18 | x | `and engagingly` | 4.19 | ['3.52', '0.80']
w2.f19 | x | `and engagingly` | 4.35 | ['3.66', '0.99']
w3.f0 |   | `, grisly and` | 3.67 | ['-0.85', '3.92', '0.99']
w3.f1 |   | `, grisly and` | 2.39 | ['1.74', '1.19', '-0.17']
w3.f2 | x | `, grisly and` | 4.57 | ['2.60', '1.58', '0.47']
w3.f3 |   | `turns fanciful ,` | 0.54 | ['0.37', '1.06', '-0.29']
w3.f4 |   | `fanciful , grisly` | 1.28 | ['1.07', '0.77', '-0.21']
w3.f5 |   | `fanciful , grisly` | 2.65 | ['1.28', '1.40', '0.29']
w3.f6 | x | `fanciful , grisly` | 3.97 | ['1.96', '0.38', '1.84']
w3.f7 | x | `, grisly and` | 5.08 | ['1.70', '2.04', '1.83']
w3.f8 |   | `@@PAD@@ @@PAD@@ by` | 0.00 | ['0.00', '0.00', '-3.74']
w3.f9 |   | `, grisly and` | 2.29 | ['-2.20', '2.20', '2.40']
w3.f10 |   | `@@UNK@@ . @@PAD@@` | 2.18 | ['0.33', '2.00', '0.00']
w3.f11 |   | `, grisly and` | 2.67 | ['-1.39', '3.66', '0.58']
w3.f12 |   | `@@PAD@@ by turns` | 2.93 | ['0.00', '3.26', '-0.19']
w3.f13 |   | `fanciful , grisly` | 4.33 | ['1.64', '1.92', '1.01']
w3.f14 | x | `@@PAD@@ by turns` | 4.45 | ['0.00', '2.00', '2.54']
w3.f15 |   | `turns fanciful ,` | 3.17 | ['-1.13', '1.77', '2.70']
w3.f16 | x | `by turns fanciful` | 4.01 | ['-0.86', '3.28', '1.96']
w3.f17 | x | `@@PAD@@ by turns` | 5.34 | ['0.00', '1.35', '4.14']
w3.f18 |   | `@@PAD@@ @@PAD@@ by` | 0.00 | ['0.00', '0.00', '-1.73']
w3.f19 |   | `fanciful , grisly` | 2.30 | ['0.47', '1.68', '0.26']

## Original input: 
``` never mind whether you buy the stuff about @@UNK@@ being a cia hit man . the @@UNK@@ yet @@UNK@@ vision clooney sustains throughout is daring , inventive and impressive . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>never <span style="background-color: #6698FF">@</span>mind <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>whether <span style="background-color: #FFFF00">@</span>you <span style="background-color: #FFFF00">@</span>buy <span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>stuff <span style="background-color: #6698FF">@</span>about <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>being <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>cia <span style="background-color: #6698FF">@</span>hit <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>man <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ yet <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>vision <span style="background-color: #FFFF00">@</span>clooney <span style="background-color: #FFFF00">@</span>sustains <span style="background-color: #FFFF00">@</span>throughout <span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>daring <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>inventive <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>impressive <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `mind whether` | 8.04 | ['6.30', '2.11']
w2.f1 | x | `stuff about` | 6.75 | ['4.93', '1.95']
w2.f2 |   | `vision clooney` | 0.21 | ['1.04', '0.22']
w2.f3 |   | `@@PAD@@ never` | 1.80 | ['0.00', '2.36']
w2.f4 | x | `vision clooney` | 6.18 | ['3.32', '3.05']
w2.f5 | x | `clooney sustains` | 7.14 | ['6.40', '1.05']
w2.f6 |   | `never mind` | 3.51 | ['2.07', '1.53']
w2.f7 |   | `mind whether` | 1.05 | ['0.40', '1.56']
w2.f8 | x | `whether you` | 3.95 | ['0.03', '4.14']
w2.f9 |   | `clooney sustains` | 4.57 | ['1.88', '2.71']
w2.f10 | x | `vision clooney` | 3.52 | ['4.80', '-1.14']
w2.f11 | x | `cia hit` | 5.31 | ['4.17', '1.41']
w2.f12 | x | `@@UNK@@ yet` | 4.37 | ['-0.28', '4.69']
w2.f13 |   | `a cia` | 1.12 | ['-0.98', '2.24']
w2.f14 |   | `being a` | 2.13 | ['1.79', '0.38']
w2.f15 | x | `, inventive` | 5.87 | ['2.19', '3.95']
w2.f16 |   | `a cia` | 0.95 | ['-0.39', '2.10']
w2.f17 |   | `throughout is` | 2.53 | ['2.34', '0.80']
w2.f18 | x | `and impressive` | 5.80 | ['3.52', '2.40']
w2.f19 | x | `and impressive` | 4.46 | ['3.66', '1.09']
w3.f0 | x | `being a cia` | 3.87 | ['1.87', '3.29', '-0.90']
w3.f1 | x | `cia hit man` | 4.90 | ['3.68', '1.07', '0.53']
w3.f2 | x | `buy the stuff` | 5.91 | ['5.17', '0.94', '-0.11']
w3.f3 | x | `yet @@UNK@@ vision` | 2.53 | ['1.05', '-0.06', '2.15']
w3.f4 |   | `@@PAD@@ @@PAD@@ never` | 3.48 | ['0.00', '0.00', '3.84']
w3.f5 | x | `, inventive and` | 9.02 | ['-0.52', '4.06', '5.81']
w3.f6 | x | `a cia hit` | 7.66 | ['1.76', '2.87', '3.24']
w3.f7 | x | `, inventive and` | 4.95 | ['1.70', '1.91', '1.83']
w3.f8 |   | `clooney sustains throughout` | 3.93 | ['0.82', '1.35', '2.04']
w3.f9 | x | `a cia hit` | 4.16 | ['-2.87', '5.42', '1.72']
w3.f10 | x | `stuff about @@UNK@@` | 5.79 | ['1.93', '3.15', '0.86']
w3.f11 | x | `@@PAD@@ @@PAD@@ never` | 6.02 | ['0.00', '0.00', '6.21']
w3.f12 | x | `about @@UNK@@ being` | 4.18 | ['0.83', '-0.16', '3.63']
w3.f13 | x | `hit man .` | 8.70 | ['4.89', '1.61', '2.45']
w3.f14 | x | `cia hit man` | 3.32 | ['0.19', '3.07', '0.16']
w3.f15 |   | `@@PAD@@ never mind` | 2.65 | ['0.00', '2.25', '0.56']
w3.f16 | x | `inventive and impressive` | 8.56 | ['6.77', '-0.30', '2.46']
w3.f17 | x | `cia hit man` | 5.72 | ['1.65', '0.36', '3.87']
w3.f18 | x | `never mind whether` | 4.39 | ['1.32', '2.30', '1.24']
w3.f19 | x | `throughout is daring` | 7.20 | ['2.06', '3.62', '1.64']

## Original input: 
``` if you love motown music , you 'll love this documentary . ``` 

## Marked input: 
<pre>if you love <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>motown <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>music <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>you <span style="background-color: #FFFF00">@</span>'ll <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>love <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>this <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>documentary <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `love motown` | 2.92 | ['2.34', '0.94']
w2.f1 | x | `motown music` | 4.43 | ['1.31', '3.25']
w2.f2 |   | `motown music` | 0.11 | ['0.63', '0.53']
w2.f3 |   | `you love` | 0.05 | ['0.42', '0.19']
w2.f4 | x | `music ,` | 7.51 | ['5.19', '2.50']
w2.f5 | x | `this documentary` | 4.72 | ['2.84', '2.18']
w2.f6 | x | `music ,` | 6.71 | ['2.88', '3.93']
w2.f7 |   | `you love` | 0.22 | ['0.12', '1.00']
w2.f8 | x | `motown music` | 6.96 | ['4.28', '2.89']
w2.f9 |   | `music ,` | 4.05 | ['3.73', '0.34']
w2.f10 | x | `you love` | 9.05 | ['4.16', '5.03']
w2.f11 |   | `you love` | 2.35 | ['1.83', '0.79']
w2.f12 | x | `motown music` | 4.27 | ['2.95', '1.36']
w2.f13 |   | `music ,` | 1.82 | ['-0.21', '2.18']
w2.f14 |   | `love motown` | 3.04 | ['1.66', '1.41']
w2.f15 | x | `, you` | 7.91 | ['2.19', '5.99']
w2.f16 | x | `love motown` | 3.16 | ['1.29', '2.63']
w2.f17 |   | `documentary .` | 1.13 | ['1.28', '0.47']
w2.f18 |   | `music ,` | 2.62 | ['1.85', '0.89']
w2.f19 |   | `you love` | 2.05 | ['0.48', '1.87']
w3.f0 | x | `love this documentary` | 6.21 | ['2.79', '1.65', '2.17']
w3.f1 |   | `, you 'll` | 2.22 | ['1.74', '-1.45', '2.31']
w3.f2 | x | `love motown music` | 3.73 | ['1.15', '0.49', '2.18']
w3.f3 |   | `documentary . @@PAD@@` | 1.08 | ['1.83', '-0.14', '0.00']
w3.f4 |   | `music , you` | 1.63 | ['-1.24', '0.77', '2.46']
w3.f5 | x | `'ll love this` | 6.24 | ['2.29', '4.59', '-0.30']
w3.f6 | x | `you love motown` | 3.90 | ['2.54', '0.29', '1.28']
w3.f7 |   | `love this documentary` | 2.85 | ['0.66', '0.43', '2.26']
w3.f8 | x | `love motown music` | 7.88 | ['1.08', '6.55', '0.54']
w3.f9 |   | `motown music ,` | 1.67 | ['0.76', '-2.04', '3.06']
w3.f10 | x | `you 'll love` | 4.97 | ['3.27', '0.76', '1.09']
w3.f11 | x | `love motown music` | 4.60 | ['3.30', '3.22', '-1.73']
w3.f12 |   | `motown music ,` | 2.17 | ['3.10', '-0.96', '0.16']
w3.f13 | x | `this documentary .` | 8.72 | ['3.44', '3.09', '2.45']
w3.f14 |   | `'ll love this` | 1.58 | ['-0.20', '2.22', '-0.35']
w3.f15 |   | `, you 'll` | 3.07 | ['1.52', '2.14', '-0.43']
w3.f16 | x | `love this documentary` | 5.84 | ['3.82', '1.31', '1.08']
w3.f17 |   | `music , you` | 1.93 | ['-1.05', '3.34', '-0.21']
w3.f18 | x | `motown music ,` | 3.92 | ['4.07', '-0.47', '0.79']
w3.f19 | x | `music , you` | 4.27 | ['0.45', '1.68', '2.24']

## Original input: 
``` [ @@UNK@@ ] takes a classic story , casts attractive and talented actors and uses a magnificent landscape to create a feature film that is wickedly fun to watch . ``` 

## Marked input: 
<pre>[ <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>] <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>takes <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>classic <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>story <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>casts <span style="background-color: #6698FF">@</span>attractive <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>talented <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>actors <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>uses <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>magnificent <span style="background-color: #FFFF00">@</span>landscape <span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>create <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>feature <span style="background-color: #FFFF00">@</span>film <span style="background-color: #FFFF00">@</span>that <span style="background-color: #FFFF00">@</span>is <span style="background-color: #FFFF00">@</span>wickedly <span style="background-color: #FFFF00">@</span>fun <span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span>watch <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ ]` | 7.99 | ['1.98', '6.38']
w2.f1 | x | `uses a` | 5.64 | ['4.79', '0.98']
w2.f2 |   | `and talented` | 0.42 | ['-0.97', '2.44']
w2.f3 |   | `and uses` | 1.20 | ['0.06', '1.69']
w2.f4 |   | `a feature` | 3.24 | ['2.27', '1.16']
w2.f5 |   | `, casts` | 2.55 | ['1.09', '1.77']
w2.f6 |   | `] takes` | 3.39 | ['1.16', '2.33']
w2.f7 |   | `@@PAD@@ [` | 1.30 | ['0.00', '2.21']
w2.f8 | x | `uses a` | 5.19 | ['2.85', '2.56']
w2.f9 |   | `and talented` | 4.53 | ['-0.02', '4.57']
w2.f10 | x | `and talented` | 3.59 | ['-0.04', '3.77']
w2.f11 | x | `a classic` | 4.34 | ['0.43', '4.18']
w2.f12 | x | `] takes` | 3.50 | ['2.73', '0.81']
w2.f13 |   | `uses a` | 1.99 | ['0.70', '1.45']
w2.f14 | x | `[ @@UNK@@` | 4.05 | ['3.78', '0.30']
w2.f15 | x | `wickedly fun` | 4.65 | ['1.37', '3.55']
w2.f16 | x | `talented actors` | 2.71 | ['2.58', '0.89']
w2.f17 | x | `@@PAD@@ [` | 5.03 | ['0.00', '5.65']
w2.f18 | x | `fun to` | 5.67 | ['3.29', '2.50']
w2.f19 | x | `and talented` | 4.06 | ['3.66', '0.70']
w3.f0 | x | `story , casts` | 7.06 | ['3.91', '-0.76', '4.30']
w3.f1 |   | `is wickedly fun` | 2.93 | ['1.18', '-1.40', '3.53']
w3.f2 | x | `a classic story` | 5.02 | ['1.87', '3.47', '-0.23']
w3.f3 |   | `] takes a` | 1.46 | ['1.49', '1.03', '-0.45']
w3.f4 | x | `] takes a` | 4.00 | ['2.23', '2.78', '-0.65']
w3.f5 | x | `talented actors and` | 6.52 | ['0.90', '0.13', '5.81']
w3.f6 |   | `a magnificent landscape` | 2.37 | ['1.76', '0.44', '0.38']
w3.f7 | x | `talented actors and` | 4.90 | ['1.61', '1.96', '1.83']
w3.f8 | x | `that is wickedly` | 5.81 | ['3.58', '4.71', '-2.19']
w3.f9 | x | `classic story ,` | 4.23 | ['1.26', '0.01', '3.06']
w3.f10 | x | `landscape to create` | 7.21 | ['1.66', '1.69', '4.01']
w3.f11 | x | `talented actors and` | 6.00 | ['5.36', '0.25', '0.58']
w3.f12 |   | `talented actors and` | 3.88 | ['1.95', '0.92', '1.15']
w3.f13 |   | `wickedly fun to` | 4.43 | ['1.98', '2.50', '0.20']
w3.f14 | x | `, casts attractive` | 6.77 | ['-0.18', '2.72', '4.31']
w3.f15 | x | `and talented actors` | 3.92 | ['-1.00', '4.82', '0.26']
w3.f16 | x | `is wickedly fun` | 5.00 | ['1.27', '1.76', '2.35']
w3.f17 |   | `, casts attractive` | 3.79 | ['0.73', '2.31', '0.91']
w3.f18 | x | `magnificent landscape to` | 5.33 | ['1.46', '2.82', '1.52']
w3.f19 | x | `a feature film` | 6.45 | ['3.70', '-0.64', '3.51']

## Original input: 
``` even horror fans will most likely not find what they 're seeking with trouble every day ; the movie lacks both thrills and humor . ``` 

## Marked input: 
<pre>even <span style="background-color: #6698FF">@</span>horror <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>fans <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>will <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>most <span style="background-color: #FFFF00">@</span>likely <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>not <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>find <span style="background-color: #6698FF">@</span>what <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>they <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>'re <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>seeking <span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>trouble <span style="background-color: #FFFF00">@</span>every <span style="background-color: #FFFF00">@</span>day ; the movie <span style="background-color: #6698FF">@</span>lacks <span style="background-color: #6698FF">@</span>both <span style="background-color: #6698FF">@</span>thrills <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>humor <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `horror fans` | 6.48 | ['1.52', '5.34']
w2.f1 | x | `seeking with` | 4.28 | ['-0.46', '4.87']
w2.f2 |   | `with trouble` | 0.14 | ['0.25', '0.93']
w2.f3 | x | `@@PAD@@ even` | 2.19 | ['0.00', '2.75']
w2.f4 | x | `most likely` | 4.01 | ['4.24', '-0.04']
w2.f5 | x | `what they` | 3.60 | ['2.99', '0.92']
w2.f6 |   | `both thrills` | 3.04 | ['2.21', '0.92']
w2.f7 |   | `even horror` | 1.14 | ['0.07', '1.98']
w2.f8 |   | `with trouble` | 2.30 | ['0.86', '1.65']
w2.f9 |   | `trouble every` | 3.63 | ['0.98', '2.66']
w2.f10 | x | `find what` | 4.12 | ['1.81', '2.44']
w2.f11 | x | `movie lacks` | 4.15 | ['-0.12', '4.54']
w2.f12 | x | `horror fans` | 4.60 | ['0.93', '3.70']
w2.f13 | x | `movie lacks` | 4.94 | ['3.71', '1.38']
w2.f14 | x | `humor .` | 5.00 | ['4.64', '0.39']
w2.f15 | x | `with trouble` | 4.59 | ['0.88', '3.98']
w2.f16 |   | `lacks both` | 2.12 | ['3.11', '-0.23']
w2.f17 |   | `horror fans` | 3.17 | ['-0.64', '4.43']
w2.f18 | x | `and humor` | 4.84 | ['3.52', '1.45']
w2.f19 | x | `and humor` | 6.71 | ['3.66', '3.34']
w3.f0 | x | `most likely not` | 6.42 | ['4.37', '1.86', '0.57']
w3.f1 |   | `horror fans will` | 1.87 | ['-0.94', '-0.51', '3.70']
w3.f2 | x | `movie lacks both` | 4.38 | ['2.41', '1.10', '0.96']
w3.f3 |   | `thrills and humor` | 1.95 | ['1.56', '-1.82', '2.82']
w3.f4 | x | `even horror fans` | 5.21 | ['3.48', '1.82', '0.28']
w3.f5 | x | `both thrills and` | 8.21 | ['1.63', '1.10', '5.81']
w3.f6 | x | `the movie lacks` | 5.51 | ['-0.32', '4.49', '1.55']
w3.f7 |   | `horror fans will` | 2.02 | ['-0.54', '1.76', '1.29']
w3.f8 | x | `horror fans will` | 6.01 | ['2.98', '3.70', '-0.40']
w3.f9 | x | `lacks both thrills` | 5.11 | ['3.42', '0.64', '1.15']
w3.f10 |   | `'re seeking with` | 2.65 | ['0.68', '2.42', '-0.30']
w3.f11 | x | `find what they` | 5.96 | ['2.70', '0.18', '3.27']
w3.f12 | x | `they 're seeking` | 5.89 | ['0.26', '1.90', '3.86']
w3.f13 |   | `horror fans will` | 3.32 | ['0.78', '4.77', '-1.98']
w3.f14 | x | `movie lacks both` | 3.64 | ['-1.35', '4.33', '0.75']
w3.f15 |   | `most likely not` | 3.44 | ['1.66', '2.29', '-0.35']
w3.f16 |   | `fans will most` | 2.27 | ['0.95', '0.00', '1.69']
w3.f17 | x | `most likely not` | 7.02 | ['0.69', '2.14', '4.34']
w3.f18 | x | `even horror fans` | 4.70 | ['0.05', '2.45', '2.67']
w3.f19 |   | `with trouble every` | 2.13 | ['3.68', '-2.06', '0.62']

## Original input: 
``` @@UNK@@ a familiar anti - feminist @@UNK@@ ( career - kids @@UNK@@ misery ) in tiresome romantic - comedy @@UNK@@ . ``` 

## Marked input: 
<pre>@@UNK@@ a familiar <span style="background-color: #FFFF00">@</span>anti <span style="background-color: #FFFF00">@</span>- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>feminist <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>( <span style="background-color: #6698FF">@</span>career <span style="background-color: #6698FF">@</span>- kids <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>misery <span style="background-color: #FFFF00">@</span>) <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>in <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>tiresome <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>romantic <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>comedy <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `( career` | 1.55 | ['2.98', '-1.05']
w2.f1 |   | `@@UNK@@ misery` | 2.56 | ['-0.88', '3.57']
w2.f2 |   | `tiresome romantic` | 0.53 | ['0.85', '0.72']
w2.f3 |   | `tiresome romantic` | 1.95 | ['1.49', '1.02']
w2.f4 | x | `a familiar` | 6.51 | ['2.27', '4.42']
w2.f5 |   | `) in` | 2.71 | ['2.11', '0.91']
w2.f6 |   | `in tiresome` | 2.58 | ['1.77', '0.91']
w2.f7 |   | `@@UNK@@ misery` | 0.68 | ['-0.69', '2.28']
w2.f8 | x | `romantic -` | 3.31 | ['1.67', '1.85']
w2.f9 |   | `@@UNK@@ misery` | 4.81 | ['2.38', '2.45']
w2.f10 | x | `- kids` | 4.72 | ['1.18', '3.67']
w2.f11 | x | `@@UNK@@ (` | 3.02 | ['-0.97', '4.26']
w2.f12 |   | `misery )` | 1.93 | ['1.07', '0.90']
w2.f13 | x | `feminist @@UNK@@` | 5.08 | ['5.33', '-0.10']
w2.f14 |   | `@@UNK@@ misery` | 2.33 | ['0.69', '1.68']
w2.f15 |   | `tiresome romantic` | 1.97 | ['1.43', '0.81']
w2.f16 | x | `tiresome romantic` | 4.01 | ['3.57', '1.21']
w2.f17 | x | `tiresome romantic` | 3.57 | ['2.80', '1.38']
w2.f18 | x | `familiar anti` | 3.41 | ['2.34', '1.20']
w2.f19 |   | `a familiar` | 2.15 | ['0.99', '1.46']
w3.f0 | x | `) in tiresome` | 5.64 | ['0.26', '1.29', '4.49']
w3.f1 | x | `) in tiresome` | 6.27 | ['1.80', '2.27', '2.57']
w3.f2 | x | `misery ) in` | 3.72 | ['2.35', '1.30', '0.16']
w3.f3 |   | `in tiresome romantic` | 1.85 | ['1.23', '0.44', '0.78']
w3.f4 | x | `@@UNK@@ misery )` | 5.29 | ['0.36', '2.21', '3.09']
w3.f5 |   | `- kids @@UNK@@` | 4.34 | ['0.99', '4.61', '-0.93']
w3.f6 |   | `in tiresome romantic` | 3.18 | ['-1.13', '4.78', '-0.27']
w3.f7 |   | `misery ) in` | 2.78 | ['1.77', '0.02', '1.49']
w3.f8 |   | `career - kids` | 3.85 | ['2.42', '-1.17', '2.88']
w3.f9 | x | `in tiresome romantic` | 11.70 | ['1.57', '6.75', '3.49']
w3.f10 |   | `) in tiresome` | 3.81 | ['1.86', '-0.64', '2.74']
w3.f11 | x | `tiresome romantic -` | 5.36 | ['5.47', '1.39', '-1.30']
w3.f12 | x | `romantic - comedy` | 6.21 | ['1.66', '2.81', '1.86']
w3.f13 |   | `in tiresome romantic` | 3.27 | ['0.07', '2.03', '1.42']
w3.f14 | x | `anti - feminist` | 6.32 | ['-0.91', '0.52', '6.81']
w3.f15 | x | `in tiresome romantic` | 7.00 | ['-0.49', '4.29', '3.37']
w3.f16 |   | `in tiresome romantic` | 1.19 | ['-1.02', '0.09', '2.49']
w3.f17 | x | `feminist @@UNK@@ (` | 6.54 | ['3.14', '1.39', '2.17']
w3.f18 |   | `in tiresome romantic` | 0.22 | ['-0.32', '-2.26', '3.26']
w3.f19 |   | `@@UNK@@ misery )` | 2.36 | ['-0.26', '0.24', '2.49']

## Original input: 
``` this is a @@UNK@@ film , once a good idea that was followed by the bad idea to turn it into a movie . ``` 

## Marked input: 
<pre>this is <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>film <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>once <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>good <span style="background-color: #FFFF00">@</span>idea <span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span>was <span style="background-color: #6698FF">@</span>followed <span style="background-color: #6698FF">@</span>by <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>bad <span style="background-color: #6698FF">@</span>idea <span style="background-color: #6698FF">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>turn <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>into <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>movie <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `was followed` | 1.73 | ['-0.59', '2.70']
w2.f1 | x | `a movie` | 3.76 | ['2.95', '0.94']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `bad idea` | 6.99 | ['3.46', '4.08']
w2.f4 | x | `film ,` | 3.64 | ['1.33', '2.50']
w2.f5 |   | `idea to` | 2.27 | ['0.18', '2.39']
w2.f6 |   | `film ,` | 3.99 | ['0.16', '3.93']
w2.f7 |   | `it into` | 0.03 | ['-0.01', '0.95']
w2.f8 |   | `into a` | 2.10 | ['-0.24', '2.56']
w2.f9 |   | `@@UNK@@ film` | 3.48 | ['2.38', '1.12']
w2.f10 | x | `a good` | 4.90 | ['1.97', '3.06']
w2.f11 |   | `bad idea` | 2.27 | ['-0.87', '3.41']
w2.f12 | x | `followed by` | 3.46 | ['-0.20', '3.71']
w2.f13 | x | `movie .` | 3.57 | ['3.71', '0.01']
w2.f14 | x | `that was` | 5.95 | ['0.85', '5.14']
w2.f15 | x | `, once` | 4.80 | ['2.19', '2.88']
w2.f16 | x | `was followed` | 4.71 | ['3.28', '2.19']
w2.f17 | x | `bad idea` | 4.98 | ['1.16', '4.44']
w2.f18 | x | `idea to` | 3.57 | ['1.19', '2.50']
w2.f19 | x | `a good` | 4.54 | ['0.99', '3.85']
w3.f0 | x | `idea that was` | 5.16 | ['4.66', '-0.36', '1.24']
w3.f1 | x | `film , once` | 4.07 | ['-0.29', '0.90', '3.84']
w3.f2 | x | `the bad idea` | 6.49 | ['-1.52', '5.83', '2.27']
w3.f3 |   | `once a good` | 1.38 | ['1.41', '-1.71', '2.29']
w3.f4 | x | `turn it into` | 4.27 | ['2.23', '-0.45', '2.85']
w3.f5 | x | `a movie .` | 5.82 | ['1.79', '0.04', '4.32']
w3.f6 | x | `a movie .` | 4.75 | ['1.76', '4.49', '-1.28']
w3.f7 | x | `to turn it` | 5.41 | ['3.76', '1.87', '0.27']
w3.f8 |   | `bad idea to` | 3.89 | ['2.53', '3.68', '-2.04']
w3.f9 | x | `bad idea to` | 7.00 | ['1.55', '5.95', '-0.38']
w3.f10 | x | `turn it into` | 4.51 | ['3.95', '-0.54', '1.24']
w3.f11 | x | `bad idea to` | 5.01 | ['5.12', '-1.98', '2.06']
w3.f12 | x | `the bad idea` | 7.59 | ['2.43', '2.46', '2.83']
w3.f13 | x | `this is a` | 6.17 | ['3.44', '2.81', '0.18']
w3.f14 | x | `idea that was` | 6.64 | ['3.63', '0.30', '2.81']
w3.f15 |   | `followed by the` | 3.55 | ['1.15', '3.36', '-0.79']
w3.f16 |   | `to turn it` | 3.22 | ['1.59', '0.15', '1.86']
w3.f17 | x | `idea to turn` | 11.23 | ['6.98', '1.66', '2.75']
w3.f18 | x | `once a good` | 4.31 | ['1.22', '-0.07', '3.62']
w3.f19 | x | `a @@UNK@@ film` | 4.70 | ['3.70', '-2.39', '3.51']

## Original input: 
``` the actors pull out all the stops in nearly every scene , but to @@UNK@@ effect . the characters never change . ``` 

## Marked input: 
<pre>the actors pull out <span style="background-color: #FFFF00">@</span>all <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>stops <span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>nearly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>every <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>scene <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>but <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>@@UNK@@ effect <span style="background-color: #FFFF00">@</span>. <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>characters <span style="background-color: #FFFF00">@</span>never <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>change <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ effect` | 4.75 | ['1.98', '3.15']
w2.f1 |   | `but to` | 3.54 | ['4.31', '-0.64']
w2.f2 |   | `nearly every` | 0.59 | ['0.80', '0.84']
w2.f3 |   | `characters never` | 1.08 | ['-0.72', '2.36']
w2.f4 |   | `the characters` | 0.90 | ['-1.38', '2.47']
w2.f5 | x | `stops in` | 4.36 | ['3.75', '0.91']
w2.f6 |   | `never change` | 3.50 | ['2.07', '1.52']
w2.f7 |   | `effect .` | 1.40 | ['2.17', '0.14']
w2.f8 |   | `characters never` | 1.01 | ['-1.12', '2.35']
w2.f9 |   | `effect .` | 3.88 | ['3.43', '0.46']
w2.f10 | x | `characters never` | 3.37 | ['0.62', '2.89']
w2.f11 | x | `every scene` | 3.95 | ['0.82', '3.40']
w2.f12 |   | `nearly every` | 2.83 | ['1.25', '1.62']
w2.f13 |   | `scene ,` | 1.61 | ['-0.42', '2.18']
w2.f14 | x | `effect .` | 3.63 | ['3.28', '0.39']
w2.f15 | x | `the characters` | 3.34 | ['-0.42', '4.03']
w2.f16 | x | `all the` | 3.95 | ['3.88', '0.83']
w2.f17 | x | `stops in` | 3.23 | ['3.04', '0.80']
w2.f18 |   | `out all` | 1.90 | ['2.90', '-0.88']
w2.f19 |   | `nearly every` | 2.36 | ['1.75', '0.91']
w3.f0 | x | `characters never change` | 6.15 | ['3.25', '1.27', '2.02']
w3.f1 |   | `pull out all` | 2.22 | ['2.35', '0.31', '-0.06']
w3.f2 | x | `never change .` | 8.42 | ['6.11', '1.55', '0.84']
w3.f3 | x | `pull out all` | 3.15 | ['-0.49', '1.31', '2.93']
w3.f4 | x | `the characters never` | 3.62 | ['-0.24', '0.38', '3.84']
w3.f5 |   | `never change .` | 4.47 | ['0.99', '-0.52', '4.32']
w3.f6 | x | `scene , but` | 4.35 | ['2.55', '0.38', '1.64']
w3.f7 | x | `stops in nearly` | 5.74 | ['2.49', '0.70', '3.04']
w3.f8 | x | `every scene ,` | 4.57 | ['-0.03', '2.74', '2.14']
w3.f9 | x | `nearly every scene` | 3.92 | ['0.36', '4.13', '-0.46']
w3.f10 | x | `characters never change` | 5.97 | ['1.23', '3.73', '1.16']
w3.f11 | x | `never change .` | 4.91 | ['3.52', '1.67', '-0.08']
w3.f12 | x | `nearly every scene` | 5.66 | ['-1.25', '1.38', '5.66']
w3.f13 |   | `the characters never` | 5.14 | ['4.70', '-0.42', '1.11']
w3.f14 | x | `nearly every scene` | 5.97 | ['4.67', '-0.72', '2.11']
w3.f15 | x | `nearly every scene` | 4.49 | ['1.68', '1.34', '1.64']
w3.f16 |   | `to @@UNK@@ effect` | 3.03 | ['1.59', '-0.81', '2.63']
w3.f17 |   | `, but to` | 3.28 | ['0.73', '2.96', '-0.25']
w3.f18 |   | `@@PAD@@ @@PAD@@ the` | 2.10 | ['0.00', '0.00', '2.57']
w3.f19 |   | `characters never change` | 3.31 | ['0.21', '3.22', '-0.01']

## Original input: 
``` mark wahlberg . . . may look @@UNK@@ in a ' 60s - homage @@UNK@@ hat , but as a character he 's dry , dry , dry . ``` 

## Marked input: 
<pre>mark <span style="background-color: #FFFF00">@</span>wahlberg <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>. . may <span style="background-color: #6698FF">@</span>look <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>in a <span style="background-color: #6698FF">@</span>' <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>60s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #6698FF">@</span>homage <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>hat <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>but as <span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>character <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>he <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>dry , <span style="background-color: #6698FF">@</span>dry <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>dry <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@PAD@@ mark` | 6.42 | ['0.00', '6.79']
w2.f1 | x | `but as` | 4.81 | ['4.31', '0.64']
w2.f2 |   | `character he` | 0.97 | ['1.16', '0.85']
w2.f3 |   | `@@PAD@@ mark` | 1.51 | ['0.00', '2.07']
w2.f4 | x | `a '` | 4.01 | ['2.27', '1.93']
w2.f5 |   | `look @@UNK@@` | 2.81 | ['3.83', '-0.71']
w2.f6 |   | `dry ,` | 2.97 | ['-0.86', '3.93']
w2.f7 |   | `homage @@UNK@@` | 1.18 | ['3.17', '-1.08']
w2.f8 | x | `character he` | 4.82 | ['2.05', '2.98']
w2.f9 |   | `@@UNK@@ in` | 4.26 | ['2.38', '1.89']
w2.f10 |   | `'s dry` | 2.31 | ['2.75', '-0.31']
w2.f11 | x | `homage @@UNK@@` | 2.96 | ['2.99', '0.25']
w2.f12 | x | `@@UNK@@ hat` | 3.64 | ['-0.28', '3.95']
w2.f13 |   | `character he` | 2.78 | ['1.03', '1.90']
w2.f14 | x | `may look` | 3.40 | ['0.80', '2.62']
w2.f15 | x | `character he` | 3.48 | ['2.16', '1.59']
w2.f16 |   | `a character` | 0.23 | ['-0.39', '1.38']
w2.f17 |   | `wahlberg .` | 3.11 | ['3.26', '0.47']
w2.f18 |   | `@@PAD@@ mark` | 3.03 | ['0.00', '3.15']
w2.f19 | x | `character he` | 4.26 | ['1.88', '2.67']
w3.f0 | x | `as a character` | 6.03 | ['-2.34', '3.29', '5.47']
w3.f1 |   | `homage @@UNK@@ hat` | 2.43 | ['1.15', '-0.73', '2.39']
w3.f2 | x | `a ' 60s` | 4.72 | ['1.87', '0.83', '2.11']
w3.f3 |   | `a character he` | 2.24 | ['-0.28', '1.65', '1.48']
w3.f4 |   | `mark wahlberg .` | 3.22 | ['2.97', '1.13', '-0.52']
w3.f5 | x | `, dry .` | 5.67 | ['-0.52', '2.20', '4.32']
w3.f6 |   | `- homage @@UNK@@` | 2.54 | ['0.68', '1.91', '0.15']
w3.f7 |   | `as a character` | 1.79 | ['1.64', '0.48', '0.17']
w3.f8 | x | `@@PAD@@ mark wahlberg` | 6.34 | ['0.00', '6.35', '0.27']
w3.f9 | x | `in a '` | 6.53 | ['1.57', '-0.16', '5.23']
w3.f10 |   | `- homage @@UNK@@` | 2.76 | ['-0.37', '2.42', '0.86']
w3.f11 | x | `a character he` | 4.02 | ['-0.77', '3.65', '1.34']
w3.f12 | x | `60s - homage` | 7.53 | ['1.82', '2.81', '3.03']
w3.f13 | x | `@@PAD@@ mark wahlberg` | 7.80 | ['0.00', '5.50', '2.55']
w3.f14 |   | `60s - homage` | 2.67 | ['-0.38', '0.52', '2.62']
w3.f15 | x | `. may look` | 3.83 | ['0.68', '0.71', '2.60']
w3.f16 |   | `hat , but` | 2.98 | ['0.91', '3.78', '-1.34']
w3.f17 | x | `dry , dry` | 5.65 | ['3.41', '3.34', '-0.94']
w3.f18 |   | `@@PAD@@ @@PAD@@ mark` | 1.90 | ['0.00', '0.00', '2.37']
w3.f19 | x | `a character he` | 3.92 | ['3.70', '-0.08', '0.42']

## Original input: 
``` if you believe any of this , i can make you a real deal on @@UNK@@ @@UNK@@ stock that will double in value a week from friday . ``` 

## Marked input: 
<pre>if you believe <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>any <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>this <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>i <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>can <span style="background-color: #6698FF">@</span>make you <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>real <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>deal <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>on <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>@@UNK@@ stock that will <span style="background-color: #6698FF">@</span>double <span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>value a <span style="background-color: #6698FF">@</span>week <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>from <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>friday .</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `you believe` | 3.62 | ['1.93', '2.07']
w2.f1 | x | `a week` | 4.21 | ['2.95', '1.40']
w2.f2 |   | `real deal` | 0.46 | ['-0.12', '1.62']
w2.f3 | x | `real deal` | 2.97 | ['0.89', '2.64']
w2.f4 | x | `you believe` | 4.35 | ['2.00', '2.55']
w2.f5 |   | `stock that` | 2.57 | ['1.56', '1.31']
w2.f6 | x | `this ,` | 4.12 | ['0.29', '3.93']
w2.f7 |   | `friday .` | 1.85 | ['2.62', '0.14']
w2.f8 | x | `make you` | 5.39 | ['1.47', '4.14']
w2.f9 |   | `a week` | 3.95 | ['-0.54', '4.51']
w2.f10 | x | `you believe` | 6.36 | ['4.16', '2.33']
w2.f11 | x | `real deal` | 4.32 | ['2.24', '2.35']
w2.f12 | x | `real deal` | 7.64 | ['3.34', '4.34']
w2.f13 | x | `real deal` | 6.24 | ['2.23', '4.16']
w2.f14 |   | `real deal` | 3.18 | ['1.20', '2.02']
w2.f15 | x | `make you` | 6.58 | ['0.86', '5.99']
w2.f16 |   | `from friday` | 1.84 | ['0.70', '1.91']
w2.f17 |   | `friday .` | 1.76 | ['1.91', '0.47']
w2.f18 |   | `i can` | 3.14 | ['1.52', '1.75']
w2.f19 |   | `you believe` | 2.55 | ['0.48', '2.37']
w3.f0 | x | `value a week` | 8.30 | ['-1.13', '3.29', '6.53']
w3.f1 | x | `real deal on` | 4.12 | ['3.68', '2.87', '-2.04']
w3.f2 |   | `, i can` | 3.46 | ['2.60', '0.71', '0.24']
w3.f3 |   | `real deal on` | 2.22 | ['0.40', '1.86', '0.57']
w3.f4 | x | `real deal on` | 4.68 | ['1.82', '3.16', '0.06']
w3.f5 |   | `@@PAD@@ @@PAD@@ if` | 4.58 | ['0.00', '0.00', '4.91']
w3.f6 | x | `a real deal` | 4.95 | ['1.76', '3.46', '-0.07']
w3.f7 |   | `, i can` | 3.54 | ['1.70', '1.03', '1.30']
w3.f8 |   | `that will double` | 4.28 | ['3.58', '1.17', '-0.19']
w3.f9 | x | `you believe any` | 5.67 | ['-0.60', '5.13', '1.25']
w3.f10 | x | `you believe any` | 6.34 | ['3.27', '3.57', '-0.35']
w3.f11 | x | `make you a` | 6.47 | ['0.27', '3.60', '2.78']
w3.f12 | x | `that will double` | 4.51 | ['2.12', '2.22', '0.29']
w3.f13 |   | `this , i` | 4.88 | ['3.44', '1.92', '-0.23']
w3.f14 | x | `friday . @@PAD@@` | 5.09 | ['5.85', '-0.66', '0.00']
w3.f15 |   | `believe any of` | 3.00 | ['-0.11', '1.27', '2.01']
w3.f16 | x | `real deal on` | 5.53 | ['5.40', '2.41', '-1.91']
w3.f17 | x | `this , i` | 5.16 | ['1.37', '3.34', '0.61']
w3.f18 | x | `you a real` | 3.54 | ['0.51', '-0.07', '3.57']
w3.f19 | x | `believe any of` | 4.48 | ['1.04', '0.89', '2.66']

## Original input: 
``` ' @@UNK@@ fans , or pretentious types who want to appear @@UNK@@ - @@UNK@@ will suck up to this project . . . ' ``` 

## Marked input: 
<pre>' @@UNK@@ fans <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>or <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>pretentious <span style="background-color: #6698FF">@</span>types <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>who <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>want <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>to <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>appear <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>- @@UNK@@ will <span style="background-color: #FFFF00">@</span>suck <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>up <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>this <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>project <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>'</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ fans` | 6.94 | ['1.98', '5.34']
w2.f1 |   | `suck up` | 2.98 | ['0.23', '2.88']
w2.f2 |   | `suck up` | 0.73 | ['0.18', '1.59']
w2.f3 | x | `or pretentious` | 2.09 | ['0.12', '2.53']
w2.f4 | x | `suck up` | 5.06 | ['4.09', '1.16']
w2.f5 |   | `this project` | 1.83 | ['2.84', '-0.71']
w2.f6 |   | `fans ,` | 3.97 | ['0.14', '3.93']
w2.f7 |   | `who want` | 1.68 | ['-0.06', '2.65']
w2.f8 | x | `suck up` | 4.12 | ['3.48', '0.85']
w2.f9 | x | `up to` | 5.77 | ['1.12', '4.67']
w2.f10 | x | `suck up` | 8.48 | ['1.68', '6.94']
w2.f11 |   | `suck up` | 1.78 | ['-0.53', '2.58']
w2.f12 | x | `to appear` | 4.36 | ['1.53', '2.87']
w2.f13 | x | `suck up` | 3.43 | ['1.35', '2.23']
w2.f14 | x | `fans ,` | 3.61 | ['2.76', '0.89']
w2.f15 |   | `this project` | 3.06 | ['3.03', '0.31']
w2.f16 |   | `pretentious types` | 2.62 | ['-1.02', '4.40']
w2.f17 | x | `types who` | 4.10 | ['2.51', '2.21']
w2.f18 | x | `will suck` | 3.54 | ['1.88', '1.79']
w2.f19 |   | `@@UNK@@ fans` | 1.73 | ['0.39', '1.63']
w3.f0 |   | `will suck up` | 2.97 | ['3.37', '-0.02', '0.00']
w3.f1 |   | `up to this` | 0.84 | ['1.84', '0.48', '-1.11']
w3.f2 | x | `, or pretentious` | 4.72 | ['2.60', '2.08', '0.12']
w3.f3 | x | `pretentious types who` | 3.01 | ['-0.58', '2.14', '2.05']
w3.f4 | x | `@@UNK@@ will suck` | 4.07 | ['0.36', '2.26', '1.81']
w3.f5 |   | `will suck up` | 3.53 | ['0.93', '1.04', '1.89']
w3.f6 |   | `or pretentious types` | 2.80 | ['-1.57', '3.90', '0.68']
w3.f7 |   | `to this project` | 3.98 | ['3.76', '0.43', '0.28']
w3.f8 | x | `@@UNK@@ fans ,` | 6.06 | ['0.50', '3.70', '2.14']
w3.f9 | x | `. . '` | 6.37 | ['0.67', '0.58', '5.23']
w3.f10 | x | `will suck up` | 5.77 | ['2.24', '-0.82', '4.51']
w3.f11 | x | `who want to` | 6.91 | ['0.78', '4.27', '2.06']
w3.f12 | x | `this project .` | 6.44 | ['0.35', '4.62', '1.61']
w3.f13 | x | `types who want` | 5.56 | ['1.57', '4.31', '-0.07']
w3.f14 | x | `or pretentious types` | 6.47 | ['2.94', '0.98', '2.64']
w3.f15 | x | `or pretentious types` | 4.30 | ['1.61', '1.35', '1.51']
w3.f16 |   | `fans , or` | 2.03 | ['0.95', '3.78', '-2.32']
w3.f17 | x | `this project .` | 4.96 | ['1.37', '2.78', '0.98']
w3.f18 | x | `types who want` | 6.57 | ['1.51', '2.93', '2.60']
w3.f19 | x | `up to this` | 6.35 | ['3.39', '0.71', '2.36']

## Original input: 
``` suffers from a lack of clarity and audacity that a subject as @@UNK@@ and pathetic as dahmer demands . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>suffers <span style="background-color: #6698FF">@</span>from <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>lack of <span style="background-color: #6698FF">@</span>clarity <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>audacity <span style="background-color: #FFFF00">@</span>that <span style="background-color: #FFFF00">@</span>a subject <span style="background-color: #FFFF00">@</span>as <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>and pathetic <span style="background-color: #6698FF">@</span>as <span style="background-color: #6698FF">@</span>dahmer <span style="background-color: #6698FF">@</span>demands <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `a subject` | 4.19 | ['1.11', '3.45']
w2.f1 |   | `a subject` | 3.07 | ['2.95', '0.25']
w2.f2 |   | `as dahmer` | 0.05 | ['0.54', '0.56']
w2.f3 | x | `pathetic as` | 2.58 | ['2.99', '0.15']
w2.f4 |   | `of clarity` | 3.28 | ['1.04', '2.43']
w2.f5 |   | `dahmer demands` | 1.27 | ['-0.00', '1.58']
w2.f6 |   | `suffers from` | 3.39 | ['1.91', '1.58']
w2.f7 |   | `pathetic as` | 1.48 | ['2.37', '0.02']
w2.f8 |   | `that a` | 3.04 | ['0.70', '2.56']
w2.f9 |   | `suffers from` | 4.12 | ['5.77', '-1.64']
w2.f10 | x | `clarity and` | 3.51 | ['2.17', '1.48']
w2.f11 |   | `and audacity` | 1.84 | ['0.34', '1.77']
w2.f12 | x | `@@PAD@@ suffers` | 4.14 | ['0.00', '4.18']
w2.f13 | x | `pathetic as` | 4.34 | ['3.19', '1.31']
w2.f14 |   | `demands .` | 3.09 | ['2.74', '0.39']
w2.f15 |   | `suffers from` | 2.23 | ['1.71', '0.79']
w2.f16 | x | `@@PAD@@ suffers` | 3.36 | ['0.00', '4.12']
w2.f17 |   | `dahmer demands` | 2.15 | ['0.81', '1.96']
w2.f18 | x | `and audacity` | 5.63 | ['3.52', '2.23']
w2.f19 |   | `and audacity` | 2.53 | ['3.66', '-0.84']
w3.f0 | x | `pathetic as dahmer` | 6.28 | ['5.02', '-0.29', '1.94']
w3.f1 |   | `@@PAD@@ suffers from` | 3.10 | ['0.00', '-0.60', '4.08']
w3.f2 | x | `@@PAD@@ @@PAD@@ suffers` | 5.24 | ['0.00', '0.00', '5.33']
w3.f3 |   | `that a subject` | 0.58 | ['2.19', '-1.71', '0.71']
w3.f4 |   | `pathetic as dahmer` | 1.49 | ['-0.25', '-0.73', '2.84']
w3.f5 | x | `of clarity and` | 7.76 | ['-0.94', '3.22', '5.81']
w3.f6 |   | `a lack of` | 2.68 | ['1.76', '1.91', '-0.79']
w3.f7 |   | `that a subject` | 1.99 | ['3.01', '0.48', '-1.01']
w3.f8 |   | `and pathetic as` | 3.54 | ['2.47', '2.01', '-0.66']
w3.f9 | x | `and pathetic as` | 4.40 | ['-2.57', '6.09', '0.99']
w3.f10 | x | `lack of clarity` | 6.25 | ['6.78', '-1.08', '0.70']
w3.f11 | x | `pathetic as dahmer` | 4.58 | ['3.85', '1.42', '-0.49']
w3.f12 | x | `pathetic as dahmer` | 6.73 | ['1.45', '4.53', '0.88']
w3.f13 |   | `dahmer demands .` | 3.51 | ['-1.37', '2.68', '2.45']
w3.f14 | x | `@@PAD@@ suffers from` | 7.42 | ['0.00', '4.91', '2.60']
w3.f15 |   | `@@PAD@@ suffers from` | 2.66 | ['0.00', '0.01', '2.82']
w3.f16 |   | `@@PAD@@ suffers from` | 2.13 | ['0.00', '-0.82', '3.33']
w3.f17 | x | `pathetic as dahmer` | 9.51 | ['6.39', '0.97', '2.31']
w3.f18 |   | `subject as @@UNK@@` | 2.61 | ['1.40', '1.90', '-0.23']
w3.f19 | x | `a subject as` | 4.63 | ['3.70', '-0.81', '1.86']

## Original input: 
``` it 's not particularly subtle . . . however , it still manages to build to a terrifying , if obvious , conclusion . ``` 

## Marked input: 
<pre>it 's <span style="background-color: #6698FF">@</span>not <span style="background-color: #6698FF">@</span>particularly <span style="background-color: #6698FF">@</span>subtle <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>. <span style="background-color: #6698FF">@</span>however <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>it <span style="background-color: #6698FF">@</span>still <span style="background-color: #6698FF">@</span>manages <span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span>build <span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>terrifying <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>if <span style="background-color: #FFFF00">@</span>obvious <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span>conclusion <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `a terrifying` | 6.62 | ['1.11', '5.88']
w2.f1 | x | `terrifying ,` | 5.20 | ['6.48', '-1.15']
w2.f2 |   | `terrifying ,` | 0.23 | ['2.00', '-0.72']
w2.f3 | x | `obvious ,` | 2.13 | ['2.25', '0.44']
w2.f4 | x | `still manages` | 8.46 | ['8.07', '0.57']
w2.f5 | x | `a terrifying` | 6.82 | ['0.71', '6.42']
w2.f6 | x | `terrifying ,` | 6.72 | ['2.88', '3.93']
w2.f7 |   | `obvious ,` | 1.65 | ['3.49', '-0.94']
w2.f8 | x | `terrifying ,` | 5.16 | ['6.16', '-0.79']
w2.f9 | x | `build to` | 5.52 | ['0.86', '4.67']
w2.f10 | x | `a terrifying` | 6.53 | ['1.97', '4.70']
w2.f11 |   | `it still` | 1.91 | ['0.00', '2.18']
w2.f12 |   | `'s not` | 1.76 | ['0.44', '1.35']
w2.f13 | x | `obvious ,` | 4.12 | ['2.09', '2.18']
w2.f14 | x | `however ,` | 6.61 | ['5.76', '0.89']
w2.f15 |   | `it still` | 2.85 | ['1.16', '1.97']
w2.f16 | x | `particularly subtle` | 3.07 | ['1.00', '2.83']
w2.f17 | x | `particularly subtle` | 5.05 | ['2.10', '3.56']
w2.f18 | x | `still manages` | 3.44 | ['0.45', '3.12']
w2.f19 | x | `still manages` | 5.58 | ['-0.32', '6.19']
w3.f0 |   | `conclusion . @@PAD@@` | 2.35 | ['2.75', '-0.01', '0.00']
w3.f1 | x | `to a terrifying` | 6.95 | ['-0.45', '-0.71', '8.48']
w3.f2 | x | `, conclusion .` | 6.52 | ['2.60', '3.16', '0.84']
w3.f3 |   | `a terrifying ,` | 1.27 | ['-0.28', '2.45', '-0.29']
w3.f4 |   | `terrifying , if` | 3.14 | ['1.76', '0.77', '0.96']
w3.f5 | x | `terrifying , if` | 8.45 | ['2.47', '1.40', '4.91']
w3.f6 | x | `. . however` | 8.26 | ['-0.68', '1.07', '8.08']
w3.f7 | x | `to a terrifying` | 6.19 | ['3.76', '0.48', '2.44']
w3.f8 | x | `a terrifying ,` | 6.63 | ['0.66', '4.12', '2.14']
w3.f9 | x | `. however ,` | 5.87 | ['0.67', '2.25', '3.06']
w3.f10 |   | `obvious , conclusion` | 3.78 | ['1.46', '-0.41', '2.87']
w3.f11 | x | `particularly subtle .` | 8.00 | ['5.72', '2.55', '-0.08']
w3.f12 | x | `however , it` | 4.94 | ['4.28', '-0.15', '0.94']
w3.f13 |   | `particularly subtle .` | 3.65 | ['-2.24', '3.69', '2.45']
w3.f14 | x | `conclusion . @@PAD@@` | 3.53 | ['4.29', '-0.66', '0.00']
w3.f15 | x | `. however ,` | 6.89 | ['0.68', '3.67', '2.70']
w3.f16 | x | `to a terrifying` | 7.07 | ['1.59', '0.35', '5.51']
w3.f17 | x | `it 's not` | 5.01 | ['1.06', '-0.23', '4.34']
w3.f18 | x | `still manages to` | 7.40 | ['4.25', '2.10', '1.52']
w3.f19 | x | `a terrifying ,` | 8.85 | ['3.70', '4.18', '1.08']

## Original input: 
``` its initial excitement settles into a warmed over pastiche . ``` 

## Marked input: 
<pre>its <span style="background-color: #6698FF">@</span>initial <span style="background-color: #6698FF">@</span>excitement <span style="background-color: #6698FF">@</span>settles <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>into <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span>warmed <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>over <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>pastiche <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `initial excitement` | 1.91 | ['-0.19', '2.47']
w2.f1 |   | `a warmed` | 1.74 | ['2.95', '-1.08']
w2.f2 |   | `a warmed` | 0.27 | ['0.10', '1.21']
w2.f3 |   | `a warmed` | 1.21 | ['-0.30', '2.07']
w2.f4 |   | `excitement settles` | 2.93 | ['0.60', '2.52']
w2.f5 |   | `settles into` | 2.46 | ['3.79', '-1.02']
w2.f6 |   | `@@PAD@@ its` | 1.45 | ['0.00', '1.55']
w2.f7 | x | `warmed over` | 2.71 | ['2.17', '1.44']
w2.f8 |   | `initial excitement` | 2.39 | ['1.42', '1.19']
w2.f9 |   | `over pastiche` | 3.31 | ['4.44', '-1.11']
w2.f10 |   | `settles into` | 2.31 | ['1.96', '0.48']
w2.f11 | x | `a warmed` | 3.10 | ['0.43', '2.94']
w2.f12 |   | `warmed over` | 2.66 | ['1.73', '0.96']
w2.f13 | x | `excitement settles` | 7.81 | ['1.61', '6.34']
w2.f14 | x | `warmed over` | 6.19 | ['1.85', '4.37']
w2.f15 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f16 |   | `a warmed` | 1.99 | ['-0.39', '3.14']
w2.f17 | x | `over pastiche` | 4.05 | ['-0.49', '5.16']
w2.f18 |   | `settles into` | 3.18 | ['1.19', '2.12']
w2.f19 |   | `excitement settles` | 2.57 | ['1.73', '1.13']
w3.f0 |   | `a warmed over` | 1.08 | ['-0.19', '1.89', '-0.23']
w3.f1 |   | `@@PAD@@ its initial` | 0.55 | ['0.00', '-0.28', '1.21']
w3.f2 |   | `excitement settles into` | 3.05 | ['1.58', '1.33', '0.23']
w3.f3 |   | `pastiche . @@PAD@@` | 0.43 | ['1.18', '-0.14', '0.00']
w3.f4 |   | `excitement settles into` | 1.32 | ['0.88', '-2.05', '2.85']
w3.f5 | x | `excitement settles into` | 7.15 | ['1.82', '0.81', '4.85']
w3.f6 | x | `@@PAD@@ its initial` | 3.73 | ['0.00', '0.89', '3.05']
w3.f7 |   | `@@PAD@@ @@PAD@@ its` | 4.09 | ['0.00', '0.00', '4.59']
w3.f8 |   | `its initial excitement` | 2.51 | ['1.38', '0.88', '0.54']
w3.f9 |   | `warmed over pastiche` | 3.63 | ['4.32', '-1.39', '0.81']
w3.f10 |   | `into a warmed` | 0.68 | ['-0.84', '1.32', '0.34']
w3.f11 |   | `@@PAD@@ @@PAD@@ its` | 2.69 | ['0.00', '0.00', '2.88']
w3.f12 | x | `warmed over pastiche` | 5.18 | ['3.94', '0.37', '1.00']
w3.f13 |   | `over pastiche .` | 3.82 | ['-0.01', '1.63', '2.45']
w3.f14 | x | `warmed over pastiche` | 3.71 | ['2.94', '0.36', '0.51']
w3.f15 |   | `into a warmed` | 3.66 | ['4.46', '-0.09', '-0.53']
w3.f16 |   | `warmed over pastiche` | 3.42 | ['3.09', '-0.26', '0.97']
w3.f17 |   | `settles into a` | 1.42 | ['5.08', '-1.57', '-1.92']
w3.f18 | x | `warmed over pastiche` | 4.06 | ['-0.73', '1.39', '3.87']
w3.f19 | x | `a warmed over` | 4.49 | ['3.70', '-1.63', '2.53']

## Original input: 
``` the @@UNK@@ @@UNK@@ you staged with your green @@UNK@@ @@UNK@@ men were more exciting and almost certainly made more sense . ``` 

## Marked input: 
<pre>the @@UNK@@ @@UNK@@ you <span style="background-color: #FFFF00">@</span>staged <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>your <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>green <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>men were <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>more <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>exciting <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>almost <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>certainly <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>made <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>more <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>sense <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ men` | 3.53 | ['1.98', '1.93']
w2.f1 | x | `staged with` | 5.36 | ['0.62', '4.87']
w2.f2 |   | `certainly made` | 0.54 | ['0.82', '0.76']
w2.f3 | x | `men were` | 2.44 | ['0.90', '2.09']
w2.f4 |   | `with your` | 2.11 | ['1.51', '0.79']
w2.f5 |   | `more exciting` | 2.32 | ['-0.44', '3.07']
w2.f6 | x | `more sense` | 5.00 | ['2.38', '2.72']
w2.f7 | x | `you staged` | 2.68 | ['0.12', '3.47']
w2.f8 | x | `staged with` | 4.65 | ['1.36', '3.50']
w2.f9 |   | `@@UNK@@ men` | 4.07 | ['2.38', '1.70']
w2.f10 | x | `with your` | 5.16 | ['1.55', '3.74']
w2.f11 | x | `were more` | 4.38 | ['3.01', '1.64']
w2.f12 |   | `were more` | 2.07 | ['2.30', '-0.19']
w2.f13 | x | `men were` | 5.69 | ['3.34', '2.49']
w2.f14 | x | `you staged` | 3.38 | ['-0.42', '3.83']
w2.f15 | x | `@@UNK@@ you` | 4.13 | ['-1.59', '5.99']
w2.f16 | x | `almost certainly` | 3.36 | ['1.88', '2.24']
w2.f17 | x | `almost certainly` | 3.80 | ['2.41', '2.01']
w2.f18 |   | `and almost` | 3.01 | ['3.52', '-0.39']
w2.f19 | x | `and almost` | 3.28 | ['3.66', '-0.08']
w3.f0 | x | `made more sense` | 5.71 | ['2.80', '4.04', '-0.74']
w3.f1 | x | `more exciting and` | 4.81 | ['4.72', '0.64', '-0.17']
w3.f2 | x | `certainly made more` | 8.26 | ['1.67', '2.00', '4.68']
w3.f3 |   | `you staged with` | 1.43 | ['0.34', '1.79', '-0.09']
w3.f4 |   | `staged with your` | 2.40 | ['0.84', '0.70', '1.22']
w3.f5 | x | `more exciting and` | 6.27 | ['0.77', '0.02', '5.81']
w3.f6 | x | `were more exciting` | 5.87 | ['0.31', '2.50', '3.27']
w3.f7 |   | `more exciting and` | 3.52 | ['-0.02', '2.21', '1.83']
w3.f8 |   | `and almost certainly` | 4.18 | ['2.47', '1.38', '0.61']
w3.f9 | x | `men were more` | 8.53 | ['1.05', '7.01', '0.58']
w3.f10 | x | `your green @@UNK@@` | 4.88 | ['4.47', '-0.30', '0.86']
w3.f11 | x | `you staged with` | 6.85 | ['1.07', '3.27', '2.70']
w3.f12 | x | `exciting and almost` | 5.74 | ['2.91', '0.95', '2.00']
w3.f13 | x | `men were more` | 6.11 | ['2.06', '2.57', '1.72']
w3.f14 | x | `were more exciting` | 7.03 | ['3.54', '4.60', '-1.02']
w3.f15 | x | `staged with your` | 3.84 | ['1.37', '3.85', '-1.21']
w3.f16 | x | `were more exciting` | 4.76 | ['2.79', '1.96', '0.39']
w3.f17 |   | `made more sense` | 3.04 | ['2.30', '1.98', '-1.08']
w3.f18 | x | `staged with your` | 3.81 | ['0.64', '2.32', '1.31']
w3.f19 | x | `almost certainly made` | 4.53 | ['0.88', '3.89', '-0.12']

## Original input: 
``` the movie succumbs to being nothing more than a formulaic chase in the dark . ``` 

## Marked input: 
<pre>the movie succumbs <span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>being <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>nothing <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>more <span style="background-color: #6698FF">@</span>than <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>formulaic <span style="background-color: #6698FF">@</span>chase <span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>dark <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `succumbs to` | 0.63 | ['1.45', '-0.45']
w2.f1 |   | `chase in` | 0.68 | ['0.54', '0.27']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `nothing more` | 2.20 | ['0.58', '2.17']
w2.f4 | x | `movie succumbs` | 4.05 | ['3.31', '0.93']
w2.f5 | x | `succumbs to` | 4.62 | ['2.53', '2.39']
w2.f6 |   | `movie succumbs` | 2.24 | ['1.65', '0.69']
w2.f7 |   | `formulaic chase` | 0.48 | ['0.67', '0.72']
w2.f8 |   | `than a` | 1.30 | ['-1.05', '2.56']
w2.f9 | x | `nothing more` | 5.77 | ['4.79', '0.99']
w2.f10 |   | `a formulaic` | 1.20 | ['1.97', '-0.64']
w2.f11 |   | `more than` | 1.98 | ['2.11', '0.14']
w2.f12 | x | `being nothing` | 9.38 | ['1.46', '7.96']
w2.f13 | x | `being nothing` | 4.58 | ['-1.23', '5.96']
w2.f14 |   | `formulaic chase` | 2.06 | ['-0.75', '2.85']
w2.f15 |   | `than a` | 0.98 | ['1.00', '0.25']
w2.f16 |   | `movie succumbs` | 2.21 | ['-0.37', '3.34']
w2.f17 |   | `movie succumbs` | 1.69 | ['-0.37', '2.68']
w2.f18 |   | `movie succumbs` | 2.94 | ['0.81', '2.25']
w2.f19 |   | `dark .` | 0.63 | ['2.21', '-1.28']
w3.f0 | x | `than a formulaic` | 5.69 | ['1.46', '3.29', '1.33']
w3.f1 | x | `succumbs to being` | 8.03 | ['3.76', '0.48', '4.17']
w3.f2 | x | `being nothing more` | 5.77 | ['-0.84', '2.01', '4.68']
w3.f3 |   | `to being nothing` | 0.19 | ['-0.69', '1.08', '0.41']
w3.f4 |   | `movie succumbs to` | 2.75 | ['2.80', '1.09', '-0.77']
w3.f5 |   | `the dark .` | 3.22 | ['-0.36', '-0.41', '4.32']
w3.f6 | x | `formulaic chase in` | 5.83 | ['2.13', '3.77', '0.14']
w3.f7 |   | `the movie succumbs` | 1.52 | ['-1.23', '2.56', '0.68']
w3.f8 |   | `nothing more than` | 2.67 | ['-0.39', '-0.18', '3.53']
w3.f9 |   | `formulaic chase in` | 3.32 | ['2.26', '1.26', '-0.08']
w3.f10 |   | `dark . @@PAD@@` | 1.61 | ['-0.24', '2.00', '0.00']
w3.f11 | x | `formulaic chase in` | 4.10 | ['0.40', '2.52', '1.38']
w3.f12 |   | `the dark .` | 3.44 | ['2.43', '-0.46', '1.61']
w3.f13 | x | `the dark .` | 11.89 | ['4.70', '4.99', '2.45']
w3.f14 | x | `succumbs to being` | 4.30 | ['3.54', '-0.41', '1.27']
w3.f15 |   | `dark . @@PAD@@` | 1.60 | ['2.29', '-0.52', '0.00']
w3.f16 |   | `succumbs to being` | 1.83 | ['1.71', '-0.49', '1.00']
w3.f17 | x | `succumbs to being` | 3.89 | ['0.64', '1.66', '1.75']
w3.f18 |   | `@@PAD@@ @@PAD@@ the` | 2.10 | ['0.00', '0.00', '2.57']
w3.f19 |   | `succumbs to being` | 1.59 | ['0.14', '0.71', '0.85']

## Original input: 
``` much like its easily @@UNK@@ take on the @@UNK@@ @@UNK@@ , there is n't much there here . ``` 

## Marked input: 
<pre>much <span style="background-color: #6698FF">@</span>like <span style="background-color: #6698FF">@</span>its <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>easily <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>take <span style="background-color: #FFFF00">@</span>on <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>@@UNK@@ , there is <span style="background-color: #6698FF">@</span>n't <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>much <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>there <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>here <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `@@UNK@@ take` | 4.79 | ['1.98', '3.18']
w2.f1 | x | `@@UNK@@ take` | 4.84 | ['-0.88', '5.85']
w2.f2 |   | `much there` | 0.13 | ['0.28', '0.89']
w2.f3 |   | `here .` | 1.07 | ['1.68', '-0.05']
w2.f4 | x | `take on` | 6.30 | ['5.42', '1.07']
w2.f5 | x | `like its` | 4.32 | ['3.40', '1.22']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `there here` | 0.29 | ['0.06', '1.14']
w2.f8 | x | `n't much` | 3.23 | ['0.91', '2.54']
w2.f9 |   | `its easily` | 4.28 | ['2.78', '1.52']
w2.f10 |   | `much like` | 2.86 | ['0.52', '2.47']
w2.f11 | x | `there here` | 3.95 | ['1.56', '2.65']
w2.f12 |   | `there here` | 3.38 | ['0.84', '2.58']
w2.f13 |   | `@@UNK@@ ,` | 2.64 | ['0.61', '2.18']
w2.f14 |   | `like its` | 2.20 | ['0.54', '1.69']
w2.f15 | x | `its easily` | 4.10 | ['-0.98', '5.35']
w2.f16 |   | `there here` | 1.83 | ['1.42', '1.17']
w2.f17 | x | `there here` | 4.01 | ['2.47', '2.16']
w2.f18 | x | `there here` | 3.57 | ['1.24', '2.44']
w2.f19 |   | `there here` | 1.36 | ['0.36', '1.30']
w3.f0 | x | `here . @@PAD@@` | 3.93 | ['4.32', '-0.01', '0.00']
w3.f1 | x | `like its easily` | 7.12 | ['3.51', '-0.28', '4.27']
w3.f2 | x | `there here .` | 4.15 | ['1.89', '1.51', '0.84']
w3.f3 |   | `like its easily` | 0.98 | ['-0.76', '-0.24', '2.58']
w3.f4 |   | `take on the` | 2.24 | ['0.76', '2.22', '-0.38']
w3.f5 | x | `there here .` | 5.66 | ['-0.51', '2.18', '4.32']
w3.f6 |   | `much there here` | 1.84 | ['1.84', '0.93', '-0.72']
w3.f7 |   | `there here .` | 4.07 | ['1.59', '2.80', '0.18']
w3.f8 |   | `@@UNK@@ @@UNK@@ ,` | 2.09 | ['0.50', '-0.27', '2.14']
w3.f9 | x | `n't much there` | 6.72 | ['2.93', '-0.44', '4.33']
w3.f10 | x | `here . @@PAD@@` | 6.14 | ['4.29', '2.00', '0.00']
w3.f11 |   | `n't much there` | 2.27 | ['0.77', '0.95', '0.75']
w3.f12 | x | `@@PAD@@ much like` | 6.01 | ['0.00', '1.24', '4.91']
w3.f13 |   | `there is n't` | 3.52 | ['1.13', '2.81', '-0.17']
w3.f14 | x | `@@PAD@@ much like` | 4.81 | ['0.00', '-0.74', '5.65']
w3.f15 | x | `n't much there` | 7.44 | ['3.56', '3.59', '0.46']
w3.f16 | x | `is n't much` | 3.96 | ['1.27', '2.52', '0.55']
w3.f17 | x | `there is n't` | 5.59 | ['-1.13', '2.35', '4.52']
w3.f18 | x | `take on the` | 3.55 | ['2.87', '-1.42', '2.57']
w3.f19 |   | `easily @@UNK@@ take` | 3.39 | ['3.28', '-2.39', '2.62']

## Original input: 
``` despite a powerful portrayal by binoche , it 's a period romance that suffers from an overly deliberate pace and uneven narrative momentum . ``` 

## Marked input: 
<pre>despite a <span style="background-color: #FFFF00">@</span>powerful <span style="background-color: #FFFF00">@</span>portrayal <span style="background-color: #FFFF00">@</span>by <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>binoche <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>a period romance that <span style="background-color: #6698FF">@</span>suffers <span style="background-color: #6698FF">@</span>from <span style="background-color: #6698FF">@</span>an <span style="background-color: #6698FF">@</span>overly <span style="background-color: #6698FF">@</span>deliberate <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>pace <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>uneven <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>narrative <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>momentum <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `deliberate pace` | 4.32 | ['1.08', '3.61']
w2.f1 | x | `despite a` | 4.23 | ['3.38', '0.98']
w2.f2 |   | `a powerful` | 0.88 | ['0.10', '1.82']
w2.f3 |   | `overly deliberate` | 1.17 | ['1.52', '0.20']
w2.f4 | x | `a powerful` | 7.78 | ['2.27', '5.70']
w2.f5 | x | `powerful portrayal` | 6.81 | ['5.32', '1.80']
w2.f6 | x | `binoche ,` | 4.47 | ['0.64', '3.93']
w2.f7 | x | `pace and` | 3.51 | ['4.33', '0.09']
w2.f8 |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 | x | `romance that` | 5.80 | ['4.72', '1.09']
w2.f10 | x | `a powerful` | 9.85 | ['1.97', '8.02']
w2.f11 |   | `pace and` | 1.30 | ['1.31', '0.27']
w2.f12 | x | `that suffers` | 5.69 | ['1.55', '4.18']
w2.f13 | x | `portrayal by` | 4.64 | ['1.32', '3.48']
w2.f14 | x | `and uneven` | 3.89 | ['0.13', '3.79']
w2.f15 | x | `overly deliberate` | 4.93 | ['3.85', '1.35']
w2.f16 |   | `that suffers` | 2.41 | ['-0.95', '4.12']
w2.f17 |   | `that suffers` | 0.98 | ['0.08', '1.51']
w2.f18 |   | `powerful portrayal` | 2.55 | ['1.63', '1.04']
w2.f19 |   | `powerful portrayal` | 3.17 | ['-0.37', '3.84']
w3.f0 | x | `pace and uneven` | 4.29 | ['3.20', '-1.09', '2.57']
w3.f1 |   | `a powerful portrayal` | 2.16 | ['-1.76', '2.08', '2.23']
w3.f2 | x | `romance that suffers` | 5.51 | ['-1.26', '1.53', '5.33']
w3.f3 | x | `and uneven narrative` | 2.49 | ['-0.66', '2.46', '1.29']
w3.f4 |   | `despite a powerful` | 3.48 | ['2.65', '0.29', '0.91']
w3.f5 |   | `deliberate pace and` | 4.32 | ['0.65', '-1.82', '5.81']
w3.f6 | x | `deliberate pace and` | 4.60 | ['1.23', '2.63', '0.95']
w3.f7 | x | `portrayal by binoche` | 6.60 | ['2.37', '1.28', '3.46']
w3.f8 | x | `by binoche ,` | 5.33 | ['1.21', '2.26', '2.14']
w3.f9 |   | `romance that suffers` | 3.58 | ['0.45', '1.05', '2.18']
w3.f10 | x | `overly deliberate pace` | 8.63 | ['5.26', '0.19', '3.32']
w3.f11 | x | `from an overly` | 5.74 | ['4.70', '-0.63', '1.86']
w3.f12 | x | `overly deliberate pace` | 5.79 | ['3.66', '1.27', '0.98']
w3.f13 |   | `@@PAD@@ despite a` | 2.26 | ['0.00', '2.33', '0.18']
w3.f14 | x | `that suffers from` | 6.97 | ['-0.45', '4.91', '2.60']
w3.f15 | x | `portrayal by binoche` | 4.06 | ['1.79', '3.36', '-0.92']
w3.f16 | x | `binoche , it` | 7.89 | ['2.63', '3.78', '1.86']
w3.f17 | x | `pace and uneven` | 6.20 | ['2.87', '1.30', '2.19']
w3.f18 | x | `deliberate pace and` | 4.06 | ['0.59', '6.06', '-2.13']
w3.f19 | x | `powerful portrayal by` | 6.28 | ['-0.80', '8.02', '-0.83']

## Original input: 
``` thanks to the château 's balance of @@UNK@@ , narrative @@UNK@@ and serious @@UNK@@ , almost every relationship and personality in the film @@UNK@@ surprises . ``` 

## Marked input: 
<pre><span style="background-color: #FFFF00">@</span>thanks <span style="background-color: #FFFF00">@</span>to <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>château <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>balance <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>narrative <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>serious @@UNK@@ , almost every <span style="background-color: #6698FF">@</span>relationship <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>personality <span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>film @@UNK@@ surprises .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ surprises` | 3.21 | ['1.98', '1.60']
w2.f1 |   | `château 's` | 2.63 | ['1.19', '1.57']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `relationship and` | 1.58 | ['2.90', '-0.76']
w2.f4 |   | `@@PAD@@ thanks` | 2.58 | ['0.00', '2.77']
w2.f5 | x | `thanks to` | 6.64 | ['4.56', '2.39']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `château 's` | 0.04 | ['1.59', '-0.64']
w2.f8 |   | `château 's` | 2.58 | ['-1.02', '3.82']
w2.f9 |   | `@@UNK@@ ,` | 2.70 | ['2.38', '0.34']
w2.f10 | x | `'s balance` | 4.48 | ['2.75', '1.87']
w2.f11 | x | `and personality` | 5.66 | ['0.34', '5.59']
w2.f12 |   | `personality in` | 3.21 | ['1.28', '1.97']
w2.f13 | x | `surprises .` | 3.20 | ['3.34', '0.01']
w2.f14 | x | `personality in` | 3.89 | ['3.32', '0.61']
w2.f15 | x | `'s balance` | 4.96 | ['1.82', '3.41']
w2.f16 |   | `every relationship` | 2.20 | ['2.04', '0.93']
w2.f17 |   | `personality in` | 2.68 | ['2.49', '0.80']
w2.f18 | x | `thanks to` | 5.99 | ['3.62', '2.50']
w2.f19 | x | `thanks to` | 4.83 | ['4.00', '1.12']
w3.f0 |   | `, almost every` | 3.22 | ['-0.85', '2.53', '1.93']
w3.f1 |   | `every relationship and` | 0.94 | ['0.15', '1.34', '-0.17']
w3.f2 |   | `narrative @@UNK@@ and` | 2.99 | ['3.26', '-0.65', '0.47']
w3.f3 |   | `in the film` | 0.05 | ['1.23', '-0.66', '0.09']
w3.f4 |   | `@@UNK@@ , almost` | 2.10 | ['0.36', '0.77', '1.33']
w3.f5 |   | `@@UNK@@ , narrative` | 2.68 | ['0.08', '1.40', '1.52']
w3.f6 | x | `, narrative @@UNK@@` | 4.60 | ['-1.13', '5.79', '0.15']
w3.f7 |   | `to the château` | 3.06 | ['3.76', '-0.92', '0.71']
w3.f8 | x | `@@PAD@@ @@PAD@@ thanks` | 4.53 | ['0.00', '0.00', '4.82']
w3.f9 | x | `almost every relationship` | 5.95 | ['1.55', '4.13', '0.38']
w3.f10 |   | `relationship and personality` | 3.88 | ['0.79', '-1.70', '4.94']
w3.f11 | x | `château 's balance` | 6.15 | ['5.20', '0.46', '0.69']
w3.f12 | x | `relationship and personality` | 4.83 | ['1.45', '0.95', '2.56']
w3.f13 | x | `the château 's` | 6.18 | ['4.70', '1.35', '0.39']
w3.f14 | x | `château 's balance` | 5.25 | ['5.11', '1.15', '-0.92']
w3.f15 |   | `, almost every` | 3.25 | ['1.52', '1.23', '0.67']
w3.f16 |   | `to the château` | 2.43 | ['1.59', '0.10', '1.13']
w3.f17 |   | `relationship and personality` | 2.50 | ['0.98', '1.30', '0.38']
w3.f18 | x | `balance of @@UNK@@` | 6.40 | ['4.99', '2.10', '-0.23']
w3.f19 | x | `'s balance of` | 5.75 | ['-0.49', '3.70', '2.66']

## Original input: 
``` reggio and glass so @@UNK@@ cynicism , with repetition and @@UNK@@ @@UNK@@ - @@UNK@@ sequences , that glass 's @@UNK@@ score becomes a @@UNK@@ - @@UNK@@ @@UNK@@ . ``` 

## Marked input: 
<pre>reggio <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>glass <span style="background-color: #FFFF00">@</span>so <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>cynicism <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span>repetition <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ - @@UNK@@ sequences <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>glass <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>score <span style="background-color: #6698FF">@</span>becomes <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>@@UNK@@ @@UNK@@ .</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `glass 's` | 1.53 | ['1.23', '0.68']
w2.f1 | x | `@@PAD@@ reggio` | 4.73 | ['0.00', '4.86']
w2.f2 |   | `score becomes` | 0.59 | ['0.52', '1.11']
w2.f3 |   | `sequences ,` | 1.27 | ['1.38', '0.44']
w2.f4 |   | `score becomes` | 2.60 | ['4.04', '-1.25']
w2.f5 |   | `, that` | 2.10 | ['1.09', '1.31']
w2.f6 |   | `cynicism ,` | 3.54 | ['-0.29', '3.93']
w2.f7 |   | `cynicism ,` | 0.08 | ['1.92', '-0.94']
w2.f8 | x | `glass 's` | 3.97 | ['0.36', '3.82']
w2.f9 | x | `@@UNK@@ score` | 5.16 | ['2.38', '2.79']
w2.f10 | x | `repetition and` | 3.70 | ['2.36', '1.48']
w2.f11 |   | `a @@UNK@@` | 0.41 | ['0.43', '0.25']
w2.f12 |   | `that glass` | 2.65 | ['1.55', '1.13']
w2.f13 | x | `repetition and` | 5.90 | ['5.48', '0.57']
w2.f14 | x | `@@UNK@@ score` | 3.58 | ['0.69', '2.93']
w2.f15 | x | `with repetition` | 3.93 | ['0.88', '3.32']
w2.f16 |   | `sequences ,` | 0.67 | ['2.97', '-1.54']
w2.f17 |   | `@@UNK@@ cynicism` | 1.86 | ['-2.10', '4.58']
w2.f18 |   | `and glass` | 2.39 | ['3.52', '-1.00']
w2.f19 | x | `and glass` | 4.73 | ['3.66', '1.36']
w3.f0 | x | `becomes a @@UNK@@` | 5.46 | ['3.76', '3.29', '-1.20']
w3.f1 | x | `, that glass` | 5.53 | ['1.74', '0.66', '3.50']
w3.f2 | x | `, with repetition` | 4.66 | ['2.60', '-0.49', '2.64']
w3.f3 | x | `that glass 's` | 3.08 | ['2.19', '1.19', '0.31']
w3.f4 |   | `@@UNK@@ score becomes` | 1.88 | ['0.36', '-0.85', '2.73']
w3.f5 | x | `with repetition and` | 7.77 | ['4.85', '-2.57', '5.81']
w3.f6 |   | `with repetition and` | 3.21 | ['2.33', '0.14', '0.95']
w3.f7 |   | `that glass 's` | 4.00 | ['3.01', '1.58', '-0.10']
w3.f8 | x | `@@UNK@@ sequences ,` | 5.73 | ['0.50', '3.37', '2.14']
w3.f9 |   | `@@PAD@@ reggio and` | 3.16 | ['0.00', '0.87', '2.40']
w3.f10 |   | `@@UNK@@ score becomes` | 2.36 | ['0.33', '0.55', '1.62']
w3.f11 |   | `that glass 's` | 0.79 | ['-1.63', '1.33', '1.27']
w3.f12 |   | `with repetition and` | 1.51 | ['0.57', '-0.08', '1.15']
w3.f13 |   | `that glass 's` | 3.34 | ['2.51', '0.68', '0.39']
w3.f14 | x | `so @@UNK@@ cynicism` | 4.59 | ['6.10', '0.79', '-2.20']
w3.f15 | x | `, with repetition` | 6.86 | ['1.52', '3.85', '1.66']
w3.f16 | x | `, that glass` | 3.88 | ['-0.14', '2.04', '2.35']
w3.f17 | x | `sequences , that` | 7.87 | ['4.48', '3.34', '0.21']
w3.f18 |   | `score becomes a` | 0.73 | ['2.11', '-0.54', '-0.37']
w3.f19 | x | `and glass so` | 7.10 | ['3.50', '3.40', '0.32']

## Original input: 
``` this @@UNK@@ , down - to - earth film is warm with the @@UNK@@ feeling of @@UNK@@ around old friends . ``` 

## Marked input: 
<pre>this @@UNK@@ , down - <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span>earth <span style="background-color: #6698FF">@</span>film <span style="background-color: #6698FF">@</span>is <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>warm <span style="background-color: #FFFF00">@</span>with <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>feeling of @@UNK@@ around old <span style="background-color: #6698FF">@</span>friends <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `down -` | 3.12 | ['4.98', '-1.49']
w2.f1 | x | `warm with` | 4.37 | ['-0.37', '4.87']
w2.f2 |   | `warm with` | 0.48 | ['1.17', '0.36']
w2.f3 |   | `@@UNK@@ around` | 1.55 | ['-0.08', '2.18']
w2.f4 |   | `around old` | 2.52 | ['-0.68', '3.39']
w2.f5 | x | `old friends` | 3.94 | ['1.76', '2.48']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `- earth` | 1.27 | ['-1.81', '3.99']
w2.f8 | x | `warm with` | 4.25 | ['0.97', '3.50']
w2.f9 |   | `- to` | 4.55 | ['-0.11', '4.67']
w2.f10 |   | `warm with` | 2.95 | ['2.83', '0.25']
w2.f11 | x | `friends .` | 3.31 | ['5.48', '-1.89']
w2.f12 | x | `old friends` | 5.01 | ['0.42', '4.63']
w2.f13 |   | `@@PAD@@ this` | 2.85 | ['0.00', '3.00']
w2.f14 |   | `@@UNK@@ feeling` | 2.86 | ['0.69', '2.21']
w2.f15 | x | `is warm` | 6.84 | ['1.15', '5.96']
w2.f16 |   | `film is` | 0.29 | ['0.91', '0.15']
w2.f17 |   | `- earth` | 1.85 | ['0.23', '2.23']
w2.f18 |   | `around old` | 2.38 | ['0.33', '2.17']
w2.f19 | x | `is warm` | 4.30 | ['0.37', '4.23']
w3.f0 | x | `around old friends` | 6.63 | ['3.94', '0.05', '3.03']
w3.f1 |   | `, down -` | 1.25 | ['1.74', '-1.77', '1.66']
w3.f2 | x | `old friends .` | 3.62 | ['2.89', '-0.03', '0.84']
w3.f3 |   | `film is warm` | 0.58 | ['0.63', '-0.61', '1.16']
w3.f4 |   | `warm with the` | 0.88 | ['0.92', '0.70', '-0.38']
w3.f5 | x | `is warm with` | 5.91 | ['0.80', '3.97', '1.46']
w3.f6 | x | `- earth film` | 3.90 | ['0.68', '3.17', '0.25']
w3.f7 |   | `, down -` | 3.89 | ['1.70', '0.87', '1.81']
w3.f8 | x | `film is warm` | 4.94 | ['-0.14', '4.71', '0.65']
w3.f9 |   | `@@PAD@@ this @@UNK@@` | 2.62 | ['0.00', '0.59', '2.13']
w3.f10 |   | `around old friends` | 3.60 | ['1.82', '1.10', '0.83']
w3.f11 | x | `around old friends` | 5.59 | ['6.22', '0.42', '-0.86']
w3.f12 | x | `to - earth` | 4.20 | ['1.38', '2.81', '0.14']
w3.f13 | x | `film is warm` | 5.75 | ['0.42', '2.81', '2.77']
w3.f14 | x | `around old friends` | 4.59 | ['4.13', '0.97', '-0.42']
w3.f15 | x | `down - to` | 3.98 | ['5.11', '-0.37', '-0.59']
w3.f16 | x | `film is warm` | 4.75 | ['-1.17', '-0.75', '7.04']
w3.f17 |   | `this @@UNK@@ ,` | 1.55 | ['1.37', '1.39', '-1.05']
w3.f18 | x | `warm with the` | 5.05 | ['0.62', '2.32', '2.57']
w3.f19 | x | `film is warm` | 4.47 | ['-1.24', '3.62', '2.21']

## Original input: 
``` what makes how i killed my father compelling , besides its terrific performances , is fontaine 's @@UNK@@ to @@UNK@@ into the dark @@UNK@@ of @@UNK@@ - child relationships without @@UNK@@ . ``` 

## Marked input: 
<pre>what makes <span style="background-color: #FFFF00">@</span>how <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>i <span style="background-color: #6698FF">@</span>killed <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>my <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>father <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>compelling <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>besides <span style="background-color: #FFFF00">@</span>its <span style="background-color: #FFFF00">@</span>terrific <span style="background-color: #FFFF00">@</span>performances <span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>is <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>fontaine <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>into <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>dark <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>@@UNK@@ - child <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>relationships <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>without <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `father compelling` | 3.31 | ['2.37', '1.32']
w2.f1 | x | `father compelling` | 6.50 | ['0.06', '6.57']
w2.f2 |   | `child relationships` | 1.05 | ['0.50', '1.59']
w2.f3 |   | `my father` | 1.82 | ['1.10', '1.29']
w2.f4 | x | `i killed` | 3.62 | ['3.61', '0.19']
w2.f5 | x | `what makes` | 6.30 | ['2.99', '3.61']
w2.f6 | x | `compelling ,` | 6.64 | ['2.81', '3.93']
w2.f7 |   | `father compelling` | 1.64 | ['1.17', '1.38']
w2.f8 | x | `fontaine 's` | 4.87 | ['1.27', '3.82']
w2.f9 | x | `@@UNK@@ to` | 7.04 | ['2.38', '4.67']
w2.f10 | x | `terrific performances` | 4.75 | ['-1.69', '6.58']
w2.f11 | x | `relationships without` | 4.97 | ['2.51', '2.73']
w2.f12 | x | `makes how` | 8.42 | ['0.99', '7.47']
w2.f13 |   | `besides its` | 3.14 | ['5.13', '-1.84']
w2.f14 | x | `@@UNK@@ into` | 3.56 | ['0.69', '2.90']
w2.f15 | x | `i killed` | 6.65 | ['-0.35', '7.28']
w2.f16 |   | `what makes` | 2.00 | ['0.04', '2.72']
w2.f17 | x | `makes how` | 4.82 | ['5.31', '0.12']
w2.f18 |   | `compelling ,` | 1.68 | ['0.91', '0.89']
w2.f19 | x | `killed my` | 3.57 | ['2.16', '1.71']
w3.f0 | x | `fontaine 's @@UNK@@` | 3.77 | ['3.44', '1.91', '-1.20']
w3.f1 | x | `performances , is` | 4.60 | ['5.96', '0.90', '-1.88']
w3.f2 | x | `- child relationships` | 5.44 | ['2.02', '1.49', '2.02']
w3.f3 | x | `relationships without @@UNK@@` | 3.59 | ['1.83', '2.29', '0.07']
w3.f4 |   | `besides its terrific` | 2.51 | ['0.16', '0.22', '2.48']
w3.f5 |   | `its terrific performances` | 4.76 | ['1.92', '0.79', '2.38']
w3.f6 |   | `performances , is` | 2.75 | ['0.94', '0.38', '1.64']
w3.f7 | x | `, besides its` | 6.78 | ['1.70', '0.98', '4.59']
w3.f8 | x | `its terrific performances` | 6.46 | ['1.38', '3.49', '1.87']
w3.f9 | x | `makes how i` | 5.65 | ['2.89', '2.06', '0.81']
w3.f10 | x | `killed my father` | 3.96 | ['0.86', '5.19', '-1.95']
w3.f11 |   | `fontaine 's @@UNK@@` | 2.33 | ['2.81', '0.46', '-0.75']
w3.f12 |   | `besides its terrific` | 2.97 | ['-0.43', '0.83', '2.69']
w3.f13 | x | `the dark @@UNK@@` | 7.77 | ['4.70', '4.99', '-1.67']
w3.f14 | x | `performances , is` | 3.22 | ['1.05', '-0.37', '2.63']
w3.f15 | x | `i killed my` | 4.69 | ['2.35', '1.48', '1.02']
w3.f16 | x | `- child relationships` | 7.33 | ['1.48', '1.03', '5.20']
w3.f17 | x | `makes how i` | 7.72 | ['2.29', '4.98', '0.61']
w3.f18 | x | `killed my father` | 6.40 | ['5.14', '0.34', '1.39']
w3.f19 | x | `its terrific performances` | 12.42 | ['3.31', '7.12', '2.10']

## Original input: 
``` millions of @@UNK@@ @@UNK@@ upon a project of such vast proportions need to @@UNK@@ more rewards than @@UNK@@ @@UNK@@ technique and stylish @@UNK@@ . ``` 

## Marked input: 
<pre>millions <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>@@UNK@@ @@UNK@@ upon a project <span style="background-color: #FFFF00">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>such <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>vast <span style="background-color: #6698FF">@</span>proportions <span style="background-color: #6698FF">@</span>need <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>more <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>rewards <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>than <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>@@UNK@@ technique and stylish <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ upon` | 3.75 | ['1.98', '2.14']
w2.f1 | x | `a project` | 4.68 | ['2.95', '1.86']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `vast proportions` | 1.96 | ['1.19', '1.33']
w2.f4 |   | `vast proportions` | 1.09 | ['2.34', '-1.05']
w2.f5 | x | `need to` | 6.07 | ['3.98', '2.39']
w2.f6 |   | `rewards than` | 1.45 | ['2.21', '-0.66']
w2.f7 |   | `such vast` | 1.20 | ['0.90', '1.20']
w2.f8 |   | `and stylish` | 0.89 | ['-0.15', '1.25']
w2.f9 | x | `need to` | 6.32 | ['1.66', '4.67']
w2.f10 |   | `a project` | 1.71 | ['1.97', '-0.12']
w2.f11 | x | `vast proportions` | 7.99 | ['0.88', '7.38']
w2.f12 |   | `vast proportions` | 1.83 | ['0.84', '1.03']
w2.f13 | x | `vast proportions` | 4.00 | ['2.94', '1.21']
w2.f14 |   | `technique and` | 2.47 | ['2.49', '0.01']
w2.f15 | x | `@@PAD@@ millions` | 3.76 | ['0.00', '4.04']
w2.f16 | x | `vast proportions` | 4.73 | ['-0.35', '5.84']
w2.f17 | x | `proportions need` | 4.46 | ['6.31', '-1.24']
w2.f18 | x | `and stylish` | 6.75 | ['3.52', '3.36']
w2.f19 | x | `and stylish` | 5.53 | ['3.66', '2.17']
w3.f0 | x | `such vast proportions` | 6.44 | ['2.67', '0.16', '4.00']
w3.f1 | x | `@@UNK@@ more rewards` | 4.13 | ['-3.01', '1.37', '6.15']
w3.f2 | x | `vast proportions need` | 5.13 | ['0.38', '4.69', '0.15']
w3.f3 |   | `@@PAD@@ @@PAD@@ millions` | 0.00 | ['0.00', '0.00', '0.37']
w3.f4 |   | `@@UNK@@ more rewards` | 3.13 | ['0.36', '-0.70', '3.83']
w3.f5 |   | `@@UNK@@ technique and` | 4.96 | ['0.08', '-0.60', '5.81']
w3.f6 | x | `@@UNK@@ more rewards` | 3.81 | ['-0.28', '2.50', '1.80']
w3.f7 |   | `more rewards than` | 1.87 | ['-0.02', '2.33', '0.06']
w3.f8 | x | `more rewards than` | 6.42 | ['-2.64', '5.80', '3.53']
w3.f9 | x | `such vast proportions` | 3.93 | ['2.19', '-0.48', '2.32']
w3.f10 |   | `@@UNK@@ more rewards` | 3.47 | ['0.33', '3.50', '-0.21']
w3.f11 | x | `proportions need to` | 5.56 | ['1.09', '2.60', '2.06']
w3.f12 | x | `project of such` | 5.23 | ['0.44', '3.24', '1.68']
w3.f13 | x | `more rewards than` | 9.10 | ['0.88', '7.54', '0.92']
w3.f14 | x | `@@UNK@@ more rewards` | 5.20 | ['-0.34', '4.60', '1.03']
w3.f15 |   | `such vast proportions` | 3.76 | ['1.65', '0.39', '1.89']
w3.f16 |   | `@@UNK@@ more rewards` | 2.73 | ['-1.96', '1.96', '3.12']
w3.f17 | x | `proportions need to` | 6.93 | ['6.14', '1.20', '-0.25']
w3.f18 | x | `proportions need to` | 6.18 | ['2.57', '2.55', '1.52']
w3.f19 | x | `a project of` | 6.45 | ['3.70', '0.20', '2.66']

## Original input: 
``` is truth @@UNK@@ than fiction ? in [ screenwriter ] charlie kaufman 's world , truth and fiction are equally strange , and his for the taking . ``` 

## Marked input: 
<pre>is truth @@UNK@@ <span style="background-color: #FFFF00">@</span>than <span style="background-color: #FFFF00">@</span>fiction <span style="background-color: #FFFF00">@</span>? in [ <span style="background-color: #6698FF">@</span>screenwriter <span style="background-color: #6698FF">@</span>] <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>charlie <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>kaufman <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>'s <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>world <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>truth <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>fiction <span style="background-color: #FFFF00">@</span>are <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>equally <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>strange <span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>his for <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>taking <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `screenwriter ]` | 7.35 | ['1.34', '6.38']
w2.f1 |   | `screenwriter ]` | 2.03 | ['1.45', '0.72']
w2.f2 |   | `truth @@UNK@@` | 0.05 | ['1.42', '-0.33']
w2.f3 |   | `are equally` | 1.74 | ['-1.16', '3.46']
w2.f4 |   | `world ,` | 3.14 | ['0.83', '2.50']
w2.f5 |   | `than fiction` | 2.87 | ['2.00', '1.17']
w2.f6 | x | `world ,` | 4.96 | ['1.13', '3.93']
w2.f7 |   | `in [` | 1.44 | ['0.14', '2.21']
w2.f8 | x | `kaufman 's` | 5.45 | ['1.85', '3.82']
w2.f9 |   | `? in` | 3.23 | ['1.35', '1.89']
w2.f10 | x | `'s world` | 9.73 | ['2.75', '7.11']
w2.f11 |   | `fiction ?` | 0.93 | ['0.24', '0.96']
w2.f12 |   | `? in` | 3.03 | ['1.10', '1.97']
w2.f13 | x | `his for` | 3.92 | ['1.28', '2.78']
w2.f14 | x | `[ screenwriter` | 3.20 | ['3.78', '-0.54']
w2.f15 | x | `, truth` | 5.36 | ['2.19', '3.44']
w2.f16 |   | `screenwriter ]` | 1.79 | ['1.00', '1.55']
w2.f17 | x | `in [` | 5.58 | ['0.54', '5.65']
w2.f18 | x | `] charlie` | 4.50 | ['2.35', '2.28']
w2.f19 |   | `and his` | 2.38 | ['3.66', '-0.99']
w3.f0 | x | `in [ screenwriter` | 7.43 | ['-0.14', '5.16', '2.80']
w3.f1 |   | `world , truth` | 3.44 | ['1.75', '0.90', '1.17']
w3.f2 | x | `fiction are equally` | 4.88 | ['0.41', '0.35', '4.21']
w3.f3 |   | `in [ screenwriter` | 2.28 | ['1.23', '0.67', '0.98']
w3.f4 | x | `and fiction are` | 3.51 | ['-0.23', '0.59', '3.51']
w3.f5 | x | `, truth and` | 5.75 | ['-0.52', '0.78', '5.81']
w3.f6 |   | `kaufman 's world` | 2.83 | ['3.76', '-1.47', '0.74']
w3.f7 |   | `fiction ? in` | 2.65 | ['1.32', '0.33', '1.49']
w3.f8 | x | `truth @@UNK@@ than` | 4.53 | ['1.55', '-0.27', '3.53']
w3.f9 | x | `screenwriter ] charlie` | 7.52 | ['5.07', '0.37', '2.18']
w3.f10 |   | `in [ screenwriter` | 3.64 | ['1.17', '-0.97', '3.59']
w3.f11 | x | `charlie kaufman 's` | 6.26 | ['1.13', '4.05', '1.27']
w3.f12 |   | `the taking .` | 3.63 | ['2.43', '-0.28', '1.61']
w3.f13 | x | `the taking .` | 11.09 | ['4.70', '4.20', '2.45']
w3.f14 | x | `[ screenwriter ]` | 4.58 | ['3.25', '0.72', '0.71']
w3.f15 | x | `equally strange ,` | 5.14 | ['1.67', '0.93', '2.70']
w3.f16 | x | `world , truth` | 6.14 | ['-0.67', '3.78', '3.40']
w3.f17 | x | `are equally strange` | 5.92 | ['2.67', '3.24', '0.16']
w3.f18 |   | `kaufman 's world` | 1.42 | ['-0.18', '0.79', '1.29']
w3.f19 | x | `and fiction are` | 8.38 | ['3.50', '0.80', '4.20']

## Original input: 
``` catch it . . . if you can ! ``` 

## Marked input: 
<pre>catch <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>. . if you <span style="background-color: #FFFF00">@</span>can <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>!</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `catch it` | 1.14 | ['-0.16', '1.67']
w2.f1 | x | `catch it` | 6.06 | ['4.42', '1.78']
w2.f2 |   | `@@PAD@@ catch` | 0.50 | ['0.00', '1.55']
w2.f3 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f4 |   | `catch it` | 2.31 | ['2.13', '0.36']
w2.f5 |   | `catch it` | 2.67 | ['2.74', '0.23']
w2.f6 |   | `catch it` | 3.81 | ['3.50', '0.41']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 | x | `catch it` | 3.34 | ['1.81', '1.75']
w2.f9 |   | `@@PAD@@ catch` | 1.94 | ['0.00', '1.95']
w2.f10 | x | `@@PAD@@ catch` | 5.48 | ['0.00', '5.61']
w2.f11 | x | `you can` | 3.73 | ['1.83', '2.17']
w2.f12 |   | `catch it` | 0.98 | ['0.05', '0.96']
w2.f13 |   | `catch it` | 2.32 | ['1.50', '0.96']
w2.f14 | x | `@@PAD@@ catch` | 5.22 | ['0.00', '5.26']
w2.f15 | x | `if you` | 5.81 | ['0.09', '5.99']
w2.f16 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f17 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f18 |   | `catch it` | 2.82 | ['1.85', '1.09']
w2.f19 |   | `you can` | 0.03 | ['0.48', '-0.15']
w3.f0 |   | `@@PAD@@ @@PAD@@ catch` | 3.44 | ['0.00', '0.00', '3.83']
w3.f1 |   | `@@PAD@@ @@PAD@@ catch` | 2.23 | ['0.00', '0.00', '2.61']
w3.f2 |   | `catch it .` | 3.49 | ['1.04', '1.70', '0.84']
w3.f3 |   | `@@PAD@@ @@PAD@@ catch` | 2.08 | ['0.00', '0.00', '2.68']
w3.f4 |   | `catch it .` | 1.88 | ['3.21', '-0.45', '-0.52']
w3.f5 |   | `@@PAD@@ catch it` | 3.81 | ['0.00', '3.75', '0.40']
w3.f6 | x | `you can !` | 6.31 | ['2.54', '0.69', '3.29']
w3.f7 |   | `@@PAD@@ @@PAD@@ catch` | 1.33 | ['0.00', '0.00', '1.83']
w3.f8 |   | `@@PAD@@ @@PAD@@ catch` | 3.52 | ['0.00', '0.00', '3.81']
w3.f9 |   | `. . if` | 1.75 | ['0.67', '0.58', '0.61']
w3.f10 | x | `you can !` | 6.37 | ['3.27', '1.16', '2.08']
w3.f11 |   | `if you can` | 2.34 | ['-2.81', '3.60', '1.74']
w3.f12 |   | `it . .` | 1.71 | ['0.79', '-0.56', '1.61']
w3.f13 |   | `it . .` | 4.56 | ['2.60', '-0.24', '2.45']
w3.f14 |   | `@@PAD@@ catch it` | 2.29 | ['0.00', '3.49', '-1.11']
w3.f15 |   | `catch it .` | 2.21 | ['0.75', '2.22', '-0.60']
w3.f16 |   | `@@PAD@@ @@PAD@@ catch` | 3.32 | ['0.00', '0.00', '3.70']
w3.f17 |   | `@@PAD@@ @@PAD@@ catch` | 0.08 | ['0.00', '0.00', '0.23']
w3.f18 |   | `catch it .` | 3.05 | ['5.57', '-1.10', '-0.95']
w3.f19 | x | `can ! @@PAD@@` | 4.01 | ['0.98', '3.15', '0.00']

## Original input: 
``` it all starts to smack of a hallmark @@UNK@@ of fame , with a few four letter words thrown in that are generally not heard on television . ``` 

## Marked input: 
<pre>it all <span style="background-color: #6698FF">@</span>starts <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>smack of a hallmark @@UNK@@ of fame , with <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>few <span style="background-color: #6698FF">@</span>four <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>letter <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>words <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>thrown <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>in <span style="background-color: #FFFF00">@</span>that <span style="background-color: #6698FF">@</span>are <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>generally <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>not <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>heard <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>on <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>television <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `words thrown` | 6.72 | ['5.26', '1.83']
w2.f1 |   | `letter words` | 2.38 | ['-0.60', '3.11']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `few four` | 2.18 | ['1.27', '1.46']
w2.f4 | x | `heard on` | 5.26 | ['4.39', '1.07']
w2.f5 | x | `few four` | 8.35 | ['2.03', '6.62']
w2.f6 |   | `in that` | 2.72 | ['1.77', '1.05']
w2.f7 | x | `are generally` | 2.44 | ['0.88', '2.46']
w2.f8 | x | `four letter` | 3.75 | ['2.52', '1.44']
w2.f9 |   | `starts to` | 4.83 | ['0.17', '4.67']
w2.f10 | x | `letter words` | 6.68 | ['2.34', '4.47']
w2.f11 | x | `heard on` | 3.83 | ['2.39', '1.71']
w2.f12 | x | `that are` | 4.09 | ['1.55', '2.57']
w2.f13 |   | `fame ,` | 2.77 | ['0.74', '2.18']
w2.f14 | x | `it all` | 3.38 | ['1.93', '1.48']
w2.f15 |   | `four letter` | 2.21 | ['1.04', '1.44']
w2.f16 | x | `all starts` | 3.01 | ['3.88', '-0.11']
w2.f17 |   | `generally not` | 0.98 | ['-0.99', '2.58']
w2.f18 | x | `letter words` | 6.32 | ['1.62', '4.82']
w2.f19 | x | `letter words` | 3.22 | ['2.39', '1.12']
w3.f0 |   | `with a few` | 2.95 | ['-2.36', '3.29', '2.41']
w3.f1 | x | `are generally not` | 3.80 | ['1.91', '2.17', '0.09']
w3.f2 | x | `, with a` | 4.29 | ['2.60', '-0.49', '2.27']
w3.f3 |   | `@@PAD@@ it all` | 1.99 | ['0.00', '-0.33', '2.93']
w3.f4 | x | `four letter words` | 5.29 | ['3.03', '-0.46', '3.08']
w3.f5 |   | `are generally not` | 4.92 | ['0.98', '-0.31', '4.57']
w3.f6 | x | `it all starts` | 3.81 | ['0.54', '-0.55', '4.03']
w3.f7 |   | `to smack of` | 2.76 | ['3.76', '1.67', '-2.18']
w3.f8 | x | `that are generally` | 5.42 | ['3.58', '0.28', '1.84']
w3.f9 | x | `four letter words` | 3.68 | ['1.08', '1.44', '1.26']
w3.f10 | x | `in that are` | 4.18 | ['1.17', '-0.63', '3.78']
w3.f11 | x | `with a few` | 5.04 | ['0.40', '0.22', '4.62']
w3.f12 | x | `that are generally` | 5.54 | ['2.12', '2.18', '1.37']
w3.f13 | x | `that are generally` | 5.45 | ['2.51', '2.28', '0.90']
w3.f14 |   | `it all starts` | 1.56 | ['0.08', '2.00', '-0.43']
w3.f15 | x | `few four letter` | 5.50 | ['5.65', '-0.16', '0.18']
w3.f16 | x | `four letter words` | 8.51 | ['4.11', '3.20', '1.58']
w3.f17 | x | `are generally not` | 8.25 | ['2.67', '1.39', '4.34']
w3.f18 | x | `generally not heard` | 3.91 | ['3.42', '-0.14', '1.09']
w3.f19 | x | `few four letter` | 5.63 | ['1.87', '1.81', '2.07']

## Original input: 
``` a sly @@UNK@@ of the @@UNK@@ of the contemporary music business and a rather sad story of the @@UNK@@ of artistic @@UNK@@ . ``` 

## Marked input: 
<pre>a sly <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>the @@UNK@@ of the <span style="background-color: #FFFF00">@</span>contemporary <span style="background-color: #FFFF00">@</span>music <span style="background-color: #FFFF00">@</span>business <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>a <span style="background-color: #FFFF00">@</span>rather <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>sad <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>story <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>of artistic <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `music business` | 4.32 | ['1.27', '3.42']
w2.f1 |   | `a rather` | 3.52 | ['2.95', '0.71']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `a rather` | 0.74 | ['-0.30', '1.60']
w2.f4 | x | `a sly` | 4.59 | ['2.27', '2.51']
w2.f5 | x | `contemporary music` | 3.30 | ['3.42', '0.18']
w2.f6 |   | `music business` | 3.29 | ['2.88', '0.51']
w2.f7 |   | `business and` | 0.28 | ['1.10', '0.09']
w2.f8 |   | `@@PAD@@ a` | 2.34 | ['0.00', '2.56']
w2.f9 |   | `@@UNK@@ of` | 4.02 | ['2.38', '1.65']
w2.f10 | x | `a sly` | 7.77 | ['1.97', '5.94']
w2.f11 | x | `rather sad` | 2.92 | ['1.17', '2.02']
w2.f12 |   | `sad story` | 1.57 | ['1.39', '0.22']
w2.f13 |   | `a sly` | 1.87 | ['-0.98', '3.00']
w2.f14 |   | `the contemporary` | 1.61 | ['0.10', '1.55']
w2.f15 | x | `rather sad` | 3.60 | ['1.67', '2.20']
w2.f16 |   | `sad story` | 2.16 | ['3.38', '-0.46']
w2.f17 |   | `sad story` | 1.16 | ['1.33', '0.45']
w2.f18 | x | `and a` | 3.49 | ['3.52', '0.10']
w2.f19 | x | `sad story` | 3.68 | ['2.59', '1.38']
w3.f0 |   | `rather sad story` | 3.48 | ['1.32', '1.72', '0.83']
w3.f1 |   | `sly @@UNK@@ of` | 2.65 | ['3.90', '-0.73', '-0.14']
w3.f2 |   | `the contemporary music` | 2.20 | ['-1.52', '1.63', '2.18']
w3.f3 |   | `a sly @@UNK@@` | 0.47 | ['-0.28', '1.29', '0.07']
w3.f4 |   | `rather sad story` | 1.64 | ['-0.27', '0.82', '1.45']
w3.f5 | x | `music business and` | 5.56 | ['2.13', '-2.05', '5.81']
w3.f6 | x | `a rather sad` | 4.17 | ['1.76', '-0.21', '2.83']
w3.f7 |   | `@@UNK@@ of artistic` | 1.60 | ['-2.01', '0.18', '3.93']
w3.f8 |   | `a rather sad` | 3.96 | ['0.66', '1.32', '2.27']
w3.f9 |   | `a rather sad` | 2.01 | ['-2.87', '3.93', '1.06']
w3.f10 | x | `of artistic @@UNK@@` | 3.99 | ['2.92', '0.36', '0.86']
w3.f11 |   | `@@PAD@@ @@PAD@@ a` | 2.59 | ['0.00', '0.00', '2.78']
w3.f12 |   | `@@UNK@@ of artistic` | 4.00 | ['-0.75', '3.24', '1.64']
w3.f13 | x | `the contemporary music` | 8.03 | ['4.70', '3.61', '-0.03']
w3.f14 | x | `rather sad story` | 3.06 | ['4.27', '-0.29', '-0.83']
w3.f15 |   | `a rather sad` | 2.36 | ['-2.48', '3.59', '1.42']
w3.f16 | x | `of the contemporary` | 5.17 | ['1.87', '0.10', '3.59']
w3.f17 |   | `rather sad story` | 3.14 | ['2.30', '0.81', '0.19']
w3.f18 | x | `story of the` | 3.88 | ['-0.32', '2.10', '2.57']
w3.f19 | x | `a sly @@UNK@@` | 4.00 | ['3.70', '2.44', '-2.02']

## Original input: 
``` . . . the whole thing @@UNK@@ only in making me @@UNK@@ . ``` 

## Marked input: 
<pre>. . . the whole <span style="background-color: #6698FF">@</span>thing <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>only <span style="background-color: #6698FF">@</span>in <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>making <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>me <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `making me` | 2.06 | ['2.19', '0.24']
w2.f1 |   | `in making` | 1.41 | ['-1.00', '2.54']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `the whole` | 2.36 | ['-1.34', '4.26']
w2.f4 |   | `making me` | 1.79 | ['2.20', '-0.22']
w2.f5 |   | `me @@UNK@@` | 1.05 | ['2.07', '-0.71']
w2.f6 |   | `in making` | 2.88 | ['1.77', '1.21']
w2.f7 |   | `in making` | 0.69 | ['0.14', '1.46']
w2.f8 |   | `me @@UNK@@` | 1.61 | ['2.54', '-0.71']
w2.f9 |   | `@@UNK@@ only` | 3.06 | ['2.38', '0.70']
w2.f10 | x | `making me` | 3.42 | ['2.59', '0.97']
w2.f11 | x | `thing @@UNK@@` | 3.28 | ['3.30', '0.25']
w2.f12 | x | `whole thing` | 6.34 | ['1.06', '5.32']
w2.f13 | x | `only in` | 5.80 | ['6.80', '-0.85']
w2.f14 | x | `@@UNK@@ only` | 6.58 | ['0.69', '5.93']
w2.f15 |   | `only in` | 1.99 | ['2.27', '-0.01']
w2.f16 | x | `making me` | 4.99 | ['-0.42', '6.17']
w2.f17 |   | `making me` | 2.84 | ['0.67', '2.79']
w2.f18 |   | `in making` | 1.66 | ['0.66', '1.12']
w2.f19 |   | `@@UNK@@ only` | 1.35 | ['0.39', '1.26']
w3.f0 |   | `making me @@UNK@@` | 1.22 | ['1.06', '1.75', '-1.20']
w3.f1 |   | `@@PAD@@ @@PAD@@ .` | 0.00 | ['0.00', '0.00', '-1.96']
w3.f2 | x | `whole thing @@UNK@@` | 4.66 | ['2.23', '2.84', '-0.31']
w3.f3 |   | `in making me` | 1.48 | ['1.23', '1.43', '-0.58']
w3.f4 |   | `the whole thing` | 0.39 | ['-0.24', '2.72', '-1.73']
w3.f5 | x | `in making me` | 6.01 | ['0.52', '3.21', '2.61']
w3.f6 |   | `the whole thing` | 3.23 | ['-0.32', '2.23', '1.53']
w3.f7 |   | `in making me` | 3.82 | ['1.23', '2.55', '0.54']
w3.f8 |   | `@@UNK@@ only in` | 1.70 | ['0.50', '1.64', '-0.15']
w3.f9 | x | `whole thing @@UNK@@` | 4.54 | ['2.71', '-0.19', '2.13']
w3.f10 |   | `@@UNK@@ . @@PAD@@` | 2.18 | ['0.33', '2.00', '0.00']
w3.f11 |   | `. the whole` | 2.20 | ['-0.15', '-0.67', '3.20']
w3.f12 |   | `thing @@UNK@@ only` | 2.93 | ['3.40', '-0.16', '-0.17']
w3.f13 |   | `@@PAD@@ @@PAD@@ .` | 2.20 | ['0.00', '0.00', '2.45']
w3.f14 | x | `thing @@UNK@@ only` | 4.70 | ['-1.70', '0.79', '5.70']
w3.f15 |   | `thing @@UNK@@ only` | 1.94 | ['3.93', '-1.69', '-0.13']
w3.f16 |   | `in making me` | 1.78 | ['-1.02', '0.89', '2.29']
w3.f17 | x | `me @@UNK@@ .` | 6.23 | ['4.02', '1.39', '0.98']
w3.f18 |   | `@@PAD@@ @@PAD@@ .` | 0.00 | ['0.00', '0.00', '-0.95']
w3.f19 | x | `only in making` | 5.28 | ['1.59', '1.23', '2.57']

## Original input: 
``` the chateau cleverly @@UNK@@ the cross - cultural differences between @@UNK@@ and @@UNK@@ . ``` 

## Marked input: 
<pre>the chateau cleverly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>cross <span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>cultural <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>differences <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>between <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>@@UNK@@ .</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `the chateau` | 0.59 | ['-1.87', '2.83']
w2.f1 |   | `- cultural` | 0.49 | ['-0.88', '1.50']
w2.f2 |   | `cultural differences` | 0.07 | ['0.49', '0.63']
w2.f3 | x | `between @@UNK@@` | 2.64 | ['3.93', '-0.73']
w2.f4 |   | `the chateau` | 0.40 | ['-1.38', '1.97']
w2.f5 |   | `chateau cleverly` | 2.23 | ['0.27', '2.27']
w2.f6 |   | `- cultural` | 0.64 | ['-0.21', '0.95']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `cleverly @@UNK@@` | 1.44 | ['2.36', '-0.71']
w2.f9 |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 | x | `- cultural` | 3.61 | ['1.18', '2.56']
w2.f11 |   | `differences between` | 2.76 | ['2.36', '0.67']
w2.f12 |   | `the chateau` | 1.66 | ['0.53', '1.17']
w2.f13 | x | `cross -` | 3.17 | ['2.12', '1.20']
w2.f14 |   | `the cross` | 2.54 | ['0.10', '2.48']
w2.f15 | x | `cultural differences` | 8.11 | ['1.60', '6.78']
w2.f16 |   | `@@PAD@@ the` | 0.07 | ['0.00', '0.83']
w2.f17 | x | `differences between` | 4.37 | ['2.39', '2.59']
w2.f18 | x | `chateau cleverly` | 4.05 | ['2.52', '1.65']
w2.f19 |   | `and @@UNK@@` | 1.21 | ['3.66', '-2.15']
w3.f0 | x | `cultural differences between` | 8.18 | ['1.22', '0.95', '6.40']
w3.f1 |   | `- cultural differences` | 2.79 | ['-2.23', '2.31', '3.09']
w3.f2 |   | `cross - cultural` | 2.50 | ['2.63', '-1.56', '1.52']
w3.f3 |   | `- cultural differences` | 0.61 | ['-0.10', '-0.59', '1.91']
w3.f4 |   | `the chateau cleverly` | 1.19 | ['-0.24', '-0.93', '2.72']
w3.f5 |   | `- cultural differences` | 3.33 | ['0.99', '3.37', '-0.69']
w3.f6 |   | `- cultural differences` | 2.40 | ['0.68', '-0.01', '1.93']
w3.f7 |   | `the cross -` | 2.42 | ['-1.23', '2.33', '1.81']
w3.f8 |   | `- cultural differences` | 1.78 | ['0.22', '0.15', '1.70']
w3.f9 | x | `chateau cleverly @@UNK@@` | 7.57 | ['0.43', '5.11', '2.13']
w3.f10 |   | `differences between @@UNK@@` | 2.89 | ['1.53', '0.66', '0.86']
w3.f11 | x | `cultural differences between` | 4.10 | ['3.42', '-0.71', '1.58']
w3.f12 |   | `cleverly @@UNK@@ the` | 2.61 | ['3.06', '-0.16', '-0.17']
w3.f13 | x | `the cross -` | 7.68 | ['4.70', '2.36', '0.87']
w3.f14 | x | `differences between @@UNK@@` | 3.58 | ['1.59', '3.45', '-1.37']
w3.f15 |   | `cross - cultural` | 0.55 | ['0.71', '-0.37', '0.38']
w3.f16 |   | `chateau cleverly @@UNK@@` | 1.56 | ['1.54', '3.92', '-3.52']
w3.f17 | x | `cultural differences between` | 4.57 | ['2.38', '1.50', '0.85']
w3.f18 |   | `cleverly @@UNK@@ the` | 3.24 | ['1.58', '-0.45', '2.57']
w3.f19 |   | `. @@PAD@@ @@PAD@@` | 0.11 | ['0.22', '0.00', '0.00']

## Original input: 
``` @@UNK@@ @@UNK@@ and exquisite trappings are @@UNK@@ by a lackluster script and @@UNK@@ performances . ``` 

## Marked input: 
<pre>@@UNK@@ @@UNK@@ and exquisite <span style="background-color: #FFFF00">@</span>trappings <span style="background-color: #FFFF00">@</span>are <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>by <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>lackluster <span style="background-color: #6698FF">@</span>script <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>performances <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `trappings are` | 2.86 | ['1.54', '1.69']
w2.f1 |   | `lackluster script` | 1.55 | ['-0.90', '2.59']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `lackluster script` | 1.14 | ['0.44', '1.25']
w2.f4 |   | `trappings are` | 1.77 | ['2.86', '-0.90']
w2.f5 |   | `exquisite trappings` | 0.90 | ['0.71', '0.50']
w2.f6 |   | `a lackluster` | 1.86 | ['0.54', '1.42']
w2.f7 | x | `lackluster script` | 2.33 | ['2.12', '1.12']
w2.f8 | x | `lackluster script` | 3.23 | ['0.27', '3.18']
w2.f9 | x | `script and` | 6.06 | ['6.59', '-0.51']
w2.f10 | x | `@@UNK@@ performances` | 6.38 | ['-0.06', '6.58']
w2.f11 |   | `trappings are` | 2.06 | ['1.93', '0.40']
w2.f12 | x | `lackluster script` | 3.94 | ['2.34', '1.64']
w2.f13 | x | `@@UNK@@ by` | 3.93 | ['0.61', '3.48']
w2.f14 |   | `@@UNK@@ by` | 2.77 | ['0.69', '2.12']
w2.f15 |   | `exquisite trappings` | 2.15 | ['1.20', '1.22']
w2.f16 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f17 |   | `and exquisite` | 0.38 | ['1.02', '-0.03']
w2.f18 |   | `a lackluster` | 2.18 | ['0.76', '1.54']
w2.f19 | x | `and exquisite` | 4.27 | ['3.66', '0.90']
w3.f0 | x | `and @@UNK@@ performances` | 4.40 | ['-1.56', '0.35', '6.00']
w3.f1 | x | `performances . @@PAD@@` | 5.23 | ['5.96', '-0.35', '0.00']
w3.f2 | x | `a lackluster script` | 6.92 | ['1.87', '0.04', '5.10']
w3.f3 |   | `performances . @@PAD@@` | 1.16 | ['1.91', '-0.14', '0.00']
w3.f4 |   | `exquisite trappings are` | 1.16 | ['-1.80', '-0.20', '3.51']
w3.f5 | x | `@@UNK@@ performances .` | 5.18 | ['0.08', '1.11', '4.32']
w3.f6 | x | `a lackluster script` | 4.23 | ['1.76', '3.42', '-0.74']
w3.f7 |   | `performances . @@PAD@@` | 1.01 | ['1.78', '-0.27', '0.00']
w3.f8 | x | `and exquisite trappings` | 5.43 | ['2.47', '1.18', '2.06']
w3.f9 | x | `performances . @@PAD@@` | 3.68 | ['3.20', '0.58', '0.00']
w3.f10 |   | `exquisite trappings are` | 3.84 | ['-0.63', '0.83', '3.78']
w3.f11 |   | `a lackluster script` | 2.89 | ['-0.77', '1.23', '2.62']
w3.f12 | x | `lackluster script and` | 6.00 | ['2.43', '2.55', '1.15']
w3.f13 |   | `@@UNK@@ performances .` | 4.88 | ['-0.04', '2.72', '2.45']
w3.f14 | x | `are @@UNK@@ by` | 5.10 | ['1.83', '0.79', '2.59']
w3.f15 |   | `lackluster script and` | 2.83 | ['0.10', '3.37', '-0.48']
w3.f16 |   | `@@PAD@@ @@PAD@@ @@UNK@@` | 0.00 | ['0.00', '0.00', '-3.52']
w3.f17 |   | `are @@UNK@@ by` | 3.05 | ['2.67', '1.39', '-0.85']
w3.f18 |   | `exquisite trappings are` | 1.20 | ['0.36', '2.82', '-1.51']
w3.f19 | x | `and exquisite trappings` | 9.51 | ['3.50', '3.00', '3.13']

## Original input: 
``` the film is visually dazzling , the @@UNK@@ events dramatic , funny and poignant . ``` 

## Marked input: 
<pre>the film <span style="background-color: #6698FF">@</span>is <span style="background-color: #6698FF">@</span>visually <span style="background-color: #6698FF">@</span>dazzling <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ events <span style="background-color: #6698FF">@</span>dramatic <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>funny <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>poignant <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ events` | 1.80 | ['1.98', '0.20']
w2.f1 |   | `and poignant` | 3.01 | ['-1.18', '4.32']
w2.f2 |   | `visually dazzling` | 0.49 | ['-0.20', '1.73']
w2.f3 |   | `is visually` | 0.73 | ['0.28', '1.00']
w2.f4 | x | `visually dazzling` | 4.29 | ['-0.42', '4.90']
w2.f5 | x | `, funny` | 4.90 | ['1.09', '4.12']
w2.f6 | x | `dazzling ,` | 4.25 | ['0.42', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `and poignant` | 0.43 | ['-0.15', '0.80']
w2.f9 |   | `@@UNK@@ events` | 4.91 | ['2.38', '2.54']
w2.f10 | x | `visually dazzling` | 7.77 | ['1.62', '6.28']
w2.f11 |   | `is visually` | 1.90 | ['-1.67', '3.85']
w2.f12 |   | `@@PAD@@ the` | 1.28 | ['0.00', '1.32']
w2.f13 | x | `dramatic ,` | 3.32 | ['1.28', '2.18']
w2.f14 |   | `visually dazzling` | 2.71 | ['-0.11', '2.85']
w2.f15 | x | `events dramatic` | 5.51 | ['4.08', '1.71']
w2.f16 |   | `film is` | 0.29 | ['0.91', '0.15']
w2.f17 |   | `poignant .` | 1.37 | ['1.52', '0.47']
w2.f18 | x | `and poignant` | 3.88 | ['3.52', '0.48']
w2.f19 | x | `and poignant` | 3.39 | ['3.66', '0.03']
w3.f0 |   | `poignant . @@PAD@@` | 2.48 | ['2.88', '-0.01', '0.00']
w3.f1 | x | `, funny and` | 4.38 | ['1.74', '3.18', '-0.17']
w3.f2 |   | `, the @@UNK@@` | 3.14 | ['2.60', '0.94', '-0.31']
w3.f3 |   | `poignant . @@PAD@@` | 0.20 | ['0.95', '-0.14', '0.00']
w3.f4 |   | `is visually dazzling` | 2.86 | ['-1.96', '0.96', '4.22']
w3.f5 | x | `and poignant .` | 6.37 | ['-0.51', '2.89', '4.32']
w3.f6 |   | `poignant . @@PAD@@` | 3.13 | ['2.27', '1.07', '0.00']
w3.f7 | x | `, funny and` | 4.38 | ['1.70', '1.34', '1.83']
w3.f8 |   | `film is visually` | 3.63 | ['-0.14', '4.71', '-0.65']
w3.f9 | x | `visually dazzling ,` | 5.37 | ['-0.84', '3.26', '3.06']
w3.f10 | x | `poignant . @@PAD@@` | 5.18 | ['3.32', '2.00', '0.00']
w3.f11 | x | `@@UNK@@ events dramatic` | 4.32 | ['-2.74', '1.25', '6.00']
w3.f12 | x | `the film is` | 4.65 | ['2.43', '0.53', '1.82']
w3.f13 | x | `funny and poignant` | 6.83 | ['5.96', '0.60', '0.51']
w3.f14 |   | `film is visually` | 1.30 | ['0.82', '0.90', '-0.33']
w3.f15 |   | `visually dazzling ,` | 2.46 | ['-1.41', '1.33', '2.70']
w3.f16 | x | `dramatic , funny` | 6.53 | ['1.04', '3.78', '2.08']
w3.f17 |   | `dazzling , the` | 1.81 | ['-2.63', '3.34', '1.25']
w3.f18 |   | `funny and poignant` | 2.84 | ['1.54', '-0.14', '1.90']
w3.f19 | x | `dramatic , funny` | 8.97 | ['3.95', '1.68', '3.45']

## Original input: 
``` this charming but slight tale has warmth , wit and interesting characters @@UNK@@ @@UNK@@ . ``` 

## Marked input: 
<pre>this <span style="background-color: #6698FF">@</span>charming <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>but <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>slight <span style="background-color: #6698FF">@</span>tale <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>has <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>warmth <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span>wit <span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>interesting <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>characters <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `, wit` | 3.95 | ['-1.14', '5.46']
w2.f1 |   | `but slight` | 3.26 | ['4.31', '-0.92']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `and interesting` | 2.23 | ['0.06', '2.72']
w2.f4 | x | `warmth ,` | 3.91 | ['1.60', '2.50']
w2.f5 |   | `this charming` | 1.84 | ['2.84', '-0.69']
w2.f6 | x | `warmth ,` | 4.75 | ['0.92', '3.93']
w2.f7 |   | `slight tale` | 1.94 | ['0.12', '2.73']
w2.f8 |   | `charming but` | 1.61 | ['1.54', '0.28']
w2.f9 |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 |   | `wit and` | 1.83 | ['0.49', '1.48']
w2.f11 |   | `interesting characters` | 2.31 | ['1.35', '1.23']
w2.f12 |   | `@@PAD@@ this` | 2.72 | ['0.00', '2.76']
w2.f13 | x | `this charming` | 3.53 | ['2.32', '1.36']
w2.f14 |   | `has warmth` | 2.32 | ['3.08', '-0.72']
w2.f15 | x | `this charming` | 3.80 | ['3.03', '1.05']
w2.f16 |   | `characters @@UNK@@` | 0.51 | ['1.81', '-0.54']
w2.f17 |   | `interesting characters` | 2.39 | ['0.81', '2.20']
w2.f18 | x | `and interesting` | 3.74 | ['3.52', '0.35']
w2.f19 | x | `this charming` | 6.11 | ['1.58', '4.84']
w3.f0 | x | `slight tale has` | 3.78 | ['-0.08', '3.79', '0.47']
w3.f1 |   | `warmth , wit` | 2.83 | ['3.97', '0.90', '-1.67']
w3.f2 | x | `@@PAD@@ this charming` | 3.65 | ['0.00', '2.87', '0.87']
w3.f3 |   | `this charming but` | 1.65 | ['-0.39', '1.96', '0.68']
w3.f4 |   | `warmth , wit` | 1.87 | ['-0.20', '0.77', '1.66']
w3.f5 | x | `, wit and` | 6.66 | ['-0.52', '1.69', '5.81']
w3.f6 | x | `and interesting characters` | 5.80 | ['-0.42', '2.77', '3.66']
w3.f7 | x | `, wit and` | 4.41 | ['1.70', '1.36', '1.83']
w3.f8 | x | `slight tale has` | 4.98 | ['1.02', '2.29', '1.95']
w3.f9 |   | `@@PAD@@ this charming` | 2.27 | ['0.00', '0.59', '1.79']
w3.f10 | x | `interesting characters @@UNK@@` | 7.98 | ['3.37', '3.90', '0.86']
w3.f11 |   | `tale has warmth` | 2.15 | ['1.34', '-1.97', '2.98']
w3.f12 |   | `but slight tale` | 2.83 | ['-0.44', '0.12', '3.27']
w3.f13 |   | `but slight tale` | 4.27 | ['1.09', '2.21', '1.21']
w3.f14 | x | `wit and interesting` | 3.46 | ['-0.28', '1.09', '2.75']
w3.f15 | x | `this charming but` | 4.56 | ['2.58', '2.19', '-0.04']
w3.f16 | x | `warmth , wit` | 5.03 | ['2.81', '3.78', '-1.18']
w3.f17 |   | `has warmth ,` | 3.22 | ['1.73', '2.70', '-1.05']
w3.f18 |   | `charming but slight` | 1.46 | ['0.71', '-1.58', '2.80']
w3.f19 | x | `has warmth ,` | 5.84 | ['-0.16', '5.03', '1.08']

## Original input: 
``` the limited sets and small @@UNK@@ and dark spaces also are @@UNK@@ to a classic low - budget film noir movie . ``` 

## Marked input: 
<pre>the limited <span style="background-color: #6698FF">@</span>sets <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>small <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>and dark <span style="background-color: #FFFF00">@</span>spaces <span style="background-color: #FFFF00">@</span>also <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>are <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>classic <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>low <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>- <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>budget <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>film <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>noir <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>movie <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `dark spaces` | 5.41 | ['-1.46', '7.25']
w2.f1 | x | `spaces also` | 5.81 | ['1.65', '4.30']
w2.f2 |   | `spaces also` | 0.62 | ['0.64', '1.03']
w2.f3 | x | `noir movie` | 3.13 | ['2.19', '1.49']
w2.f4 |   | `film noir` | 3.57 | ['1.33', '2.43']
w2.f5 | x | `limited sets` | 4.67 | ['-0.21', '5.18']
w2.f6 |   | `a classic` | 1.37 | ['0.54', '0.92']
w2.f7 |   | `budget film` | 1.59 | ['2.83', '-0.33']
w2.f8 | x | `spaces also` | 4.44 | ['3.36', '1.30']
w2.f9 | x | `@@UNK@@ to` | 7.04 | ['2.38', '4.67']
w2.f10 | x | `limited sets` | 3.57 | ['0.71', '2.99']
w2.f11 | x | `a classic` | 4.34 | ['0.43', '4.18']
w2.f12 |   | `spaces also` | 3.11 | ['1.42', '1.73']
w2.f13 | x | `low -` | 4.31 | ['3.26', '1.20']
w2.f14 | x | `sets and` | 3.72 | ['3.74', '0.01']
w2.f15 | x | `budget film` | 3.78 | ['2.18', '1.88']
w2.f16 | x | `film noir` | 2.95 | ['0.91', '2.80']
w2.f17 |   | `also are` | 2.22 | ['2.16', '0.68']
w2.f18 | x | `and dark` | 3.72 | ['3.52', '0.32']
w2.f19 | x | `and small` | 5.47 | ['3.66', '2.10']
w3.f0 | x | `to a classic` | 4.15 | ['-0.93', '3.29', '2.19']
w3.f1 | x | `budget film noir` | 3.81 | ['0.05', '1.18', '2.96']
w3.f2 | x | `a classic low` | 6.88 | ['1.87', '3.47', '1.63']
w3.f3 |   | `- budget film` | 1.61 | ['-0.10', '2.23', '0.09']
w3.f4 | x | `spaces also are` | 7.58 | ['1.92', '2.50', '3.51']
w3.f5 | x | `limited sets and` | 9.08 | ['2.17', '1.43', '5.81']
w3.f6 | x | `the limited sets` | 3.83 | ['-0.32', '-0.04', '4.39']
w3.f7 | x | `to a classic` | 5.75 | ['3.76', '0.48', '2.00']
w3.f8 | x | `and dark spaces` | 7.12 | ['2.47', '3.32', '1.61']
w3.f9 | x | `limited sets and` | 3.83 | ['1.20', '0.34', '2.40']
w3.f10 | x | `spaces also are` | 4.68 | ['1.75', '-0.70', '3.78']
w3.f11 | x | `limited sets and` | 4.41 | ['4.97', '-0.95', '0.58']
w3.f12 | x | `budget film noir` | 4.94 | ['2.43', '0.53', '2.10']
w3.f13 |   | `the limited sets` | 3.55 | ['4.70', '-1.33', '0.42']
w3.f14 | x | `limited sets and` | 5.09 | ['3.34', '2.45', '-0.61']
w3.f15 |   | `the limited sets` | 3.52 | ['-0.02', '3.96', '-0.25']
w3.f16 | x | `to a classic` | 3.95 | ['1.59', '0.35', '2.39']
w3.f17 |   | `are @@UNK@@ to` | 3.66 | ['2.67', '1.39', '-0.25']
w3.f18 | x | `sets and small` | 3.85 | ['4.64', '-0.14', '-0.19']
w3.f19 | x | `low - budget` | 4.83 | ['2.37', '1.48', '1.09']

## Original input: 
``` although it lacks the detail of the book , the film does pack some serious suspense . ``` 

## Marked input: 
<pre>although it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>lacks <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span>detail of <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>book <span style="background-color: #FFFF00">@</span>, the film does <span style="background-color: #6698FF">@</span>pack <span style="background-color: #6698FF">@</span>some <span style="background-color: #6698FF">@</span>serious <span style="background-color: #6698FF">@</span>suspense <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `film does` | 3.59 | ['0.25', '3.71']
w2.f1 |   | `serious suspense` | 1.78 | ['-1.68', '3.60']
w2.f2 |   | `it lacks` | 0.22 | ['0.50', '0.77']
w2.f3 |   | `does pack` | 1.86 | ['-1.79', '4.21']
w2.f4 |   | `book ,` | 2.53 | ['0.22', '2.50']
w2.f5 |   | `although it` | 2.10 | ['2.18', '0.23']
w2.f6 |   | `book ,` | 2.26 | ['-1.58', '3.93']
w2.f7 | x | `does pack` | 2.73 | ['1.64', '1.99']
w2.f8 | x | `although it` | 3.46 | ['1.92', '1.75']
w2.f9 |   | `it lacks` | 1.04 | ['-1.50', '2.55']
w2.f10 |   | `suspense .` | 0.58 | ['1.88', '-1.16']
w2.f11 | x | `pack some` | 6.56 | ['3.01', '3.82']
w2.f12 | x | `does pack` | 4.17 | ['2.29', '1.92']
w2.f13 | x | `suspense .` | 3.41 | ['3.55', '0.01']
w2.f14 | x | `it lacks` | 4.99 | ['1.93', '3.09']
w2.f15 |   | `the film` | 1.19 | ['-0.42', '1.88']
w2.f16 | x | `film does` | 3.75 | ['0.91', '3.60']
w2.f17 | x | `pack some` | 5.62 | ['2.05', '4.19']
w2.f18 | x | `although it` | 4.48 | ['3.52', '1.09']
w2.f19 |   | `of the` | 1.58 | ['1.68', '0.20']
w3.f0 | x | `does pack some` | 6.70 | ['2.11', '3.15', '1.83']
w3.f1 |   | `some serious suspense` | 2.83 | ['1.19', '1.35', '0.66']
w3.f2 | x | `although it lacks` | 4.91 | ['1.80', '1.70', '1.50']
w3.f3 |   | `film does pack` | 2.07 | ['0.63', '1.99', '0.06']
w3.f4 |   | `@@PAD@@ although it` | 1.21 | ['0.00', '1.22', '0.34']
w3.f5 |   | `some serious suspense` | 2.35 | ['-0.11', '0.34', '2.45']
w3.f6 | x | `does pack some` | 7.80 | ['3.17', '2.29', '2.56']
w3.f7 |   | `serious suspense .` | 0.98 | ['0.63', '0.67', '0.18']
w3.f8 |   | `@@PAD@@ @@PAD@@ although` | 4.25 | ['0.00', '0.00', '4.54']
w3.f9 | x | `does pack some` | 4.52 | ['-0.14', '5.08', '-0.31']
w3.f10 |   | `of the book` | 2.28 | ['2.92', '-1.03', '0.53']
w3.f11 |   | `lacks the detail` | 0.86 | ['1.56', '-0.67', '0.16']
w3.f12 | x | `does pack some` | 4.92 | ['1.90', '-0.57', '3.71']
w3.f13 |   | `the detail of` | 4.45 | ['4.70', '-2.70', '2.71']
w3.f14 | x | `pack some serious` | 6.93 | ['2.89', '3.18', '0.95']
w3.f15 | x | `although it lacks` | 4.26 | ['0.20', '2.22', '2.00']
w3.f16 |   | `@@PAD@@ although it` | 2.13 | ['0.00', '0.65', '1.86']
w3.f17 | x | `pack some serious` | 10.81 | ['5.43', '4.63', '0.89']
w3.f18 | x | `detail of the` | 5.20 | ['1.00', '2.10', '2.57']
w3.f19 |   | `suspense . @@PAD@@` | 0.63 | ['2.59', '-1.84', '0.00']

## Original input: 
``` there are no special effects , and no hollywood @@UNK@@ . ``` 

## Marked input: 
<pre>there <span style="background-color: #FFFF00">@</span>are <span style="background-color: #FFFF00">@</span>no <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>special <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>effects <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>no <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>hollywood <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `hollywood @@UNK@@` | 0.45 | ['1.61', '-0.79']
w2.f1 |   | `hollywood @@UNK@@` | 1.80 | ['3.18', '-1.25']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `no hollywood` | 3.04 | ['0.98', '2.62']
w2.f4 | x | `no hollywood` | 4.30 | ['1.84', '2.65']
w2.f5 |   | `effects ,` | 3.17 | ['4.77', '-1.30']
w2.f6 |   | `effects ,` | 3.22 | ['-0.61', '3.93']
w2.f7 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f8 |   | `no hollywood` | 1.00 | ['-0.61', '1.82']
w2.f9 |   | `@@UNK@@ .` | 2.83 | ['2.38', '0.46']
w2.f10 | x | `no special` | 2.97 | ['-1.42', '4.52']
w2.f11 |   | `there are` | 1.69 | ['1.56', '0.40']
w2.f12 |   | `there are` | 3.37 | ['0.84', '2.57']
w2.f13 | x | `effects ,` | 4.02 | ['1.98', '2.18']
w2.f14 | x | `and no` | 6.36 | ['0.13', '6.27']
w2.f15 | x | `no hollywood` | 4.79 | ['1.16', '3.90']
w2.f16 |   | `there are` | 0.07 | ['1.42', '-0.59']
w2.f17 |   | `there are` | 2.53 | ['2.47', '0.68']
w2.f18 |   | `and no` | 2.39 | ['3.52', '-1.01']
w2.f19 |   | `special effects` | 2.58 | ['1.36', '1.53']
w3.f0 |   | `effects , and` | 2.81 | ['2.97', '-0.76', '0.99']
w3.f1 |   | `are no special` | 0.15 | ['1.91', '-1.38', '-0.00']
w3.f2 | x | `hollywood @@UNK@@ .` | 4.29 | ['4.19', '-0.65', '0.84']
w3.f3 |   | `@@PAD@@ @@PAD@@ there` | 0.00 | ['0.00', '0.00', '0.23']
w3.f4 | x | `@@PAD@@ there are` | 3.91 | ['0.00', '0.75', '3.51']
w3.f5 | x | `effects , and` | 6.17 | ['-0.72', '1.40', '5.81']
w3.f6 |   | `effects , and` | 1.54 | ['0.43', '0.38', '0.95']
w3.f7 |   | `effects , and` | 1.20 | ['0.23', '-0.37', '1.83']
w3.f8 | x | `special effects ,` | 4.86 | ['2.64', '0.36', '2.14']
w3.f9 | x | `special effects ,` | 5.13 | ['-1.73', '3.91', '3.06']
w3.f10 | x | `no hollywood @@UNK@@` | 5.95 | ['2.04', '3.20', '0.86']
w3.f11 |   | `and no hollywood` | 2.31 | ['-1.12', '2.82', '0.81']
w3.f12 |   | `no special effects` | 3.37 | ['4.16', '1.67', '-2.33']
w3.f13 | x | `no special effects` | 8.16 | ['2.14', '2.24', '4.02']
w3.f14 | x | `are no special` | 5.83 | ['1.83', '4.41', '-0.32']
w3.f15 | x | `no special effects` | 4.84 | ['2.27', '0.67', '2.07']
w3.f16 |   | `and no hollywood` | 1.23 | ['-1.34', '1.53', '1.42']
w3.f17 | x | `effects , and` | 7.01 | ['3.98', '3.34', '-0.15']
w3.f18 |   | `hollywood @@UNK@@ .` | 1.29 | ['3.16', '-0.45', '-0.95']
w3.f19 |   | `@@PAD@@ there are` | 2.42 | ['0.00', '-1.66', '4.20']

## Original input: 
``` one of the most incoherent features in recent memory . ``` 

## Marked input: 
<pre>one of <span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>most <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>incoherent <span style="background-color: #6698FF">@</span>features <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>in <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>recent <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>memory <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@PAD@@ one` | 0.66 | ['0.00', '1.03']
w2.f1 | x | `recent memory` | 4.81 | ['1.62', '3.33']
w2.f2 |   | `recent memory` | 0.44 | ['1.24', '0.25']
w2.f3 |   | `most incoherent` | 1.73 | ['-0.24', '2.52']
w2.f4 | x | `incoherent features` | 8.39 | ['1.78', '6.80']
w2.f5 |   | `features in` | 0.90 | ['0.30', '0.91']
w2.f6 |   | `incoherent features` | 2.97 | ['0.10', '2.96']
w2.f7 | x | `incoherent features` | 2.52 | ['3.52', '-0.10']
w2.f8 | x | `incoherent features` | 3.32 | ['-1.02', '4.56']
w2.f9 |   | `incoherent features` | 3.54 | ['3.79', '-0.23']
w2.f10 | x | `recent memory` | 4.07 | ['1.28', '2.92']
w2.f11 |   | `most incoherent` | 0.65 | ['-0.12', '1.03']
w2.f12 |   | `features in` | 3.20 | ['1.26', '1.97']
w2.f13 |   | `the most` | 1.68 | ['-0.60', '2.42']
w2.f14 |   | `recent memory` | 2.92 | ['2.96', '-0.01']
w2.f15 |   | `in recent` | 2.42 | ['0.06', '2.63']
w2.f16 | x | `most incoherent` | 3.90 | ['-0.71', '5.37']
w2.f17 | x | `most incoherent` | 6.64 | ['0.85', '6.40']
w2.f18 | x | `incoherent features` | 3.78 | ['-1.22', '5.12']
w2.f19 | x | `in recent` | 3.36 | ['0.45', '3.21']
w3.f0 |   | `recent memory .` | 3.35 | ['1.69', '1.68', '0.37']
w3.f1 | x | `memory . @@PAD@@` | 4.52 | ['5.25', '-0.35', '0.00']
w3.f2 |   | `recent memory .` | 1.89 | ['0.55', '0.59', '0.84']
w3.f3 |   | `in recent memory` | 1.57 | ['1.23', '-0.53', '1.48']
w3.f4 |   | `in recent memory` | 1.99 | ['-0.60', '0.89', '2.06']
w3.f5 | x | `incoherent features in` | 9.38 | ['0.93', '7.90', '0.88']
w3.f6 | x | `incoherent features in` | 5.12 | ['3.76', '1.43', '0.14']
w3.f7 | x | `recent memory .` | 4.43 | ['2.80', '1.94', '0.18']
w3.f8 | x | `recent memory .` | 5.23 | ['3.46', '3.93', '-1.87']
w3.f9 |   | `in recent memory` | 3.35 | ['1.57', '3.30', '-1.41']
w3.f10 |   | `incoherent features in` | 3.50 | ['4.16', '0.77', '-1.28']
w3.f11 | x | `most incoherent features` | 5.63 | ['2.02', '1.80', '2.00']
w3.f12 | x | `the most incoherent` | 4.19 | ['2.43', '0.57', '1.31']
w3.f13 | x | `recent memory .` | 6.00 | ['1.45', '2.35', '2.45']
w3.f14 |   | `incoherent features in` | 0.92 | ['2.28', '0.04', '-1.30']
w3.f15 |   | `@@PAD@@ one of` | 2.95 | ['0.00', '1.11', '2.01']
w3.f16 | x | `features in recent` | 8.51 | ['4.77', '1.85', '2.26']
w3.f17 | x | `of the most` | 4.00 | ['-1.64', '0.47', '5.32']
w3.f18 | x | `one of the` | 3.48 | ['-0.72', '2.10', '2.57']
w3.f19 | x | `in recent memory` | 4.38 | ['-1.65', '1.32', '4.82']

## Original input: 
``` though lan yu lacks a sense of dramatic urgency , the film makes up for it with a pleasing @@UNK@@ . ``` 

## Marked input: 
<pre>though <span style="background-color: #FFFF00">@</span>lan <span style="background-color: #FFFF00">@</span>yu <span style="background-color: #FFFF00">@</span>lacks a <span style="background-color: #6698FF">@</span>sense <span style="background-color: #6698FF">@</span>of <span style="background-color: #6698FF">@</span>dramatic <span style="background-color: #6698FF">@</span>urgency <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>film makes <span style="background-color: #6698FF">@</span>up <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>for <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>it <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>with <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>pleasing <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `for it` | 2.86 | ['1.57', '1.67']
w2.f1 | x | `makes up` | 7.57 | ['4.82', '2.88']
w2.f2 |   | `makes up` | 1.69 | ['1.15', '1.59']
w2.f3 |   | `lacks a` | 1.80 | ['2.12', '0.24']
w2.f4 |   | `makes up` | 3.49 | ['2.52', '1.16']
w2.f5 |   | `film makes` | 3.00 | ['-0.31', '3.61']
w2.f6 | x | `urgency ,` | 5.06 | ['1.22', '3.93']
w2.f7 |   | `film makes` | 1.79 | ['0.28', '2.42']
w2.f8 | x | `with a` | 3.21 | ['0.86', '2.56']
w2.f9 |   | `yu lacks` | 4.64 | ['2.11', '2.55']
w2.f10 | x | `makes up` | 10.37 | ['3.57', '6.94']
w2.f11 |   | `makes up` | 2.77 | ['0.46', '2.58']
w2.f12 |   | `though lan` | 2.82 | ['-2.13', '4.99']
w2.f13 | x | `urgency ,` | 3.95 | ['1.92', '2.18']
w2.f14 |   | `it with` | 3.02 | ['1.93', '1.12']
w2.f15 |   | `@@PAD@@ though` | 2.91 | ['0.00', '3.18']
w2.f16 | x | `film makes` | 2.87 | ['0.91', '2.72']
w2.f17 | x | `makes up` | 4.01 | ['5.31', '-0.68']
w2.f18 |   | `urgency ,` | 2.64 | ['1.87', '0.89']
w2.f19 |   | `urgency ,` | 1.56 | ['1.84', '0.02']
w3.f0 | x | `up for it` | 3.88 | ['5.35', '-2.28', '1.20']
w3.f1 | x | `@@PAD@@ though lan` | 3.85 | ['0.00', '-0.33', '4.55']
w3.f2 | x | `dramatic urgency ,` | 4.36 | ['2.46', '0.67', '1.32']
w3.f3 |   | `lan yu lacks` | 1.74 | ['1.20', '1.55', '-0.40']
w3.f4 |   | `film makes up` | 3.11 | ['-0.42', '1.83', '2.06']
w3.f5 |   | `film makes up` | 3.45 | ['1.39', '0.50', '1.89']
w3.f6 |   | `urgency , the` | 1.36 | ['2.35', '0.38', '-1.16']
w3.f7 |   | `sense of dramatic` | 3.42 | ['1.05', '0.18', '2.69']
w3.f8 | x | `dramatic urgency ,` | 5.28 | ['2.79', '0.64', '2.14']
w3.f9 | x | `lacks a sense` | 4.07 | ['3.42', '-0.16', '0.91']
w3.f10 |   | `film makes up` | 3.50 | ['0.46', '-1.32', '4.51']
w3.f11 | x | `it with a` | 4.90 | ['1.01', '1.30', '2.78']
w3.f12 | x | `lacks a sense` | 5.47 | ['1.67', '-0.46', '4.39']
w3.f13 |   | `lan yu lacks` | 3.65 | ['2.83', '0.38', '0.69']
w3.f14 | x | `of dramatic urgency` | 3.43 | ['-0.37', '2.30', '1.60']
w3.f15 |   | `it with a` | 3.13 | ['0.62', '3.85', '-1.17']
w3.f16 | x | `@@PAD@@ though lan` | 5.79 | ['0.00', '-1.07', '7.23']
w3.f17 | x | `up for it` | 6.05 | ['2.46', '5.11', '-1.37']
w3.f18 | x | `makes up for` | 6.76 | ['4.92', '1.30', '1.01']
w3.f19 | x | `up for it` | 7.13 | ['3.39', '2.83', '1.02']

## Original input: 
``` @@UNK@@ , elling never gets too cloying thanks to the actors ' perfect comic timing and sweet , genuine chemistry . ``` 

## Marked input: 
<pre>@@UNK@@ , elling never <span style="background-color: #6698FF">@</span>gets <span style="background-color: #6698FF">@</span>too <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>cloying <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>thanks <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>actors ' perfect <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>comic <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>timing <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span>sweet <span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span>genuine <span style="background-color: #FFFF00">@</span>chemistry <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `perfect comic` | 6.03 | ['2.11', '4.29']
w2.f1 | x | `gets too` | 4.56 | ['4.15', '0.55']
w2.f2 |   | `elling never` | 0.10 | ['1.20', '-0.05']
w2.f3 | x | `gets too` | 4.37 | ['0.84', '4.09']
w2.f4 | x | `' perfect` | 6.73 | ['1.10', '5.82']
w2.f5 | x | `thanks to` | 6.64 | ['4.56', '2.39']
w2.f6 | x | `sweet ,` | 4.50 | ['0.66', '3.93']
w2.f7 | x | `gets too` | 2.95 | ['2.03', '1.83']
w2.f8 |   | `elling never` | 2.31 | ['0.17', '2.35']
w2.f9 |   | `' perfect` | 2.73 | ['2.80', '-0.06']
w2.f10 |   | `never gets` | 2.11 | ['-0.29', '2.54']
w2.f11 | x | `too cloying` | 6.37 | ['3.88', '2.76']
w2.f12 | x | `' perfect` | 3.91 | ['2.20', '1.75']
w2.f13 |   | `@@UNK@@ ,` | 2.64 | ['0.61', '2.18']
w2.f14 | x | `gets too` | 4.70 | ['2.62', '2.11']
w2.f15 | x | `, genuine` | 5.33 | ['2.19', '3.41']
w2.f16 |   | `genuine chemistry` | 2.03 | ['-0.53', '3.33']
w2.f17 |   | `elling never` | 3.13 | ['0.65', '3.09']
w2.f18 | x | `thanks to` | 5.99 | ['3.62', '2.50']
w2.f19 | x | `thanks to` | 4.83 | ['4.00', '1.12']
w3.f0 | x | `gets too cloying` | 4.33 | ['1.99', '-1.08', '3.82']
w3.f1 | x | `' perfect comic` | 5.21 | ['0.51', '2.05', '3.03']
w3.f2 | x | `never gets too` | 8.85 | ['6.11', '2.33', '0.50']
w3.f3 | x | `sweet , genuine` | 3.39 | ['2.11', '-0.65', '2.54']
w3.f4 | x | `sweet , genuine` | 5.17 | ['3.34', '0.77', '1.42']
w3.f5 |   | `, genuine chemistry` | 4.55 | ['-0.52', '3.94', '1.45']
w3.f6 | x | `gets too cloying` | 6.44 | ['1.60', '4.25', '0.80']
w3.f7 |   | `to the actors` | 3.28 | ['3.76', '-0.92', '0.93']
w3.f8 | x | `too cloying thanks` | 6.70 | ['1.35', '0.81', '4.82']
w3.f9 | x | `too cloying thanks` | 4.57 | ['-0.97', '4.33', '1.32']
w3.f10 | x | `elling never gets` | 8.59 | ['1.63', '3.73', '3.38']
w3.f11 | x | `never gets too` | 7.94 | ['3.52', '0.84', '3.78']
w3.f12 | x | `too cloying thanks` | 6.27 | ['4.03', '3.76', '-1.39']
w3.f13 |   | `the actors '` | 4.07 | ['4.70', '-0.11', '-0.28']
w3.f14 | x | `gets too cloying` | 8.70 | ['1.07', '3.69', '4.03']
w3.f15 | x | `perfect comic timing` | 5.04 | ['1.20', '1.14', '2.86']
w3.f16 | x | `sweet , genuine` | 5.40 | ['-0.58', '3.78', '2.58']
w3.f17 | x | `gets too cloying` | 6.63 | ['0.80', '2.80', '3.19']
w3.f18 |   | `elling never gets` | 2.99 | ['0.40', '2.30', '0.75']
w3.f19 | x | `and sweet ,` | 3.93 | ['3.50', '-0.53', '1.08']

## Original input: 
``` a bittersweet drama about the @@UNK@@ of grief and how truth - telling can open the door to @@UNK@@ . ``` 

## Marked input: 
<pre>a bittersweet <span style="background-color: #FFFF00">@</span>drama <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>about <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>grief <span style="background-color: #FFFF00">@</span>and how <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>truth <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>- <span style="background-color: #FFFF00">@</span>telling <span style="background-color: #6698FF">@</span>can <span style="background-color: #6698FF">@</span>open <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>door <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>@@UNK@@ .</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `bittersweet drama` | 4.34 | ['4.73', '-0.02']
w2.f1 | x | `a bittersweet` | 6.21 | ['2.95', '3.39']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 |   | `truth -` | 0.46 | ['0.48', '0.54']
w2.f4 | x | `bittersweet drama` | 6.71 | ['5.78', '1.13']
w2.f5 |   | `can open` | 2.54 | ['0.75', '2.10']
w2.f6 |   | `bittersweet drama` | 2.72 | ['3.40', '-0.58']
w2.f7 |   | `door to` | 0.78 | ['3.66', '-1.97']
w2.f8 |   | `bittersweet drama` | 3.01 | ['1.49', '1.73']
w2.f9 |   | `@@UNK@@ of` | 4.02 | ['2.38', '1.65']
w2.f10 | x | `a bittersweet` | 5.03 | ['1.97', '3.20']
w2.f11 |   | `about the` | 1.35 | ['1.20', '0.42']
w2.f12 | x | `and how` | 7.61 | ['0.18', '7.47']
w2.f13 |   | `and how` | 2.31 | ['-0.53', '3.00']
w2.f14 |   | `truth -` | 2.17 | ['1.87', '0.33']
w2.f15 | x | `how truth` | 4.62 | ['1.44', '3.44']
w2.f16 |   | `the door` | 2.33 | ['-1.19', '4.28']
w2.f17 |   | `drama about` | 0.74 | ['0.55', '0.80']
w2.f18 |   | `and how` | 2.46 | ['3.52', '-0.94']
w2.f19 | x | `and how` | 6.47 | ['3.66', '3.11']
w3.f0 | x | `bittersweet drama about` | 6.67 | ['0.41', '4.45', '2.20']
w3.f1 |   | `how truth -` | 2.98 | ['0.16', '1.54', '1.66']
w3.f2 |   | `bittersweet drama about` | 3.31 | ['2.59', '1.38', '-0.58']
w3.f3 |   | `bittersweet drama about` | 0.67 | ['2.14', '-0.26', '-0.61']
w3.f4 |   | `a bittersweet drama` | 1.57 | ['-1.11', '1.56', '1.48']
w3.f5 | x | `a bittersweet drama` | 5.45 | ['1.79', '3.58', '0.41']
w3.f6 |   | `telling can open` | 2.28 | ['2.38', '0.69', '-0.59']
w3.f7 |   | `of grief and` | 2.67 | ['0.84', '0.50', '1.83']
w3.f8 |   | `door to @@UNK@@` | 2.62 | ['1.55', '1.89', '-0.54']
w3.f9 | x | `open the door` | 5.77 | ['-0.15', '-0.12', '6.15']
w3.f10 |   | `door to @@UNK@@` | 3.90 | ['1.51', '1.69', '0.86']
w3.f11 | x | `- telling can` | 3.78 | ['1.42', '0.81', '1.74']
w3.f12 |   | `truth - telling` | 3.91 | ['-0.27', '2.81', '1.49']
w3.f13 | x | `the @@UNK@@ of` | 5.41 | ['4.70', '-1.74', '2.71']
w3.f14 | x | `open the door` | 4.79 | ['-3.19', '-0.32', '8.39']
w3.f15 |   | `open the door` | 1.86 | ['0.32', '-1.54', '3.25']
w3.f16 |   | `@@PAD@@ a bittersweet` | 2.87 | ['0.00', '0.35', '2.90']
w3.f17 |   | `and how truth` | 3.42 | ['-1.40', '4.98', '-0.00']
w3.f18 | x | `drama about the` | 5.26 | ['1.79', '1.36', '2.57']
w3.f19 | x | `a bittersweet drama` | 9.10 | ['3.70', '2.29', '3.23']

## Original input: 
``` a worthy entry into a very difficult genre . ``` 

## Marked input: 
<pre>a worthy <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>entry <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>into <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>very <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>difficult <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>genre <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `very difficult` | 3.20 | ['4.99', '-1.41']
w2.f1 |   | `worthy entry` | 3.67 | ['0.95', '2.85']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `very difficult` | 3.01 | ['2.65', '0.92']
w2.f4 |   | `a worthy` | 3.21 | ['2.27', '1.13']
w2.f5 |   | `very difficult` | 2.77 | ['2.67', '0.41']
w2.f6 |   | `entry into` | 1.48 | ['3.65', '-2.07']
w2.f7 |   | `entry into` | 1.18 | ['1.14', '0.95']
w2.f8 |   | `@@PAD@@ a` | 2.34 | ['0.00', '2.56']
w2.f9 |   | `difficult genre` | 4.66 | ['3.58', '1.10']
w2.f10 | x | `a worthy` | 6.31 | ['1.97', '4.47']
w2.f11 | x | `a worthy` | 4.53 | ['0.43', '4.37']
w2.f12 |   | `worthy entry` | 2.24 | ['2.33', '-0.05']
w2.f13 | x | `into a` | 3.36 | ['2.06', '1.45']
w2.f14 | x | `very difficult` | 7.44 | ['0.87', '6.60']
w2.f15 |   | `entry into` | 0.14 | ['2.29', '-1.88']
w2.f16 | x | `a worthy` | 2.78 | ['-0.39', '3.93']
w2.f17 | x | `worthy entry` | 4.86 | ['3.47', '2.00']
w2.f18 | x | `a very` | 5.53 | ['0.76', '4.89']
w2.f19 | x | `a very` | 3.67 | ['0.99', '2.97']
w3.f0 | x | `worthy entry into` | 5.61 | ['4.18', '1.01', '0.81']
w3.f1 | x | `very difficult genre` | 4.35 | ['3.07', '1.42', '0.24']
w3.f2 | x | `a very difficult` | 3.92 | ['1.87', '0.12', '2.01']
w3.f3 |   | `@@PAD@@ @@PAD@@ a` | 0.00 | ['0.00', '0.00', '-0.45']
w3.f4 |   | `worthy entry into` | 0.81 | ['-1.50', '-0.18', '2.85']
w3.f5 |   | `entry into a` | 2.99 | ['2.26', '-0.02', '1.07']
w3.f6 |   | `a very difficult` | 2.69 | ['1.76', '1.59', '-0.45']
w3.f7 |   | `very difficult genre` | 0.93 | ['-0.88', '1.61', '0.71']
w3.f8 |   | `a worthy entry` | 4.17 | ['0.66', '5.93', '-2.12']
w3.f9 |   | `@@PAD@@ @@PAD@@ a` | 1.03 | ['0.00', '0.00', '1.13']
w3.f10 |   | `worthy entry into` | 3.44 | ['3.24', '-0.89', '1.24']
w3.f11 |   | `entry into a` | 2.90 | ['0.38', '-0.07', '2.78']
w3.f12 |   | `very difficult genre` | 3.28 | ['1.51', '2.28', '-0.38']
w3.f13 |   | `entry into a` | 4.28 | ['4.46', '-0.12', '0.18']
w3.f14 | x | `worthy entry into` | 3.17 | ['1.25', '1.25', '0.76']
w3.f15 |   | `a very difficult` | 2.76 | ['-2.48', '4.81', '0.59']
w3.f16 |   | `a very difficult` | 3.36 | ['-0.19', '1.36', '2.57']
w3.f17 |   | `difficult genre .` | 2.48 | ['1.55', '0.11', '0.98']
w3.f18 |   | `worthy entry into` | 1.96 | ['2.34', '0.05', '0.04']
w3.f19 | x | `a worthy entry` | 5.49 | ['3.70', '2.79', '-0.88']

## Original input: 
``` it 's the cinematic equivalent of a good page - @@UNK@@ , and even if it 's nonsense , its @@UNK@@ dig surprisingly deep . ``` 

## Marked input: 
<pre>it 's the cinematic <span style="background-color: #6698FF">@</span>equivalent <span style="background-color: #6698FF">@</span>of <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>a <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>good <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>page <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- @@UNK@@ , <span style="background-color: #FFFF00">@</span>and <span style="background-color: #FFFF00">@</span>even <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>if <span style="background-color: #6698FF">@</span>it 's nonsense <span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>its <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>dig surprisingly <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>deep <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `dig surprisingly` | 4.27 | ['2.85', '1.80']
w2.f1 |   | `if it` | 3.03 | ['1.39', '1.78']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `and even` | 2.25 | ['0.06', '2.75']
w2.f4 |   | `nonsense ,` | 3.01 | ['0.69', '2.50']
w2.f5 | x | `surprisingly deep` | 6.14 | ['4.16', '2.28']
w2.f6 |   | `@@UNK@@ ,` | 3.90 | ['0.07', '3.93']
w2.f7 |   | `dig surprisingly` | 0.54 | ['1.01', '0.44']
w2.f8 |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 |   | `@@UNK@@ ,` | 2.70 | ['2.38', '0.34']
w2.f10 | x | `a good` | 4.90 | ['1.97', '3.06']
w2.f11 | x | `cinematic equivalent` | 6.52 | ['0.15', '6.65']
w2.f12 |   | `'s nonsense` | 3.35 | ['0.44', '2.95']
w2.f13 | x | `nonsense ,` | 5.60 | ['3.57', '2.18']
w2.f14 |   | `nonsense ,` | 2.49 | ['1.64', '0.89']
w2.f15 | x | `surprisingly deep` | 8.49 | ['2.85', '5.91']
w2.f16 | x | `cinematic equivalent` | 5.09 | ['-0.20', '6.05']
w2.f17 |   | `nonsense ,` | 2.86 | ['3.86', '-0.38']
w2.f18 |   | `page -` | 2.36 | ['3.77', '-1.28']
w2.f19 | x | `a good` | 4.54 | ['0.99', '3.85']
w3.f0 |   | `surprisingly deep .` | 3.20 | ['1.09', '2.12', '0.37']
w3.f1 |   | `good page -` | 3.37 | ['0.34', '1.75', '1.66']
w3.f2 | x | `'s nonsense ,` | 5.21 | ['0.87', '3.10', '1.32']
w3.f3 | x | `dig surprisingly deep` | 3.58 | ['0.86', '1.18', '2.15']
w3.f4 | x | `surprisingly deep .` | 4.40 | ['1.73', '3.56', '-0.52']
w3.f5 | x | `@@UNK@@ , and` | 6.96 | ['0.08', '1.40', '5.81']
w3.f6 | x | `the cinematic equivalent` | 4.54 | ['-0.32', '1.02', '4.05']
w3.f7 | x | `nonsense , its` | 4.88 | ['1.17', '-0.37', '4.59']
w3.f8 |   | `dig surprisingly deep` | 4.24 | ['-1.94', '2.33', '4.14']
w3.f9 |   | `nonsense , its` | 1.38 | ['-0.49', '-1.33', '3.30']
w3.f10 | x | `of a good` | 5.95 | ['2.92', '1.32', '1.86']
w3.f11 | x | `dig surprisingly deep` | 8.12 | ['4.13', '3.09', '1.10']
w3.f12 | x | `equivalent of a` | 4.61 | ['2.17', '3.24', '-0.67']
w3.f13 | x | `surprisingly deep .` | 6.64 | ['2.21', '2.23', '2.45']
w3.f14 | x | `cinematic equivalent of` | 4.77 | ['2.84', '2.87', '-0.85']
w3.f15 | x | `cinematic equivalent of` | 4.49 | ['0.53', '2.12', '2.01']
w3.f16 | x | `dig surprisingly deep` | 6.81 | ['2.59', '0.64', '3.96']
w3.f17 | x | `cinematic equivalent of` | 5.16 | ['-0.41', '3.86', '1.87']
w3.f18 | x | `equivalent of a` | 3.67 | ['2.41', '2.10', '-0.37']
w3.f19 |   | `dig surprisingly deep` | 3.25 | ['-0.06', '-0.96', '4.38']

## Original input: 
``` the film would have been more enjoyable had the balance @@UNK@@ in favor of water - bound action over the land - based ' drama , ' but the emphasis on the latter leaves blue crush waterlogged . ``` 

## Marked input: 
<pre>the film would <span style="background-color: #6698FF">@</span>have <span style="background-color: #6698FF">@</span>been <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>more <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>enjoyable <span style="background-color: #FFFF00">@</span>had <span style="background-color: #FFFF00">@</span>the balance @@UNK@@ in favor <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>water <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>bound <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>action <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>over <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>land - <span style="background-color: #FFFF00">@</span>based <span style="background-color: #FFFF00">@</span>' <span style="background-color: #FFFF00">@</span>drama <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>' <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>but <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>emphasis <span style="background-color: #6698FF">@</span>on <span style="background-color: #6698FF">@</span>the latter leaves blue crush <span style="background-color: #6698FF">@</span>waterlogged <span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `have been` | 5.66 | ['0.65', '5.38']
w2.f1 | x | `land -` | 3.89 | ['2.27', '1.75']
w2.f2 |   | `@@PAD@@ @@PAD@@` | 0.00 | ['0.00', '0.00']
w2.f3 | x | `blue crush` | 4.69 | ['1.19', '4.06']
w2.f4 | x | `based '` | 7.40 | ['5.66', '1.93']
w2.f5 | x | `in favor` | 6.23 | ['0.92', '5.62']
w2.f6 |   | `would have` | 3.93 | ['2.48', '1.55']
w2.f7 | x | `blue crush` | 3.53 | ['1.99', '2.45']
w2.f8 |   | `land -` | 2.57 | ['0.94', '1.85']
w2.f9 | x | `action over` | 5.48 | ['2.20', '3.30']
w2.f10 | x | `- bound` | 4.70 | ['1.18', '3.65']
w2.f11 | x | `would have` | 4.28 | ['3.02', '1.53']
w2.f12 | x | `' drama` | 4.86 | ['2.20', '2.70']
w2.f13 | x | `crush waterlogged` | 4.74 | ['1.94', '2.95']
w2.f14 | x | `action over` | 5.87 | ['1.54', '4.37']
w2.f15 | x | `' drama` | 6.72 | ['2.81', '4.18']
w2.f16 | x | `film would` | 5.88 | ['0.91', '5.74']
w2.f17 | x | `have been` | 4.66 | ['2.06', '3.21']
w2.f18 |   | `drama ,` | 1.55 | ['0.78', '0.89']
w2.f19 |   | `drama ,` | 2.90 | ['3.18', '0.02']
w3.f0 | x | `' drama ,` | 3.99 | ['1.32', '4.45', '-1.39']
w3.f1 | x | `favor of water` | 4.77 | ['4.26', '-0.85', '1.73']
w3.f2 | x | `bound action over` | 4.23 | ['-0.05', '4.45', '-0.07']
w3.f3 |   | `would have been` | 1.92 | ['0.84', '0.81', '0.87']
w3.f4 | x | `been more enjoyable` | 3.68 | ['0.05', '-0.70', '4.69']
w3.f5 |   | `latter leaves blue` | 3.93 | ['1.57', '4.01', '-1.32']
w3.f6 | x | `but the emphasis` | 3.90 | ['1.54', '0.45', '2.12']
w3.f7 |   | `water - bound` | 3.46 | ['1.73', '-1.06', '3.28']
w3.f8 |   | `based ' drama` | 3.52 | ['2.01', '2.32', '-0.52']
w3.f9 | x | `of water -` | 4.53 | ['-1.50', '4.83', '1.30']
w3.f10 | x | `waterlogged . @@PAD@@` | 5.02 | ['3.16', '2.00', '0.00']
w3.f11 | x | `blue crush waterlogged` | 5.80 | ['1.30', '2.11', '2.58']
w3.f12 | x | `blue crush waterlogged` | 10.53 | ['3.20', '2.86', '4.60']
w3.f13 | x | `based ' drama` | 8.61 | ['2.71', '4.49', '1.66']
w3.f14 | x | `' but the` | 6.51 | ['1.53', '3.83', '1.24']
w3.f15 |   | `the emphasis on` | 3.74 | ['-0.02', '2.16', '1.77']
w3.f16 | x | `drama , '` | 6.94 | ['4.42', '3.78', '-0.88']
w3.f17 | x | `' but the` | 6.69 | ['2.63', '2.96', '1.25']
w3.f18 | x | `bound action over` | 5.08 | ['3.67', '-0.33', '2.20']
w3.f19 | x | `based ' drama` | 5.37 | ['1.30', '0.95', '3.23']

## Original input: 
``` like the chelsea 's @@UNK@@ . . . @@UNK@@ 's collage - form scenario tends to over - @@UNK@@ the spiritual @@UNK@@ of the struggling @@UNK@@ . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>like <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>chelsea <span style="background-color: #FFFF00">@</span>'s <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>. . . @@UNK@@ 's collage <span style="background-color: #6698FF">@</span>- <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>form <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>scenario <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>tends <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>over <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>- <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>the spiritual @@UNK@@ of the <span style="background-color: #FFFF00">@</span>struggling <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `@@UNK@@ 's` | 2.28 | ['1.98', '0.68']
w2.f1 | x | `form scenario` | 3.73 | ['-0.11', '3.97']
w2.f2 |   | `form scenario` | 0.17 | ['1.30', '-0.08']
w2.f3 |   | `collage -` | 1.72 | ['1.73', '0.54']
w2.f4 | x | `scenario tends` | 4.88 | ['5.11', '-0.04']
w2.f5 | x | `scenario tends` | 3.59 | ['3.24', '0.66']
w2.f6 |   | `'s collage` | 2.54 | ['1.03', '1.61']
w2.f7 |   | `form scenario` | 0.77 | ['0.72', '0.96']
w2.f8 | x | `collage -` | 3.91 | ['2.27', '1.85']
w2.f9 | x | `tends to` | 9.79 | ['5.13', '4.67']
w2.f10 | x | `form scenario` | 3.59 | ['1.83', '1.90']
w2.f11 |   | `spiritual @@UNK@@` | 2.74 | ['2.76', '0.25']
w2.f12 | x | `form scenario` | 4.10 | ['0.20', '3.94']
w2.f13 | x | `scenario tends` | 8.50 | ['5.23', '3.42']
w2.f14 | x | `form scenario` | 5.25 | ['0.69', '4.59']
w2.f15 | x | `scenario tends` | 4.09 | ['2.07', '2.29']
w2.f16 |   | `scenario tends` | 2.40 | ['1.95', '1.21']
w2.f17 |   | `collage -` | 2.63 | ['4.58', '-1.34']
w2.f18 |   | `- form` | 2.16 | ['-0.43', '2.70']
w2.f19 |   | `- form` | 2.60 | ['0.44', '2.46']
w3.f0 |   | `chelsea 's @@UNK@@` | 2.36 | ['2.04', '1.91', '-1.20']
w3.f1 |   | `spiritual @@UNK@@ of` | 3.14 | ['4.39', '-0.73', '-0.14']
w3.f2 | x | `- form scenario` | 4.76 | ['2.02', '-1.31', '4.14']
w3.f3 |   | `form scenario tends` | 0.81 | ['-0.41', '0.92', '0.90']
w3.f4 |   | `@@PAD@@ @@PAD@@ like` | 2.87 | ['0.00', '0.00', '3.23']
w3.f5 |   | `@@UNK@@ . .` | 3.67 | ['0.08', '-0.40', '4.32']
w3.f6 | x | `'s collage -` | 5.95 | ['3.62', '3.09', '-0.54']
w3.f7 | x | `to over -` | 8.52 | ['3.76', '3.44', '1.81']
w3.f8 |   | `@@UNK@@ 's collage` | 1.33 | ['0.50', '0.26', '0.86']
w3.f9 |   | `. . @@UNK@@` | 3.28 | ['0.67', '0.58', '2.13']
w3.f10 |   | `tends to over` | 2.81 | ['1.31', '1.69', '-0.04']
w3.f11 | x | `collage - form` | 6.49 | ['3.51', '0.54', '2.63']
w3.f12 | x | `@@PAD@@ @@PAD@@ like` | 4.78 | ['0.00', '0.00', '4.91']
w3.f13 | x | `the chelsea 's` | 5.81 | ['4.70', '0.97', '0.39']
w3.f14 | x | `form scenario tends` | 8.17 | ['2.95', '1.33', '3.98']
w3.f15 | x | `collage - form` | 4.48 | ['1.07', '-0.37', '3.94']
w3.f16 | x | `of the struggling` | 3.87 | ['1.87', '0.10', '2.29']
w3.f17 |   | `spiritual @@UNK@@ of` | 3.75 | ['0.66', '1.39', '1.87']
w3.f18 | x | `collage - form` | 4.77 | ['0.75', '0.97', '3.53']
w3.f19 |   | `- form scenario` | 3.83 | ['0.33', '-0.72', '4.33']

## Original input: 
``` ' blue crush ' @@UNK@@ away with the @@UNK@@ movie of the summer award . ``` 

## Marked input: 
<pre><span style="background-color: #6698FF">@</span>' <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>blue <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>crush <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>' <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>away <span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>the <span style="background-color: #FFFF00">@</span>@@UNK@@ movie of <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>summer <span style="background-color: #FFFF00">@</span>award <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `summer award` | 3.49 | ['5.45', '-1.59']
w2.f1 | x | `away with` | 4.00 | ['-0.74', '4.87']
w2.f2 |   | `summer award` | 0.21 | ['0.28', '0.98']
w2.f3 | x | `blue crush` | 4.69 | ['1.19', '4.06']
w2.f4 |   | `movie of` | 2.57 | ['3.31', '-0.55']
w2.f5 | x | `the summer` | 4.92 | ['1.16', '4.07']
w2.f6 | x | `summer award` | 4.04 | ['2.23', '1.91']
w2.f7 | x | `blue crush` | 3.53 | ['1.99', '2.45']
w2.f8 |   | `away with` | 2.94 | ['-0.34', '3.50']
w2.f9 | x | `@@UNK@@ away` | 6.37 | ['2.38', '4.00']
w2.f10 | x | `summer award` | 4.23 | ['3.63', '0.73']
w2.f11 |   | `with the` | 2.51 | ['2.35', '0.42']
w2.f12 |   | `' @@UNK@@` | 2.38 | ['2.20', '0.22']
w2.f13 | x | `movie of` | 3.80 | ['3.71', '0.24']
w2.f14 | x | `@@UNK@@ away` | 4.97 | ['0.69', '4.32']
w2.f15 | x | `summer award` | 3.74 | ['4.52', '-0.50']
w2.f16 |   | `@@PAD@@ '` | 0.36 | ['0.00', '1.12']
w2.f17 |   | `' blue` | 2.74 | ['3.04', '0.32']
w2.f18 |   | `summer award` | 1.92 | ['0.33', '1.71']
w2.f19 |   | `of the` | 1.58 | ['1.68', '0.20']
w3.f0 |   | `award . @@PAD@@` | 2.93 | ['3.33', '-0.01', '0.00']
w3.f1 |   | `@@PAD@@ @@PAD@@ '` | 0.00 | ['0.00', '0.00', '-0.55']
w3.f2 | x | `summer award .` | 3.91 | ['1.71', '1.44', '0.84']
w3.f3 |   | `' @@UNK@@ away` | 1.32 | ['0.78', '-0.06', '1.21']
w3.f4 | x | `the summer award` | 3.62 | ['-0.24', '2.56', '1.66']
w3.f5 |   | `summer award .` | 4.39 | ['0.14', '0.25', '4.32']
w3.f6 |   | `@@UNK@@ movie of` | 3.21 | ['-0.28', '4.49', '-0.79']
w3.f7 |   | `blue crush '` | 1.56 | ['3.29', '-1.09', '-0.14']
w3.f8 |   | `blue crush '` | 2.92 | ['0.38', '1.56', '1.26']
w3.f9 | x | `@@PAD@@ @@PAD@@ '` | 5.12 | ['0.00', '0.00', '5.23']
w3.f10 |   | `of the summer` | 3.52 | ['2.92', '-1.03', '1.77']
w3.f11 | x | `' blue crush` | 9.22 | ['0.98', '2.75', '5.69']
w3.f12 | x | `blue crush '` | 7.72 | ['3.20', '2.86', '1.78']
w3.f13 | x | `@@PAD@@ ' blue` | 6.49 | ['0.00', '4.49', '2.24']
w3.f14 | x | `@@PAD@@ ' blue` | 5.54 | ['0.00', '0.41', '5.22']
w3.f15 |   | `away with the` | 3.54 | ['0.65', '3.85', '-0.79']
w3.f16 |   | `of the summer` | 1.95 | ['1.87', '0.10', '0.37']
w3.f17 | x | `@@PAD@@ ' blue` | 6.19 | ['0.00', '1.95', '4.40']
w3.f18 | x | `summer award .` | 5.20 | ['3.70', '2.91', '-0.95']
w3.f19 |   | `@@UNK@@ away with` | 0.79 | ['-0.26', '1.91', '-0.75']

## Original input: 
``` the film is ultimately about as inspiring as a hallmark card . ``` 

## Marked input: 
<pre>the film is <span style="background-color: #6698FF">@</span>ultimately <span style="background-color: #6698FF">@</span>about <span style="background-color: #6698FF">@</span>as <span style="background-color: #6698FF">@</span>inspiring <span style="background-color: #6698FF">@</span>as <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>hallmark <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>card <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `as inspiring` | 2.20 | ['-1.33', '3.90']
w2.f1 |   | `inspiring as` | 3.02 | ['2.52', '0.64']
w2.f2 |   | `inspiring as` | 0.23 | ['1.24', '0.03']
w2.f3 |   | `inspiring as` | 0.08 | ['0.49', '0.15']
w2.f4 |   | `inspiring as` | 3.28 | ['4.62', '-1.15']
w2.f5 |   | `a hallmark` | 2.22 | ['0.71', '1.81']
w2.f6 |   | `inspiring as` | 2.03 | ['2.39', '-0.27']
w2.f7 |   | `hallmark card` | 0.98 | ['0.17', '1.72']
w2.f8 |   | `inspiring as` | 2.27 | ['1.16', '1.33']
w2.f9 |   | `hallmark card` | 2.88 | ['1.80', '1.09']
w2.f10 |   | `hallmark card` | 2.85 | ['-0.50', '3.49']
w2.f11 |   | `inspiring as` | 1.15 | ['1.24', '0.19']
w2.f12 |   | `@@PAD@@ the` | 1.28 | ['0.00', '1.32']
w2.f13 |   | `inspiring as` | 2.77 | ['1.61', '1.31']
w2.f14 |   | `inspiring as` | 2.18 | ['1.87', '0.34']
w2.f15 |   | `the film` | 1.19 | ['-0.42', '1.88']
w2.f16 |   | `ultimately about` | 1.99 | ['2.79', '-0.04']
w2.f17 |   | `card .` | 2.68 | ['2.83', '0.47']
w2.f18 |   | `hallmark card` | 1.96 | ['0.52', '1.56']
w2.f19 |   | `as inspiring` | 3.00 | ['1.84', '1.46']
w3.f0 |   | `film is ultimately` | 1.52 | ['-3.30', '2.08', '3.13']
w3.f1 |   | `is ultimately about` | 3.08 | ['1.18', '-0.45', '2.72']
w3.f2 |   | `as inspiring as` | 2.12 | ['0.16', '1.89', '0.16']
w3.f3 |   | `card . @@PAD@@` | 0.01 | ['0.76', '-0.14', '0.00']
w3.f4 |   | `about as inspiring` | 1.42 | ['-0.46', '-0.73', '2.97']
w3.f5 | x | `a hallmark card` | 5.15 | ['1.79', '0.07', '3.62']
w3.f6 | x | `a hallmark card` | 3.86 | ['1.76', '1.15', '1.16']
w3.f7 |   | `as a hallmark` | 1.49 | ['1.64', '0.48', '-0.14']
w3.f8 |   | `film is ultimately` | 3.51 | ['-0.14', '4.71', '-0.77']
w3.f9 |   | `inspiring as a` | 3.38 | ['2.60', '-0.25', '1.13']
w3.f10 | x | `ultimately about as` | 4.16 | ['0.92', '3.15', '0.23']
w3.f11 | x | `inspiring as a` | 5.73 | ['1.72', '1.42', '2.78']
w3.f12 | x | `about as inspiring` | 5.51 | ['0.83', '4.53', '0.28']
w3.f13 | x | `hallmark card .` | 5.55 | ['1.19', '2.16', '2.45']
w3.f14 | x | `film is ultimately` | 6.23 | ['0.82', '0.90', '4.60']
w3.f15 |   | `as inspiring as` | 3.27 | ['-1.43', '3.83', '1.03']
w3.f16 |   | `about as inspiring` | 3.20 | ['-2.73', '1.13', '5.18']
w3.f17 |   | `film is ultimately` | 2.56 | ['-2.69', '2.35', '3.06']
w3.f18 |   | `@@PAD@@ @@PAD@@ the` | 2.10 | ['0.00', '0.00', '2.57']
w3.f19 |   | `a hallmark card` | 1.81 | ['3.70', '-0.68', '-1.09']

## Original input: 
``` as written by michael @@UNK@@ and michael j . wilson from a story by wilson , this relentless , all - wise - guys - all - the - time approach tries way too hard and gets @@UNK@@ in no time at all . ``` 

## Marked input: 
<pre>as written by <span style="background-color: #6698FF">@</span>michael <span style="background-color: #6698FF">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span>and michael <span style="background-color: #FFFF00">@</span>j <span style="background-color: #FFFF00">@</span>. <span style="background-color: #FFFF00">@</span>wilson from <span style="background-color: #6698FF">@</span>a <span style="background-color: #6698FF">@</span>story <span style="background-color: #6698FF">@</span>by <span style="background-color: #6698FF">@</span>wilson , this <span style="background-color: #6698FF">@</span>relentless <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>all <span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span>wise <span style="background-color: #FFFF00">@</span>- <span style="background-color: #FFFF00">@</span>guys <span style="background-color: #FFFF00">@</span>- all - the - time <span style="background-color: #FFFF00">@</span>approach <span style="background-color: #FFFF00">@</span>tries <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>way <span style="background-color: #6698FF">@</span>too <span style="background-color: #6698FF">@</span>hard <span style="background-color: #6698FF">@</span>and <span style="background-color: #6698FF">@</span>gets <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>in <span style="background-color: #6698FF">@</span>no <span style="background-color: #6698FF">@</span>time <span style="background-color: #6698FF">@</span>at <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>all <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `way too` | 2.45 | ['-0.28', '3.11']
w2.f1 | x | `wise -` | 4.48 | ['2.87', '1.75']
w2.f2 |   | `as written` | 0.45 | ['0.54', '0.96']
w2.f3 | x | `approach tries` | 3.81 | ['0.74', '3.62']
w2.f4 | x | `michael j` | 5.39 | ['5.39', '0.19']
w2.f5 | x | `this relentless` | 3.50 | ['2.84', '0.96']
w2.f6 |   | `wilson ,` | 3.88 | ['0.04', '3.93']
w2.f7 | x | `approach tries` | 2.54 | ['0.04', '3.41']
w2.f8 |   | `guys -` | 2.89 | ['1.25', '1.85']
w2.f9 | x | `at all` | 5.60 | ['4.66', '0.95']
w2.f10 | x | `and michael` | 7.03 | ['-0.04', '7.20']
w2.f11 | x | `too hard` | 6.46 | ['3.88', '2.85']
w2.f12 | x | `gets @@UNK@@` | 3.90 | ['3.71', '0.22']
w2.f13 | x | `approach tries` | 5.20 | ['5.79', '-0.44']
w2.f14 | x | `in no` | 6.10 | ['-0.13', '6.27']
w2.f15 | x | `this relentless` | 5.07 | ['3.03', '2.31']
w2.f16 |   | `way too` | 2.03 | ['1.05', '1.74']
w2.f17 | x | `wilson from` | 4.39 | ['4.22', '0.79']
w2.f18 | x | `michael j` | 3.72 | ['2.07', '1.77']
w2.f19 | x | `and gets` | 4.34 | ['3.66', '0.98']
w3.f0 | x | `from a story` | 6.20 | ['2.47', '3.29', '0.83']
w3.f1 | x | `at all .` | 4.91 | ['7.39', '-0.14', '-1.96']
w3.f2 | x | `, this relentless` | 5.61 | ['2.60', '2.87', '0.23']
w3.f3 | x | `time at all` | 5.71 | ['1.81', '1.58', '2.93']
w3.f4 |   | `too hard and` | 2.88 | ['3.10', '1.23', '-1.09']
w3.f5 | x | `- time approach` | 6.16 | ['0.99', '4.58', '0.93']
w3.f6 | x | `way too hard` | 6.69 | ['2.10', '4.25', '0.55']
w3.f7 | x | `, all -` | 5.37 | ['1.70', '2.35', '1.81']
w3.f8 | x | `and michael j` | 7.58 | ['2.47', '1.67', '3.72']
w3.f9 | x | `no time at` | 3.89 | ['0.30', '3.71', '-0.01']
w3.f10 | x | `from a story` | 3.94 | ['1.55', '1.32', '1.22']
w3.f11 | x | `tries way too` | 7.23 | ['3.86', '-0.21', '3.78']
w3.f12 | x | `too hard and` | 6.06 | ['4.03', '1.01', '1.15']
w3.f13 |   | `this relentless ,` | 4.24 | ['3.44', '1.08', '-0.03']
w3.f14 | x | `written by michael` | 3.82 | ['0.03', '2.00', '1.88']
w3.f15 | x | `approach tries way` | 5.21 | ['1.38', '2.55', '1.45']
w3.f16 | x | `relentless , all` | 9.46 | ['4.07', '3.78', '1.99']
w3.f17 | x | `way too hard` | 8.02 | ['0.08', '2.80', '5.30']
w3.f18 | x | `this relentless ,` | 5.09 | ['0.37', '4.39', '0.79']
w3.f19 | x | `and michael j` | 4.93 | ['3.50', '-1.47', '3.01']

## Original input: 
``` if you 're willing to have fun with it , you wo n't feel cheated by the high infidelity of unfaithful . ``` 

## Marked input: 
<pre>if you 're willing <span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span>have <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>fun <span style="background-color: #FFFF00">@</span>with <span style="background-color: #FFFF00">@</span>it <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>, <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>you <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>wo <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>n't <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>feel <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>cheated <span style="background-color: #6698FF">@</span>by <span style="background-color: #6698FF">@</span>the <span style="background-color: #6698FF">@</span>high <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>infidelity <span style="background-color: #FFFF00">@</span>of <span style="background-color: #FFFF00">@</span>unfaithful <span style="background-color: #6698FF">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `with it` | 4.74 | ['3.44', '1.67']
w2.f1 |   | `fun with` | 3.28 | ['-1.46', '4.87']
w2.f2 |   | `you wo` | 1.71 | ['0.78', '1.97']
w2.f3 |   | `feel cheated` | 2.02 | ['0.61', '1.96']
w2.f4 | x | `you wo` | 5.98 | ['2.00', '4.17']
w2.f5 |   | `have fun` | 2.52 | ['1.79', '1.03']
w2.f6 |   | `it ,` | 2.08 | ['-1.76', '3.93']
w2.f7 |   | `unfaithful .` | 1.35 | ['2.12', '0.14']
w2.f8 | x | `fun with` | 3.97 | ['0.69', '3.50']
w2.f9 |   | `willing to` | 2.77 | ['-1.88', '4.67']
w2.f10 | x | `you wo` | 8.70 | ['4.16', '4.67']
w2.f11 | x | `with it` | 3.36 | ['2.35', '1.28']
w2.f12 | x | `cheated by` | 4.88 | ['1.21', '3.71']
w2.f13 | x | `cheated by` | 4.61 | ['1.29', '3.48']
w2.f14 | x | `cheated by` | 3.37 | ['1.29', '2.12']
w2.f15 | x | `, you` | 7.91 | ['2.19', '5.99']
w2.f16 | x | `of unfaithful` | 3.76 | ['0.18', '4.34']
w2.f17 | x | `unfaithful .` | 4.91 | ['5.06', '0.47']
w2.f18 | x | `wo n't` | 4.02 | ['1.02', '3.11']
w2.f19 |   | `you 're` | 2.58 | ['0.48', '2.40']
w3.f0 |   | `fun with it` | 3.49 | ['-0.66', '3.34', '1.20']
w3.f1 | x | `to have fun` | 4.67 | ['-0.45', '1.97', '3.53']
w3.f2 |   | `with it ,` | 3.00 | ['0.07', '1.70', '1.32']
w3.f3 |   | `to have fun` | 0.89 | ['-0.69', '0.81', '1.38']
w3.f4 | x | `to have fun` | 3.97 | ['0.06', '1.26', '3.01']
w3.f5 | x | `have fun with` | 5.66 | ['-0.05', '4.58', '1.46']
w3.f6 | x | `feel cheated by` | 5.99 | ['1.22', '2.63', '2.35']
w3.f7 |   | `to have fun` | 3.21 | ['3.76', '-0.57', '0.51']
w3.f8 |   | `willing to have` | 2.34 | ['-1.38', '1.89', '2.12']
w3.f9 | x | `unfaithful . @@PAD@@` | 4.00 | ['3.53', '0.58', '0.00']
w3.f10 | x | `you wo n't` | 4.31 | ['3.27', '0.84', '0.35']
w3.f11 | x | `'re willing to` | 6.48 | ['0.62', '3.99', '2.06']
w3.f12 | x | `cheated by the` | 4.06 | ['1.10', '3.26', '-0.17']
w3.f13 | x | `the high infidelity` | 6.87 | ['4.70', '2.36', '0.05']
w3.f14 | x | `cheated by the` | 5.17 | ['2.01', '2.00', '1.24']
w3.f15 | x | `, you wo` | 5.29 | ['1.52', '2.14', '1.79']
w3.f16 | x | `fun with it` | 6.75 | ['5.88', '-0.61', '1.86']
w3.f17 | x | `cheated by the` | 4.13 | ['1.68', '1.35', '1.25']
w3.f18 |   | `fun with it` | 1.16 | ['0.33', '2.32', '-1.03']
w3.f19 | x | `with it ,` | 3.98 | ['3.68', '-0.66', '1.08']

## Original input: 
``` the @@UNK@@ is spectacular and unlike most @@UNK@@ from japan , the characters move with grace and panache . ``` 

## Marked input: 
<pre>the @@UNK@@ is spectacular and unlike <span style="background-color: #FFFF00">@</span>most <span style="background-color: #FFFF00">@</span>@@UNK@@ <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>from <span style="background-color: #6698FF">@</span>japan <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>the <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>characters <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>move <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>with <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>grace <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>and <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>panache <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: pos, Prediction: pos


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 | x | `with grace` | 5.17 | ['3.44', '2.10']
w2.f1 | x | `move with` | 5.99 | ['1.25', '4.87']
w2.f2 |   | `with grace` | 0.48 | ['0.25', '1.27']
w2.f3 |   | `panache .` | 1.23 | ['1.84', '-0.05']
w2.f4 |   | `unlike most` | 3.54 | ['2.47', '1.26']
w2.f5 |   | `with grace` | 2.45 | ['0.84', '1.91']
w2.f6 |   | `japan ,` | 3.29 | ['-0.55', '3.93']
w2.f7 |   | `grace and` | 0.80 | ['1.63', '0.09']
w2.f8 | x | `move with` | 3.85 | ['0.57', '3.50']
w2.f9 |   | `panache .` | 1.57 | ['1.12', '0.46']
w2.f10 | x | `unlike most` | 6.72 | ['2.08', '4.77']
w2.f11 | x | `with grace` | 3.32 | ['2.35', '1.24']
w2.f12 | x | `characters move` | 3.51 | ['0.77', '2.78']
w2.f13 | x | `japan ,` | 3.84 | ['1.81', '2.18']
w2.f14 | x | `from japan` | 4.50 | ['0.72', '3.82']
w2.f15 | x | `the characters` | 3.34 | ['-0.42', '4.03']
w2.f16 | x | `characters move` | 3.45 | ['1.81', '2.40']
w2.f17 |   | `and panache` | 0.57 | ['1.02', '0.17']
w2.f18 | x | `and unlike` | 6.74 | ['3.52', '3.35']
w2.f19 | x | `and panache` | 6.33 | ['3.66', '2.96']
w3.f0 | x | `most @@UNK@@ from` | 5.27 | ['4.37', '0.35', '0.94']
w3.f1 |   | `grace and panache` | 0.86 | ['2.67', '-1.74', '0.31']
w3.f2 |   | `unlike most @@UNK@@` | 3.19 | ['1.96', '1.64', '-0.31']
w3.f3 |   | `from japan ,` | 0.81 | ['0.06', '1.64', '-0.29']
w3.f4 |   | `move with grace` | 2.44 | ['0.07', '0.70', '2.03']
w3.f5 | x | `with grace and` | 12.07 | ['4.85', '1.73', '5.81']
w3.f6 | x | `grace and panache` | 4.02 | ['2.54', '0.25', '1.44']
w3.f7 |   | `from japan ,` | 2.05 | ['1.07', '0.30', '1.18']
w3.f8 | x | `from japan ,` | 6.52 | ['5.16', '-0.49', '2.14']
w3.f9 | x | `from japan ,` | 3.66 | ['-1.52', '2.23', '3.06']
w3.f10 | x | `move with grace` | 5.53 | ['2.70', '1.77', '1.21']
w3.f11 |   | `from japan ,` | 3.35 | ['4.70', '-1.35', '0.19']
w3.f12 | x | `grace and panache` | 5.45 | ['2.91', '0.95', '1.71']
w3.f13 |   | `the characters move` | 4.08 | ['4.70', '-0.42', '0.06']
w3.f14 | x | `grace and panache` | 4.71 | ['0.98', '1.09', '2.74']
w3.f15 | x | `from japan ,` | 4.73 | ['-1.33', '3.53', '2.70']
w3.f16 | x | `grace and panache` | 4.95 | ['0.80', '-0.30', '4.84']
w3.f17 | x | `japan , the` | 6.47 | ['2.03', '3.34', '1.25']
w3.f18 | x | `move with grace` | 6.27 | ['2.23', '2.32', '2.18']
w3.f19 | x | `and panache .` | 4.48 | ['3.50', '3.47', '-2.38']

## Original input: 
``` it 's too long , too repetitive , and takes way too many years to @@UNK@@ to be a total winner . ``` 

## Marked input: 
<pre>it 's too <span style="background-color: #FFFF00">@</span>long <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>too <span style="background-color: #6698FF">@</span>repetitive <span style="background-color: #6698FF">@</span>, <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>and <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>takes <span style="background-color: #FFFF00">@</span>way <span style="background-color: #FFFF00">@</span>too <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>many <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>years <span style="background-color: #FFFF00">@</span><span style="background-color: #6698FF">@</span>to <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>@@UNK@@ to <span style="background-color: #6698FF">@</span>be <span style="background-color: #6698FF">@</span>a total <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>winner <span style="background-color: #6698FF">@</span><span style="background-color: #FFFF00">@</span>.</pre> 

Gold: neg, Prediction: neg


filter | passes | ngram | activation | slots
:-- | :-- | :-- | :-- | :--
w2.f0 |   | `many years` | 3.59 | ['2.70', '1.27']
w2.f1 | x | `a total` | 4.55 | ['2.95', '1.73']
w2.f2 |   | `too long` | 0.64 | ['0.04', '1.65']
w2.f3 | x | `way too` | 2.83 | ['-0.70', '4.09']
w2.f4 | x | `way too` | 5.25 | ['5.36', '0.08']
w2.f5 |   | `years to` | 3.03 | ['0.94', '2.39']
w2.f6 |   | `long ,` | 2.65 | ['-1.18', '3.93']
w2.f7 | x | `too repetitive` | 2.28 | ['0.79', '2.39']
w2.f8 |   | `it 's` | 2.89 | ['-0.72', '3.82']
w2.f9 | x | `@@UNK@@ to` | 7.04 | ['2.38', '4.67']
w2.f10 |   | `takes way` | 1.98 | ['1.75', '0.37']
w2.f11 | x | `too many` | 6.09 | ['3.88', '2.48']
w2.f12 |   | `too repetitive` | 3.33 | ['1.83', '1.54']
w2.f13 | x | `total winner` | 10.62 | ['7.24', '3.53']
w2.f14 |   | `way too` | 2.58 | ['0.50', '2.11']
w2.f15 | x | `total winner` | 4.54 | ['-0.28', '5.10']
w2.f16 | x | `too long` | 5.68 | ['2.26', '4.18']
w2.f17 | x | `repetitive ,` | 4.79 | ['5.79', '-0.38']
w2.f18 | x | `and takes` | 4.11 | ['3.52', '0.72']
w2.f19 | x | `and takes` | 4.17 | ['3.66', '0.81']
w3.f0 |   | `it 's too` | 3.74 | ['-0.60', '1.91', '2.82']
w3.f1 |   | `winner . @@PAD@@` | 2.39 | ['3.12', '-0.35', '0.00']
w3.f2 | x | `a total winner` | 6.15 | ['1.87', '3.13', '1.24']
w3.f3 |   | `total winner .` | 0.84 | ['1.86', '0.35', '-0.75']
w3.f4 | x | `too many years` | 4.41 | ['3.10', '-1.43', '3.10']
w3.f5 | x | `repetitive , and` | 5.23 | ['-1.66', '1.40', '5.81']
w3.f6 | x | `way too many` | 7.45 | ['2.10', '4.25', '1.31']
w3.f7 |   | `winner . @@PAD@@` | 1.99 | ['2.76', '-0.27', '0.00']
w3.f8 | x | `too many years` | 4.79 | ['1.35', '2.29', '1.43']
w3.f9 | x | `, too repetitive` | 4.56 | ['-2.20', '2.90', '3.97']
w3.f10 |   | `years to @@UNK@@` | 3.31 | ['0.92', '1.69', '0.86']
w3.f11 | x | `too many years` | 7.44 | ['3.15', '0.33', '4.15']
w3.f12 | x | `total winner .` | 5.10 | ['-0.15', '3.77', '1.61']
w3.f13 |   | `too many years` | 3.20 | ['-0.56', '3.09', '0.92']
w3.f14 | x | `way too many` | 4.89 | ['-0.87', '3.69', '2.15']
w3.f15 | x | `, too repetitive` | 6.13 | ['1.52', '3.12', '1.65']
w3.f16 | x | `'s too long` | 3.81 | ['2.11', '-0.92', '3.01']
w3.f17 | x | `total winner .` | 9.16 | ['5.76', '2.58', '0.98']
w3.f18 |   | `takes way too` | 2.87 | ['1.30', '2.05', '-0.02']
w3.f19 | x | `and takes way` | 8.79 | ['3.50', '2.81', '2.60']
