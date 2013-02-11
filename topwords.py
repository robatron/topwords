#! /usr/bin/env python

'''
Display the most common words in a list of words split across one or more files.

E.g., 

    1000: foo bar
    985: baz qux
    184: corge grault
    10: garply waldo
    ...
    
See "Settings" below for more details
'''
import os

# SETTINGS 
# --------
# B/c I'm too lazy to implement command-line args

# List of files to consider
WORDS_FILE_NAMES = [
    os.path.join("test-words", "moby-dick.word-list"),
    os.path.join("test-words", "shakespeare-works.word-list"),
]

# Display only the top X number of words. Set to None to display all.
TOP_HOW_MANY = 20

# Tells us details of what's going on
DEBUG = True


# Init
# ----

if DEBUG:
    print "Debug mode ON (Set DEBUG -> False to squelch progress output)"
    print "Finding top words.."

# Read in words and tally
# -----------------------
# For every words list file, record each word and the frequency it occurs

for word_file_name in WORDS_FILE_NAMES:
    
    if DEBUG:
        print "Tallying words in file {fname}...".format(fname=word_file_name)
    
    # Grab the words file descriptor
    words_file = open(word_file_name, 'r');
    
    # Tally up the words, using the word as the key, e.g., if "foo" occured 100
    # times, it would look like "foo":100 in the tally dict
    tally = {}
    for line in words_file:
        word = line.strip()
        try:
            tally[word] += 1
        except KeyError:
            tally[word] = 1
    
    # Close the file
    words_file.close()


# Categorize words by tally
#--------------------------
# Categorize the words by their tally count, e.g., if "foo" and "bar" occurred 
# 100 times, it would look like 100:["foo","bar"] in the categorized tally dict

if DEBUG:
    print "Categorizing words by tally number..."

categorized_tally = {}

for key,val in tally.iteritems():
    try:
        categorized_tally[val].append(key)
    except KeyError:
        categorized_tally[val] = [key]


# Sort
# ----
# Create a sorted list from the categorized tally dict by the tally count 
# (decending). Will be a list of tuples where the tally is the first item, and
# a list of the words with that tally as the second item.

if DEBUG:
    print "Sorting tally categories in decending order..."

sorted_tally_categories = sorted(

    # Sort by a list of tuples of key (tally) and values (list of words with 
    # tally) of the categorized tally dictionary
    categorized_tally.iteritems(), 

    # Key off of the tally for sorting
    key=lambda category: category[0], 

    # Sort decending instead of acending
    reverse=True
)

# Fortmat and print
# -----------------
# Print results to stdout

if DEBUG:
    print "Displaying results...\n"
    
line = ""
for i,category in enumerate(sorted_tally_categories):
    if TOP_HOW_MANY and i > TOP_HOW_MANY - 1:
        break
    
    line += "{tally}: ".format(tally=category[0])
    for word in category[1]:
        line += "{word} ".format(word=word)
    line += '\n'
print line