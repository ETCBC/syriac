# The ETCBC Syriac Corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16966129.svg)](https://doi.org/10.5281/zenodo.16966129)

This is the Text-Fabric dataset of the ETCBC database of Syriac literature. It is the result of a collaboration of the [**ETCBC**](https://etcbc.nl) and the [**CACCHT**](https://github.com/CACCHT) project (Creating Annotated Corpora of Classical Hebrew Texts).

## Texts
Version 0.8 of the dataset (based on the morphologically parsed file s10-out) is based on the following texts:
- Peshitta 
    - Genesis 
    - Exodus 
    - Leviticus 
    - Deuteronomy 
    - Joshua 
    - Judges
    - 1 Samuel
    - 1 and 2 Kings
    - Psalms 1-30
    - Jeremiah 1-10
    - Ezekiel
    - Daniel
    - Jonah
    - Zechariah
    - Sirach
- Syrohexapla: Psalms 1–32
- Bardaisan, The Book of the Laws of the Countries
- Oratio Manasseh, Prayer of Manasseh (versions A and B)
- Epistle of Baruch (versions A and B)
- Ephrem's Prose Refutation against Mani
- Ephrem’s Sermon on the Ninevites
- Pseudo-Methodius
- The Apocalypse of Pseudo-Ezra

## Features
All the text features are based on the ETCBC transcription. The dataset contains a representation of the consonantal text in Estrangela script as well.

The texts are annotated with the following word level features:

**g_cons**: the text of a word in ETCBC transcription  
**g_cons_utf8**: the text of a word in estrangela script  
**lex**: lexeme in ETCBC transcription  
**gloss**: English gloss  
**sp**: part of speech  
**vs**: verbal stem  
**vt**: verbal tense  
**ps**: person  
**gn**: gender  
**nu**: number  
**vo**: voice  
**st**: state  
**ls**: lexical set of a word  
**trailer**: comes after a word, can be empty space or None  
**vpm**: vowel pattern marker  

Morphemes  
**g_lex**: Realization of the lexeme in ETCBC transcription  
**g_emf**: Realized form of the emphatic state morpheme  
**emf**: Paradigmatic form of the emphatic state morpheme  
**g_nme**: Realized form of the nominal ending morpheme  
**nme**: Paradigmatic form of the nominal ending morpheme  
**g_pfm**: Realized form of the preformative morpheme  
**pfm**: Paradigmatic form of the preformative morpheme  
**g_pfx**: Realized form of the passive prefix morpheme  
**pfx**: Paradigmatic form of the passive prefix morpheme  
**g_vbe**: Realized form of the verbal stem morpheme  
**vbe**: Paradigmatic form of the verbal stem morpheme  
**g_vbs**: Realized form of the verbal stem morpheme  
**vbs**: Paradigmatic form of the verbal stem morpheme  

And finally, of course:  
**book**, **chapter** and **verse**.  

The dataset is work in progress.

## Acknowledgements
The following people contributed to the dataset:
- Dirk Bakker
- Gegham Bdoyan
- Matthias Benabdellah
- Mignon van Bokhoven
- Hans Rutger Bosker
- Logan Copley
- Janet Dyk
- Ariel Gutman
- Piotr Jutkiewicz
- Percy van Keulen
- Willem van Peursen
- Constantijn Sikkel
- Umut Var
- Geert Jan Veldman

The texts are based on the following editions, we thank the editors for their permission to use them in our dataset.

- For the Peshitta, the text is taken from [Vetus Testamentum Syriace](https://brill.com/display/serial/PES) prepared by the Peshitta Institute Amsterdam (formerly Leiden), also electronically integrated in the [Brill Scholarly editions](https://scholarlyeditions.brill.com/peso/). Our text does not include the critical apparatus. The text of Ben Sira is a preliminary version. The official edition is in preparation.
- The Book of the Laws of the Countries was prepared by Dirk Bakker on the basis of [Drijvers' edition](https://archive.org/details/bookoflawsofcoun0000bard/) as part of his [PhD project](https://scholarlypublications.universiteitleiden.nl/handle/1887/17580) (2006–2010).
- The text of the sermon of Ephrem the Syrian on Nineveh and Jonah was prepared by Constantijn Sikkel and Geert-Jan Veldman. It is based on the running text in Des heiligen Ephraem des Syrers Sermones II (Corpus scriptorum Christianorum Orientalium 311 = Scriptores Syri 134), with application of Beck's emendations introduced by "Lege", "Corrige", or "Omitte", provided that they are based on a manuscript.
- The text of Pseudo-Methodius is based on the edition by Reinink (Corpus scriptorum Christianorum Orientalium).
- We used a slightly corrected version of the text of The Apocalypse of Pseudo-Ezra that was prepared by Laura Locke Estes for her [MA Thesis](https://digitalcommons.acu.edu/etd/41/).
