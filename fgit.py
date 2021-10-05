from plumbum import cli
from pyfiglet import Figlet
from plumbum.cmd import ls
from questionary import prompt

def print_banner(text):
    print(Figlet(font='slant').renderText(text))

def get_files():
    ls_output = ls().strip()  
    files = ls_output.split("\n")
    
    return files

def generate_question(files):
    return [{
        'type': 'checkbox',
        'name': 'files',
        'message': 'what would you like to add?',
        'choices': [{'name': file.strip()} for file in files],
    }]

def filter_function(variable):
    if '_' in variable:
        return False;
    return True;





class FancyGitAdd(cli.Application):

    VERSION = "1.3"

    def main(self):
        print_banner("Git Fancy Add")
        files = get_files()

        updated_files = []

        for file in files:
            filtered_file = "".join(filter(filter_function, file))
            updated_files.append(filtered_file)


        question = generate_question(updated_files)
        answers = prompt(question)
        print(answers['files'])

if __name__ == "__main__":
    FancyGitAdd()


#TESTS

def test_getfiles():
    files = get_files()
    assert len(files) == 7, "There should be enough files."

def test_generate_questions():
    files = ["best.rb", "good.kt", "small.py"]
    question = generate_question(files)
    assert len(question) == 1, "has to be one question"
    assert question[0]['type'] == 'checkbox', "has to allow multiple selections"
    assert len(question[0]['choices']) == len(files), "same number of choices as files"

    

