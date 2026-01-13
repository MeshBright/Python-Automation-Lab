

# The Cost Registry (Cost of each component)
component_costs = {
    'a': 10, 'b': 20, 'c': 5,  'd': 30, 'e': 5,
    'f': 50, 'g': 20, 'h': 10, 'i': 5,  'j': 15,
    'k': 5,  'l': 10, 'm': 20, 'n': 5,  'o': 10,
    'p': 20, 'q': 80, 'r': 10, 's': 5,  't': 5,
    'u': 5,  'v': 40, 'w': 40, 'x': 80, 'y': 40, 'z': 90
}

# The Messy Machine Log
# Note: Separators include commas, slashes, and uneven spaces.
batch_log = """
    aa-bb,  cc/dd/ee,   ff-gg,
    hh/ii/jj,  kk-ll-mm,   nn,
    oo/pp/qq,  rr-ss-tt,   uu/vv,
    ww-xx-yy,  zz
"""

##########################  My code for the project ##############################
punctuation = ["-", "/", " ", "\n", "\t"]

batch_log_remove_punctuation_and_space = batch_log

for sign in punctuation:
    batch_log_remove_punctuation_and_space = batch_log_remove_punctuation_and_space.replace(sign, "")

final_content = batch_log_remove_punctuation_and_space.split(",")

final_unique_content = set(final_content)

word_and_values = {}
for word in final_unique_content:
    score = 0
    
    for letter in word:
        score_for_letter = component_costs[letter]
        score = score + score_for_letter
    if "x" in word:
        score = score + 25 
    word_and_values[word] = score

highest_scores_breakdown = [f"{word} ==> {val}" for word, val in word_and_values.items() if val > 100]

print("Words with the highest score:")
print(highest_scores_breakdown)




####################  AI's 100% efficiency code for the same project ##################################

# 1. CLEANING
# First, split by the ONLY true batch separator: the comma.

raw_batches = batch_log.split(',')

results = {}

for raw_batch in raw_batches:
    # Now clean the specific batch. 
    # We replace - and / with empty string "" to merge them (aa-bb -> aabb)
    # .strip() removes the newlines and spaces around the batch
    clean_batch = raw_batch.replace("-", "").replace("/", "").strip()
    
    # Skip if the batch is empty (e.g. trailing commas)
    if not clean_batch:
        continue

    # 2. CALCULATION
    current_cost = 0
    for letter in clean_batch:
        current_cost += component_costs[letter]
    
    # 3. LOGIC (Hazard Fee - Improved Position)
    # Check 'x' once per batch, not once per letter
    if 'x' in clean_batch:
        current_cost += 25
        
    results[clean_batch] = current_cost

# 4. FILTERING (The List Comprehension you missed)
# This is the "Pythonic" way to filter the list at the end
high_value_report = [
    f"{batch} ==> {cost}" 
    for batch, cost in results.items() 
    if cost > 100
]

print(high_value_report)


