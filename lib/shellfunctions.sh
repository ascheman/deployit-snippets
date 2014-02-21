
# TODO: Check how to return an array to the caller!
get_environment_from_file () {
    # The parameters
    local file=$1
    local environment=$2

    # Some constants
    local comment_re="^\s*\#.*"
    local emptyline_re="^\s*$"
    local other_environment_re="^\[.*\]$"
    
    local environment_found=false
    cat $file | while read line
    do
        environment_re="^\[$environment\]$"
         
        if echo "$line" | egrep "$comment_re" >/dev/null
           then continue
        elif echo "$line" | egrep "$emptyline_re" >/dev/null
           then continue
        elif echo "$line" | egrep "$environment_re" >/dev/null
	       then environment_found=true
	    elif eval "$environment_found"
	       then if echo "$line" | egrep "$other_environment_re" >/dev/null
                   then environment_found=false
	               else echo -n " -$line"
	            fi
	    fi
    done
}


