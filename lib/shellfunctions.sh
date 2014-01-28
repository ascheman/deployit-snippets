
# TODO: Check how to return an array to the caller!
get_environment_from_file () {
    local file=$1
    local environment=$2

    local environment_found=false
    cat $file | while read line
    do
        environment_re="^\[$environment\]$"
        other_environment_re="^\[.*\]$"
        
        if echo $line | egrep "$environment_re" >/dev/null
	       then environment_found=true
	    elif eval $environment_found
	       then if echo $line | egrep "$other_environment_re" >/dev/null
                   then environment_found=false
	               else echo -n " -$line"
	            fi
	    fi
    done
}


