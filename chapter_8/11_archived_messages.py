def show_messages(list_of_messages):
    print("Here is a list of your messages:")
    for message in list_of_messages:
        print(message)

def send_messages(list_of_messages, sent_messages):
    while list_of_messages:
        current_message = list_of_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["LOL", "ROFL", "TTYL", "LMAO", "TTFN"]
sent_messages = []

show_messages(messages)
show_messages(sent_messages)

send_messages(messages[:], sent_messages)
print()
show_messages(messages)
print()
show_messages(sent_messages)