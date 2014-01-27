
# TODO: Check how to return an array to the caller!
get_user_and_pass_from_file () {
    local file=$1
    local server=$2

    local machine_found=false
    cat $file | while read line
    do
        server_re="^\\s*machine\\s+$server$"
        other_server_re="^\\s*machine\\s+"
        if echo $line | egrep "$server_re" >/dev/null
	   then machine_found=true
	elif echo $line | egrep "$other_server_re" >/dev/null
	   then machine_found=false
	elif eval $machine_found
	   then username_re="^\\s*username\\s+"
	        password_re="^\\s*password\\s+"
		if echo $line | egrep "$username_re" >/dev/null
		   then echo -n $line | awk '{print $2}'; echo " "
		elif echo $line | egrep "$password_re" >/dev/null
		   then echo -n $line | awk '{print $2}'
		fi
	fi
    done
}

# Usage/Test:
# declare username_password=`get_user_and_pass_from_file $HOME/.deployit.netrc tst`
# username=`echo $username_password | awk '{print $1}'`
# password=`echo $username_password | awk '{print $2}'`
# echo "User: '$username'"
# echo "Pass: '$password'"

