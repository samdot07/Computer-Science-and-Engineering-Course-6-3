# Problem Set 3
# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math

### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    '''
    - filename: string, name of file to read.
    ---
    #### Return: 
        string, contains file contents.
    '''
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    
    # Loop: iterate over each char in the string
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    
    return line.lower()

### Problem 0: Prep Data ###
def text_to_list(input_text):
    '''
    - input_text: string, representation of text from file.
        Assume the string is made of lowercase characters.
    ---
    #### Return:
        list, representation of input_text, where each word is a different element in the list.
    '''
    return input_text.split(' ')

### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    '''
    - input_iterable: a string or a list of strings, all are made of lowercase characters.
    ---
    #### Return:
        dictionary, that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable.
    ---
    #### Note: 
        You can assume that the only kinds of white space in the text 
        documents we provide will be new lines or space(s) between words 
        (i.e. there are no tabs).
    '''
    # Loop: iterate over each word in the input
    return {w: int(input_iterable.count(w)) for w in input_iterable}

### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    '''
    - word: word as a string.
    ---
    #### Return:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word.
    '''
    return get_frequencies(word)

### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    '''
    - freq_dict1: frequency dictionary of letters of word1 or words of text1.
    - freq_dict2: frequency dictionary of letters of word2 or words of text2.
    ---
    #### Return:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other.
    ---
    #### Note:
        The difference in words/text frequencies = DIFF sums words from these three scenarios:
            - If an element occurs in dict1 and dict2 then
            get the difference in frequencies.
            - If an element occurs only in dict1 then take the
            frequency from dict1.
            - If an element occurs only in dict2 then take the
            frequency from dict2.
        The total frequencies = ALL is calculated by summing all frequencies in both dict1 and dict2.\n
        Return 1-(DIFF/ALL) rounded to 2 decimal places.
    #### The keys of dict1 and dict2 are all lowercase, you will NOT need to worry about case sensitivity.
    '''
    # Loop: iterate over each key in freq_dict1 and freq_dict2 combined
    diff_tot = sum(abs(freq_dict1.get(k, 0) - freq_dict2.get(k, 0)) 
                   for k in (freq_dict1 | freq_dict2).keys()
                  )
    
    add_tot = sum(freq_dict1.values()) + sum(freq_dict2.values())

    if add_tot == 0:
        return 1.0

    similarity = 1 - (diff_tot/add_tot)
    
    return round(similarity, 2)

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    '''
    - freq_dict1: frequency dictionary for one text.
    - freq_dict2: frequency dictionary for another text.
    ---
    #### Return:
        list of the most frequent word(s) in the input dictionaries.
    ---    
    #### Note: 
        The most frequent word:
        - is based on the combined word frequencies across both dictionaries.
            If a word occurs in both dictionaries, consider the sum the
            freqencies as the combined word frequency.
        - need not be in both dictionaries, i.e it can be exclusively in
            dict1, dict2, or shared by dict1 and dict2.
        If multiple words are tied (i.e. share the same highest frequency),
        return an alphabetically ordered list of all these words.
    #### The keys of dict1 and dict2 are all lowercase, you will NOT need to worry about case sensitivity.
    '''
    # Loop: iterate over each [key:value] pair in freq_dict1 and freq_dict2 combined
    return [k for k, v in freq_dict1.items() | freq_dict2.items() 
            if v == max(freq_dict2.values()) or v == max(freq_dict1.values())
           ]

### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    '''
    - file_path: name of file in the form of a string.
    ---
    #### Return:
        dictionary, mapping each word to its TF.
    ---   
    #### Note:
        TF is calculatd as TF(i) = (number times word *i* appears in the document) / (total number of words in the document).
        Think about how we can use get_frequencies from earlier.
    '''
    file_list = text_to_list(load_file(file_path))
    freq_dict = get_frequencies(file_list)
    
    # Loop: iterate over each [key:value] pair in the dict
    return {k : v / len(file_list) for k, v in freq_dict.items()}

def get_idf(file_paths):
    '''
    - file_paths: list of names of files, where each file name is a string.
    #### Return:
       dictionary, mapping each word to its IDF.
    ---
    #### Note:
        IDF is calculated as IDF(i) = log_10(total number of documents / number of
        documents with word *i* in it), where log_10 is log base 10 and can be called
        with math.log10().
    '''
    doc_count = {}

    # Loop: iterate over each file path in the list 'file_paths' and
    # over each word in the set
    for f in file_paths:
        for w in set(text_to_list(load_file(f))):
            doc_count[w] = doc_count.get(w, 0) + 1

    # Loop: iterate over each [key:value] pair in doc_dount
    return {k : math.log10(len(file_paths) / v) for k, v in doc_count.items()}

def get_tfidf(tf_file_path, idf_file_paths):
    '''
    - tf_file_path: name of file in the form of a string (used to calculate TF).
    - idf_file_paths: list of names of files, where each file name is a string
        (used to calculate IDF).
    ---   
    #### Return:
        a sorted list of tuples (in increasing TF-IDF score), where each tuple is
        of the form (word, TF-IDF). In case of words with the same TF-IDF, the
        words should be sorted in increasing alphabetical order.
    ---
    #### Note:
        TF-IDF(i) = TF(i) * IDF(i).
    '''
    tf_dict = get_tf(tf_file_path)
    id_fdict = get_idf(idf_file_paths)
    
    # Loop: iterate over each key in the instersection between freq_dict1 and freq_dict2
    tot_dict = {k : tf_dict.get(k, 0) * id_fdict.get(k, 0) for k in tf_dict.keys() & id_fdict.keys()}
    
    # Loop: iterate over each [key:value] pair in tot_dict
    return sorted([(k, v) for k, v in tot_dict.items()])

if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    # Tests Problem 0: Prep Data
    # Uncomment and change the path to where hello_world.txt and hello_friends.txt are
    # test_directory = '/Users/username/tests/student_tests/'
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    print(world)      # should print ['hello', 'world', 'hello']
    print(friend)     # should print ['hello', 'friends']

    # Tests Problem 1: Get Frequencies
    # Uncomment and change the path to where hello_world.txt and hello_friends.txt are
    # test_directory = '/Users/username/tests/student_tests/'
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    # Tests Problem 2: Get Letter Frequencies
    freq1 = get_letter_frequencies('hello')
    freq2 = get_letter_frequencies('that')
    print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    # Tests Problem 3: Similarity
    # Uncomment and change the path to where hello_world.txt and hello_friends.txt are
    # test_directory = '/Users/username/tests/student_tests/'
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    word1_freq = get_letter_frequencies('toes')
    word2_freq = get_letter_frequencies('that')
    word3_freq = get_frequencies('nah')
    word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    print(word_similarity1)       # should print 1.0
    print(word_similarity2)       # should print 0.25
    print(word_similarity3)       # should print 0.0
    print(word_similarity4)       # should print 0.4

    # Tests Problem 4: Most Frequent Word(s)
    freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    # Uncomment and change the path to where hello_world.txt and hello_friends.txt are
    # tf_text_file = '/Users/username/tests/student_tests/hello_world.txt'
    # idf_text_files = ['/Users/username/tests/student_tests/hello_world.txt', '/Users/username/tests/student_tests/hello_friends.txt']
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]