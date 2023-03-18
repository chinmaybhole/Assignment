def count_notes(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10,
             5, 2, 1]  # List of available notes
    counts = [0] * len(notes)  # Initialize counts to zero

    for i, note in enumerate(notes):
        counts[i] = amount // note
        amount %= note

    return dict(zip(notes, counts))


# Example usage
balance = 1339
notes_count = count_notes(balance)
print("Balance amount: Rs.", balance)
print("Minimum number of notes required:")
for note, count in notes_count.items():
    if count > 0:
        print(f"{count} x Rs. {note}")
