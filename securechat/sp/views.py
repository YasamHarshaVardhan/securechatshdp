import base64
from django.shortcuts import render, redirect
from .forms import U1Form, U2Form
from .models import U1, U2



# Function to encode the message using Base64
def encode_message(message):
    return base64.b64encode(message.encode('utf-8')).decode('utf-8')











# Function to delete all data from U1 and U2 tables
def delete_chats(request):
    if request.method == 'POST':
        # Delete all data from both U1 and U2 tables
        U1.objects.all().delete()
        U2.objects.all().delete()
        return redirect('chat_view')  # Redirect back to the chat view after deletion
    














def chat_view(request):
    if request.method == 'POST':
        # Process U1 form
        form_u1 = U1Form(request.POST)
        if form_u1.is_valid():
            # Encode the message before saving
            encoded_msg1 = encode_message(form_u1.cleaned_data['msg1'])
            U1.objects.create(msg1=encoded_msg1)  # Save encoded message to the database
            return redirect('chat_view')  # Redirect to avoid re-submission

        # Process U2 form
        form_u2 = U2Form(request.POST)
        if form_u2.is_valid():
            # Encode the message before saving
            encoded_msg2 = encode_message(form_u2.cleaned_data['msg2'])
            U2.objects.create(msg2=encoded_msg2)  # Save encoded message to the database
            return redirect('chat_view')  # Redirect to avoid re-submission
    else:
        # Initialize empty forms for both User1 and User2
        form_u1 = U1Form()
        form_u2 = U2Form()

    # Fetch all messages for U1 and U2
    u1_messages = U1.objects.all()  # Fetch all U1 messages
    u2_messages = U2.objects.all()  # Fetch all U2 messages

    # Decode the messages before displaying
    decoded_u1_messages = [base64.b64decode(msg.msg1).decode('utf-8') for msg in u1_messages]
    decoded_u2_messages = [base64.b64decode(msg.msg2).decode('utf-8') for msg in u2_messages]

    # Combine U1 and U2 messages while keeping the sequence (User1 first, then User2)
    combined_messages = []
    
    # Here, we'll iterate over the messages correctly and append the decoded messages
    for u1_msg, u2_msg in zip(decoded_u1_messages, decoded_u2_messages):
        combined_messages.append(('u1', u1_msg))  # User1 message
        combined_messages.append(('u2', u2_msg))  # User2 message
    
    # Handle any leftover messages if U1 and U2 have different numbers of messages
    if len(decoded_u1_messages) > len(decoded_u2_messages):
        for remaining_u1 in decoded_u1_messages[len(decoded_u2_messages):]:
            combined_messages.append(('u1', remaining_u1))
    elif len(decoded_u2_messages) > len(decoded_u1_messages):
        for remaining_u2 in decoded_u2_messages[len(decoded_u1_messages):]:
            combined_messages.append(('u2', remaining_u2))

    # Pass both forms and combined messages to the template
    return render(request, 'p.html', {'form_u1': form_u1, 'form_u2': form_u2, 'combined_messages': combined_messages})



















