import os

class Template:
    template_path = ""
    subject = ""
    
    def __init__(self, template_path, subject):
        self.template_path = template_path
        self.subject = subject
    
    def get_template(self, name):
        if not os.path.exists(self.template_path):
            raise Exception("This path does not exist")
        template_string = ""
        with open(self.template_path, 'r') as f:
            template_string = f.read().format(name=name)
        return template_string

    