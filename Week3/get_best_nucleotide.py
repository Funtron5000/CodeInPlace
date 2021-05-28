"""
File: get_best_nucleotide.py
--------------
ADD YOUR DESCRIPTION HERE
"""
import os
import sys

from TextGrid import TextGrid, Cell

SEQUENCES_FOLDER = 'week3/sequences/no_blanks'

def assemble_sequence(sequence1, sequence2, sequence3):
    """
    Given three TextGrid objects, this function creates and returns a solution genome based on the sequences passed in. All the sequences passed in will be the same size.

    Input:
        three TextGrids to be processed
    Returns:
        a new solution genome (also a TextGrid)
    """
    assembled_sequence = TextGrid.blank(sequence1.width, sequence1.height)
    sequence_list = [sequence1, sequence2, sequence3]
    current_nuc = 0

    for sequence in sequence_list:
        nuc_list = []
        for cell in sequence:
            nuc_list.append(cell)
        assembled_sequence.set_cell(current_nuc, 0, get_best_nucleotide(*nuc_list))
        current_nuc += 1
    return assembled_sequence


def get_best_nucleotide(nucleotide1, nucleotide2, nucleotide3):
    """
    Given three nucleotides, returns a nucleotide with the most common *non-blank* value. If multiple nucleotides have the same value, it doesn't matter which specific nucleotide is returned so long as its value is correct. You can assume there will never be ambiguity -- there will always be a clear majority non-blank character.

    Input:
        three nucleotides (Cells) to be compared
    Returns:
        best (Cell): nucleotide with most common non-blank value

    This doctest creates nucleotides for simple tests.
    >>> grid = TextGrid('ATCG_.txt')
    >>> A = grid.get_cell(0,0)
    >>> T = grid.get_cell(1,0)
    >>> C = grid.get_cell(2,0)
    >>> G = grid.get_cell(3,0)
    >>> blank = grid.get_cell(4,0)
    >>> best1 = get_best_nucleotide(A, A, A)
    >>> best1.value
    'A'
    >>> best2 = get_best_nucleotide(A, T, T)
    >>> best2.value
    'T'
    >>> best3 = get_best_nucleotide(A, blank, A)
    >>> best3.value
    'A'
    >>> best4 = get_best_nucleotide(blank, blank, T)
    >>> best4.value
    'T'
    >>> best5 = get_best_nucleotide(blank, blank, blank)
    >>> best5.value
    '_'
    """
    
    if nucleotide1.value == nucleotide2.value == nucleotide3.value and nucleotide1.value != '_':
        return nucleotide1
    elif ((nucleotide1.value == nucleotide2.value) or (nucleotide1.value == nucleotide3.value)) and nucleotide1.value != '_':
        return nucleotide1
    elif nucleotide2 == nucleotide3 and nucleotide2 != '_':
        return nucleotide2
    else:
        return nucleotide3

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

def txts_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a directory, returns a list of the .txt filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filenames.append(os.path.join(directory, filename))
    return filenames

def load_sequences(directory):
    """
    DO NOT MODIFY
    Given a directory name, reads all the .txt files within it into memory and
    returns them in a list. Prints to terminal the names of the files it loads.

    Input:
        dir (string): name of directory
    Returns:
        sequences (List[TextGrids]): list of sequences in directory
    """
    sequences = []
    txts = txts_in_dir(directory)
    txts.sort()
    for filename in txts:
        print("Loading", filename)
        sequence = TextGrid(filename)
        sequences.append(sequence)
    return sequences

def main():
    # DO NOT MODIFY
    sequences = load_sequences(SEQUENCES_FOLDER)
    full_genome = assemble_sequence(sequences[0], sequences[1], sequences[2])
    if full_genome:
        print("Genome assembled as follows:")
        print(full_genome)
    else:
        print("No genome to display!")

if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) > 0:
        SEQUENCES_FOLDER = args[0]
    main()