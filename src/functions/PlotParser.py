from argparse import ArgumentParser

def comma_separated(value):
    return [float(item) for item in value.split(',')]

def create_parser():

    # Arg parser set up
    # ------------------------------------------------------------------------
    parser = ArgumentParser(
        description="General command line argument initializer.",
        epilog="for now only works for one script."
        )

    subparsers = parser.add_subparsers(
        dest='command',
        help='Available commands'
        )

    # First command definition with respective flags.
    # ------------------------------------------------------------------------
    command1_parser = subparsers.add_parser(
        'data',
        help='Handles the data range, color and specific values'
        )

    command1_group = command1_parser.add_mutually_exclusive_group(
        required=True
        )

    command1_group.add_argument(
        '--xaxis',
        type=str,
        help='Name of the dataframe column for the x axis'
        )

    command1_group.add_argument(
        '--yaxis',
        type=str,
        help='name of the df column for a y axis'
        )

    command1_group.add_argument(
        '--xrange',
        type=comma_separated,
        help='Pass a comma separated range of values like 1.23,3.21'
        )

    command1_group.add_argument(
        '--yrange',
        type=comma_separated,
        help='Pass a comma separated range of values like 1.23,3.21'
        )

    command1_group.add_argument(
        '--src',
        help='Pass the path with the file that contains the values to plot'
        )

    command1_group.add_argument(
        '--color',
        type=str,
        help='input the color that uses the selected column'
        )

    command1_group.add_argument(
        '--show',
        action='store_true',
        help='it displays all the configurable values and data'
        )

    # Second command definition with respective flags.
    # ------------------------------------------------------------------------
    command2_parser = subparsers.add_parser('format', help='Second command')
    
    command2_group = command2_parser.add_mutually_exclusive_group(required=True)
    command2_group.add_argument('--optionA', help="Option A for command2")
    command2_group.add_argument('--optionB', help="Option B for command2")

    # Return Namespace with the parsed args.
    # ------------------------------------------------------------------------


    return parser.parse_args()



