import os


def read_matrices_from_file(input_filename):
    matrices = []
    with open(input_filename, 'r') as infile:
        current_matrix = []
        for line in infile:
            line = line.strip()
            if line:
                current_matrix.append(list(map(int, line.split())))
            else:
                if current_matrix:
                    matrices.append(current_matrix)
                    current_matrix = []
        if current_matrix:
            matrices.append(current_matrix)
    return matrices


def write_results_to_file(output_filename, results):
    with open(output_filename, 'w') as outfile:
        for result in results:
            for row in result:
                outfile.write(' '.join(map(str, row)) + '\n')
            outfile.write('\n')


def process_matrices(matrices):
    return matrices


if __name__ == "__main__":
    input_filename = r"E:\Praktika9-5variant.txt"
    output_filename = r"E:\Praktika10.txt"

    if not os.path.exists(input_filename):
        print(f"Error: Input file {input_filename} does not exist.")
    else:
        matrices = read_matrices_from_file(input_filename)
        results = process_matrices(matrices)
        write_results_to_file(output_filename, results)
        print("Processing complete. Results written to:", output_filename)
