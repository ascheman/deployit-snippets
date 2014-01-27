
declare -x username=''
declare -x password=''

declare -a return
get_user_and_pass_from_file () {
    local file=$1
    local server=$2

# username=''
# password=''
    local machine_found=false
    cat $file | while read line
    do
        echo line: $line >&2
        server_re="^\\s*machine\\s+$server$"
        other_server_re="^\\s*machine\\s+"
        if echo $line | egrep "$server_re" >/dev/null
	   then machine_found=true
#                 continue
	elif echo $line | egrep "$other_server_re" >/dev/null
	   then machine_found=false
# 	        continue
	elif eval $machine_found
	   then username_re="^\\s*username\\s+"
	        password_re="^\\s*password\\s+"
		if echo $line | egrep "$username_re" >/dev/null
		   then return[0]=`echo $line | awk '{print $2}'`
		        echo -n "${return[0]} "
		elif echo $line | egrep "$password_re" >/dev/null
		   then return[1]=`echo $line | awk '{print $2}'`
		        echo -n ${return[1]}
		fi
	fi
	echo "Current: ${return[*]}" >&2
    done

#    return $return
#     echo "${return[@]}"
}

echo "User: '$username'"
echo "Pass: '$password'"

declare username_password=`get_user_and_pass_from_file $HOME/.deployit.netrc tst`

# echo "${return[@]}"
echo "${username_password}"
# username=$username_password
# password=$username_password

username=`echo $username_password | awk '{print $1}'`
password=`echo $username_password | awk '{print $2}'`
echo "User: '$username'"
echo "Pass: '$password'"

