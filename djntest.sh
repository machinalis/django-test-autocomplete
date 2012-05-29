# bash completion for running python tests with djntest

_djntest()
{
    local cur prev words cword

    COMPREPLY=()
    _get_comp_words_by_ref cur prev words cword

    local tcases

    if [[ $cur = ":" ]]
        then
        # <command> test_file.py:<TAB>
        # cur = :
        # prev = test_file.py
        tcases=$(testcases $PWD/$prev)
    else
        if [[ ! -z $cur ]] && [[ $prev = ":" ]]
            then
            case $cur in
                *.* )
                # <command> test_file.py:TestAutocomplete.<TAB>
                # cur = TestAutocomplete.
                # prev = :
                # preprev = test_file.py
                tcases=$(get_testcases $PWD/${words[cword-2]} --units=$cur);
                ;;
                * )
                # <command> test_file.py:TestDo<TAB>
                # cur = TestDo
                # prev = :
                # preprev = test_file.py
                tcases=$(get_testcases $PWD/${words[cword-2]})
            esac
        fi
    fi

    if [[ -z $tcases ]]
        then
            _filedir
        else
            COMPREPLY=()
            # Variable to hold the current word
            cur="${COMP_WORDS[COMP_CWORD]}"
            local stripped_cur=${cur#":"}
            # Generate possible matches and store them in the
            # array variable COMPREPLY
            COMPREPLY=($(compgen -W "${tcases}" $stripped_cur))
    fi

}
complete -F _djntest djntest
