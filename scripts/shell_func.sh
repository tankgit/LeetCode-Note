function leet {
    if [[ $# -eq 2 ]];
	then
		if [[ $2 =~ ^[0-9]+$ ]];
		then
			notePath=$LEETCODE_PATH/archive/$2.md
		else
			echo "Please enter a valid number of leetcode problems."
			return
		fi
		if [[ $1 =~ s ]];then
			if [[ ! -f "$notePath" ]] || [[ $1 =~ f ]];then
				pbpaste | cat >! $notePath
				gleet
			else
				echo "Failed: save: The problem $2 has already existed."
				echo "If you want to overwrite it, please use -f."
				return
			fi
		fi
		if [[ $1 =~ o ]];then
			if [[ -f "$notePath" ]];then
			    open $notePath
			else
			    echo "Failed: open: The problem $2 has not been saved."
			    return
			fi
		fi
		else
		echo "Usage: leet [-osf] [NUMBER]\n\n -o    open the problem of NUMBER\n -s    save the problem of NUMBER\n -f    force to overwrite existed note"
    fi
}

