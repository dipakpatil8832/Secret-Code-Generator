"""
Secret Code Generator (Caesar-style)
- Encode a message by shifting letters by N positions.
- Decode by shifting back.
- Preserves case, leaves non-letters unchanged.
- Provides a simple text menu.
"""

from typing import Callable

ALPHABET_SIZE = 26

def normalize_shift(shift: int) -> int:
    """Ensure the shift stays within 0–25."""
    return shift % ALPHABET_SIZE

def shift_char(c: str, shift: int) -> str:
    """Shift a single character, preserving case."""
    if 'a' <= c <= 'z':
        base = ord('a')
        new_ord = base + (ord(c) - base + shift) % ALPHABET_SIZE
        return chr(new_ord)
    elif 'A' <= c <= 'Z':
        base = ord('A')
        new_ord = base + (ord(c) - base + shift) % ALPHABET_SIZE
        return chr(new_ord)
    else:
        return c  

def transform_message(message: str, shift: int) -> str:
    """Apply shift to each character in the message."""
    return ''.join(shift_char(c, shift) for c in message)

def encode(message: str, shift: int) -> str:
    """Encode (shift forward)."""
    shift = normalize_shift(shift)
    return transform_message(message, shift)

def decode(message: str, shift: int) -> str:
    """Decode (shift backward)."""
    shift = normalize_shift(shift)
    return transform_message(message, -shift)

def get_int(prompt: str) -> int:
    """Get a valid integer input from user."""
    while True:
        user = input(prompt).strip()
        if user == '':
            print("Input cannot be empty — please enter a number.")
            continue
        try:
            val = int(user)
            return val
        except ValueError:
            print("That's not a valid integer. Try again (example: 3 or -2).")

def run_menu():
    """Main interactive menu loop."""
    MENU = (
        "\nSecret Code Generator\n"
        "1. Encode a message\n"
        "2. Decode a message\n"
        "3. Exit\n"
    )
    actions: dict[str, Callable[[], None]] = {
        '1': lambda: handle_encode(),
        '2': lambda: handle_decode(),
        '3': lambda: exit_program()
    }

    while True:
        print(MENU)
        choice = input("Choose an option (1/2/3): ").strip()
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please type 1, 2, or 3.")

def handle_encode():
    message = input("Enter the message to ENCODE: ")
    shift = get_int("Enter shift number (e.g., 3 or -2): ")
    encoded = encode(message, shift)
    print("\nEncoded message:")
    print(encoded)
    print("-" * 40)

def handle_decode():
    message = input("Enter the message to DECODE: ")
    shift = get_int("Enter shift number used to encode (e.g., 3): ")
    decoded = decode(message, shift)
    print("\nDecoded message:")
    print(decoded)
    print("-" * 40)

def exit_program():
    print("Goodbye! (Secret code generator exiting.)")
    raise SystemExit

if __name__ == "__main__":
    try:
        run_menu()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")

