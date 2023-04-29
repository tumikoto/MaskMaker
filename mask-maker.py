#
# Script to parse a wordlist, calculate hashcat password masks for each, and display the top X number of masks (poor man's statsgen/maskgen)
#

import re
import itertools


# Regex patterns and character masks
pattern_lower = "[a-z]"
pattern_upper = "[A-Z]"
pattern_number = "[0-9]"
pattern_symbol = "[^a-zA-Z0-9]"

# Character masks
mask_lower = "?l"
mask_upper = "?u"
mask_number = "?d"
mask_symbol = "?s"

# List mapping regex patterns to masks
pattern_mask_map = [
    [pattern_lower, mask_lower],
    [pattern_upper, mask_upper],
    [pattern_number, mask_number],
    [pattern_symbol, mask_symbol]
]

# Number of masks to print
num_masks = 10

# Our main function
def main():

    # In case something goes wrong
    try:
        # Wordlist to process
        passwords_file = "./wordlist.txt"

        # Read contents of wordlist
        f = open(passwords_file, "r")
        lines = f.read().split("\n")
        f.close()

        # Dict to store mask results
        results = {}

        # Loop through all lines
        for line in lines:

            # String to store mask for current line
            mask = ""

            # Loop through all characters in line
            chars = itertools.islice(line, 0, None)
            for char in chars:

                # Loop through all patterns
                for item in pattern_mask_map:

                    # Check charset for current char
                    if re.match(item[0], char):

                        # Append to mask for current line
                        mask = mask + item[1]
                        continue

            # Check if completed mask is already in results, then increment, else add new mask to results
            if mask in results:
                results[mask] += 1
            else:
                results[mask] = 1

        # Sort the results by count
        sorted_results = sorted(results.items(), key=lambda x:x[1], reverse=True)

        # Slice out the top X number of results
        top_results = sorted_results[0:num_masks]

        # Print the results
        print(f"\n[+] TOP {num_masks} PASSWORD MASKS\n")
        for result in top_results:
            print(f"{result[0]}{' '*(45-len(result[0]))}: {result[1]}")

        print("")
        
    # Whoopsie daisies
    except Exception as ex:
        print(f"[!] Oops, that's an error:\n{str(ex)}")


# Program execution starts here
if __name__ == "__main__":
    main()
