import time
import os


def keyword_extract(input_file):
    """
    This function finds the keyword from the input file and returns it.

    The keyword is found at the end of the input file after 'keyword: '
    """
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        last_line = lines[-1].strip()  # isolates the last line

        if last_line.startswith("keyword: "):
            keyword = last_line[len("keyword: "):].strip()  # removes "keyword: " to isolate the keyword
            return keyword

    except FileNotFoundError:  # exception to check if the file is there
        print(f"Error: The file {input_file} was not found.")
        return None


def filter_recipes(input_file, output_file, keyword):
    """
    This function filters the recipes based on the keyword and writes the results to the output file.
    """
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            recipes = lines[:-1]  # reads all lines of recipes except for last line with the keyword

        filtered_recipes = [recipe.strip() for recipe in recipes if keyword.lower() in recipe.lower()]

        if filtered_recipes:
            with open(output_file, 'w') as output:
                output.write("\n".join(filtered_recipes))
            print(f"Filtered recipes have been saved to {output_file}.")
        else:
            print(f"No recipes found containing the keyword '{keyword}'.")

    except Exception as e:
        print(f"Error while filtering recipes: {e}")


if __name__ == "__main__":
    input_file = "unfiltered_recipes"
    output_file = "filtered_recipes"

    print("Checking file...")

    last_processed = None   # monitor unfiltered_recipes for new keywords
    while True:
        file_modified = os.path.getmtime(input_file)

        if last_processed is None or file_modified > last_processed:
            last_processed = file_modified

            print("Checking new keyword...")
            keyword = keyword_extract(input_file)

            print(f"Using '{keyword}' as the filter keyword.")
            filter_recipes(input_file, output_file, keyword)

        else:
            print("No changes in the file.")

        time.sleep(3)
