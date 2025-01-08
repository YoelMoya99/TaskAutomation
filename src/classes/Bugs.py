class Bugs:

    def __init__(self):
        self.path = None

    def save_bug(self, title, context, msg, date):
    
        log = f'''## Date: {date}
- **Title**: {title}
- **Context of the issue**: {context}
- **Description of the issue**: {msg}

'''
        with open("log.md", "a") as file:
            file.write(log)
        
        print(f"Issue written:\n\n{log}")


