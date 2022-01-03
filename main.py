def main():
    template = "efer"
    input_string = "reference"
    find_template_occurrence(template, input_string)


def find_template_occurrence(template: str, input_string: str):
    return find_template_occurrence_by_offsets(template, input_string, create_template(template))


def create_template(template: str):
    unique_symbols_in_template = set()
    offsets = {}
    for i in range(len(template) - 2, -1, -1):
        if template[i] not in unique_symbols_in_template:
            offsets[template[i]] = len(template) - i - 1
            unique_symbols_in_template.add(template[i])
    if template[len(template) - 1] not in unique_symbols_in_template:
        offsets[template[len(template) - 1]] = len(template)
    offsets["DEFAULT"] = len(template)
    print(offsets)
    return offsets


def find_template_occurrence_by_offsets(template: str, input_string: str, offsets: dict):
    if len(input_string) >= len(template):
        input_string_iterator = len(template) - 1
        while input_string_iterator < len(input_string):
            template_to_input_offset = 0
            found_template = True
            for j in range(len(template) - 1, -1, -1):
                if input_string[input_string_iterator - template_to_input_offset] != template[j]:
                    if j == len(template) - 1:
                        if offsets.get(input_string[input_string_iterator], False):
                            current_offset = offsets[input_string[input_string_iterator]]
                        else:
                            current_offset = offsets["DEFAULT"]
                    else:
                        current_offset = offsets[template[j]]
                    input_string_iterator += current_offset
                    found_template = False
                    break
                template_to_input_offset += 1
            if found_template:
                found_index = input_string_iterator - template_to_input_offset + 1
                print(f"Template was found at index {found_index}")
                return found_index
        error_message = "No template in input string"
        print(error_message)
        return error_message
    else:
        error_message = "Template is too long"
        print(error_message)
        return error_message


if __name__ == '__main__':
    main()
