# Define the map_number function again to use for mappings
def map_number(source_number, mapping):
    for dest_start, src_start, range_length in mapping:
        if src_start <= source_number < (src_start + range_length):
            return dest_start + (source_number - src_start)
    # Default case: if source_number is not in any range, map to itself.
    return source_number

# Define a function to directly compute the destination for each number in a seed range using the mappings
def find_destination(seed_range, mappings_sequence):
    results = []
    for seed_start, range_length in seed_range:
        # For each number in the range apply all mappings in sequence.
        for num in range(seed_start, seed_start + range_length):
            for mapping in mappings_sequence:
                num = map_number(num, mapping)
            results.append(num)
    return results

# Define a function to parse the entire file content and extract seed ranges and mappings
def parse_content(content):
    lines = content.splitlines()
    seeds_line = lines[0]
    seeds = [(int(x.split()[0]), int(x.split()[1])) for x in seeds_line.split(':')[1].strip().split(';')]
    
    # Mappings start after the first line
    mappings_content = lines[1:]
    categories = ["seed-to-soil map", "soil-to-fertilizer map", 
                  "fertilizer-to-water map", "water-to-light map", 
                  "light-to-temperature map", "temperature-to-humidity map", 
                  "humidity-to-location map"]
    mappings = {}

    current_category = None
    for line in mappings_content:
        # New category indicated by line ending with ':'
        if line.endswith(":"):
            current_category = line[:-1]
            mappings[current_category] = []
        # Add mapping to the current category
        elif line.strip():  # ignore empty lines
            mapping = list(map(int, line.split()))
            mappings[current_category].append(mapping)
    
    # Extract mappings sequences based on categories
    mappings_sequence = [mappings[category] for category in categories if category in mappings]

    return seeds, mappings_sequence

# Read the file content
file_path = 'input.txt'
with open(file_path, 'r') as file:
    content = file.read()

# Parse and extract seeds and mappings sequences
seed_ranges, mappings_sequence = parse_content(content)

# Find the destination numbers for each seed number in the ranges
destination_numbers = find_destination(seed_ranges, mappings_sequence)

# Find the lowest location number among the destination numbers
lowest_location_number = min(destination_numbers)
print(lowest_location_number)