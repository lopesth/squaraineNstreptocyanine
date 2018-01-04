for case in case1 case2 case3; do
	cd $case"/5C"
	for i in `ls *com | sed 's/.com//g' | tr -s '\n' ' '`; do
		g09 $i".com" $i".log"
	done
	cd ../../
done
