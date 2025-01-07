from argparse import ArgumentParser
import os
import subprocess as sp
import shutil as sh


def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        '--path',
        help='relative path to directory to organize'
        )
    parser.add_argument(
        '--temporal',
        help='build temporal folder',
        default=False,
        action='store_true'
        )
    parser.add_argument(
        '--latex_conference',
        help='build template file system for latex',
        default=False,
        action='store_true'
        )
    parser.add_argument(
        '--latex_personal',
        help='build template file system for latex',
        default=False,
        action='store_true'
        )
    parser.add_argument(
        '--universidad',
        help='build template file system for courses',
        default=False,
        action='store_true'
        )

    args = parser.parse_args()
    return args


def display_dir(path):
    
    if os.path.exists(path):
        
        result = sp.run(
            ['tree', path],
            capture_output=True,
            text=True
            )
        
        print("STDOUT:\n\n", result.stdout)

def gen_latex(path, which_tex):

    conference = '/mnt/c/Users/Yoel/Documents/LaTeX/IEEE_Conference_Template/'
    personal = '/mnt/c/Users/Yoel/Documents/LaTeX/Personal/'
    shared_files = '/mnt/c/Users/Yoel/Documents/LaTeX/shared_files/'

    src_dir = conference # default value

    if (which_tex == 'conference'):
        src_dir = conference
    elif (which_tex == 'personal'):
        src_dir = personal


    target_dir = os.path.join(path, 'latexfiles')
    os.makedirs(target_dir, exist_ok=True)
   
    sh.copytree(
        os.path.join(src_dir, 'dirs'),
        target_dir,
        dirs_exist_ok=True
        )
    
    sh.copy2(
        os.path.join(src_dir, 'main.tex'),
        os.path.join(target_dir, 'main.tex')
        )

    os.symlink(
        os.path.join(shared_files, 'Makefile'),
        os.path.join(target_dir, 'Makefile')
        )
    
    os.symlink(
        os.path.join(src_dir, 'preamble.tex'),
        os.path.join(target_dir, 'preamble.tex')
        ) 

    os.symlink(
        os.path.join(shared_files, 'references.bib'),
        os.path.join(target_dir, 'references.bib')
        )


def gen_temporal(path):
    new_dir = os.path.join(path, 'temp')
    os.makedirs(new_dir, exist_ok=True)

def gen_universidad_template(path):
    
    loop = 1
    while (loop):
        course = input('Numero y nombre del curso: ')
        root = os.path.join(path, course)
        
        directories = ['Enunciados/Tareas',
                       'Enunciados/Examenes',
                       'Enunciados/Quices',
                       'Enunciados/Practica',
                       'Teoria',
                       'Entregables',
                       'Practica'
                       ]

        for directorie in directories:
            os.makedirs(
                os.path.join(root, directorie)
                )
        loop = int(input('Want to continue? (1/0): ')) 


def main():
    args = get_args()

    if (args.latex_conference) or (args.latex_personal):
        print('\n ====== Generating LaTeX Template ======\n')
        if args.latex_conference:
            which_tex = 'conference'
        else:
            which_tex = 'personal'
        gen_latex(args.path, which_tex)

    if args.temporal:
        print('\n ====== Generating temp File ======')
        gen_temporal(args.path)

    if args.universidad:
        print('\n ====== Generating course Template ======\n')
        gen_universidad_template(args.path)

    display_dir(args.path)


if __name__ == '__main__':
    main()
