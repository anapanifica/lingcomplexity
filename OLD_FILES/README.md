# Morphological complexity

The Heap's curve shows the dependence of the number of token types and the total number of tokens in a corpus. To draw the Heap's curve, we "read" the corpus from the beginning to the end and place new dots to the graph depending on whether each new token has already occured or not.


Figure 0. Heap's curves for corpora of different size.
![Figure 0](random_texts/Figure_0.png)


We use the following formula to simulate the Heap's curve: <img src="https://render.githubusercontent.com/render/math?math=f(n) = f(n-1)%2B\sum_{i}p_i*(1-p_i)^{n-1}">. The main idea is that we first compile a frequency list and after that add tokens from this list to the graph according to their frequency.


Figure 1. Simulated Heap's curves for corpora of different size.
![Figure 1](random_texts/Figure_1.png)

As can be seen from Figure 1, the Tokita curve started to coincide with the horisontal asymptote when it achieves 40,000 tokens (or even ealier). This is explained by the very small size of the Tokita corpus.

I manually cutted all the corpora (except Tokita), so that their size would be about 26,000 tokens.

Figure 2. Simulated Heap's curves for corpora of similar size.
![Figure 2](random_texts/Figure_2.png)


Figures 3-4 show Zipf's curves (dependence of frequency of tokens from their rank) for corpora of different size and for corpora of similar size respectively.

Figure 3. Zipf's curves for corpora of different size.
![Figure 3](random_texts/Figure_3.png)

Figure 3 (zoomed). Zipf's curves for corpora of different size.
![Figure 3 (zoomed](random_texts/Figure_3_zoomed.png)

Figure 4. Zipf's curves for corpora of similar size.
![Figure 4](random_texts/Figure_4.png)

Figure 4 (zoomed). Zipf's curves for corpora of similar size.
![Figure 4 (zoomed)](random_texts/Figure_4_zoomed.png)


## Bible texts

Gospel of Luke in four Daghestanian languages, Russian and English.

Figure 5. Zipf.
![Figure 5](bible_texts/Figure_5.png)

Figure 5. Zipf (zoomed).
![Figure 5 (zoomed)](bible_texts/Figure_5_zoomed.png)

Figure 6. (Real) Heap.
![Figure 6](bible_texts/Figure_6.png)

Figure 7. Simulated Heap.
![Figure 7](bible_texts/Figure_7.png)


## Sampling

Sampling of 100 sentences 1000 times (Bible texts).

Figure 8. Distribution of the number of token types in 100 sentences.
![Figure 8](sampling/Figure_8.png)

Figure 9. Distribution of TTR in 100 sentences.
![Figure 9](sampling/Figure_9.png)

Figure 10. Distribution of the number of token types in 100 sentences (y = probability density function).
![Figure 10](sampling/Figure_10.png)

Figure 11. Distribution of TTR in 100 sentences (y = probability density function).
![Figure 11](sampling/Figure_11.png)

Sampling of n sentences so that the total number of tokens would be about 1000 (Bible texts).  

Figure 12. Distribution of the number of token types in a sample of sentences.
![Figure 12](sampling/Figure_12.png)

Figure 13. Distribution of TTR in a sample of sentences.
![Figure 13](sampling/Figure_13.png)

Figure 14. Distribution of TTR in a sample of sentences (+ non-bible texts).
![Figure 13](sampling/Figure_14.png)

## Folklore texts

Figure 15. Distribution of TTR in samples of sentences from folklore texts.
![Figure 15](sampling/Figure_15.png)

The total number of tokens:

agx-folk.txt  4839
ava-folk.txt  35532
kum-folk.txt  44748
rut-folk.txt  18845
dar-folk.txt  31931
tab-folk.txt  23430
lak-folk.txt  30796
lez-folk.txt  39082
nog-folk.txt  4967
tkr-folk.txt  4495
tat-folk.txt  18742
rus-folk.txt  288801
arch-folk.txt  9094
khv-folk.txt  6704

Russian translations from SVOD are added as `rus-folk`.

Figure 16. Distribution of TTR in samples of sentences from folklore texts.
![Figure 16](sampling/Figure_16.png)

All previous plots were build based on 1000 TTRs per language. In Figures 17.1 and 17.2 there are only 100 TTRs per language.

Figure 17.1. Distribution of TTR in samples of sentences from folklore texts (100 TTRs / language).
![Figure 17.1](sampling/Figure_17.1.png)

Just a bit different visualization of the same data:

Figure 17.2. Distribution of TTR in samples of sentences from folklore texts (100 TTRs / language).
![Figure 17.2](sampling/Figure_17.2.png)

Comparison of TTR across volumes for languages with a large number of tokens:

Figure 18. TTR in folklore texts (1000 TTRs / language).
![Figure 18](sampling/Figure_18.png)

To check whether TTR in previous plots reflects the complexity of the language and not the texts, Russian translations of the texts in each of the languages are taken instead.

Figure 19. TTR in Russian translations of folklore texts (1000 TTRs / language).
![Figure 19](sampling/Figure_19.png)

Violinplots for bible texts (Gospel of Luke):

Figure 20. TTR in bible texts (1000 TTRs / language).
![Figure 20](sampling/Figure_20.png)
