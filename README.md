# Gossip Analytics
Don't you want to find out which of your friends are texting each other on Telegram?

## Setup
* Install Python
* Build the [Telegram Database library](https://tdlib.github.io/td/build.html?language=Python)
* Obtain api_key and api_hash for your application at [my.telegram.org](https://my.telegram.org/apps). Export them as environment variables GOSSIP_ANALYTICS_API_ID and GOSSIP_ANALYTICS_API_HASH.
* Run the `whoiswho.py` script to load your contacts to the `names.txt` file
* Start the `ostrovid.py` script and keep it running, it log online statuses of your contacts to the `onlines.txt` file
* After some time, you can run the `anna_liza.py` script to analyse the collected data and find out which contacts of yours spent the most time online together

## ATP (the algorithm)
1. Computes how much time each person spent online and how much time each pair spent online together. The T parameter specifies the tolerance of what it means to be together - e.g. does one person being online at 10:05 and the other at 10:08 count?
2. For each pair, divide the time both were online by the time at least one of the two was online. The quotient is the ratio of online time which these two spent together.
3. Sort pairs by the quotient.
4. Filter the pairs, keeping only those pairs (X,Y) which have the highest quotient of all pairs involving person X or person Y. Those pairs are marked as suspicious.
5. After repeating steps 1-4 for different values of the T parameter, from zero to maximum T.
6. The field `inclusions` denotes how many times the pair was marked as suspicious. The strictness of the filter determines the minimum number of `inclusions` for which the pair is printed.
