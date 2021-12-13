# config options





# prefixes/suffixes
    # set to '\0' if your arch doesn't support something
    # if your arch doesn't support something a program tries to use the compile will fail (except for multiline comments and labels)

label =                     '.'
ram_address =               'M'
heap_address =              'H'
rom_address =               'C'
port =                      '%'
register =                  'R'
comment =                   '//'
multiline_start =           '/*' # if multiline isn't supported then single line comments will be
multiline_end =             '*/' # used when possible
compiler_instr =            '&'
immediate =                 ''

# misc

code_header = """""" # code put before the urcl program

code_footer = """""" # code put at the end of the urcl program

# compiler instructions
    # these are compiler instructions that need to be handled by the assembler (words, fillto, org, etc.)

{
    'words': '',
    'fillto': '',
    'org': '',
    'string': '',
    'utfstring': '', # this shouldn't really be used all that much don't worry about it
    'compiler': '',
    }

# urcl instructions
    # these are the instructions actually executed by the cpu