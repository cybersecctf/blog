from enigma.machine import EnigmaMachine

# Create an Enigma machine with specific settings based on the theme
machine = EnigmaMachine.from_key_sheet(
    rotors='IV V III',
    reflector='B',
    ring_settings=[1, 20, 11],
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

# Set the message to decrypt
encrypted_message = "WEQEXFTUXQHVOUFPSVLPTORHAFBQE"

# Decrypt the message
decrypted_message = machine.process_text(encrypted_message)

# Replace spaces with underscores as per the requirement
decrypted_message_with_underscores = decrypted_message.replace(' ', '_')

print("Decrypted message with underscores:", decrypted_message_with_underscores)

