from argparse import ArgumentParser


def createParser():

    # Arg parser set up
    # ------------------------------------------------------------------------
    parser = ArgumentParser(
        description="General command line argument initializer.",
        epilog="for now only works for one script."
        )

    '''
    ---------------------- Process flags ------------------------
    '''
    parser.add_argument(
            '--genMD',
            action = 'store_true',
            help = (
                'This is the flag that you raise at the beginning of the '
                'command argument, so that the script knows that the rest '
                'of the arguments are for the context of generating the '
                'markdown files for the review process :)'
                )
            )

    parser.add_argument(
            '--genPDF',
            action = 'store_true',
            help = (
                'This is the flag that you raise at the beginning of the '
                'command argument, so that the script knows that the rest '
                'of the arguments are for the context of generating the '
                'PDF files from the markdown files generated and filled '
                'in the review process :)'
                )
            )

    '''
    ---------------------- Process flags ------------------------
    '''

    parser.add_argument(
        '--inDir',
        type = str,
        help = (
            'This is the argument for the path of input directories, for '
            'whatever process is going to be done.'
            )
        )

    parser.add_argument(
        '--outDir',
        type = str,
        help = (
            'This is the argument for the path of output directories, for '
            'whatever process is going to be done.'
            )
        )

    parser.add_argument(
        '--rubric',
        type = str,
        help = (
            'This is the argument for the path of the rubric that will be '
            'used to generate the files for each student.'
            )
        )
    
    return parser.parse_args()

