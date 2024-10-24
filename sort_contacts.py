# Contact List
# Write a sorting function that takes in a list of names and sorts them by last name either alphabetically (ASC) or reverse-alphabetically (DESC).

# Examples
# sort_contacts([
#   "John Locke",
#   "Thomas Aquinas",
#   "David Hume",
#   "Rene Descartes"
# ], "ASC") ➞ [
#   "Thomas Aquinas",
#   "Rene Descartes",
#   "David Hume",
#   "John Locke"
# ]

# # Aquinas (A) < Descartes (D) < Hume (H) < Locke (L)

# sort_contacts([
#   "Paul Erdos",
#   "Leonhard Euler",
#   "Carl Gauss"
# ], "DESC") ➞ [
#   "Carl Gauss",
#   "Leonhard Euler",
#   "Paul Erdos"
# ]

# # Gauss (G) > Erdos (ER) > Euler (EU)

# sort_contacts([], "DESC") ➞ []

# sort_contacts(None, "DESC") ➞ []
# Notes
# A list with a single name should be trivially returned.
# An empty list, or an input of None should return an empty list.




def sort_contacts(names, order):
    
    if not names:
        return []

    
    if order == "ASC":
        return sorted(names, key=lambda name: name.split()[-1])
    elif order == "DESC":
        return sorted(names, key=lambda name: name.split()[-1], reverse=True)


print(sort_contacts([
  "John Locke",
  "Thomas Aquinas",
  "David Hume",
  "Rene Descartes"
], "ASC"))  

print(sort_contacts([
  "Paul Erdos",
  "Leonhard Euler",
  "Carl Gauss"
], "DESC"))  

print(sort_contacts([], "DESC"))  # Expected: []

print(sort_contacts(None, "DESC"))  # Expected: []
