# Guess Who

A project implemented with entity detection, the program parses through transcripts and quotations of potential entities and predicts who the most likely speaker is.

Implemented in Python, and leveraged the power of Markov Models.

Pseudocode -

For a given word, check who says the next *n* words, and accordingly update their scores. Thus, a probabilistic guess can be made.