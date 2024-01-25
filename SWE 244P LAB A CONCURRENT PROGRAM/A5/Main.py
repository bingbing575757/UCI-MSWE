import re,collections,concurrent.futures,threading

# Read the stop words list
stopwords = set(open('stop_words').read().split(','))
# Global word frequency counter
global_counter = collections.Counter()
# Create a thread lock
lock = threading.Lock()
# List of text files to process
txt_files = ['anonymit.txt', 'cDc-0200.txt', 'crossbow.txt', 'gems.txt']

# Function to count words in a single file
def count_file(file_name):
    local_counter = collections.Counter()
    with open(file_name, 'r') as f:
        # Read the file content, convert it to lowercase, and use regex to find words
        words = re.findall(r'\w{3,}', f.read().lower())
        # Update the local word frequency counter
        local_counter.update(w for w in words if w not in stopwords)
    return local_counter

# Function to update the global word frequency counter
def update_global_counter(file_counter):
    with lock:
        # Use a lock to update the global word frequency counter
        global_counter.update(file_counter)

# Execute file processing using a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit tasks to the thread pool and map the task results to corresponding files
    futures = {executor.submit(count_file, file): file for file in txt_files}
    # Iterate through completed tasks
    for future in concurrent.futures.as_completed(futures):
        # Get the filename associated with the currently completed task
        file = futures[future]
        try:
            # Get the result of the task, i.e., word frequency count for the file, and update the global counter
            file_counter = future.result()
            update_global_counter(file_counter)
        except Exception as e:
            # Handle possible exceptions
            print(f"Error processing {file}: {e}")

# Output the top 40 words with their frequencies from the global word frequency counter
for w, c in global_counter.most_common(40):
    print(w, '-', c)
