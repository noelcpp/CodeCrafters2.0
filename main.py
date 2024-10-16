# Input prompt in a loop

print("MAX: Sup buddy! Got something to ask?")

while True:
    giberish = input("User: ")
    finp = giberish.strip()  # Use the user's input directly for checking

    # Check for exit condition
    if finp.lower() in ["exit", "quit"]:
        print("MAX: Goodbye!")
        break 

    # Data
    Arto = """
Artificial intelligence (AI) focuses on creating machines and software that can perform tasks typically requiring human intelligence. This includes capabilities such as learning from experience, understanding natural language, recognizing patterns, and making decisions. AI technologies, like machine learning and neural networks, are increasingly integrated into various applications, from virtual assistants and chatbots to advanced robotics and autonomous vehicles. The ongoing research and development in AI promise to enhance efficiency and productivity across multiple industries, while also raising important ethical considerations regarding bias, transparency, and the impact on employment.
    
    """

    cyb = """
Cybersecurity is the practice of protecting computer systems, networks, and data from theft, damage, or unauthorized access. With the rise of digital technologies, the importance of cybersecurity has skyrocketed, as organizations face increasing threats from cybercriminals and malicious actors. Effective cybersecurity measures encompass a range of strategies, including encryption, firewalls, intrusion detection systems, and user education. As cyber threats evolve, so too must security protocols, emphasizing the need for continuous monitoring and updating of defenses to safeguard sensitive information and maintain trust in digital platforms.
    """

    clo = """
Cloud computing refers to the delivery of computing services—such as storage, processing power, and applications—over the internet, allowing users to access resources on demand. This model offers flexibility, scalability, and cost efficiency, making it popular among businesses and individuals alike. Major cloud service providers, such as Amazon Web Services (AWS), Microsoft Azure, and Google Cloud, enable organizations to host applications, store data, and utilize advanced computing capabilities without the need for extensive physical infrastructure. As cloud computing continues to evolve, it fosters innovation by facilitating collaboration, remote work, and the development of new technologies.
    """
    
    py = """Python is a high level programming language which was developed by Guido Van Rossum and released in 1991. Python is a dynamic, high level, free open source and interpreted programming language. It also supports multiple inheritance, unlike Java.
A sample code:

print("Hola mi amigos!")
    """
        
    # Check for keywords in user input and respond accordingly
    if "artificial" in finp.lower():
        print(Arto)
    elif "cyber" in finp.lower():
        print(cyb)
    elif "cloud" in finp.lower():
        print(clo)
    elif "python" in finp.lower():    
        print(py)
    else:
        print("Sorry, I don't have information on that topic.")
