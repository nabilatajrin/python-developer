# Iterate over the first twenty entries in labeled_entries
for s in labeled_entries:
    # if the entry's species equals Chinstrap
    if s.species == 'Chinstrap':
      # Print each entry's sex and body_mass separated by a colon
      print(f'{s.sex}:{s.body_mass}')
