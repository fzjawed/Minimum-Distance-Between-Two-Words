# Minimum-Distance-Between-Two-Words

>24th May 2021 07:14 PM

This one really twisted my brain - but it isn't that hard. When I first saw it I knew I wanted to convert the string into a list and I was right about that. So my first code had a for loop that would store the index when the last occurence of both the words is found and subtract them - however this was because I was trying to work on getting the "correct" answer for a single test case and wasn't considering all the testcases.

***Question: Given the strings text, word0, and word1, return the smallest distance between any two occurrences of word0 and word1 in text, measured in number of words in between. If either word0 or word1 doesn't appear in text, return -1.***

After running into the errors I tried to split it into cases by checking if both words were next to each other and then return 0. If not then traverse the list further and store those indexes. However that isn't working either because the order of the letters is not specified. The last statement sounds ambiguous but I guess you'll understand if you look at my code. Bad code tho 💀


Anywho the final solution works by finding the index of whatever is found first in the list - word0 or word1. We then go into a while loop to traverse the list (i don't like while loops ok - don't ask why they're just yucky) and we see if the next word found is the same as word0 or word1 but ensure that it's not the same as the word found in the first for loop. This way you're making sure word1 and word2 aren't the same. Here we're also checking to make sure the "min_dist" is the smallest possible.
