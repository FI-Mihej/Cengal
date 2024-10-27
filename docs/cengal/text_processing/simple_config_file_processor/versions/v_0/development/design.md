# Simple configuration file processor

## Example

```python
# line = 'asdf'  # will end script with error: attempt to reassign reserved word. All predefined functions and standard brackets (and their predefined lists) are reserved words

# my_app1_name = env('MY_APP_NAME', 'my_app')
my_app1_name = env('MY_APP_NAME')  # will end script with error if env-var is not declared or empty

# dir1_name = '/etc/my_app/my_config'
dir1_name = format('/etc/{}/my_config', my_app1_name)

ensure_dir(dir1_name)

# cd('/etc/my_app/my_config')
cd(dir1_name)  # will end script with error if dir not exists
ensure_cd(dir1_name)  # will create dir and cd to it
dir1_exists = check_dir(dir1_name)  # bool

file1_name = 'my_file'

# full_file1_name = cd_relative('../my_config/my_file')
full_file1_name = relative(dir1_name, '../my_config/my_file')

# ensure_file('my_file')
# ensure_file('my_config/my_file')
# ensure_file('../my_config/my_file')
# ensure_file('/etc/my_app/my_config/my_file')
# ensure_file(file1_name)
ensure_file(full_file1_name)  # will create required directories and file
file1_exists = check_file(full_file1_name)  # bool

# ensure cd restored after end of block
with cd:
    ...

# makes dir1_name a cd for the block and restores previous cd after end of block
with dir(dir1_name):
    ...

# open file, read it's content to memory, perform operations in memory, write result back to file, close file
with file(full_file1_name) as file1_data:  # provides brackets for a file content (decoded and without BOM)
    var db_path
    with inner(file1_data):
        commented_text = Bracket('#', line_break)

        # uncomment only lines with env-var export command
        text_to_uncomment = Bracket('export', line_break)
        for inner(line):
            with outer(commented_text):
                clean_line = data
                with inner(commented_text):
                    # uncommented_line = data
                    # with outer(text_to_uncomment):
                    #     clean_line = uncommented_line
                    if positions(text_to_uncomment):
                        clean_line = data
                
                data = clean_line

        # uncomment all commented lines
        for inner(line):
            with outer(commented_text):
                clean_line = data
                with inner(commented_text):
                    clean_line = data
                
                data = clean_line
        
        without_prefix = removeprefix(data, 'prefix_')
        if equal


with file(full_file1_name):  # behaves as a compositions of `with_file ... as ...` and `with inner(...)`
    # for outer(line):
    for inner(line):


```
