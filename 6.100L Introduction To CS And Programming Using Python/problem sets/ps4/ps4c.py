# Problem Set 4c
import json
import ps4b # Importing your work from Part B

### HELPER CODE ###
def load_words(file_name):
    '''
    - file_name: string, the name of the file containing
        the list of words to load.
    ---
    #### return: 
        list, valid words. Words are strings of lowercase letters.
    ---
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist

def is_word(word_list, word):
    '''
    - word_list: list, words in the dictionary.
    - word: string, a possible word.
    ---
    #### return: 
        True if word is in word_list, False otherwise.
    ---
    Determines if word is a valid word, ignoring capitalization and punctuation.
    '''
    # Example:
    # >>> is_word(word_list, 'bat') returns
    # True
    # >>> is_word(word_list, 'asdf') returns
    # False
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list

def get_story_string():
    '''
    ---
    #### return: 
        a story in encrypted text.
    ---
    '''
    f = open('story.txt', 'r')
    story = str(f.read())
    f.close()
    return story[:-1]

def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)
 
WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###

def decrypt_message_try_pads(ciphertext, pads):
    '''
    - ciphertext: EncryptedMessage, the ciphertext.
    - pads: list of lists of ints, list of pads which might have been used
        to encrypt the ciphertext.
    ---
    #### return: 
        PlaintextMessage, message with the decrypted ciphertext and the best pad.
    ---
    #### Note:
        We will consider the pad used to create it the pad which when used to decrypt 
        ciphertext results in a plaintext with the most valid English words. 
        In the event of ties return the last pad that results in the maximum number 
        of valid English words.
    ---
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext.
    '''
    word_list = load_words(WORDLIST_FILENAME)
    
    def decrypt_helper(pads_remain, count_wrd=-1, msg=None):
        if not pads_remain:
            return msg
        
        try:
            msg_decrypted = ciphertext.decrypt_message(pads_remain[0])
        
        except ValueError:
            # Recursion: attempt to decrypt the message with the next pad (skipping the current one)
            return decrypt_helper(pads_remain[1:], count_wrd, msg)
        
        text = msg_decrypted.get_text()
        # Loop: iterate over each word in 'text'
        count_valid = sum(1 for word in text.split() if is_word(word_list, word))
        
        if count_valid >= count_wrd:
            # Recursion: update and recurse with the new count and decrypted message
            return decrypt_helper(pads_remain[1:], count_valid, msg_decrypted)
        
        # Recursion: else, keep the previous best message and word count
        return decrypt_helper(pads_remain[1:], count_wrd, msg)
    
    # Recursion: start with the initial list of pads
    return decrypt_helper(pads)

def decode_story():
    '''
    #### return: 
        string, the decoded story.
    ---
    Write your code here to decode Bob's story using a list of possible pads.\n
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.
    '''
    ciphertext = ps4b.EncryptedMessage(get_story_string())
    story_decrypted = decrypt_message_try_pads(ciphertext, get_story_pads())
    
    return story_decrypted.get_text()

if __name__ == '__main__':
    # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)