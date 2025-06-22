from langchain_text_splitters import RecursiveCharacterTextSplitter
text = """
Title: The Benefits of Meditation

Meditation has been practiced for thousands of years. It is a simple technique that can help reduce stress, improve focus, and promote emotional health. Many people who practice meditation report increased feelings of well-being and lower levels of anxiety.

There are many different types of meditation, including mindfulness, transcendental, and loving-kindness meditation. Each type offers unique benefits, and the best one for you may depend on your personal goals and preferences.

To get started, set aside just five to ten minutes each day. Sit quietly, focus on your breath, and gently return your attention whenever your mind wanders. Over time, you may find it easier to concentrate and feel more at peace.

Meditation is not a cure-all, but it can be a valuable part of a healthy lifestyle.
    """
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # Size of each chunk
    chunk_overlap=20,  # Overlap between chunks
    length_function=len,  # Function to determine the length of the text
    separators=["\n\n", "\n", " ", ""],  # Different separators to use for splitting
)

result = splitter.split_text(text)
print(result)